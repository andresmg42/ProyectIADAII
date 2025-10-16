import copy
import concurrent.futures
from load_data import LoadData
from brute_force import brute_force_algorithm
from dynamic_and_recursive import DinamicAlogorithm
from Voraz import Voraz
from write_data import Write_output
from write_benchmark import Write_output_b
import os

class Controller:
    def __init__(self):
        self.time = 0
        self.executed_algorthrim = "Nothing"
        self.load_data = LoadData()

        # Inicializar los algoritmos aquí
        self.brute_force_al = brute_force_algorithm()
        self.dinamic_al = DinamicAlogorithm()
        self.voraz_al = Voraz()

    def load_data_txt(self, path):
        """Carga los datos desde un archivo y maneja errores."""
        try:
            self.load_data.load_data_and_validate(path)
            self.load_data.process_content()
            print(f"Datos cargados desde: {path}")
        except FileNotFoundError:
            print(f"Error: El archivo {path} no se encontró.")
        except ValueError as ve:
            print(f"Error en los datos del archivo: {ve}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

    def print_loaded_data(self):
        """Imprime los datos cargados (estudiantes y materias)."""
        for student in self.load_data.students:
            print(student.return_info())

    def find_solution(self, method):
        """Encuentra una solución según el algoritmo elegido."""
        students = copy.deepcopy(self.load_data.students)
        subjects = copy.deepcopy(self.load_data.subjects)

        try:
            if method == 'rocFB':
                self.executed_algorthrim = "Brute Force"
                self.solution, self.time = self.brute_force_al.rocFB(subjects, students)
            elif method == 'rocPD':
                self.executed_algorthrim = "Dinamic"
                self.solution, self.time = self.dinamic_al.rocPD(subjects, students)
            elif method == 'rocV':
                self.executed_algorthrim = "Voraz"
                self.solution, self.time = self.voraz_al.rocV(subjects, students)
            else:
                raise ValueError("Método no reconocido")
        except Exception as e:
            print(f"Error al ejecutar el algoritmo {method}: {e}")

    def benchmark_solutions(self):
        """Ejecuta y mide los tiempos de los tres algoritmos en paralelo."""
        students = self.load_data.students
        subjects = self.load_data.subjects

        self.solutions = []  # Lista para almacenar las soluciones
        self.times = []      # Lista para almacenar los tiempos de ejecución

        try:
            # Ejecutar algoritmos en paralelo usando ThreadPoolExecutor
            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = [
                    executor.submit(self.brute_force_al.rocFB, subjects, students),
                    executor.submit(self.dinamic_al.rocPD, subjects, students),
                    executor.submit(self.voraz_al.rocV, subjects, students)
                ]

                for future in concurrent.futures.as_completed(futures):
                    solution, exec_time = future.result()
                    self.solutions.append(solution)
                    self.times.append(exec_time)
        except Exception as e:
            print(f"Error al ejecutar los algoritmos en paralelo: {e}")

    def write_FB_solution(self):
        """Guarda la solución obtenida por el algoritmo Brute Force."""
        Writer = Write_output(self.time, self.solution, self.executed_algorthrim, self.load_data.filename)
        Writer.write_solution()

    def write_all_solution(self):
        """Guarda todas las soluciones obtenidas de los algoritmos de benchmark."""
        Writer = Write_output_b(self.times, self.solutions, "Benchmark", self.load_data.filename)
        print(f"Soluciones={self.solutions}")
        Writer.write_solution()

    def print_solution(self):
        """Imprime la solución obtenida junto con el tiempo de ejecución."""
        if self.solution:
            print(f"Valor de la solución: {self.solution['min']}\n")
            print(f"Tiempo de ejecución: {self.time:.4f} segundos\n")
            print('Solución:')
            for s in self.solution['solution']:
                print(s.return_info_sol())
        else:
            print("No se ha encontrado una solución.")





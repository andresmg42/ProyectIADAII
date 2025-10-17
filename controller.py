import copy
import concurrent.futures
from load_data import LoadData
from brute_force import brute_force_algorithm
from dynamic_and_recursive import DinamicAlogorithm
from Voraz import Voraz
from write_data import Write_output
import copy

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
        """retorna los datos cargados (estudiantes y materias)."""
        info=''
        for student in self.load_data.students:
            info +=student.return_info()+'\n'
        return info

    def find_solution(self, method):
        """Encuentra una solución según el algoritmo elegido."""
        students = copy.deepcopy(self.load_data.students)
        subjects = copy.deepcopy(self.load_data.subjects)

        students=copy.deepcopy(self.load_data.students)
        subjects=copy.deepcopy(self.load_data.subjects)
        match method:
            case 'rocFB':
                brute_force_al= brute_force_algorithm()
                self.executed_algorthrim = "rocFB"
                self.solution,self.time = brute_force_al.rocFB(subjects,students)
            case 'rocPD':
                dinamic_al= DinamicAlogorithm()
                self.executed_algorthrim = "rocPD"
                self.solution,self.time= dinamic_al.rocPD(subjects,students)
            case 'rocV':
                voraz_al = Voraz()
                self.executed_algorthrim = "Voraz"
                self.solution,self.time = voraz_al.rocV(subjects,students)

    def benchmark_solutions(self):
        """Ejecuta y mide los tiempos de los tres algoritmos en paralelo."""
        students = self.load_data.students
        subjects = self.load_data.subjects

        brute_force_al= brute_force_algorithm()
        dinamic_al= DinamicAlogorithm()
        voraz_al = Voraz()

        self.solutions = []  # aquí guardamos las soluciones
        self.times = []      # aquí guardamos los tiempos

        # Brute Force
        solution, exec_time = brute_force_al.rocFB(subjects, students)
        self.solutions.append(solution)
        self.times.append(exec_time)

        # Dinamic
        solution, exec_time = dinamic_al.rocPD(subjects, students)
        self.solutions.append(solution)
        self.times.append(exec_time)

        # Voraz
        solution, exec_time = voraz_al.rocV(subjects, students)
        self.solutions.append(solution)
        self.times.append(exec_time)

    def write_solution_controller(self,path):
        Writer = Write_output(self.time,self.solution,self.executed_algorthrim,self.load_data.filename)
        Writer.write_solution(path)

        

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





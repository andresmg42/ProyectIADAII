from load_data import LoadData
from brute_force import brute_force_algorithm
from dynamic_and_recursive import DinamicAlogorithm
from Voraz import Voraz
from write_data import Write_output
from write_benchmark import Write_output_b

class Controller:
    def __init__(self):
        self.brute_force_al= brute_force_algorithm()
        self.dinamic_al= DinamicAlogorithm()
        self.voraz_al=Voraz()
        
        

    def load_data(self,path):
        self.load_data=LoadData()
        self.load_data.load_data_and_validate(path)
        self.load_data.process_content()
        
    
    def print_load_data(self):
        print(self.load_data.content)
    
    def find_solution(self,method):

        students=self.load_data.students
        subjects=self.load_data.subjects
        match method:
            case 'rocFB':
                self.solution= self.brute_force_al.rocFB(subjects,students)
            case 'rocPD':
                self.solution= self.dinamic_al.rocPD(subjects,students)
            case 'rocV':
                self.executed_algorthrim = "Voraz"
                self.solution,self.time = self.voraz_al.rocV(subjects,students)

    def benchmark_solutions(self):
        students = self.load_data.students
        subjects = self.load_data.subjects

        self.solutions = []  # aquí guardamos las soluciones
        self.times = []      # aquí guardamos los tiempos

        # Brute Force
        solution, exec_time = self.brute_force_al.rocFB(subjects, students)
        self.solutions.append(solution)
        self.times.append(exec_time)

        # Dinamic
        solution, exec_time = self.dinamic_al.rocPD(subjects, students)
        self.solutions.append(solution)
        self.times.append(exec_time)

        # Voraz
        solution, exec_time = self.voraz_al.rocV(subjects, students)
        self.solutions.append(solution)
        self.times.append(exec_time)

    def write_FB_solution(self):
        Writer = Write_output(self.time,self.solution,self.executed_algorthrim,self.load_data.filename)
        Writer.write_solution()

    
    def write_all_solution(self):
        Writer = Write_output_b(self.times,self.solutions,"Bencmark",self.load_data.filename)
        print(f"Solutions={self.solutions}")
        Writer.write_solution()
    

    def print_solution(self):
        
        print(f'solution value: {self.solution['min']}')
        for s in self.solution['solution']:
            print(s.return_info_sol())





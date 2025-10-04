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
        self.load_data=LoadData()
        

    def load_data_txt(self,path):
       
        self.load_data.load_data_and_validate(path)
        self.load_data.process_content()
        
    
    def print_load_data_raw(self):
        print(self.load_data.content)

    def print_loaded_data(self):
        for student in self.load_data.students:
            print(student.return_info())

    def find_solution(self,method):

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
                voraz_al=Voraz()
                self.executed_algorthrim = "rocV"
                self.solution,self.time = voraz_al.rocV(subjects,students)
    
    def write_solution(self):
        Writer = Write_output(self.time,self.solution,self.executed_algorthrim,self.load_data.filename)
        expected_output = Writer.write_solution()
        return expected_output
    
 

    def print_solution(self):
        
        print(f'valor de la solución: {self.solution['min']}\n')
        print(f'tiempo de ejecución: {self.time}\n')
        print('solucion:')
        for s in self.solution['solution']:
            print(s.return_info_sol())

    





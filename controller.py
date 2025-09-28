from load_data import LoadData
from brute_force import brute_force_algorithm
from dynamic_and_recursive import DinamicAlogorithm
from Voraz import Voraz

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
                self.solution= self.voraz_al.rocV(subjects,students)

    def print_solution(self):
        
        print(f'solution value: {self.solution['min']}')
        for s in self.solution['solution']:
            print(s.return_info_sol())





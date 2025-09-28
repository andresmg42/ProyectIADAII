from load_data import LoadData
from brute_force import brute_force_algorithm
from dynamic_and_recursive import DinamicAlogorithm

class Controller:
    def __init__(self):
        self.brute_force_al= brute_force_algorithm()
        self.dinamic_al= DinamicAlogorithm()
        
        

    def load_data(self,path):
        self.load_data=LoadData()
        self.load_data.load_data_and_validate(path)
        self.load_data.process_content()
        
    
    def print_load_data(self):
        print(self.load_data.content)
    
    def find_solution(self,method):
        match method:
            case 'rocFB':
                self.solution= self.brute_force_al.rocFB(self.load_data.subjects,self.load_data.students)
            case 'rocPD':
                self.solution= self.dinamic_al.rocPD(self.load_data.subjects,self.load_data.students)

    def print_solution(self):
        
        print(f'solution value: {self.solution['min']}')
        for s in self.solution['solution']:
            print(s.return_info_sol())





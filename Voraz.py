from classes import Student
from time import time

class Voraz:
    def __init__(self) -> None:
        pass

    def global_insatisfaction(self,students) -> float:
        """Calcula la insatisfacción global promedio"""
        if len(students) == 0:
            return 0.0
        return sum(student.calculate_insatisfaction() for student in students) / len(
            students
        )

    def greedy_algorithm(self,subjects, students ):
        """Asigna materias a estudiantes según prioridad de solicitud"""
        solution = [Student(stu.code, stu.solicited_subjects[:]) for stu in students]
        
        for subj in subjects:
            
            requests = []
            for idx, stu in enumerate(students):
                for sol in stu.solicited_subjects:
                    if sol.code == subj.code:
                        requests.append((idx, sol))

            
            requests.sort(key=lambda x: x[1].priority, reverse=True)

            quotas = subj.quotas
            for idx, sol in requests:
                if quotas <= 0:
                    break
                solution[idx].assign_subject(subj.code)
                quotas -= 1

            subj.quotas = quotas  

        return solution
    
    def rocV(self,subjects,students):
        start = time()
        students_sol=self.greedy_algorithm(subjects,students)

        global_ins=self.global_insatisfaction(students_sol)
        end = time()
        final_time = end - start
        return {'min':global_ins,'solution':students_sol},final_time




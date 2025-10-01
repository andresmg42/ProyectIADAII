class Write_output:
    def __init__(self, exec_time, solution, algorhtrim):
        self.exec_time = exec_time
        self.solution = solution
        self.executed_algorthrim = algorhtrim
    
    def write_solution(self, filename=None):

        if filename is None:
            filename = f"salida_{self.executed_algorthrim}.txt"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"{self.exec_time:.4f}\n")  

            for student in self.solution["solution"]:
                f.write(f"{student.code},{len(student.assigned_subjects)}\n")
                for subj in student.assigned_subjects:
                    f.write(f"{subj.code}\n")
                f.write("\n")


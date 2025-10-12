import os

class Write_output_b:
    def __init__(self, exec_times, solutions, algorhtrim, load_data_name):
        self.exec_times = exec_times
        self.solutions = solutions
        self.executed_algorthrim = algorhtrim
        self.load_data_name = load_data_name

    def write_solution(self, filename=None):
        base_dir = os.path.dirname(os.path.abspath(__file__))   
        outputs_dir = os.path.join(base_dir, "outputs")

        os.makedirs(outputs_dir, exist_ok=True)

        if filename is None:
            filename = f"salida_{self.executed_algorthrim}_{self.load_data_name}"

        file_path = os.path.join(outputs_dir, filename)

        with open(file_path, "w", encoding="utf-8") as f:
            for idx, (time, solution) in enumerate(zip(self.exec_times, self.solutions), start=1):
                f.write(f"=== SOLUCIÓN {idx} ===\n")
                f.write(f"Tiempo de ejecución: {time:.6f} segundos\n")
                f.write(f"Insatisfacción mínima: {solution['min']}\n")
                f.write("----------------------------\n")

                for student in solution["solution"]:
                    f.write(f"{student.code},{len(student.assigned_subjects)}\n")
                    for subj in student.assigned_subjects:
                        f.write(f"{subj.code}\n")
                    f.write("\n")
                f.write("===============\n\n")

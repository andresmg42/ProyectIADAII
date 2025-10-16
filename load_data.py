import sys
import os
import re
from classes import Student, Subject, SolicitedSubject

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class LoadData:
    def __init__(self):
        self.subjects = []
        self.students = []
        self.filename = None   

    def load_data_and_validate(self, path):

        file_path = path

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                self.content = file.read()


            self.filename = os.path.basename(file_path)

        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def clear_data(self):
        self.subjects = []
        self.students = []
        self.filename = None

    def process_content(self):
        lines = self.content.splitlines()
        # print(self.content)
        num_subjects = int(lines[0])
        for i in range(1, num_subjects + 1):
            subject_code, quotas = lines[i].split(sep=",")
            sbj = Subject(subject_code, int(quotas), i - 1)
            self.subjects.append(sbj)

        student_block = lines[num_subjects + 1 + 1 :]

        def get_students(block):
            if len(block) == 0:
                return

            st = block[0].split(sep=",")
            student_code = st[0]
            num_soli_sbj = int(st[1])

            student = Student(code=student_code)
            student.solicited_subjects = []

            for j in range(1, num_soli_sbj + 1):
                s_sbj = block[j].split(sep=",")
                subject = next(
                    (sbj for sbj in self.subjects if sbj.code == s_sbj[0]), None
                )
                student.solicited_subjects.append(
                    SolicitedSubject(subject, int(s_sbj[1]))
                )

            self.students.append(student)
            get_students(block[num_soli_sbj + 1 :])

        get_students(student_block)

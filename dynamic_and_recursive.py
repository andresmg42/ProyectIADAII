import copy
import math
from time import time
from typing import List, Tuple, Dict, Any
from classes import SolicitedSubject,Student,Subject


class DinamicAlogorithm:

    def __init__(self) -> None:
        pass

    def power_set_recursive(self, s: List[Any]) -> List[List[Any]]:

        result = []

        def backtrack(start, current):
            result.append(current[:])
            for i in range(start, len(s)):
                current.append(s[i])
                backtrack(i + 1, current)
                current.pop()

        backtrack(0, [])
        return result

    def posible_assignments_by_student(self, student) -> List[List["SolicitedSubject"]]:
        solicited_subjects = student.solicited_subjects
        return self.power_set_recursive(solicited_subjects)

    def is_valid(
        self, assigned_subjects: List["SolicitedSubject"], c: List[int]
    ) -> bool:

        return all(c[assigned_subject.i] >= 1 for assigned_subject in assigned_subjects)

    def c_less_used_quotas_of(
        self, c: List[int], assigned_subjects: List["SolicitedSubject"]
    ) -> List[int]:

        for assigned_subject in assigned_subjects:
            c[assigned_subject.i] -= 1
        return c

    def calculate_insatisfaction(self, student, assigned_subjects):

        if not student.solicited_subjects:
            return 0.0

        assigned_subject_codes = {subject.code for subject in assigned_subjects}
        maj_size = len(assigned_subjects)
        msj_size = len(student.solicited_subjects)
        if msj_size == 0:
            return 0.0

        unsupplied_subjects = [
            sol
            for sol in student.solicited_subjects
            if sol.code not in assigned_subject_codes
        ]

        sum_pjl = sum(sol.priority for sol in unsupplied_subjects)

        fun_Y = msj_size * 3 - 1
        return (1 - (maj_size / msj_size)) * (sum_pjl / fun_Y)

    def rocPD(
        self, subjects: List["Subject"], students: List["Student"]
    ) -> Tuple[Dict[str, Any], float]:
        start = time()

        memo: Dict[Tuple[int, Tuple[int, ...]], Tuple[float, List["Student"]]] = {}

        c = [subject.quotas for subject in subjects]

        def solve(j: int, c: List[int]) -> Tuple[float, List["Student"]]:
            """
            Solves the dynamic programming subproblem for student j and remaining quotas c.
            Returns the minimum insatisfaction and the best assignment path from j onwards.
            """
            if j >= len(students):
                return 0.0, []

            state = (j, tuple(c))
            if state in memo:
                return memo[state]

            min_local_insatisfaction = math.inf
            best_path_from_j = []

            student_j = students[j]

            posible_assignments = self.posible_assignments_by_student(student_j)

            for assigned_subjects in posible_assignments:

                if self.is_valid(assigned_subjects, c):

                    new_quotas = self.c_less_used_quotas_of(c[:], assigned_subjects)

                    future_insatisfaction, best_future_path = solve(j + 1, new_quotas)

                    actual_insatisfaction = self.calculate_insatisfaction(
                        student_j, assigned_subjects
                    )

                    total_insatisfaction = actual_insatisfaction + future_insatisfaction

                    if total_insatisfaction < min_local_insatisfaction:
                        min_local_insatisfaction = total_insatisfaction

                        assigned_student_j = copy.deepcopy(student_j)
                        assigned_student_j.assigned_subjects = assigned_subjects
                        best_path_from_j = [assigned_student_j] + best_future_path

            memo[state] = (min_local_insatisfaction, best_path_from_j)

            return min_local_insatisfaction, best_path_from_j

        min_local_insatisfaction, best_path = solve(0, c)
        end = time()
        final_time = end - start

        min_avg_insatisfaction = (
            min_local_insatisfaction / len(students) if len(students) > 0 else 0.0
        )

        return {"min": min_avg_insatisfaction, "solution": best_path}, final_time

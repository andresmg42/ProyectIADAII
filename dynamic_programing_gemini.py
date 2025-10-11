from re import sub
import copy
import math
from time import time
from typing import List, Tuple, Dict, Any
from classes import SolicitedSubject,Student,Subject

# Keeping the Student, Subject, and SolicitedSubject classes the same
# ... (The provided class definitions are assumed to be here) ...

class DinamicAlogorithm:

    def __init__(self) -> None:
        pass
    
    # power_set_recursive is fine for generating combinations
    def power_set_recursive(self, s: List[Any]) -> List[List[Any]]:
        # This is already a relatively clean implementation of powerset
        result = []
        def backtrack(start, current):
            result.append(current[:])
            for i in range(start, len(s)):
                current.append(s[i])
                backtrack(i + 1, current)
                current.pop()
        backtrack(0, [])
        return result

    # 🚀 IMPROVEMENT 1: Return combinations (list of SolicitedSubject)
    # instead of a list of deep-copied Student objects.
    # This avoids O(2^|Sj|) deep-copies and list appends of Student objects.
    def posible_assignments_by_student(self, student) -> List[List['SolicitedSubject']]:
        solicited_subjects = student.solicited_subjects
        # Returns a list of lists, where each inner list is a combination
        # of SolicitedSubject objects from the student's solicitations.
        return self.power_set_recursive(solicited_subjects)

    # is_valid remains simple and efficient
    def is_valid(self, assigned_subjects: List['SolicitedSubject'], c: List[int]) -> bool:
        # Check if all assigned subjects have at least 1 quota left
        return all(c[assigned_subject.i] >= 1 for assigned_subject in assigned_subjects)

    # c_less_used_quotas_of remains simple and efficient
    def c_less_used_quotas_of(self, c: List[int], assigned_subjects: List['SolicitedSubject']) -> List[int]:
        # c[:] is already passed as a copy by the caller
        for assigned_subject in assigned_subjects:
            c[assigned_subject.i] -= 1
        return c

    # ⚠️ The recursive_solve and dynamic_solve_solution_value are removed 
    # as the main function rocPD is the one to be used and improved.

    # 🚀 IMPROVEMENT 2: Consolidate logic in rocPD to use the
    # combination instead of new Student object in the main loop.
    # Only create a new student object for the *best path* tracking.
    def rocPD(self, subjects: List['Subject'], students: List['Student']) -> Tuple[Dict[str, Any], float]:
        start = time()
        # 🔑 The key remains (j, tuple(c))
        memo: Dict[Tuple[int, Tuple[int, ...]], Tuple[float, List['Student']]] = {}
        
        c = [subject.quotas for subject in subjects]

        def solve(j: int, c: List[int]) -> Tuple[float, List['Student']]:
            """
            Solves the dynamic programming subproblem for student j and remaining quotas c.
            Returns the minimum insatisfaction and the best assignment path from j onwards.
            """
            if j >= len(students): # j>len(students)-1 simplifies to j>=len(students)
                return 0.0, []

            state = (j, tuple(c))
            if state in memo:
                return memo[state]

            min_local_insatisfaction = math.inf
            best_path_from_j = []

            student_j = students[j]
            # Use the improved function to get combinations of SolicitedSubject
            posible_assignments = self.posible_assignments_by_student(student_j)

            for assigned_subjects in posible_assignments:
                # 1. Check validity using the combination and current quotas c
                if self.is_valid(assigned_subjects, c):

                    # 2. Calculate new quotas c_new immediately
                    # c[:] creates a copy of the list for safe modification
                    new_quotas = self.c_less_used_quotas_of(c[:], assigned_subjects)

                    # 3. Recursively solve for the next state
                    future_insatisfaction, best_future_path = solve(j + 1, new_quotas)

                    # 4. 💡 Temporary Student object creation (or better: calculate insatisfaction without it)
                    # To calculate 'actual_insatisfaction', we need the Student's method, 
                    # which needs the 'assigned_subjects' and 'solicited_subjects'.
                    # 🚀 IMPROVEMENT 3: Calculate insatisfaction outside the Student class.
                    # Since we are keeping the classes the same, we must create a temporary object.
                    
                    # Create a temporary student object to calculate insatisfaction
                    temp_student = copy.copy(student_j) # Use shallow copy for speed
                    temp_student.assigned_subjects = assigned_subjects # Assign the combination
                    actual_insatisfaction = temp_student.calculate_insatisfaction()
                    # ⚠️ We must rely on the fact that student_j.solicited_subjects
                    # is correctly referenced by the temporary object (safe with copy.copy).

                    total_insatisfaction = actual_insatisfaction + future_insatisfaction

                    if total_insatisfaction < min_local_insatisfaction:
                        min_local_insatisfaction = total_insatisfaction
                        
                        # 5. 💡 Path Construction: Create the *actual* assigned Student 
                        # object only for the best path tracking.
                        # This student object stores the specific assignment for student j.
                        
                        # Create a true deep-copy of the student object *only* for the best path
                        assigned_student_j = copy.deepcopy(student_j)
                        assigned_student_j.assigned_subjects = assigned_subjects # Re-assign the combination
                        best_path_from_j = [assigned_student_j] + best_future_path
                        
            memo[state] = (min_local_insatisfaction, best_path_from_j)

            return min_local_insatisfaction, best_path_from_j
        
        min_local_insatisfaction, best_path = solve(0, c)
        end = time()
        final_time = end - start
        
        # Ensure division by len(students) is only done if the list is not empty
        min_avg_insatisfaction = min_local_insatisfaction / len(students) if len(students) > 0 else 0.0

        return {'min': min_avg_insatisfaction, 'solution': best_path}, final_time
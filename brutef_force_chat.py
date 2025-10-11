from typing import List
from classes import SolicitedSubject,Student,Subject


# Helper function to calculate insatisfaction without modifying the student object
def calculate_insat_for_subset(solicited: List[SolicitedSubject], chosen_codes: List[str]) -> float:
    msj_size = len(solicited)
    if msj_size == 0:
        return 0.0
    maj_size = len(chosen_codes)
    unsupplied_subjects = [sol for sol in solicited if sol.code not in chosen_codes]
    sum_pjl = sum(sol.priority for sol in unsupplied_subjects)
    fun_Y = msj_size * 3 - 1
    return (1 - (maj_size / msj_size)) * (sum_pjl / fun_Y)

# Function to generate all possible subsets of indices
def generate_subsets(n: int, k: int) -> List[List[int]]:
    def backtrack(start: int, k: int, current: List[int], results: List[List[int]]):
        if len(current) == k:
            results.append(current[:])
            return
        for i in range(start, n):
            current.append(i)
            backtrack(i + 1, k, current, results)
            current.pop()
    
    results = []
    backtrack(0, k, [], results)
    return results

# The improved brute-force algorithm using backtracking with pruning
def optimal_assignment(students: List[Student], subjects: List[Subject]) -> float:
    if not subjects:
        total_insat = sum(student.calculate_insatisfaction() for student in students)
        return total_insat

    # Prepare quotas as list indexed by index_id
    max_id = max(s.index_id for s in subjects) if subjects else 0
    quotas = [0] * (max_id + 1)
    for s in subjects:
        quotas[s.index_id] = s.quotas

    best_insat = float('inf')
    best_assign = None  # Will be list of lists of assigned codes per student

    def backtrack(student_idx: int, current_insat: float, current_quotas: List[int], current_assign: List[List[str]]):
        nonlocal best_insat, best_assign

        # Prune if current insatisfaction exceeds best found
        if current_insat >= best_insat:
            return

        # Base case: processed all students
        if student_idx == len(students):
            if current_insat < best_insat:
                best_insat = current_insat
                best_assign = [x[:] for x in current_assign]
            return

        student = students[student_idx]
        # Sort solicited subjects by priority (descending) to try better assignments first
        solicited = sorted(student.solicited_subjects, key=lambda ss: ss.priority, reverse=True)
        n = len(solicited)

        # Try subsets from largest to smallest
        for k in range(n, -1, -1):
            # Generate all subsets of size k
            subsets = generate_subsets(n, k)
            for indices in subsets:
                valid = True
                chosen_i = []  # subject indices
                chosen_codes = []
                # Check if subset is valid (respects quotas)
                for j in indices:
                    i = solicited[j].i
                    code = solicited[j].code
                    if current_quotas[i] < 1:
                        valid = False
                        break
                    chosen_i.append(i)
                    chosen_codes.append(code)

                if not valid:
                    continue

                # Apply assignment temporarily
                for ii in chosen_i:
                    current_quotas[ii] -= 1

                # Calculate insatisfaction for this assignment
                insat = calculate_insat_for_subset(student.solicited_subjects, chosen_codes)

                # Recurse to next student
                backtrack(student_idx + 1, current_insat + insat, current_quotas, current_assign + [chosen_codes])

                # Undo assignment
                for ii in chosen_i:
                    current_quotas[ii] += 1

    # Start backtracking
    backtrack(0, 0.0, quotas, [])

    # Apply the best assignment found
    if best_assign is not None:
        for i, ass_codes in enumerate(best_assign):
            for code in ass_codes:
                students[i].assign_subject(code)

    return best_insat
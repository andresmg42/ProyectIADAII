import copy
import math
from time import time
from typing import List,Any,Dict
from classes import Student

class brute_force_algorithm:

  def __init__(self) -> None:
    pass


  
  

  def combinations(self, elements, k):
      """
      Generates all unique combinations of size k from the elements list using backtracking.
      
      :param elements: The list of items to choose from.
      :param k: The size of the combinations to find.
      :return: A list of all combinations.
      """
      # 1. Initialize the storage for all results
      results = []
      
      # 2. Handle invalid input cases early
      if k < 0 or k > len(elements):
          return []
      
      def _backtrack( elements, k, start_index, current_combo):
        """
        The recursive helper function that implements the backtracking logic.
        
        :param elements: The list of items to choose from (static).
        :param k: The target size of the combination (static).
        :param start_index: The index in 'elements' from which to begin selection in this call.
        :param current_combo: The combination being built (the current state).
        """
        
        # 🛑 Base Case (Goal Reached)
        # If the current combination has the target size k, it's a valid result.
        if len(current_combo) == k:
            # Add a *copy* of the combination to the results. 
            # We copy because current_combo will be modified later in the recursion.
            results.append(list(current_combo)) 
            return

        # 🔄 Recursive Step (Choose and Recurse)
        # Iterate through possible choices for the *next* element.
        # We start from 'start_index' to ensure we only select elements 
        # that come *after* the last element added, preventing duplicates 
        # and ensuring combinations (order doesn't matter).
        for i in range(start_index, len(elements)):
            
            # ➡️ Choose: Select the element at index i
            element = elements[i]
            current_combo.append(element)
            
            # ↪️ Recurse: Move to the next state
            # The next element must be chosen from index i + 1 onwards.
            _backtrack(elements, k, i + 1, current_combo)
            
            # ⬅️ Un-choose (Backtrack): Revert the state
            # Remove the last element added to explore other paths (combinations).
            current_combo.pop()
      
      # 3. Start the backtracking process
      # We pass the input list, the target size k, the index to start searching from, 
      # and the current combination (initially empty).
      _backtrack(elements, k, 0, [])
      
      return results

    


  def combinations_by_subject(self,subject,students):
    quotes=subject.quotas
    code=subject.code
    applicant_students=[student for student in students if any([solicitedsubject.code==code for solicitedsubject in student.solicited_subjects])]
    applicant_students_codes=[student.code for student in applicant_students]
    
    if quotes>=len(applicant_students):
      return [applicant_students_codes]
    comb =self.combinations(applicant_students_codes,quotes)

    return comb
  

  
  def distribution_final(self,distributions):
    """
    Generates the Cartesian product of the lists in 'distributions' using backtracking.

    :param distributions: A list of lists (e.g., [[A, B], [1, 2]]).
    :return: A list of lists, where each inner list is one product 
             (e.g., [[A, 1], [A, 2], [B, 1], [B, 2]]).
    """
    results = []
    
    def _backtrack(list_index, current_product):
        """
        The recursive helper function.
        
        :param list_index: The index of the list we are currently choosing an element from.
        :param current_product: The product element being built (the current state).
        """
        
        # 🛑 Base Case: If we've selected an element from every list, we've found a full product.
        if list_index == len(distributions):
            # Store a *copy* of the product before the function returns and modifies the list.
            results.append(list(current_product))
            return

        # 🔄 Recursive Step: Iterate through all elements in the current list
        current_list = distributions[list_index]
        for element in current_list:
            
            # ➡️ Choose: Add the element to the current state
            current_product.append(element)
            
            # ↪️ Recurse: Move to the next list in the 'distributions' array
            _backtrack(list_index + 1, current_product)
            
            # ⬅️ Un-choose (Backtrack): Remove the last element to revert the state 
            # and allow the loop to try the next element from the current list.
            current_product.pop()

    # Start the process from the first list (index 0) with an empty product.
    _backtrack(0, [])
    
    return results



  def distribute_solutions(self,subjects,students):
    subject_distribution=[]

    for subject in subjects:
      posible_comb=self.combinations_by_subject(subject,students)
      subject_distribution.append(posible_comb)


    return subject_distribution
  


  def get_final_solutions(self,distributed_solutions,students,subjects):
    final_solutions=[]
    
    for sol in distributed_solutions:
       students_dic={student.code:[] for student in students}
       for sol_i in range(len(sol)):
          for st_code in sol[sol_i]:
             students_dic[st_code].append(subjects[sol_i].code)
       final_solutions.append(students_dic)
    
    return final_solutions
          
  def calculate_insatisfaction(self,student,assigned_subject_codes):
        
        if not student.solicited_subjects or not student:
            return 0.0

        
        maj_size = len(assigned_subject_codes)
        msj_size = len(student.solicited_subjects)
        if msj_size == 0:
            return 0.0

        unsupplied_subjects = [sol for sol in student.solicited_subjects if sol.code not in assigned_subject_codes]
        
        sum_pjl = sum(sol.priority for sol in unsupplied_subjects)

        fun_Y = msj_size * 3 - 1
        return (1 - (maj_size / msj_size)) * (sum_pjl / fun_Y)

  def find_optimal_solution(self,final_solutions:List[Dict],students:List[Student]):
    min_general_satisfaction={'min':math.inf,'solution':None}
    for solution in final_solutions:
      acumulated_insatisfaction=0
      for key,value in solution.items():

        assigned_subjects=value

        student=next((student for student in students if student.code==key),None)

        student_insatisfaction=self.calculate_insatisfaction(student,assigned_subjects)

        acumulated_insatisfaction+=student_insatisfaction

      general_insatisfaction=acumulated_insatisfaction/len(students)
      if min_general_satisfaction['min']>general_insatisfaction:
        min_general_satisfaction['min']=general_insatisfaction
        min_general_satisfaction['solution']=solution
    
    return min_general_satisfaction

  def get_complete_solution(self,solution:Dict,students:List[Student]):
     full_solution=[]
     min_insatisfaction=solution['min']
     solution_dict=solution['solution']
     for key,assigned_subjects in solution_dict.items():
        students=copy.deepcopy(students)

        student=next((student for student in students if student.code==key),None)
        if student:
            student.assigned_subjects=assigned_subjects
        full_solution.append(student)
     
     return {'min':min_insatisfaction,'solution':full_solution}

        
    


  def rocFB(self,subjects,students):
    start = time()
    subject_distribution= self.distribute_solutions(subjects,students)

    distributed_solutions=self.distribution_final(subject_distribution)

    final_solutions=self.get_final_solutions(distributed_solutions,students,subjects)

    optimal_solution=self.find_optimal_solution(final_solutions,students)

    full_solution=self.get_complete_solution(optimal_solution,students)
    end = time()
    final_time = end - start
    return full_solution, final_time
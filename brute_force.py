import copy
import math
from time import time

class brute_force_algorithm:

  def __init__(self) -> None:
    pass


  def combinations(self,elements, k):

      if k == 0:
          return [[]]

      if len(elements) < k:
          return []

      first = elements[0]
      remain = elements[1:]

      whit_first = [[first] + c for c in self.combinations(remain, k-1)]

      whitout_first = self.combinations(remain, k)

      return whit_first + whitout_first


  def combinations_by_subject(self,subject,students):
    quotes=subject.quotas
    code=subject.code
    applicant_students=[student for student in students if any([solicitedsubject.code==code for solicitedsubject in student.solicited_subjects])]

    comb =self.combinations([student.code for student in applicant_students],quotes)

    return comb

  def distribution_final(self,distributions):

    if len(distributions)==0:
      return [[]]

    first_array=distributions[0]

    rest_array=distributions[1:]

    rest_combines=self.distribution_final(rest_array)

    result=[]
    for element in first_array:
      for comb in rest_combines:
        result.append([element]+comb)

    return result


  def distribute_solutions(self,subjects,students):
    subject_distribution=[]

    for subject in subjects:
      posible_comb=self.combinations_by_subject(subject,students)
      subject_distribution.append(posible_comb)


    return subject_distribution


  def get_final_solutions(self,distributed_solutions,students,subjects):
    final_solutions=[]
    for solution in distributed_solutions:
      new_students=copy.deepcopy(students)
      for i in range(len(solution)):
        for student in new_students:
          subject_code=subjects[i].code
          if student.code in solution[i]:
            student.assign_subject(subject_code)
      final_solutions.append(new_students)
    return final_solutions

  def find_optimal_solution(self,final_solutions,students):
    min_general_satisfaction={'min':math.inf,'solution':None}
    for solution in final_solutions:
      acumulated_insatisfaction=0
      for i in range(len(solution)):

        student=solution[i]

        student_insatisfaction=student.calculate_insatisfaction()

        acumulated_insatisfaction+=student_insatisfaction

      general_insatisfaction=acumulated_insatisfaction/len(students)
      if min_general_satisfaction['min']>general_insatisfaction:
        min_general_satisfaction['min']=general_insatisfaction
        min_general_satisfaction['solution']=solution
    # print("DEBUG en brute_force class solution:", min_general_satisfaction['solution'])
    return min_general_satisfaction


  def rocFB(self,subjects,students):
    start = time()
    subject_distribution= self.distribute_solutions(subjects,students)

    distributed_solutions=self.distribution_final(subject_distribution)

    final_solutions=self.get_final_solutions(distributed_solutions,students,subjects)

    optimal_solution=self.find_optimal_solution(final_solutions,students)
    end = time()
    final_time = end - start
    return optimal_solution, final_time
from re import sub
import copy
import math
from time import time

class DinamicAlogorithm:

  def __init__(self) -> None:
    pass

  def power_set_recursive(self,s):
    result = []

    def backtrack(start, current):
        result.append(current[:])
        for i in range(start, len(s)):
            current.append(s[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result

  def posible_assignments_by_student(self,student):
      solution=[]
      solicited_subjects=student.solicited_subjects
      posible_combinations=self.power_set_recursive(solicited_subjects)
      for combination in posible_combinations:
        new_student=copy.deepcopy(student)
        if len(combination)!=0:
          for solicited_subject in combination:
            new_student.assign_subject(solicited_subject.code)
        solution.append(new_student)

      return solution

  def is_valid(self,student,c):

      assigned_subjects=student.assigned_subjects
      valid=all(c[assigned_subject.i]>=1 for assigned_subject in assigned_subjects)
      return valid

  def c_less_used_quotas_of(self,c,student):

    index_assigned_subjects=[solicited_subject.i for solicited_subject in student.assigned_subjects]

    for i in range(len(c)):
      if i in index_assigned_subjects:
        c[i]-=1
    return c
  
  def recursive_solve(self,students,subjects):

    c=[subject.quotas for subject in subjects]

    def solve(j,c):

      if j>len(students)-1:
        return 0

      min_local_insatisfaction=math.inf

      posible_assigns_ej=self.posible_assignments_by_student(students[j])

      for student in posible_assigns_ej:

        if self.is_valid(student,c):

          actual_insatisfaction=student.calculate_insatisfaction()

          new_quotas= self.c_less_used_quotas_of(c[:],student)

          future_insatisfaction=solve(j+1,new_quotas)

          total_insatisfaction=actual_insatisfaction + future_insatisfaction

          min_local_insatisfaction=min(min_local_insatisfaction,total_insatisfaction)

      return min_local_insatisfaction

    return solve(0,c)


  def dynamic_solve_solution_value(self,students,subjects):

      memo={}

      c=[subject.quotas for subject in subjects]

      def solve(j,c):

        if j>len(students)-1:
          return 0

        if (j,tuple(c)) in memo:
          return memo[(j,tuple(c))]

        min_local_insatisfaction=math.inf

        posible_assigns_ej=self.posible_assignments_by_student(students[j])

        for student in posible_assigns_ej:

          if self.is_valid(student,c):

            actual_insatisfaction=student.calculate_insatisfaction()

            new_quotas= self.c_less_used_quotas_of(c[:],student)

            future_insatisfaction=solve(j+1,new_quotas)

            total_insatisfaction=actual_insatisfaction + future_insatisfaction

            min_local_insatisfaction=min(min_local_insatisfaction,total_insatisfaction)

        memo[(j,tuple(c))]=min_local_insatisfaction

        return min_local_insatisfaction

      return solve(0,c)
  
  def rocPD(self,subjects,students):
      start = time()
      memo={}
      
      c=[subject.quotas for subject in subjects]

      def solve(j,c):

        if j>len(students)-1:
          return 0,[]

        if (j,tuple(c)) in memo:
          return memo[(j,tuple(c))]

        min_local_insatisfaction=math.inf

        best_path=[]

        posible_assigns_ej=self.posible_assignments_by_student(students[j])

        for student in posible_assigns_ej:

          if self.is_valid(student,c):

            actual_insatisfaction=student.calculate_insatisfaction()

            new_quotas= self.c_less_used_quotas_of(c[:],student)

            future_insatisfaction,best_future_path=solve(j+1,new_quotas)

            total_insatisfaction=actual_insatisfaction + future_insatisfaction

            if total_insatisfaction < min_local_insatisfaction:
              min_local_insatisfaction=total_insatisfaction
              best_path=[student] + best_future_path
              

        memo[(j,tuple(c))]=(min_local_insatisfaction,best_path)

        return min_local_insatisfaction,best_path
      
      min_local_insatisfaction,best_path=solve(0,c)
      end = time()
      final_time = end - start
      return {'min':min_local_insatisfaction/len(students),'solution':best_path},final_time


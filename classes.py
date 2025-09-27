from typing import List

class Subject:
  def __init__(self,code,quotas,id):
    self.code:str=code
    self.quotas:int=quotas
    self.index_id:int=id

class Student:
  
  
  def __init__(self,code=None,solicited_subjects=None):
    self.code:str=code
    self.solicited_subjects:List[SolicitedSubject]=solicited_subjects
    self.assigned_subjects:List[SolicitedSubject]=[]


  def return_info(self):
    string=f'\n{self.code}\n'
    for s_subject in self.solicited_subjects:
       string+=s_subject.return_info()
    return string

  def return_info_sol(self):
    string=f'\n{self.code}\n'
    for s_subject in self.assigned_subjects:
       string+=s_subject.return_info()
    return string


  def calculate_insatisfaction(self):

    if len(self.solicited_subjects)==0:
      return 0.0

    assigned_subject_codes={subject.code for subject in self.assigned_subjects}
    maj_size=len(self.assigned_subjects)
    msj_size=len(self.solicited_subjects)
    if msj_size==0:
      return 0.0
    unsupplied_subjects=[solicited for solicited in self.solicited_subjects if solicited.code not in assigned_subject_codes ]
    sum_pjl=sum(solicited_subject.priority for solicited_subject in unsupplied_subjects)
    fun_Y= msj_size*3-1

    return (1-(maj_size/msj_size))*(sum_pjl/fun_Y)


  def assign_subject(self,subject_code):

    solicited_subject=next((solicited_subject for solicited_subject in self.solicited_subjects if solicited_subject.code==subject_code),None)
    if solicited_subject:
      self.assigned_subjects.append(solicited_subject)


class SolicitedSubject:
  def __init__(self,subject=None,priority=0):
    self.subject=subject
    self.priority:int=priority


  def return_info(self):
    return f'({self.subject.code},{self.priority})'

  @property
  def code(self) -> str:
    return self.subject.code

  @property
  def i(self)-> int:
    return self.subject.index_id
from classes import Subject,Student,SolicitedSubject
from brute_force import brute_force_algorithm
from dynamic_and_recursive import DinamicAlogorithm

subjects=[
  Subject('M1',3,0),
  Subject('M2',4,1),
  Subject('M3',2,2)
]

students=[
    Student('e1',[SolicitedSubject(subjects[0],5),
                  SolicitedSubject(subjects[1],2),
                  SolicitedSubject(subjects[2],1)
                  ],1),
    Student('e2',[SolicitedSubject(subjects[0],4),
                  SolicitedSubject(subjects[1],1),
                  SolicitedSubject(subjects[2],3)
                  ],2),
    Student('e3',[SolicitedSubject(subjects[1],3),
                  SolicitedSubject(subjects[2],2)
                  ],3),
    Student('e4',[SolicitedSubject(subjects[0],2),
                  SolicitedSubject(subjects[2],3)
                  ],4),
    Student('e5',[SolicitedSubject(subjects[0],3),
                  SolicitedSubject(subjects[1],2),
                  SolicitedSubject(subjects[2],3)
                  ],5)

]

# al_b=brute_force_algorithm()

# sol=al_b.bruteforce_pipeline(subjects,students)

# for s in sol['solution']:
#     print(s.return_info_sol())

al_d=DinamicAlogorithm()

v_s,sol=al_d.dynamic_solve_solution(students,subjects)

for s in sol:
    print(s.return_info_sol())
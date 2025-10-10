from classes import Subject,Student,SolicitedSubject
from brute_force import brute_force_algorithm
from dynamic_and_recursive import DinamicAlogorithm
from Voraz import Voraz
from controller import Controller

subjects=[
  Subject('M1',3,0),
  Subject('M2',4,1),
  Subject('M3',2,2)
]

students=[
    Student('e1',[SolicitedSubject(subjects[0],5),
                  SolicitedSubject(subjects[1],2),
                  SolicitedSubject(subjects[2],1)
                  ]),
    Student('e2',[SolicitedSubject(subjects[0],4),
                  SolicitedSubject(subjects[1],1),
                  SolicitedSubject(subjects[2],3)
                  ]),
    Student('e3',[SolicitedSubject(subjects[1],3),
                  SolicitedSubject(subjects[2],2)
                  ]),
    Student('e4',[SolicitedSubject(subjects[0],2),
                  SolicitedSubject(subjects[2],3)
                  ]),
    Student('e5',[SolicitedSubject(subjects[0],3),
                  SolicitedSubject(subjects[1],2),
                  SolicitedSubject(subjects[2],3)
                  ])

]


controller=Controller()

controller.load_data_txt('./inputs/test1.txt')

controller.print_load_data_raw()

#controller.find_solution('rocFB')

#controller.find_solution('rocPD')

controller.find_solution('rocV')

controller.write_FB_solution()

#controller.benchmark_solutions()

#controller.write_all_solution()


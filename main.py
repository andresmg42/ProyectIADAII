from classes import Subject,Student,SolicitedSubject
from controller import Controller
from view import View

subjects=[
  Subject('M1',6,0),
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
                  SolicitedSubject(subjects[2],2),
                  ]),
    Student('e4',[SolicitedSubject(subjects[0],2),
                  SolicitedSubject(subjects[2],3)
                  ]),
    Student('e5',[SolicitedSubject(subjects[0],3),
                  SolicitedSubject(subjects[1],2),
                  SolicitedSubject(subjects[2],3)
                  ])

]

view=View()
view.app_init()


# c=Controller()

# c.load_data_txt('./inputs/test1.txt')
# c.find_solution('rocPD')
# print('solution using rocPD')
# c.print_solution()
# c.find_solution('rocFB')
# print('solution using rocFB')
# c.print_solution()
# c.find_solution('rocV')
# print('solution using rocV')
# c.print_solution()

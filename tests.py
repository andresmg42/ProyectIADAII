from classes import Subject,Student,SolicitedSubject
from controller import Controller
from view import View
from load_data import LoadData
from dynamic_and_recursive import DinamicAlogorithm
from dynamic_programing_gemini_v2 import DinamicAlogorithm as PDG
from dynamic_and_recursive import DinamicAlogorithm as PD
# import brutef_force_chat as bt
from  brute_force  import brute_force_algorithm as bt
from brute_force_v2 import brute_force_algorithm as btb


# subjects=[
#   Subject('M1',6,0),
#   Subject('M2',4,1),
#   Subject('M3',2,2)
# ]

# students=[
#     Student('e1',[SolicitedSubject(subjects[0],5),
#                   SolicitedSubject(subjects[1],2),
#                   SolicitedSubject(subjects[2],1)
#                   ]),
#     Student('e2',[SolicitedSubject(subjects[0],4),
#                   SolicitedSubject(subjects[1],1),
#                   SolicitedSubject(subjects[2],3)
#                   ]),
#     Student('e3',[SolicitedSubject(subjects[1],3),
#                   SolicitedSubject(subjects[2],2),
#                   ]),
#     Student('e4',[SolicitedSubject(subjects[0],2),
#                   SolicitedSubject(subjects[2],3)
#                   ]),
#     Student('e5',[SolicitedSubject(subjects[0],3),
#                   SolicitedSubject(subjects[1],2),
#                   SolicitedSubject(subjects[2],3)
#                   ])

# ]

load=LoadData()
load.load_data_and_validate('./inputs/Prueba3.txt')
load.process_content()

students=load.students
subjects=load.subjects


btf=bt()
btfb=btb()

# dist=btf.distribute_solutions(subjects,students)

# print(len(btf.distribution_final(dist)))
# print()
# print(len(btf.distribution_final2(dist)))

# solbt=btf.rocFB(subjects,students)
# solbtb=btfb.rocFB(subjects,students)

# pd=PD()
# solpd=pd.rocPD(subjects,students)

# pdg=PDG()
# solpdg=pdg.rocPD(subjects,students)


# print('Time pd sol:',solpdg[1])
# print('Time pdg sol:',solpd[1])
# print('Time bt sol:',solbt[1])
# print('Time btb',solbtb[1])


# print(btf.combinations_by_subject(subjects[1],students))

print(btf.combinations([1,2,3,4],3))
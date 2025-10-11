from classes import Subject,Student,SolicitedSubject
from controller import Controller
from view import View
from load_data import LoadData
from dynamic_and_recursive import DinamicAlogorithm
from dynamic_programing_gemini_v2 import DinamicAlogorithm as PDG
from dynamic_and_recursive import DinamicAlogorithm as PD
# import brutef_force_chat as bt
from  brute_force  import brute_force_algorithm as bt
from brute_force_v2 import brute_force_algorithm as bt2
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
load.load_data_and_validate('./inputs/Prueba1.txt')
load.process_content()

students=load.students
subjects=load.subjects


btf2=bt2()
btf=bt()
# btfb=btb()



# solbt2=btf2.rocFB(subjects,students)
solbt=btf.rocFB(subjects,students)

# pd=PD()
# solpd=pd.rocPD(subjects,students)

# pdg=PDG()
# solpdg=pdg.rocPD(subjects,students)


# print('Time pd sol:',solpdg[1])
# print('Time pdg sol:',solpd[1])
print('Time bt sol:',solbt)
# print('Time btb',solbtb[1])


# subject_distribution= btf2.distribute_solutions(subjects,students)

# distributed_solutions=btf2.distribution_final(subject_distribution)

# final_solutions=btf2.get_final_solutions(distributed_solutions,students,subjects)

# optimal_solution=btf2.find_optimal_solution(final_solutions,students)

# full_solution=btf2.get_complete_solution(optimal_solution,students)

# print(full_solution)


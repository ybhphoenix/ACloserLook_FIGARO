import matplotlib.pyplot as plt
from csv import DictReader

#obtain the feedback coefficients and entropy results of continuous periodic oscillations
coef_continuous=[]
entropy_continuous=[]
with open('../data/continuous_periodic_oscillation_data.csv') as f_con:
    for col_con in DictReader(f_con):
        coef_continuous.append(col_con["feedback coefficients"])
        coef_continuous=[element_con[0:14] for element_con in coef_continuous]
        entropy_continuous.append(col_con["min-entropy"])
    # print(coef_continuous[-10:],"\n")
    # print(entropy_continuous[-10:],"\n")

#obtain the feedback coefficients and entropy results of intermittent periodic oscillations
coef_intermittent=[]
entropy_intermittent=[]
with open('../data/intermittent_periodic_oscillation_data.csv') as f_inter:
    for col_inter in DictReader(f_inter):
        coef_intermittent.append(col_inter["feedback coefficients"])
        coef_intermittent=[element_inter[0:14] for element_inter in coef_intermittent]
        entropy_intermittent.append(col_inter["min-entropy"])
    # print(coef_intermittent[-10:], "\n")
    # print(entropy_intermittent[-10:], "\n")

#obtain the feedback coefficients and entropy results of chaotic oscillations
coef_chaotic=[]
entropy_chaotic=[]
with open('../data/chaotic_oscillation_data.csv') as f_chao:
    for col_chao in DictReader(f_chao):
        coef_chaotic.append(col_chao["feedback coefficients"])
        coef_chaotic=[element_chao[0:14] for element_chao in coef_chaotic]
        entropy_chaotic.append(col_chao["min-entropy"])
    # print(coef_chaotic[-10:], "\n")
    # print(entropy_chaotic[-10:], "\n")

#convert the strings to integer numbers and floating numbers
coef_continuous=[int(a_con,2) for a_con in coef_continuous]
entropy_continuous=[float(e_con) for e_con in entropy_continuous]

coef_intermittent=[int(a_inter,2) for a_inter in coef_intermittent]
entropy_intermittent=[float(e_inter) for e_inter in entropy_intermittent]

coef_chaotic=[int(a_chao,2) for a_chao in coef_chaotic]
entropy_chaotic=[float(e_chao) for e_chao in entropy_chaotic]

plt.figure()
plt.plot(coef_continuous, entropy_continuous, 'r+', label='periodic')
plt.plot(coef_intermittent, entropy_intermittent, 'g+', label='mixed')
plt.plot(coef_chaotic, entropy_chaotic, 'b.', label='chaotic')
plt.xticks([0, 4000, 8000, 12000, 16000], fontsize=15)
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1], fontsize=15)
plt.xlabel("Decimal representation of feedback coefficients", fontsize=15)
plt.ylabel("min-entropy", fontsize=15)
plt.legend(loc='upper right', fontsize=11)
plt.ylim(0, 1.1)
# plt.savefig('min-entro-garo.eps', dpi=200, bbox_inches='tight')
plt.show()
import matplotlib.pyplot as plt
from csv import DictReader

#obtain the Lyapunov exponents and entropy results of continuous periodic oscillations
lya_continuous=[]
entropy_continuous=[]
with open('../data/continuous_periodic_oscillation_data.csv') as f_con:
    for col_con in DictReader(f_con):
        lya_continuous.append(col_con["Lyapunov exponent"])
        entropy_continuous.append(col_con["min-entropy"])
    # print(lya_continuous[-10:],"\n")
    # print(entropy_continuous[-10:],"\n")

#obtain the Lyapunov exponents, entropy results and duration of chaotic oscillations in the intermittent periodic oscillations
lya_intermittent=[]
entropy_intermittent=[]
duration_intermittent=[]
with open('../data/intermittent_periodic_oscillation_data.csv') as f_inter:
    for col_inter in DictReader(f_inter):
        lya_intermittent.append(col_inter["Lyapunov exponent"])
        entropy_intermittent.append(col_inter["min-entropy"])
        duration_intermittent.append(col_inter["duration of chaotic oscillation(%)"])
    # print(lya_intermittent[-10:], "\n")
    # print(entropy_intermittent[-10:], "\n")

#obtain the Lyapunov exponents and entropy results of chaotic oscillations
lya_chaotic=[]
entropy_chaotic=[]
with open('../data/chaotic_oscillation_data.csv') as f_chao:
    for col_chao in DictReader(f_chao):
        lya_chaotic.append(col_chao["Lyapunov exponent"])
        entropy_chaotic.append(col_chao["min-entropy"])
    # print(lya_chaotic[-10:], "\n")
    # print(entropy_chaotic[-10:], "\n")

#convert strings to floating number
lya_continuous=[float(l_con) for l_con in lya_continuous]
entropy_continuous=[float(e_con) for e_con in entropy_continuous]

lya_intermittent=[float(l_inter) for l_inter in lya_intermittent]
entropy_intermittent=[float(e_inter) for e_inter in entropy_intermittent]
duration_intermittent=[int(d_inter) for d_inter in duration_intermittent]

#obtain the Lyapunov exponents and entropy results in mixed situations with the duration of chaotic oscillation [75%,100%)
idx_inter_all=[i for i,m in enumerate(duration_intermittent)]
idx_mix=[i for i,m in enumerate(duration_intermittent) if m>=75]
lya_mix=[lya_intermittent[l] for l in idx_mix]
entropy_mix=[entropy_intermittent[e] for e in idx_mix]

#combine the remaining data in intermittent periodic oscillation and all the data in continuous periodic oscillation to form the periodic situations
lya_per=[lya_intermittent[l] for l in idx_inter_all if l not in idx_mix] + lya_continuous
entropy_per=[entropy_intermittent[e] for e in idx_inter_all if e not in idx_mix] + entropy_continuous


lya_chaotic=[float(l_chao) for l_chao in lya_chaotic]
entropy_chaotic=[float(e_chao) for e_chao in entropy_chaotic]

plt.figure()
plt.plot(entropy_per, lya_per, 'r+', label='periodic')
plt.plot(entropy_mix, lya_mix, 'g*', label='mixed')
plt.plot(entropy_chaotic, lya_chaotic, 'b.', label='chaotic')
plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], fontsize=15)
plt.yticks([-0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3], fontsize=15)
plt.xlabel("min-entropy", fontsize=15)
plt.ylabel("Lyapunov exponent", fontsize=15)
plt.legend(loc='upper right', fontsize=11)
plt.ylim(-0.3, 0.3)
plt.hlines(y=0,xmin=0,xmax=1,linestyles='--',colors='r')
plt.show()
from rule_test import abandon_classical
from rule_test import abandon_deduction
from rule_test import abandon_rule1
from rule_test import abandon_rule2
from rule_test import abandon_rule3

#/////////////////the indexes of all the peridic oscillations measured from an inplementation on FPGA.
#the index of the classical ring oscillator with the feedback polynomial f(x)=x^15+1
c_per_classical = [0]
#the indexes of the measured periodic oscillations for Deduction rule
c_per_deduction = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#the indexes of the measured periodic oscillations for Decision rule1
c_per_rule1 = [142, 351, 20, 348, 2286, 679, 947, 2004, 194, 677, 106,
               115, 136, 251, 682, 721, 1215, 178, 210]
#the indexes of the measured periodic oscillations for Decision rule2
c_per_rule2 = [17, 86, 96, 122, 149, 203, 215, 219, 236, 197, 4445, 229,
               261, 135, 157, 284, 293, 338, 341, 1615]
#the indexes of the measured periodic oscillations for Decision rule3
c_per_rule3 = [1557, 1172, 1329, 1815, 2113, 4285, 2281, 1976, 1716, 2076, 1466, 1621, 1682]

# check whether all the measured periodic oscillations with entropy loss are detected successfully
fit_classical = []
unfit_classical = []
for t_c in range(len(c_per_classical)):
    if (c_per_classical[t_c] in abandon_classical):
        fit_classical.append(c_per_classical[t_c])
    else:
        unfit_classical.append(c_per_classical[t_c])

fit_deduction = []
unfit_deduction = []
for t_d in range(len(c_per_deduction)):
    if (c_per_deduction[t_d] in abandon_deduction):
        fit_deduction.append(c_per_deduction[t_d])
    else:
        unfit_deduction.append(c_per_deduction[t_d])

fit_rule1 = []
unfit_rule1 = []
for t1 in range(len(c_per_rule1)):
    if (c_per_rule1[t1] in abandon_rule1):
        fit_rule1.append(c_per_rule1[t1])
    else:
        unfit_rule1.append(c_per_rule1[t1])

fit_rule2 = []
unfit_rule2 = []
for t2 in range(len(c_per_rule2)):
    if (c_per_rule2[t2] in abandon_rule2):
        fit_rule2.append(c_per_rule2[t2])
    else:
        unfit_rule2.append(c_per_rule2[t2])

fit_rule3 = []
unfit_rule3 = []
for t3 in range(len(c_per_rule3)):
    if (c_per_rule3[t3] in abandon_rule3):
        fit_rule3.append(c_per_rule3[t3])
    else:
        unfit_rule3.append(c_per_rule3[t3])

print("fit_classical", fit_classical)
print("unfit_classical", unfit_classical)
print("fit_deduction", fit_deduction)
print("unfit_deduction", unfit_deduction)
print("fit_rule1", fit_rule1)
print("unfit_rule1", unfit_rule1)
print("fit_rule2", fit_rule2)
print("unfit_rule2", unfit_rule2)
print("fit_rule3", fit_rule3)
print("unfit_rule3", unfit_rule3)
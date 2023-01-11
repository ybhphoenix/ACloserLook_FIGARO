import numpy as np
import os
import matplotlib.pyplot as plt
from collections import defaultdict

data = np.loadtxt("./c_special.txt", dtype=int)

#obtain the challenges
d_la = []
len_d = int(data.shape[0] / 2)
for i in range(len_d):
    d = data[2 * i]
    d1 = data[2 * i + 1]
    d = bin(d)[2:]
    d = d.rjust(8, '0')
    d1 = bin(d1)[2:]
    d1 = d1.rjust(5, '0')
    d_last = d1 + d

    x_msb = 0
    X_bin = ''
    for k in range(0, 13):
        x_msb = x_msb ^ int(d_last[k], 2)
    X_bin += '1'
    X_bin += d_last
    X_bin += str(x_msb)
    X_bin += '1'
    d_la.append(X_bin)

chal = [t[::-1] for t in d_la]

c_per_rule1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 142, 351, 20, 348, 2286, 679, 947, 2004, 194, 677, 106,
               115, 136, 251, 682, 721, 1215, 178, 210]
c_per_rule2 = [17, 86, 96, 122, 149, 203, 215, 219, 236, 197, 4445, 229, 261, 135, 157, 284, 293, 338, 341, 1615]
c_per_rule3 = [1557, 1172, 1329, 1815, 2113, 4285, 2281, 1976, 1716, 2076, 1466, 1621, 1682]

delay = [34.4923, 34.4923, 32.3499, 29.7053, 27.9767, 25.1206, 23.4170, 20.8960, 18.6123, 16.4995, 14.0861, 11.0914,
         8.8842, 6.3834, 3.7998, 0]

delta = 0.38
DIV_min = 0.79

abandon_rule1 = []
abandon_rule2 = []
abandon_rule3 = []
for i in range(8192):
    delay_sel = []
    delay_diff = []
    abandon = 0

    #obtain the corresponding delay differences for decision rule1 and rule2
    for j in range(len(chal[i])):
        if (chal[i][j] == '1'):
            delay_sel.append(delay[j])
    diff_num = int(len(delay_sel) / 2)
    for j1 in range(diff_num):
        delay_diff.append((delay_sel[2 * j1] - delay_sel[2 * j1 + 1]) / 2)
    #obtain the corresponding delay differences for decision rule3
    delay_diff1 = []
    for j2 in range(len(delay_sel) - 1):
        delay_diff1.append((delay_sel[j2] - delay_sel[j2 + 1]) / 2)

    # //////////////////////decision rule1
    p = 1
    while (delay_diff[-1] / p > DIV_min):
        div_init = delay_diff[-1] / p
        abandon = 0
        if (p % 2 == 1):
            res_even = []
            div_even = []
            for k in range(len(delay_diff) - 1):
                if (delay_diff[k] % div_init >= (div_init / 2)):
                    res_value = div_init - delay_diff[k] % div_init
                    res_even.append(res_value)
                    div_even.append(int(delay_diff[k] / div_init) + 1)
                else:
                    res_value = delay_diff[k] % div_init
                    res_even.append(res_value)
                    div_even.append(int(delay_diff[k] / div_init))

        if (all(v < delta for v in res_even)):
            if(sum(div_even) % 2 == 0):
                abandon = 1
                abandon_rule1.append(i)
            else:
                abandon = 0
            break
        p+=1

    # /////////////////////////decision rule2
    p=1
    while (delay_diff[-1] / p > DIV_min):
        div_init = delay_diff[-1] / p
        abandon = 0
        res_odd = []
        div_odd = []
        for k1 in range(len(delay_diff) - 1):
            if (delay_diff[k1] % div_init >= (div_init / 2)):
                res_value = div_init - delay_diff[k1] % div_init
                res_odd.append(res_value)
                div_odd.append(int(delay_diff[k1] / div_init) + 1)
            else:
                res_value = delay_diff[k1] % div_init
                res_odd.append(res_value)
                div_odd.append(int(delay_diff[k1] / div_init))

        if (all(v1 < delta for v1 in res_odd)):
            if (sum(div_odd) % 2 == 1):
                abandon = 1
                abandon_rule2.append(i)
            else:
                abandon = 0
            break
        p+=1

    # //////////////////////decision rule3
    p=1
    while (delay_diff[-1] / p > DIV_min):
        div_init = delay_diff[-1] / p
        abandon = 0
        if (p % 2 == 1):
            res = []
            div = []
            for k2 in range(len(delay_diff) - 1):
                if (delay_diff[k2] % div_init >= (div_init / 2)):
                    res_value = div_init - delay_diff[k2] % div_init
                    res.append(res_value)
                    div.append(int(delay_diff[k2] / div_init) + 1)
                else:
                    res_value = delay_diff[k2] % div_init
                    res.append(res_value)
                    div.append(int(delay_diff[k2] / div_init))

            rule12 = []
            for n in range(len(res)):
                if (res[n] < delta):
                    rule12.append(1)
                else:
                    rule12.append(0)

            rule3 = []
            rule3_1 = []
            for m in range(int((len(delay_diff1) - 3) / 2)):
                h = delay_diff1[2 * m] % (2 * div_init)
                res1 = delay_diff1[2 * m + 1] % div_init
                if (res1 > div_init / 2):
                    res1 = div_init - res1
                if((delay_diff1[2 * m + 2] + h - div_init)>0):
                    res2 = (delay_diff1[2 * m + 2] + h - div_init) % div_init
                    div2 = int((delay_diff1[2 * m + 2] + h - div_init) / div_init)
                    if (res2 > div_init / 2):
                        res2 = div_init - res2
                        div2 = div2 + 1
                else:
                    res2 = abs(delay_diff1[2 * m + 2] + h - div_init)
                    div2 = 0

                condition1 = ((h > 0) and (h < div_init) and (res1 < delta) and (res2 < delta) and (div2 % 2 == 0))
                condition1_1 = ((h > 0) and (h < div_init) and (res1 < delta) and (res2 < delta) and (div2 % 2 == 1))

                if((delay_diff1[2 * m + 1] - div_init + h)>0):
                    res1 = (delay_diff1[2 * m + 1] - div_init + h) % div_init
                    if (res1 > div_init / 2):
                        res1 = div_init - res1
                else:
                    res1 = abs(delay_diff1[2 * m + 1] - div_init + h)
                if((delay_diff1[2 * m + 2] - h)>0):
                    res2 = (delay_diff1[2 * m + 2] - h) % div_init
                    div2 = int((delay_diff1[2 * m + 2] - h) / div_init)
                    if (res2 > div_init / 2):
                        res2 = div_init - res2
                        div2 = div2 + 1
                else:
                    res2 = abs(delay_diff1[2 * m + 2] - h)
                    div2 = 0

                condition2 = ((h > 0) and (h < div_init) and (res1 < delta) and (res2 < delta) and (div2 % 2 == 1))
                condition2_1 = ((h > 0) and (h < div_init) and (res1 < delta) and (res2 < delta) and (div2 % 2 == 0))

                res1 = delay_diff1[2 * m + 1] % div_init
                if (res1 > div_init / 2):
                    res1 = div_init - res1
                if((delay_diff1[2 * m + 2] - 2 * div_init + h)>0):
                    res2 = (delay_diff1[2 * m + 2] - 2 * div_init + h) % div_init
                    div2 = int((delay_diff1[2 * m + 2] - 2 * div_init + h) / div_init)
                    if (res2 > div_init / 2):
                        res2 = div_init - res2
                        div2 = div2 + 1
                else:
                    res2 = abs(delay_diff1[2 * m + 2] - 2 * div_init + h)
                    div2 = 0

                condition3 = ((h > div_init) and (h < 2 * div_init) and (res1 < delta) and (res2 < delta) and (
                            div2 % 2 == 1))
                condition3_1 = ((h > div_init) and (h < 2 * div_init) and (res1 < delta) and (res2 < delta) and (
                            div2 % 2 == 0))

                if((delay_diff1[2 * m + 1] - 2 * div_init + h)>0):
                    res1 = (delay_diff1[2 * m + 1] - 2 * div_init + h) % div_init
                    if (res1 > div_init / 2):
                        res1 = div_init - res1
                else:
                    res1 = abs(delay_diff1[2 * m + 1] - 2 * div_init + h)
                if((delay_diff1[2 * m + 2] - h + div_init)>0):
                    res2 = (delay_diff1[2 * m + 2] - h + div_init) % div_init
                    div2 = int((delay_diff1[2 * m + 2] - h + div_init) / div_init)
                    if (res2 > div_init / 2):
                        res2 = div_init - res2
                        div2 = div2 + 1
                else:
                    res2 = abs(delay_diff1[2 * m + 2] - h + div_init)
                    div2 = 0

                condition4 = ((h > div_init) and (h < 2 * div_init) and (res1 < delta) and (res2 < delta) and (
                            div2 % 2 == 0))
                condition4_1 = ((h > div_init) and (h < 2 * div_init) and (res1 < delta) and (res2 < delta) and (
                            div2 % 2 == 1))

                if ((condition1 or condition2 or condition3 or condition4) == 1):
                    rule3.append(1)
                else:
                    rule3.append(0)

                if ((condition1_1 or condition2_1 or condition3_1 or condition4_1) == 1):
                    rule3_1.append(1)
                else:
                    rule3_1.append(0)

            rule3.append(0)
            rule3_1.append(0)

            rule12_pure = []
            for r in range(len(rule12)):
                if ((rule12[r] == 1) and (rule3[r] == 0) and (rule3_1[r] == 0)):
                    rule12_pure.append(1)
                else:
                    rule12_pure.append(0)

            rule3_pure = []
            rule3_1_pure = []
            for r1 in range(len(rule12)):
                if ((rule12[r1] == 0) and (rule3[r1] == 1)):
                    rule3_pure.append(1)
                else:
                    rule3_pure.append(0)

                if ((rule12[r1] == 0) and (rule3_1[r1] == 1)):
                    rule3_1_pure.append(1)
                else:
                    rule3_1_pure.append(0)

            sum12 = 0
            sum3 = 0
            sum3_1 = 0
            rk = 0
            while (rk < len(rule12)):
                if ((rule12[rk] == 0) and (rule3_pure[rk] == 0) and (rule3_1_pure[rk] == 0)):
                    break
                elif (rule12[rk] == 1):
                    sum12 += div[rk]
                    rk += 1
                elif (rule3_pure[rk] == 1):
                    rk += 2
                    sum3 += 1
                elif (rule3_1_pure[rk] == 1):
                    rk += 2
                    sum3_1 += 1

            sum12a = 0
            sum3a = 0
            sum3a_1 = 0
            rka = 0
            while (rka < len(rule12)):
                if ((rule12_pure[rka] == 0) and (rule3[rka] == 0) and (rule3_1[rka] == 0)):
                    break
                elif (rule12_pure[rka] == 1):
                    sum12a += div[rka]
                    rka += 1
                elif (rule3[rka] == 1):
                    rka += 2
                    sum3a += 1
                elif (rule3_1[rka] == 1):
                    rka += 2
                    sum3a_1 += 1

            if((rk == len(rule12)) or (rka == len(rule12))):
                if (((rk == len(rule12)) and ((sum12 + sum3) % 2 == 0)) or (
                        (rka == len(rule12)) and ((sum12a + sum3a) % 2 == 0))):
                    abandon = 1
                    abandon_rule3.append(i)
                break

        p += 1

rule_all=abandon_rule1+abandon_rule2+abandon_rule3
print("len_all",len(list(set(rule_all))))

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

print("fit_rule1", fit_rule1)
print("unfit_rule1", unfit_rule1)
print("fit_rule2", fit_rule2)
print("unfit_rule2", unfit_rule2)
print("fit_rule3", fit_rule3)
print("unfit_rule3", unfit_rule3)

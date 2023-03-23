import numpy as np

#obtain the binary feedback coefficients. 
#In our test, the feedback coefficients are obtained from c_special.txt, which is consistent with the data transferred from computer to the FPGA
data = np.loadtxt("./c_special.txt", dtype=int)

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

    #x_msb: bit13(MSB) of the 14-bit feedback coefficient, which is determined by the other 13 bits to make sure the even HW of feedback coefficient
    x_msb = 0
    X_bin = ''
    for k in range(0, 13):
        x_msb = x_msb ^ int(d_last[k], 2)
    #the extra `1` value in X_bin representing the rightmost feedback wire at the feedback circuit
    X_bin += '1'
    X_bin += d_last
    X_bin += str(x_msb)
    # the extra `1` value in X_bin representing the leftmost feedback wire at the feedback circuit
    X_bin += '1'
    d_la.append(X_bin)

chal = [t[::-1] for t in d_la]

#the oscillation periods for all the loops measured from an FPGA implementation
delay = [34.4923, 34.4923, 32.3499, 29.7053, 27.9767, 25.1206, 23.4170, 20.8960,
         18.6123, 16.4995, 14.0861, 11.0914, 8.8842, 6.3834, 3.7998, 0]
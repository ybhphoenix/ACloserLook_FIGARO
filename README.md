Introduction
===

This project corresponds to the paper entitled "A Closer Look at the Chaotic Ring Oscillators based TRNG Design". <br />
It mainly includes:

### 1) model.sp:
One example of the gate-level model as described in Section 4 in the paper, which satisfies Decision rule1 with the feedback polynomial f(x)=x^15+x^14+x^6+x^3+x+1.<br />
The configuration and utilization of the model are described as follows:<br />
a) Transient noise analysis is performed on the output signal of the ring oscillator to obtain the simulated waveforms for the cause analysis of periodic oscillations.<br />
b) The simulation is conducted under the temperature 25 degrees Celsius and voltage vdd=1.5V.<br />
c) Two library files "cln28hpcp_1d8_elk_v1d0_2p9_shrink0d9_embedded_usage.l" and "tcbn28hpcplusbwp12t30p140_170a.spi" are included for the simulation under the technology TSMC28nm. Other technology files can be adopted to replace the two library files, where a consistent simulated result can be obtained with the same delay relationships.<br />
d) The aspect ratios of instantiated cells in the file "tcbn28hpcplusbwp12t30p140_170a.spi" are adjusted to realize the delay relationships measured from FPGA implementation. In our test, the simulated oscillation period of each loop is 10% of the corresponding measured value in Table I in the paper, with the same delay relationships.<br />
e) The input connections of some AND gates are determined by the applied feedback polynomial to implement closed or open feedback paths.<br />
f) After the start signal is set to 1, the simulated ring oscillator starts oscillating.<br />


### 2) original-data.xlsx:
The original data measured from FPGA implementation for all the 8192 feedback polynomials, which is divided into three categories: continuous periodic oscillation, intermittent periodic oscillation and chaotic oscillation. The binary challenges, min-entropy, Lyapunov exponents and the numbers of different states in 10000 samples are included in this file. <br />
The summary graphs displayed in the paper for all the feedback polynomials can be obtained from the original data. The entropy results are displayed with challenegs as the x-axis, and the Lyapunov exponent results are shown with the min-entropy as the x-axis. The summary graphs can verify the effectiveness of selected threshold and modified detector to detect periodic oscillations for all the feedback polynomials, as proposed in Subsection 3.2.<br />

### 3) python code:
The python script to implement the proposed Algorithm 2 in Subsection 6.1 to select a suitable feedback polynomial without periodic oscillation.



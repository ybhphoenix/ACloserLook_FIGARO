Introduction
===

This artifact corresponds to the paper entitled "A Closer Look at the Chaotic Ring Oscillators based TRNG Design". One SPICE simulation model (model.sp), one dataset (original-data.xlsx) and one Python code to select a proper feedback polynomial are included in this artifact.

### 1  Simulation model:
One SPICE simulation example of the gate-level model as described in Section 4 of the paper is provided in the .sp file: model.sp, which satisfies Decision rule1 with the feedback polynomial f(x)=x^15+x^14+x^6+x^3+x+1.

#### 1.1  Configuration

##### 1.1.1  Environmental conditions
	
The simulation is conducted under the temperature of 25 degrees Celsius and voltage vdd=1.5V.

##### 1.1.2  Library
	
The model is simulated with the technology TSMC 28nm. Two library files "cln28hpcp_1d8_elk_v1d0_2p9_shrink0d9_embedded_usage.l" and "tcbn28hpcplusbwp12t30p140_170a.spi" are included for the simulation, which are commercial libraries and cannot be uploaded. Other technology files can be adopted to replace the two library files, where a consistent simulated result can be obtained with the same delay relationships. For example, we have conducted the simulation with the same delay relationships under the technology GF22nm and obtained consistent results.

#### 1.2  Utilization

After the configuration of environmental conditions and library, the utilization steps are listed as follows:
	a) Adjust the aspect ratios of instantiated cells in the file "tcbn28hpcplusbwp12t30p140_170a.spi" to realize the delay relationships measured from FPGA or ASIC implementation. The simulated oscillation period of each loop in the example model is about 10% of the corresponding measured value in Table I in the paper, with the same delay relationships.
	b) The input connections of some AND gates are determined by the applied feedback polynomial to implement closed or open feedback paths.
	c) The start signal is configured as a pwl (piece-wise linear) input stimulus to enable the oscillation.
	d) Transient noise analysis is performed on the output signal of the ring oscillator to obtain the simulated waveforms for the cause analysis of periodic oscillations.
	e) The tool HSPICE is applied to run the model with the instruction: hspice model.sp. The version of HSPICE used in this paper is HSPICE Version Q-2020.03-3.
	
### 2  Dataset

A dataset original-data.xlsx is provided, which includes the original data measured from an FPGA implementation for all the 8192 feedback polynomials. In this file, the data is divided into three categories based on the oscillation situation: continuous periodic oscillation, intermittent periodic oscillation and chaotic oscillation. The binary feedback coefficients, min-entropy, Lyapunov exponents and the numbers of different states in 10000 samples are listed.

The summary graphs Figure 7 and Figure 9 displayed in the paper for all the feedback polynomials can be obtained from the original data. The entropy results are displayed with the feedback coefficient as the x-axis, and the Lyapunov exponent results are shown with the min-entropy as the x-axis. The summary graphs can verify the effectiveness of the selected threshold and modified detector to detect periodic oscillations for all the feedback polynomials, as proposed in Subsection 3.2 of the paper.

### 3  python code:
The python script to implement the proposed Algorithm 2 in Subsection 6.1 to select a suitable feedback polynomial without periodic oscillation.



Introduction
===

This artifact corresponds to the paper entitled "A Closer Look at the Chaotic Ring Oscillators based TRNG Design". One SPICE simulation model (model.sp), one dataset and corresponding processing scripts (directory: original data) and one Python code to select a proper feedback polynomial are included in this artifact. 

### 1  Simulation model:
One SPICE simulation example of the gate-level model as described in Section 4 of the paper is provided in the .sp file: model.sp, which satisfies Decision rule1 with the feedback polynomial f(x)=x^15+x^14+x^6+x^3+x+1.

#### 1.1  Configuration

##### 1.1.1  Environmental conditions
	
The simulation is conducted under the temperature of 25 degrees Celsius and voltage vdd=1.5V.

##### 1.1.2  Library
	
The model is simulated with the technology TSMC 28nm. Two library files "cln28hpcp_1d8_elk_v1d0_2p9_shrink0d9_embedded_usage.l" and "tcbn28hpcplusbwp12t30p140_170a.spi" are necessary for the simulation but are not included because they are commercial libraries. Other technology files can be adopted to replace the two library files, where a consistent simulated result can be obtained with the same delay relationships and similar filtering or drive capabilities. After replacing the library files, the instantiated cells in the simulated circuit should also be replaced by the corresponding cells defined in the replaced files. For example, we have conducted the simulation with the same delay relationships and similar filtering or drive capabilities under the technology GF22nm and obtained consistent results.

#### 1.2  Utilization

After the configuration of environmental conditions and library, the utilization steps are listed as follows:<br />
        a) Construct the ring oscillator circuit by instantiating the cells in the file "tcbn28hpcplusbwp12t30p140_170a.spi", as displayed in Figure 12 in the paper where buffers can also be implemented by AND gates with one input tied to VDD to imitate the delays of routes. The input connections of the AND gates instantiated to implement switches are determined by the applied feedback polynomial to implement closed or open feedback paths, with one input tied to GND or VDD.<br />
	b) Adjust the aspect ratios or the number of instantiated cells to realize similar filtering or drive capabilities and the same delay relationships measured from FPGA or ASIC implementation. The delay values can be obtained by measuring the oscillation periods of equivalent classical ring oscillators with the feedback polynomial f(x)=x^15+x^14+x^m+1 (m=1,2,...,13). The simulated oscillation period of each loop in the example model is about 10% of the corresponding measured value in Table I in the paper, with the same delay relationships.<br />
	c) The start signal as one input signal of the NAND gate is configured as a pwl (piece-wise linear) input stimulus to enable the oscillation.<br />
	d) Transient noise analysis is performed on the output signal of the ring oscillator to obtain the simulated waveforms for the cause analysis of periodic oscillations.<br />
	e) The tool HSPICE is applied to run the model with the instruction: hspice model.sp. The version of HSPICE used in this paper is HSPICE Version Q-2020.03-3.<br />
	
### 2  Dataset

A dataset and corresponding processing scripts are provided in the directory "original data", which includes the original data measured from an FPGA implementation of a GARO for all the 8192 feedback polynomials and two scripts to obtain the summary graphs Figure 7(b) and Figure 9(b) in the paper. The data acquisition and processing for FIRO are similar to GARO, with the same classifications in Figure 7(a) and Figure 9(a) with Figure 7(b) and Figure 9(b). In the directory "data", there are three .csv files corresponding to three categories divided based on the oscillation situation: continuous periodic oscillation (continuous_periodic_oscillation_data.csv), intermittent periodic oscillation (intermittent_periodic_oscillation_data.csv) and chaotic oscillation (chaotic_periodic_oscillation_data.csv). The binary feedback coefficients, min-entropy, Lyapunov exponents and the numbers of different states in 10000 samples are listed. In the directory "scripts", there are two scripts entropy_plt_garo.py and lya_plt_garo.py for the data processing to obtain Figure 7(b) and Figure 9(b) respectively.

In the obtained summary graphs, the entropy results are displayed with the feedback coefficient as the x-axis, and the Lyapunov exponent results are shown with the min-entropy as the x-axis. The categories in Figure 7(b) are consistent with the original data, where "mixed" corresponds to intermittent periodic oscillations. In Figure 9(b), the mixed situations are divided from intermittent periodic oscillations, where the duration of chaotic oscillation accounts for [75%, 100%) of the sampling time. The remaining intermittent periodic oscillations and continuous periodic oscillations are classified as the periodic situations. To differentiate the mixed situations in Figure 7(b) and Figure 9(b), the duration of chaotic oscillation is listed in intermittent_periodic_oscillation_data.csv, where the mixed situations in Figure 9 are also identified by ticking to improve readability.

The summary graphs can verify the effectiveness of the selected threshold and modified detector to detect periodic oscillations for all the feedback polynomials, as proposed in Subsection 3.2 of the paper.

### 3  python code:
The python script to implement the proposed Algorithm 2 in Subsection 6.1 to select a suitable feedback polynomial without periodic oscillation, which is described in detail in README.md in the directory "python code".



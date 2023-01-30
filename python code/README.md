Introduction
===

A Python script rule_test.py is provided to implement the proposed Algorithm 2 in Subsection 6.1 to select a suitable feedback polynomial without periodic oscillation. We have utilized Python 3.7 to run the script and check whether all the periodic oscillations with entropy loss are detected and filtered successfully.

### 1  Input

#### 1.1  Feedback coefficients

The binary feedback coefficients should be inputted to determine the oscillator structure and corresponding delay relationships, which are represented by the variable: chal. The specific feedback coefficients in the provided script are obtained from the file: c_special.txt. 
The file c_special.txt includes the bit12-bit0 of the feedback coefficients for all the 8192 feedback polynomials. The 13 bits of the feedback coefficients are split into two integer values to be transmitted by Nodejs. The first and second values represent bit5-bit12 and bit0-bit4 respectively. Another bit bit13 is determined by the bit12-bit0 to avoid fixed points.

#### 1.2  Oscillation periods

Before applying Algorithm 2 to evaluate the inputted feedback coefficients, we should obtain the corresponding delay differences from the inputted oscillation periods of all the closed loops. The inputted oscillation periods are measured from actual implementation and represented by the variable: delay. 

### 2  Output

The output variable abandon represents whether the corresponding feedback polynomial should be filtered with possible periodic oscillation. If abandon=1, the corresponding feedback polynomial should be filtered. Otherwise, the corresponding feedback polynomial can be applied to build a robust TRNG.

### 3  Configuration parameters
There are two parameters to configure the evaluation algorithm: delta and DIV_min. The selection of delta and DIV_min is making a trade-off between missed detection and false alarm. All the periodic oscillations with entropy loss obtained from an FPGA implementation in this paper can be detected and filtered with delta=0.38 and DIV_min=0.79. Also, there is still enough space left to select a suitable feedback polynomial without periodic oscillation.

#### 3.1  delta
The parameter delta represents the tolerable variation of delay differences for periodicity conditions only causing glitches in the specific outputs. A larger value of delta represents a looser requirement, which will cause more feedback polynomials to be detected and filtered. However, a larger value of delta brings the glitches closer to complete signals which will be maintained and propagated, and the periodic conditions will not be satisfied to cause periodic oscillations.

#### 3.2  DIV_min
The parameter DIV_min represents the minimum value of $DIV_δ$ or $DIV'_δ$. The proposed periodic conditions are easier to be satisfied with a smaller value of DIV_min, which will cause more feedback polynomials to be detected and filtered. However, a smaller value of DIV_min brings the signal of periodic oscillation closer to the glitch. Once the DIV_min is small enough, the periodic oscillation cannot be maintained and periodic behavior will not be presented.

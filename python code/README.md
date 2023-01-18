Introduction
===

The python script to implement the proposed Algorithm 2 in the paper to select a suitable feedback polynomial without periodic oscillation. The feedback polynomials with possible periodic oscillations are filtered and a large enough space is remained for the selection of feedback polynomial without periodic oscillation in this script.

### c_special.txt:
The bit12-bit0 of all the 8192 challenges, which are split into two integer values to be transmitted by nodejs. The first and second values represent bit5-bit12 and bit0-bit4 respectively. Another challenge bit bit13 is determined by the bit12-bit0 to avoid fixed points.

### rule_test.py:
the Python script to realize the proposed algorithm.  

#### input:
1. chal: the binary feedback coefficients. In our test, the feedback coefficients are obtained from c_special.txt
2. delay: the oscillation periods of all the loops measured from actual implementation. Before applying Algorithm 2 to evaluate the inputted feedback polynomial, we should obtain the corresponding delay differences from the inputted delays.

#### output:
*abandon*: if *abandon*=1, the corresponding feedback polynomial should be filtered with possible periodic oscillation.

#### configuration parameters:
1. delta: The tolerable variation of delay differences for periodicity conditions. A smaller value of delta represents a more stringent requirement, which will cause less feedback polynomials to be detected and filtered.
2. DIV_min: the minimum value of $DIV_δ$ or $DIV'_δ$. The proposed periodic conditions are easier to be satisfied with a smaller value of DIV_min, which will cause more feedback polynomials to be detected and filtered. However, a smaller value of DIV_min brings the signal of periodic oscillations closer to the glitch. Once the DIV_min is small enough, the periodic oscillation can not be maintained and periodic behavior will not be presented.

Thus, the selection of delta and DIV_min is making a trade-off between missed detection and false alarm. 
In our test, all the periodic oscillations with entropy loss can be detected and filtered with delta=0.38 and DIV_min=0.79. 
Also, there is still enough space left to select a suitable feedback polynomial without periodic oscillation.

rule_test.py:
the Python script to realize the proposed algorithm to select a suitable feedback polynomial without periodic oscillation.

input:
1. chal: the binary feedback coefficients. In our test, the feedback coefficients are obtained from c_special.txt
2. delay: the oscillation periods of all the loops obtained from actual implementation.

output:
abandon: if abandon=1, the corresponding feedback polynomial should not be selected to build a TRNG, which may enter periodic oscillation.

configuration parameters:
1. delta: The tolerable variation of delay differences for periodicity conditions. A smaller value of delta represents a more stringent requirement, 
which will cause less feedback polynomial to be detected and filtered.
2. DIV_min: the minimum value of DIVδ or DIVδ’. The proposed periodic conditions are easier to be satisfied with a smaller value of DIV_min, 
which will cause more feedback polynomials to be detected and filtered. 
However, a smaller value of DIV_min brings the signal of periodic oscillations closer to the glitch. 
Once the DIV_min is small enough, the periodic oscillation can not be maintained and periodic behavior will not be presented.

Thus, the selection of delta and DIV_min is making a trade-off between missed detection and false alarm. 
In our test, all the periodic oscillations with entropy loss can be detected and filtered with delta=0.38 and DIV_min=0.79. 
Also, there is still enough space left to select a suitable feedback polynomial without periodic oscillation.

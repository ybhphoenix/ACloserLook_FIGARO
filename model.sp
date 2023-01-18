** Generated for: hspiceD
** Generated on: Dec 16 12:56:51 2022
** Design library name: tsmc28_sim
** Design cell name: garo_351
** Design view name: schematic

.option post probe
.option runlvl=5

.GLOBAL vdd!

.PROBE TRAN
+    V(net22)
+    V(net20)
+    V(net25)
+    V(net84)
+    V(net83)
+    V(net86)
+    V(net106)
+    V(net105)
+    V(net109)
+    V(net124)
+    V(net122)
+    V(net127)
+    V(net133)

.TRAN 1e-9 150e-9 START=0.0

** transient noise analysis
.trannoise v(net133) SWEEP MONTE=1 FIRSTRUN=2
+FMAX=50G SCALE=10

.TEMP 25.0
.OPTION
+    ARTIST=2
+    INGOLD=2
+    PARHIER=LOCAL
+    PSF=2
+    macmod=1

** library files
.lib "./spice_tsmc28/SPICE/tn28clsp079/1_0_2p9/cln28hpcp_1d8_elk_v1d0_2p9_shrink0d9_embedded_usage.l" TTMacro_MOS_MOSCAP
.lib "./spice_tsmc28/SPICE/tn28clsp079/1_0_2p9/cln28hpcp_1d8_elk_v1d0_2p9_shrink0d9_embedded_usage.l" pre_simu
.inc "./spice_sim/garo_2076_morebuf/tcbn28hpcplusbwp12t30p140_170a.spi"

** Library name: tsmc28_sim
** Cell name: garo_351
** View name: schematic
xi75 vdd! net133 net134 vdd! 0 AN2D0BWP12T30P140_SIM_L1
xi74 vdd! net134 net130 vdd! 0 AN2D0BWP12T30P140_SIM_L1
xi56 vdd! net130 net5 vdd! 0 AN2D0BWP12T30P140_SIM_L1
xi55 vdd! net127 net132 vdd! 0 AN2D0BWP12T30P140_SIM_L1
xi54 vdd! net119 net122 vdd! 0 AN2D0BWP12T30P140_SIM_L2
xi53 vdd! net116 net147 vdd! 0 AN2D0BWP12T30P140_SIM_L2
xi52 vdd! net111 net113 vdd! 0 AN2D0BWP12T30P140_SIM_L3
xi51 vdd! net109 net146 vdd! 0 AN2D0BWP12T30P140_SIM_L3
xi50 vdd! net103 net105 vdd! 0 AN2D0BWP12T30P140_SIM_L4
xi49 vdd! net101 net145 vdd! 0 AN2D0BWP12T30P140_SIM_L4
xi48 vdd! net95 net97 vdd! 0 AN2D0BWP12T30P140_SIM_L5
xi47 vdd! net93 net144 vdd! 0 AN2D0BWP12T30P140_SIM_L5
xi46 vdd! net88 net90 vdd! 0 AN2D0BWP12T30P140_SIM_L6
xi45 vdd! net86 net143 vdd! 0 AN2D0BWP12T30P140_SIM_L6
xi44 vdd! net81 net83 vdd! 0 AN2D0BWP12T30P140_SIM_L7
xi43 vdd! net79 net142 vdd! 0 AN2D0BWP12T30P140_SIM_L7
xi42 vdd! net73 net75 vdd! 0 AN2D0BWP12T30P140_SIM_L8
xi41 vdd! net70 net141 vdd! 0 AN2D0BWP12T30P140_SIM_L8
xi40 vdd! net65 net67 vdd! 0 AN2D0BWP12T30P140_SIM_L9
xi39 vdd! net63 net140 vdd! 0 AN2D0BWP12T30P140_SIM_L9
xi38 vdd! net57 net59 vdd! 0 AN2D0BWP12T30P140_SIM_L10
xi37 vdd! net55 net139 vdd! 0 AN2D0BWP12T30P140_SIM_L10
xi36 vdd! net49 net51 vdd! 0 AN2D0BWP12T30P140_SIM_L11
xi35 vdd! net47 net10 vdd! 0 AN2D0BWP12T30P140_SIM_L11
xi34 vdd! net41 net43 vdd! 0 AN2D0BWP12T30P140_SIM_L12
xi33 vdd! net39 net138 vdd! 0 AN2D0BWP12T30P140_SIM_L12
xi32 vdd! net35 net37 vdd! 0 AN2D0BWP12T30P140_SIM_L13
xi31 vdd! net33 net135 vdd! 0 AN2D0BWP12T30P140_SIM_L13
xi30 vdd! net27 net29 vdd! 0 AN2D0BWP12T30P140_SIM_L14
xi29 vdd! net25 net137 vdd! 0 AN2D0BWP12T30P140_SIM_L14
xi0 net5 vdd! net22 vdd! 0 AN2D0BWP12T30P140_SIM
xi13 net5 vdd! net124 vdd! 0 AN2D0BWP12T30P140_SIM
xi12 net5 0 net114 vdd! 0 AN2D0BWP12T30P140_SIM
xi11 net5 vdd! net106 vdd! 0 AN2D0BWP12T30P140_SIM
xi10 net5 0 net98 vdd! 0 AN2D0BWP12T30P140_SIM
xi9 net5 0 net91 vdd! 0 AN2D0BWP12T30P140_SIM
xi8 net5 vdd! net84 vdd! 0 AN2D0BWP12T30P140_SIM
xi7 net5 0 net76 vdd! 0 AN2D0BWP12T30P140_SIM
xi6 net5 0 net68 vdd! 0 AN2D0BWP12T30P140_SIM
xi5 net5 0 net60 vdd! 0 AN2D0BWP12T30P140_SIM
xi4 net5 0 net52 vdd! 0 AN2D0BWP12T30P140_SIM
xi3 net5 0 net44 vdd! 0 AN2D0BWP12T30P140_SIM
xi2 net5 0 net38 vdd! 0 AN2D0BWP12T30P140_SIM
xi1 net5 0 net30 vdd! 0 AN2D0BWP12T30P140_SIM
xi27 net22 net20 net25 vdd! 0 XOR2D0BWP12T30P140_SIM
xi26 net30 net29 net33 vdd! 0 XOR2D0BWP12T30P140_SIM
xi25 net38 net37 net39 vdd! 0 XOR2D0BWP12T30P140_SIM
xi24 net44 net43 net47 vdd! 0 XOR2D0BWP12T30P140_SIM
xi23 net52 net51 net55 vdd! 0 XOR2D0BWP12T30P140_SIM
xi22 net60 net59 net63 vdd! 0 XOR2D0BWP12T30P140_SIM
xi21 net68 net67 net70 vdd! 0 XOR2D0BWP12T30P140_SIM
xi20 net76 net75 net79 vdd! 0 XOR2D0BWP12T30P140_SIM
xi19 net84 net83 net86 vdd! 0 XOR2D0BWP12T30P140_SIM
xi18 net91 net90 net93 vdd! 0 XOR2D0BWP12T30P140_SIM
xi17 net98 net97 net101 vdd! 0 XOR2D0BWP12T30P140_SIM
xi16 net106 net105 net109 vdd! 0 XOR2D0BWP12T30P140_SIM
xi15 net114 net113 net116 vdd! 0 XOR2D0BWP12T30P140_SIM
xi14 net124 net122 net127 vdd! 0 XOR2D0BWP12T30P140_SIM
xi28 net136 net20 vdd! 0 BUFFD0BWP12T30P140_SIM_L15
xi70 net5 net136 vdd! 0 INVD0BWP12T30P140_SIM_L15
xi69 net137 net27 vdd! 0 INVD0BWP12T30P140_SIM
xi68 net135 net35 vdd! 0 INVD0BWP12T30P140_SIM
xi67 net138 net41 vdd! 0 INVD0BWP12T30P140_SIM
xi66 net10 net49 vdd! 0 INVD0BWP12T30P140_SIM
xi65 net139 net57 vdd! 0 INVD0BWP12T30P140_SIM
xi64 net140 net65 vdd! 0 INVD0BWP12T30P140_SIM
xi63 net141 net73 vdd! 0 INVD0BWP12T30P140_SIM
xi62 net142 net81 vdd! 0 INVD0BWP12T30P140_SIM
xi61 net143 net88 vdd! 0 INVD0BWP12T30P140_SIM
xi60 net144 net95 vdd! 0 INVD0BWP12T30P140_SIM
xi59 net145 net103 vdd! 0 INVD0BWP12T30P140_SIM
xi58 net146 net111 vdd! 0 INVD0BWP12T30P140_SIM
xi57 net147 net119 vdd! 0 INVD0BWP12T30P140_SIM
xi71 net132 start net133 vdd! 0 ND2D0BWP12T30P140_SIM
vstart start 0 pwl 0 0 2n 0 2.01n 1.5 TD=0
vvdd! vdd! 0 DC=1.5
.END

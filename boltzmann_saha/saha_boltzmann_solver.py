import numpy as np
import matplotlib.pyplot as plt
from functions.functions import boltzmann_ratio, saha_ratio

# エネルギー差 [eV]
dE = 10.2
x = 13.6

# 温度範囲 [K]
T = np.linspace(1000, 50000, 1000)

# 統計重率
g_0 = 2
g_1 = 8

# 分配関数
U_1 = 1
U_2 = 1

# ボルツマン分布
N1_N0 = boltzmann_ratio(T, dE, g_0, g_1)

# サハ分布
# G型（6000K）での電子圧を仮定
T_G = 6000
Pe_G = 1.2  # 電子圧 [N/m^2]
NIo_N1N0_G = saha_ratio(U_1, U_2, T_G, x, Pe_G)

# A型（10000K）での電子圧を仮定
T_A = 10000
Pe_A = 14  # 電子圧 [N/m^2]
NIo_N1N0_A = saha_ratio(U_1, U_2, T_A, x, Pe_A)

# B型（15000K）での電子圧を仮定
T_B = 15000
Pe_B = 57.5  # 電子圧 [N/m^2]
NIo_N1N0_B = saha_ratio(U_1, U_2, T_B, x, Pe_B)
print("G型(6000K)でのサハ分布 N2/N1:", NIo_N1N0_G)
print("A型(10000K)でのサハ分布 N2/N1:", NIo_N1N0_A)
print("B型(15000K)でのサハ分布 N2/N1:", NIo_N1N0_B)

# グラフ描画
plt.figure(figsize=(8, 5))
plt.plot(T, N1_N0, linewidth=2)
#plt.plot(T_G, NIo_N1N0_G, 'ro', label='G-type (6000K)')
#plt.plot(T_A, NIo_N1N0_A, 'go', label='A-type (10000K)')
#plt.plot(T_B, NIo_N1N0_B, 'bo', label='B-type (15000K)')
plt.xlabel('Temperature T [K]')

plt.ylabel('N1 / N0')
plt.title('Boltzmann Distribution (Hydrogen n=1 → n=2)')

plt.grid(True)
plt.yscale('log')
plt.xscale('log')
plt.show()
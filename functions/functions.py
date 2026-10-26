import numpy as np
import constants.constants

#ボルツマン分布
def boltzmann_ratio(T, dE, g_i, g_j):
    """
    ボルツマン分布の比率を計算する関数
    ---parameters
    T:温度[K]
    dE:準位間エネルギー差[eV]
    g_i:下位準位の統計重率
    g_j:上位準位の統計重率
    """
    return (g_j / g_i) * np.exp(-dE / (constants.constants.kB_eV * T))

#サハ分布
def saha_ratio(U_1, U_2, T, x, Pe):
    """
    サハ分布(N_2(1回電離の原子数)÷N_1(中性原子の数))を求める関数
    ---parameters
    U_1:中性原子の分配関数
    U_2:1回電離の分配関数
    T:温度[K]
    x:電離エネルギー[eV]
    Pe:電子圧[N/m^2]
    """
    return 2 * (U_2 / U_1) * (2 * np.pi * constants.constants.m_e)**(3/2) * (constants.constants.kB_J * T )**(5/2) *(1/constants.constants.h**3)* (1 / Pe) * np.exp(-x / (constants.constants.kB_eV * T))
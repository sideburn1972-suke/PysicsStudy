from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
from config import DATA_DIR, HR_DIAGRAM_DIR, CONSTANTS_DIR
import numpy as np
import constants.constants
import pandas as pd

original_file = DATA_DIR / "main_sequence_stars.csv"

print(original_file)

df = pd.read_csv(original_file)
# 必要な列だけ取り出して列名を変更
df_new =df[["SpT", "B-V", "U-B", "Teff", "Mv", "Mbol", "BCv", "Msun", "R_Rsun"]].rename(
    columns={
        "SpT": "スペクトル型(SpT)",
        "B-V": "B-V色指数",
        "U-B": "U-B色指数",
        "Teff": "有効温度(Teff)",
        "Mv": "実視絶対等級(Mv)",
        "Mbol": "輻射絶対等級(Mbol)",
        "BCv": "色指数補正(BCv)",
        "Msun": "太陽質量(Msun)",
        "R_Rsun": "太陽半径(Rsun)"
    }
)


df_new["太陽半径相当輻射絶対等級(Mbol_Sun)"] =constants.constants.M_sun - 5 * (np.log10(1)) - 10*np.log10(df_new["有効温度(Teff)"] / constants.constants.T_sun) 
df_new["計算上の輻射絶対等級(Mbol_calc)"] =constants.constants.M_sun - 5 * (np.log10(df_new["太陽半径(Rsun)"])) - 10*np.log10(df_new["有効温度(Teff)"] / constants.constants.T_sun) 
df_new["色指数補正後実視絶対等級(Mv-BCv)"] =df_new["輻射絶対等級(Mbol)"] - df_new["色指数補正(BCv)"]
df_new["光度(L/Lsun)"] = (10 ** (-0.4* (df_new["輻射絶対等級(Mbol)"] - constants.constants.M_sun ) ))

# 新しいCSVとして保存
df_new.to_csv(HR_DIAGRAM_DIR / "main_sequence_stars.csv", index=False, encoding="utf-8-sig")

print("CSVを保存しました")

#プロジェクトルート、パスなどの基本設定
from pathlib import Path
import sys
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
from config import DATA_DIR, HR_DIAGRAM_DIR, CONSTANTS_DIR

#必要なライブラリのインポート
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#日本語フォントの指定
plt.rcParams["font.family"] = "Yu Gothic" 
plt.rcParams["axes.unicode_minus"] = False #マイナスの文字化け対策

# CSV読込
csv_file = HR_DIAGRAM_DIR / "main_sequence_stars.csv"
df = pd.read_csv(csv_file)



# グラフ作成
plt.figure(figsize=(10, 6))

plt.scatter(
    df["太陽質量(Msun)"],
    df["光度(L/Lsun)"],
    label="質量 vs 光度(データよりプロット)",
    color="blue"
)

#　１次関数にフィッティングするための準備
df_fit = df[["太陽質量(Msun)", "光度(L/Lsun)"]].dropna()

x=np.log10(df_fit["太陽質量(Msun)"])
y=np.log10(df_fit["光度(L/Lsun)"]) 

a,b = np.polyfit(x, y, 1)  # 1次関数でフィッティング

x_fit = np.linspace(min(x), max(x), 100)
y_fit = a * x_fit + b
print(f"L ∝ M^{a:.2f}")
plt.plot(10**x_fit, 10**y_fit, color="red", linewidth=2,label=f"L ∝ M^{a:.2f}(フィッティング結果)")
#plt.plot    (x_fit, y_fit, color="red") 

plt.xscale("log")
plt.yscale("log")
plt.xlabel("質量 (Msun)")
plt.ylabel("光度 (L/Lsun)")
plt.title("質量と光度の関係")

plt.grid(True)
plt.legend()
plt.tight_layout()

plt.show()
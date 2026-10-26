#プロジェクトルート、パスなどの基本設定
from pathlib import Path
import sys
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
from config import DATA_DIR, HR_DIAGRAM_DIR, CONSTANTS_DIR

#必要なライブラリのインポート
import pandas as pd
import matplotlib.pyplot as plt

#日本語フォントの指定
plt.rcParams["font.family"] = "Yu Gothic" 
plt.rcParams["axes.unicode_minus"] = False #マイナスの文字化け対策

csv_file = HR_DIAGRAM_DIR / "main_sequence_stars.csv"

df = pd.read_csv(csv_file)

plt.figure(figsize=(10, 8))

# -------------------------
# 質量 vs 半径
# -------------------------
plt.subplot(2, 1, 1)

plt.scatter(
    df["太陽質量(Msun)"],
    df["太陽半径(Rsun)"],
    color="blue"
)

plt.xscale("log")
plt.yscale("log")

plt.grid(True)
plt.title("質量と半径の関係")
plt.xlabel("質量 (Msun)")
plt.ylabel("半径 (Rsun)")

# -------------------------
# 質量 vs 温度
# -------------------------
plt.subplot(2, 1, 2)

plt.scatter(
    df["太陽質量(Msun)"],
    df["有効温度(Teff)"],
    color="red"
)

plt.xscale("log")
plt.yscale("log")

plt.grid(True)
plt.title("質量と有効温度の関係")
plt.xlabel("質量 (Msun)")
plt.ylabel("有効温度 (K)")

plt.tight_layout()
plt.show()
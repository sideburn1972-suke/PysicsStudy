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

# CSV読込
csv_file = HR_DIAGRAM_DIR / "main_sequence_stars.csv"
df = pd.read_csv(csv_file)

# グラフ作成
plt.figure(figsize=(10, 6))

plt.scatter(
    df["有効温度(Teff)"],
    df["輻射絶対等級(Mbol)"],
    label="実際の輻射絶対等級Mbol",
    color="blue"
)

plt.scatter(
    df["有効温度(Teff)"],
    df["太陽半径相当輻射絶対等級(Mbol_Sun)"],
    label="太陽半径相当の輻射絶対等級Mbol_Sun",
    color="red"
)

# HR図の慣例
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()

plt.xscale("log")
plt.xlabel("有効温度 (K)")
plt.ylabel("輻射絶対等級")
plt.title("HR図")

plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
#EEM_dwarf_UBVIJHK_colors_Teff.txtをmain_sequence_stars.csvに変換する

import pandas as pd
from pathlib import Path

base_dir = Path(__file__).parent
txt_file = base_dir / "EEM_dwarf_UBVIJHK_colors_Teff.txt"

print(txt_file)

df = pd.read_csv(
    txt_file,
    sep=r"\s+",
    comment="#",
    na_values=["...", "....", "....."],
    engine="python"   
    )

print(df.dtypes)
df.to_csv(base_dir / "main_sequence_stars.csv", index=False)

print("CSV出力完了")
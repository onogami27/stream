import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

#タイトルを追加
st.title("streamlit超入門")

#データフレームを追加する
df = pd.DataFrame({
    "1列目":[1,2,3,4],
    "2列目":[2,4,6,8],
    "3列目":[3,6,9,12],
})
st.text("st.write")
st.write(df)
st.text("st.dataframe")
st.dataframe(df)
st.text("st.table")
st.table(df)

#データフレームを追加する
dff = pd.DataFrame(
  np.random.rand(20, 3),
  columns=["a", "b", "c"])

#チャートを描く
st.line_chart(dff)

#マップをプロットする
df_map = pd.DataFrame(
  np.random.rand(100, 2)/[50,50] + [35.69, 139.70],
  columns=["lat", "lon"])

st.map(df_map)

#画像を表示
img = Image.open(r"C:\Users\onoga\OneDrive\Desktop\MyDocker\venvs\ttt\iiiiii.jpg")
st.image(img, caption = "グラフ", use_column_width = True)

#インタラクティブウィジェット
#チェックボックス
if st.checkbox("push"):
    st.image(img)

#セレクトボックス
option = st.selectbox(
    "選択してください",
    ["バナナ", "リンゴ", "ゴリラ", "ラッパ"])
"選択結果は", option, "でした"

#テキスト入力
text = st.text_input("文字を入力してください")
"入力結果は", text, "でした"

#スライダー
condition = st.slider("あなたの調子は？", 0, 100, 50)#[最小値,最大値,デフォルトの値]
"コンディション", condition




"""


```python 

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

#タイトルを追加
st.title("streamlit超入門")

#データフレームを追加する
df = pd.DataFrame({
    "1列目":[1,2,3,4],
    "2列目":[2,4,6,8],
    "3列目":[3,6,9,12],
})
st.text("st.write")
st.write(df)
st.text("st.dataframe")
st.dataframe(df)
st.text("st.table")
st.table(df)


```
"""


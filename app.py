import streamlit as st
from PIL import Image
import numpy as np
import io

st.title("ピクセルアート変換アプリ")
st.write("画像をアップロードして、お好みのサイズのピクセルアートに変換するナリ！")

# サイドバーで設定を行う
st.sidebar.header("設定")
width = st.sidebar.number_input("横幅（ドット）", min_value=8, max_value=256, value=16, step=8)
height = st.sidebar.number_input("縦幅（ドット）", min_value=8, max_value=256, value=48, step=8)

uploaded_file = st.file_uploader("画像をアップロードするナリ", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    # 画像を読み込む
    image = Image.open(uploaded_file)
    
    # 元の画像を表示
    st.write("元の画像:")
    st.image(image)
    
    # ピクセルアートに変換
    pixel_art = image.resize((width, height), Image.Resampling.NEAREST)
    # 表示用に拡大（見やすくするため）
    display_size = (width * 10, height * 10)
    display_image = pixel_art.resize(display_size, Image.Resampling.NEAREST)
    
    # 変換後の画像を表示
    st.write("ピクセルアート:")
    st.image(display_image)
    
    # ダウンロードボタン
    buf = io.BytesIO()
    pixel_art.save(buf, format="PNG")
    st.download_button(
        label="ピクセルアートをダウンロード",
        data=buf.getvalue(),
        file_name="pixel_art.png",
        mime="image/png"
    ) 
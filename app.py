import numpy as np
import pandas as pd
import streamlit as st

st.write("### Airbnb宿泊候補")
link = '[①静岡県河津町](https://www.airbnb.jp/rooms/50889044?check_in=2023-05-05&check_out=2023-05-06&guests=1&adults=5&s=67&unique_share_id=0caf5ce0-638b-442e-846a-dece35a2c84f)'
st.markdown(link, unsafe_allow_html=True)
st.write("5人で29,800円,ビリヤード台がある")

link = '[②静岡県伊豆市](https://www.airbnb.jp/rooms/51496325?check_in=2023-05-05&check_out=2023-05-06&guests=1&adults=5&s=67&unique_share_id=5a37ecd3-db98-4c09-a76a-74db5f43e22b)'
st.markdown(link, unsafe_allow_html=True)
st.write("5人で36,000円、海が近い")

link = '[③山梨県笛吹市](https://www.airbnb.jp/rooms/808401459552836241?check_in=2023-05-05&check_out=2023-05-06&guests=1&adults=5&s=67&unique_share_id=2b88b443-6591-43ed-a19b-b1530c6e2f08)'
st.markdown(link, unsafe_allow_html=True)
st.write("5人で23,683円、ワイナリーが近いのがオススメ")

link = '[④神奈川県藤沢市鵠沼](https://www.airbnb.jp/rooms/6390627?check_in=2023-05-05&check_out=2023-05-06&guests=1&adults=5&s=67&unique_share_id=02af7235-21ac-42a3-b4ba-403e2cce07a9)'
st.markdown(link, unsafe_allow_html=True)
st.write("5人で31,193円、家に卓球台がある")


df = pd.DataFrame(
    np.array([[34.757476, 138.975080],
    [34.912419, 138.794992],
    [35.6573, 138.6352],
    [35.339888, 139.479858]]),
    columns=['lat', 'lon'])

print(df)
st.map(df)

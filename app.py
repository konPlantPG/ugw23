import streamlit as st
import os


st.write("# 2023第3回GW旅程")


pagelist = ["スケジュール", "食べ物", "観光地", "宿泊場所"]
selector=st.sidebar.radio( "ページ選択",pagelist)

home = os.getcwd()

if selector == "スケジュール":
    st.write("スマホの人は左上の「>」でサイドバー表示")
    st.write("決めてないけどそれっぽく書く")
    st.write("### 1日目")

    st.write(" ")
    st.write("12:00 [石和温泉駅](https://transit.yahoo.co.jp/?from=&to=%E7%9F%B3%E5%92%8C%E6%B8%A9%E6%B3%89%E9%A7%85&fromgid=&togid=&flatlon=&tlatlon=&via=&viacode=&y=2023&m=04&d=09&hh=15&m1=2&m2=6&type=1&ticket=ic&expkind=1&userpass=1&ws=3&s=0&al=1&shin=1&ex=1&hb=1&lb=1&sr=1)南口集合")
    
    st.write("昼ごはん")
    st.write("宿へチェックイン＆荷下ろし")

    st.write(" ")
    st.write("ここから未定だけどワイナリー行けたら嬉しい")

    st.write(" ")
    st.write("---")

    st.write("### 2日目")
    st.write("未定")



elif selector == '食べ物':

    st.write("## Googleマップで評価高いところ抜粋")
    link = '[①甲州ほうとう小作 石和駅前通り店](https://goo.gl/maps/sRgjm4Pc5buFX4gv7)'
    st.write("小作というのが山梨で有名な、ほうとうのお店らしい。小久保さんTwitter情報")
    st.markdown(link, unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("外観")
        st.image(home+"//images//hoto1.png", use_column_width=True)

    with col2:
        st.write("ほうとう")
        st.image(home+"//images//hoto2.png", use_column_width=True)
        
    with col3:
        st.write("メニュー")
        st.image(home+"//images//hoto3.png", use_column_width=True)

    st.write("---")

    link = '[②食いもん屋 北甲斐道](https://goo.gl/maps/Bq7RxpqvawzYtb6v9)'
    st.markdown(link, unsafe_allow_html=True)
    st.write("馬肉丼という言葉に釣られました。美味い店らしい")
    col4, col5, col6 = st.columns(3)
    with col4:
        st.write("外観")
        st.image(home+"//images//baniku1.png", use_column_width=True)

    with col5:
        st.write("馬肉丼")
        st.image(home+"//images//baniku2.png", use_column_width=True)
        
    with col6:
        st.write("メニュー")
        st.image(home+"//images//baniku3.png", use_column_width=True)

    st.write("---")
    link = '[③男の厨房](https://goo.gl/maps/eR2JMDfnPkuyzZtf7)'
    st.markdown(link, unsafe_allow_html=True)
    st.write("安い・美味い・安い")
    col7, col8, col9 = st.columns(3)
    with col7:
        st.write("外観")
        st.image(home+"//images//otoko1.png", use_column_width=True)

    with col8:
        st.write("かつ丼")
        st.image(home+"//images//otoko2.png", use_column_width=True)
        
    with col9:
        st.write("メニュー")
        st.image(home+"//images//otoko3.png", use_column_width=True)

    st.write("---")

    st.write("昼ごはんが食べられるところのイメージで探しました。")
    st.write("初日のお昼までと2日目はお酒飲まないので運転できます")

elif selector=='観光地':

    st.write("宿の周辺には温泉とワイン、県内なら信玄餅工場とか")
    st.write("### 石和温泉役周辺")

    #st.write("### 石和温泉役周辺")
    link = '[マルス山梨ワイナリー 本坊酒造](https://goo.gl/maps/4gcB5fCwrhLZjtaW8)'
    st.markdown(link, unsafe_allow_html=True)
    st.write('山梨きたらワイン工房行きたい。宿から歩ける距離')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("外観")
        st.image(home+"//images//wine1.png", use_column_width=True)

    with col2:
        st.write("見学コース")
        st.image(home+"//images//wine2.png", use_column_width=True)
        
    with col3:
        st.write("試飲")
        st.image(home+"//images//wine3.png", use_column_width=True)

    st.write('試飲できるそう')
    st.write("---")

    link = '[②石和温泉 ホテル新光](https://goo.gl/maps/qEBgTPF1eMRz9qRGA)'
    st.markdown(link, unsafe_allow_html=True)
    st.write('せっかく温泉街にきたので。')
    col4, col5, col6 = st.columns(3)
    with col4:
        st.write("外観")
        st.image(home+"//images//furo1.png", use_column_width=True)

    with col5:
        st.write("普通風呂")
        st.image(home+"//images//furo2.png", use_column_width=True)
        
    with col6:
        st.write("ワイン風呂")
        st.image(home+"//images//furo3.png", use_column_width=True)

    st.write('温泉は色々あるけど、石和温泉が1番宿から近い')
    st.image(home+"//images//onsen_list.png")

    st.write("---")

    st.write("### ドライブで行けそうなところ")

    link = '[①昇仙峽](https://goo.gl/maps/z4bqqsJasuHwPhj1A)'
    st.markdown(link, unsafe_allow_html=True)
    st.write('良い感じの写真がとれる')
    col7, col8, col9 = st.columns(3)
    with col7:
        st.write("あんな感じ")
        st.image(home+"//images//kanko1.png", use_column_width=True)

    with col8:
        st.write("そんな感じ")
        st.image(home+"//images//kanko2.png", use_column_width=True)
        
    with col9:
        st.write("こんな感じ")
        st.image(home+"//images//kanko3.png", use_column_width=True)

    st.write("---")

    link = '[②桔梗信玄餅 工場テーマパーク](https://goo.gl/maps/VFt1nKfpgQ2ADa3CA)'
    st.markdown(link, unsafe_allow_html=True)
    st.write('信玄餅の工場')
    col10, col11, col12 = st.columns(3)
    with col10:
        st.write("外観")
        st.image(home+"//images//moti1.png", use_column_width=True)

    with col11:
        st.write("見学コース")
        st.image(home+"//images//moti2.png", use_column_width=True)
        
    with col12:
        st.write("お土産")
        st.image(home+"//images//moti3.png", use_column_width=True)

    st.write("---")

    link = '[②富士スピードウェイ&モータースポーツミュージアム](https://goo.gl/maps/JmaJMM6wYowSaM8i6)'
    st.markdown(link, unsafe_allow_html=True)
    st.write('カートで遊べるのと多分社割が使える')
    col13, col14, col15 = st.columns(3)
    with col13:
        st.write("コース全体")
        st.image(home+"//images//car1.png", use_column_width=True)

    with col14:
        st.write("カート走れます")
        st.image(home+"//images//car2.png", use_column_width=True)
        
    with col15:
        st.write("ミュージアムもあります")
        st.image(home+"//images//car3.png", use_column_width=True)




else:
    st.write("## 宿泊場所")
    link = '[③山梨県笛吹市](https://www.airbnb.jp/rooms/808401459552836241?check_in=2023-05-05&check_out=2023-05-06&guests=1&adults=5&s=67&unique_share_id=2b88b443-6591-43ed-a19b-b1530c6e2f08)'
    st.markdown(link, unsafe_allow_html=True)

    st.write("タオルとドライヤーは必要なさそう。歯ブラシはいるかも")

    col1, col2 = st.columns(2)

    with col1:
        st.write("アメニティー1")
        st.image(home+"//images//ame1.png", use_column_width=True)

    with col2:
        st.write("アメニティー2")
        st.image(home+"//images//ame2.png", use_column_width=True)


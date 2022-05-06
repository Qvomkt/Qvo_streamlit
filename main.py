
import streamlit as st

import time

st.title('Stremlit 超入門')

st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!'

# text = st.text_input('あなたの趣味を教えてください。')
# 'あなたの趣味：', text, 'です。'

# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション：', condition

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問合せ1')
expander.write('問合せ内容を書く')
expander.write('問合せ内容を書く')
expander.write('問合せ内容を書く')
expander.write('問合せ内容を書く')

# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1, 11))
# )

# 'あなたの好きな数字は、', option, 'です。'


# if st.checkbox('Show Image'):

#     img = Image.open('IMG_1652.JPG')
#     img = img.rotate(-90)
#     st.image(img, caption='test', use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50]+[35.69, 139.70],
#     columns=['lat', 'lon']
# )
# st.dataframe(df)
# st.map(df)

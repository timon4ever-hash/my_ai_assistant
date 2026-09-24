import streamlit as st

st.set_page_config(page_title="AI Assistant", page_icon="🤖")
st.title("🤖 تجربة واجهة الشات")

# خانة الشات الأساسية
prompt = st.chat_input("اكتب أي شيء هنا وتأكد من ظهور الخانة...")

if prompt:
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        st.write(f"مرحباً! لقد استلمت رسالتك: {prompt}")

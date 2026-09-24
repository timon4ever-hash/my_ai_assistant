import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="مساعدي الشخصي", page_icon="🤖")
st.title("🤖 مساعدي الذكي")

# قراءة المفتاح بأمان من الخزنة
API_KEY = st.secrets["API_KEY"]
genai.configure(api_key=API_KEY)

# 2. إعداد الذاكرة (Session State)
# هذا الجزء يتأكد أن التطبيق لا ينسى المحادثة عند تحديث الصفحة
if "chat_session" not in st.session_state:
    # تهيئة النموذج الذكي وبدء محادثة جديدة تتذكر التاريخ
    model = genai.GenerativeModel('models/gemini-3.8-flash')
    st.session_state.chat_session = model.start_chat(history=[])
    
# ذاكرة إضافية لحفظ الرسائل وعرضها على الشاشة
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. عرض جميع الرسائل السابقة على الشاشة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 4. استلام رسالتك الجديدة
prompt = st.chat_input("تحدث مع مساعدك...")

if prompt:
    # عرض رسالتك على الشاشة وحفظها في الذاكرة
    with st.chat_message("user"):
        st.write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 5. إرسال الرسالة للعقل المدبر (Gemini) واستلام الرد
    with st.chat_message("assistant"):
        # إرسال الرسالة داخل جلسة المحادثة (لكي يتذكر ما سبق)
        response = st.session_state.chat_session.send_message(prompt)
        st.write(response.text)
        
    # حفظ رد المساعد في الذاكرة
    st.session_state.messages.append({"role": "assistant", "content": response.text})
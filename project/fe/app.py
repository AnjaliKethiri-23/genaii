# third part lib streamlit install 
# pip install streamlit
# streamlit ru/n command
# streamlit run filename.py
#pip install requests  (requests part py lib which is used to create apis and it isused to perform http requets with requests methods )
#requests methods:post(),get(),put(),
import streamlit as st
import requests

#
# requests.post(be_server_running_url,json=registered_data)
t1, t2 = st.tabs(["🔑 Login", "📝 Register"])
with t1:
    st.title("🌈 Login Form 📝")
    with st.form("Login Form"):
        st.text_input("📧 Email", placeholder="Enter email here")
        st.text_input(
            "🔒 Password",
            placeholder="Enter password here",
            type="password"
        )
        st.selectbox("🎭 Role", ["", "trainer", "student"])
        st.form_submit_button("🚀 Login")
with t2:
    st.title("🌈 Registration Form 📝")
    with st.form("Reg form"):
        n=st.text_input("👤 Name", placeholder="Enter name here")
        e=st.text_input("📧 Email", placeholder="Enter email here")
        p=st.text_input(
            "🔒 Password",
            placeholder="Enter password here",
            type="password"
        )
        c_p=st.text_input(
            "🔐 Confirm Password",
            placeholder="Re-enter password here",
            type="password"
        )
        r=st.selectbox("🎭 Role", ["", "trainer", "student"])
        r_btn=st.form_submit_button("🚀 Register")
        if r_btn:
            new_user={
                "name":n,
                "email":e,
                "password":p,
                "c_password":c_p,
                "role":r
            }
            res=requests.post("http://127.0.0.1:8000/register",json=new_user)
            if res.status_code == 200:
                st.write(res.json())
            else:
                st.write("some error occured")    
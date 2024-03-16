import streamlit as st,uuid,scratchattach as scratch3
from multiapp import MultiApp
account={}
def page_main():
    global account
    st.header('キー作成')
    name=st.text_input("名前を入力")
    password=st.text_input("パスワードを入力")
    if st.button("作成"):
        try:
            scratch3.login(name,password)
            uuid4=str(uuid.uuid4())
            account[uuid4]={"name":name,"password":password}
            st.write(f"成功!\nキー:{uuid4}")
        except:
            st.write("失敗!パスワードを確認してね！")
def page_edit():
    global account
    st.header('キー作成')
    key=st.text_input("キー")
    ploject=st.number_input("作品のID")
    cloud=st.text_input("cloud変数名")
    num=st.number_input("cloud変数内容")
    if st.button("変更!"):
        try:
            session = scratch3.login(account[key]["name"],account[key]["password"])
            conn = session.connect_cloud(str(ploject))
            conn.set_var(cloud,str(num))
            st.write("成功!")
        except:
            st.write("失敗!!")
app = MultiApp()
app.add_app("キー生成", page_main)
app.add_app("編集", page_edit)
app.run()

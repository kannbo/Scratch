import os

a=True

import streamlit as st,uuid,scratchattach as scratch3,os
from multiapp import MultiApp
if len(st.session_state)==0:
    st.session_state["account"]={}

print(len(st.session_state))

def page_main():
    st.header('キー作成')
    name=st.text_input("名前を入力")
    password=st.text_input("セッションIDを入力")
    if st.button("作成"):
        try:
            scratch3.Session(password,username=password)
            uuid4=str(uuid.uuid4())
            st.session_state["account"][uuid4]={"name":name,"password":password}
            st.write(f"成功!\nキー:{uuid4}")
            print(st.session_state["account"])
        except Exception as e:
            st.write(f"失敗!パスワードを確認してね！{e}")
def page_edit():
    st.header('キー作成')
    key=st.text_input("キー")
    ploject=st.text_input("作品のID")
    cloud=st.text_input("cloud変数名")
    num=st.text_input("cloud変数内容")
    if st.button("変更!"):
        try:
            session = scratch3.Session(st.session_state["account"][key]["password"],username=st.session_state["account"][key]["name"])
            conn = session.connect_cloud(str(ploject))
            conn.set_var(cloud,str(num))
            st.write("成功!")
        except Exception as e:
            st.write(f"失敗!!:{e}")
def comment():
    st.header('無料でお届け')
    key=st.text_input("キー")
    ploject=st.text_input("作品のID")
    text=st.text_input("投稿内容")
    if st.button("変更!"):
        try:
            session = scratch3.Session(st.session_state["account"][key]["password"],username=st.session_state["account"][key]["name"])
            project = session.connect_project(ploject)
            project.post_comment(content=text)
            st.write("成功")
        except Exception as e:
            st.write(f"失敗{e}")
def getplo(aa):
    return scratch3.Session(st.session_state["account"][aa]["password"],username=st.session_state["account"][aa]["name"])
def studio():
    lists=["35441603","32635350","32203566","1435670","31772464","4955848"]
    st.header('スタジオ')
    key=st.text_input("キー")
    studioans=st.text_input("スタジオのID")
    ploject=st.text_input("プロジェクトのID")
    if st.button("フォロー!"):
        aaaa=getplo(key)
        try:
            studioa=aaaa.connect_studio(studioans)
            studioa.follow()
            st.write("成功")
        except Exception as e:
            st.write(f"失敗{e}")
    if st.button("フォロー解除"):
        try:
            studioa=getplo(key).connect_studio(studioans)
            studioa.unfollow()
            st.write("成功")
        except Exception as e:
            st.write(f"失敗{e}")
    if st.button("追加!"):
        try:
            studioa=getplo(key).connect_studio(studioans)
            studioa.remove_project(ploject)
            studioa.add_project(ploject)
            st.write("成功")
        except Exception as e:
            st.write(f"失敗{e}")
    if st.button("何でもに投稿"):
        try:
            aaaa=getplo(key)
            for i in lists:
                studioa=aaaa.connect_studio(i)
                studioa.remove_project(ploject)
                studioa.add_project(ploject)
                st.write("成功")
        except Exception as e:
            st.write(f"失敗{e}")

app = MultiApp()
app.add_app("キー生成", page_main)
app.add_app("編集", page_edit)
app.add_app("コメント投稿", comment)
app.add_app("スタジオチート", studio)
app.run()

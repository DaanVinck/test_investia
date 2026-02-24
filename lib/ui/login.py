import streamlit as st
import os
from supabase import create_client, Client


def credentials(url, key):
    supabase = create_client(url, key)
    data = supabase.table("test_investia").select("id, pasword").execute()

    for item in data:
        for i in item:
            if type(i) == list:
                mylist = i
    name_list = []
    code_dict = {}
    for item in mylist:
        name_list.append(item.get('id'))
        code_dict[item.get('id')] = (item.get('pasword'))
    return name_list, code_dict
###################################################

def login_page(name_list, code_dict):
    st.title('Login')
    name = st.text_input('Enter your name')
    code = st.text_input('Paswoord')
    if st.button('Submit'):
        if name in name_list:
            if code_dict[name] == code:
                st.session_state['screen'] = 'home'
                return name
            else:
                st.session_state['screen'] = 'foute_code'

    if st.session_state['screen'] == 'foute_code':
        st.error('foute code, probeer opniew of maak een nieuw acc aan!')
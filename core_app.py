import streamlit as st
from functions import login
from functions import acc
from functions import home
from dotenv import load_dotenv 
load_dotenv()
import os
from supabase import create_client, Client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
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

# Initialiseer de login state als die nog niet bestaat
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Toon de juiste pagina
if st.session_state['logged_in'] == 'home':
    home(st.session_state['naam'])
elif st.session_state['logged_in'] == 'new_acc':
    name, email, code = acc(name_list)
    if not name or name == "bla" or not code or code == "bla" or not email or email == "bla":
        st.error("Vul alstublieft alle velden in!")
    elif name in name_list:
        st.error("je zit al in het systeem!")
    else:
        res = supabase.table("test_investia").insert([{"id": name, "pasword": code, "email": email}]).execute()
        st.session_state['logged_in'] = 'home'
        st.session_state['naam'] = name
else:
    name = login(name_list, code_dict)
    st.session_state['naam'] = name

import streamlit as st
from supabase import create_client, Client
from lib.backend.base import different
from lib.backend.base import unpack

def home_page(url, key):
    supabase = create_client(url, key)
    st.title("Home")
    if st.session_state['edit'] == 'add':
        newcomp = st.text_input("Naam")
        if st.button('Submit'):
            if newcomp != '':
                st.session_state['edit'] = False
                supabase.table("quiz").insert({"comp": newcomp}).execute()
    data = supabase.table("quiz").select("comp").execute()
    data = unpack(data)
    data_list = different(data)
    for naam in data_list:
    # use_container_width=True zorgt voor de "band" look
        if st.button(naam, use_container_width=True, key=f"btn_{naam}"):
            st.session_state['screen'] = 'comp'

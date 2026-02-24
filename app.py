import streamlit as st
from lib.ui.header import header
from lib.home import home_page
from lib.comp import comp_page
from lib.quiz import quiz_page
from dotenv import load_dotenv 

load_dotenv()
import os
from supabase import create_client, Client
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
if not url or not key:
    print("FOUT: SUPABASE_URL of SUPABASE_KEY niet gevonden in .env bestand!")
else:
    # Verwijder eventuele onzichtbare spaties of extra aanhalingstekens
    url = url.strip().replace('"', '').replace("'", "")
    key = key.strip().replace('"', '').replace("'", "")
    
    print(f"DEBUG: Verbinding maken met URL: {url}") # Check of dit eruit ziet als https://xyz...
# --- DEBUGGING EIND ---
supabase = create_client(url, key)





# Initialiseer de login state als die nog niet bestaat
if 'screen' not in st.session_state:
    st.session_state['screen'] = 'home'
if 'edit' not in st.session_state:
    st.session_state['edit'] = False

# Toon de juiste pagina
if st.session_state['screen'] == 'home':
    header(st.session_state['screen'])
    home_page(url, key)

elif st.session_state['screen'] == 'comp':
    header(st.session_state['screen'])
    comp_page()

elif st.session_state['screen'] == 'quiz':
    header(st.session_state['screen'])
    quiz_page()



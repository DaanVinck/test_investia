import streamlit as st
def login(name_list, code_dict):
    st.title('Login')
    name = st.text_input('Enter your name')
    code = st.text_input('Paswoord')
    if st.button('Submit'):
        if name in name_list:
            if code_dict[name] == code:
                st.session_state['logged_in'] = 'home'
                return name
            else:
                st.session_state['logged_in'] = 'foute_code'

    if st.button('new acc'):
        st.session_state['logged_in'] = 'new_acc'

    if st.session_state['logged_in'] == 'foute_code':
        st.error('foute code, probeer opniew of maak een nieuw acc aan!')

####################################################
def acc(name_list):
    st.title('Nieuw acc aanmaken')
    name = st.text_input('Enter your name')
    code = st.text_input('Paswoord')
    email = st.text_input('email')
    if st.button('Submit'):
        if not name or not code or not email:
            i = 1
        else:
            return name, email, code
    return "bla", "bla", "bla"
###################################################
def home(name):
    st.title('Home')
    st.write(f'Welkom op de Home pagina {name}!')

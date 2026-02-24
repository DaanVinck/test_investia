import streamlit as st

def header(screen):
    col1, col2, col3, col4, col5 = st.columns([2, 2, 6, 2, 2])  # verhouding: smal-breed-smal
    with col1:
        if screen != 'home':
            if st.button("←"):
                if screen == 'quiz':
                    st.session_state['screen'] = 'comp'
                else:
                    st.session_state['screen'] = 'home'
        
    with col3:
        st.markdown("<h3 style='text-align:center;'>Investia Quiz</h3>", unsafe_allow_html=True)
    with col4:
        if st.button("add"):
            st.session_state['edit'] = 'add'
    with col5:
        if st.button("edit"):
            st.session_state['edit'] == 'edit'
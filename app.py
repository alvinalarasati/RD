import streamlit as st
import home
import auth

def run():
    if 'authentication_status' not in st.session_state:
        st.session_state['authentication_status'] = None

    if st.session_state['authentication_status']:
        st.sidebar.title(f"Welcome, {st.session_state['name']}")

        menu = st.sidebar.radio("Menu", ["🏠 Home", "📝 History", "👋 Logout"])

        if menu == "🏠 Home":
            home.main()
        elif menu == "📝 History":
            home.show_history()
        elif menu == "👋 Logout":
            auth.logout()
    else:
        option = st.sidebar.radio("Select", ["🔐 Login", "Register"])
        if option == "🔐 Login":
            auth.login_form()
        else:
            auth.register_form()

if __name__ == "__main__":
     run()

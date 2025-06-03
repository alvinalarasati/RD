import sqlite3
import hashlib
import streamlit as st

DB_PATH = 'users.db'

def create_user_table():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        name TEXT,
        password TEXT
    )
    ''')
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, name, password):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users VALUES (?, ?, ?)", (username, name, hash_password(password)))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def verify_user(username, password):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT name, password FROM users WHERE username=?", (username,))
    user = c.fetchone()
    conn.close()
    if user and user[1] == hash_password(password):
        return user[0]
    return None

def login_form():
    st.header("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        name = verify_user(username, password)
        if name:
            st.session_state['authentication_status'] = True
            st.session_state['username'] = username
            st.session_state['name'] = name
            st.success("Logged in successfully")
            st.rerun()
        else:
            st.error("Incorrect username or password")

def register_form():
    st.header("Register")
    username = st.text_input("Choose Username")
    name = st.text_input("Your Full Name")
    password = st.text_input("Choose Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    if st.button("Register"):
        if password != confirm_password:
            st.error("Passwords do not match")
        elif register_user(username, name, password):
            st.success("Registration successful, please login.")
        else:
            st.error("Username already exists")

def logout():
    st.session_state['authentication_status'] = None
    st.session_state['username'] = None
    st.session_state['name'] = None
    st.success("Logged out")
    st.rerun()

create_user_table()


import streamlit as st
import pandas as pd
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="BROBOND ERP", page_icon="⚪", layout="wide")

# --- LOGIN LOGIC ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.markdown("""
        <style>
        .login-box {
            background-color: #ffffff;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        st.image("LOGO.png", width=200) if os.path.exists("LOGO.png") else st.title("BROBOND ERP")
        st.subheader("🔐 SECURE LOGIN")
        
        user = st.text_input("Username")
        pw = st.text_input("Password", type="password")
        
        if st.button("LOGIN NOW"):
            if user == "DHRUVIL" and pw == "2211":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Bhai, galat details hain! Sahi username/password daal.")
        st.markdown('</div>', unsafe_allow_html=True)

# Agar logged in nahi hai toh login page dikhao
if not st.session_state.logged_in:
    login()
    st.stop()

# --- ERP CODE STARTS AFTER LOGIN ---

# Column Definitions
CRM_COLUMNS = ["Lead", "Owner", "First Name", "Last Name", "Email", "Mobile", "Lead Status", "State", "City", "Date"]

# Styling (Wall-to-Wall Buttons)
st.markdown("""
    <style>
    [data-testid="stSidebar"] { background-color: #f8f9fa !important; border-right: none !important; }
    [data-testid="stSidebarContent"] { padding: 0px !important; }
    
    .brand-name { font-size: 50px; font-weight: 900; color: #000; text-align: center; line-height: 0.9; padding-top: 20px; }
    .brand-tagline { font-size: 14px; font-weight: 700; color: #444; text-align: center; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 20px; }
    
    div.stButton > button { 
        width: 100% !important; border-radius: 0px !important; height: 70px !important; 
        font-weight: 800 !important; font-size: 20px !important; background-color: white !important; 
        border: none !important; border-bottom: 1px solid #eee !important; margin: 0px !important; 
    }
    .category-label { text-align: center; font-weight: 900; font-size: 18px; background

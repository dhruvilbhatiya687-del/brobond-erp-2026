import streamlit as st
import pandas as pd
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="BROBOND ERP", layout="wide")

# --- CSS FIX FOR FULL-WIDTH BUTTONS & CLEAN SIDEBAR ---
st.markdown("""
    <style>
    /* 1. Sidebar se woh black line hatane ke liye */
    [data-testid="stSidebar"] {
        background-color: #f8f9fa;
        border-right: none !important;
    }
    
    /* 2. Sidebar ka extra gap khatam karne ke liye */
    [data-testid="stSidebarContent"] {
        padding-top: 10px !important;
        padding-left: 0px !important;
        padding-right: 0px !important;
    }

    /* 3. Branding Header Styling */
    .brand-name { font-size: 50px; font-weight: 900; color: #000; text-align: center; line-height: 0.9; margin-bottom: 0px; }
    .brand-tagline { font-size: 16px; font-weight: 700; color: #444; text-align: center; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 20px; }
    
    /* 4. CATEGORY BUTTONS: Full width fix */
    div.stButton > button {
        width: 100% !important;   /* Button ko poora corner tak touch karne ke liye */
        border-radius: 0px !important; 
        height: 70px !important;
        font-weight: 800 !important;
        font-size: 22px !important;
        background-color: white !important;
        border-top: 1px solid #eee !important;
        border-bottom: 1px solid #eee !important;
        border-left: none !important;
        border-right: none !important;
        margin-bottom: 0px !important;
        color: #000 !important;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #f0f2f6 !important;
    }

    .category-label {
        text-align: center; font-weight: 900; font-size: 20px; 
        margin-top: 20px; margin-bottom: 10px; color: #333;
        padding-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR CONTENT ---
with st.sidebar:
    # Branding wapas jaisa pehle tha
    st.markdown('<div class="brand-name">BROBOND</div>', unsafe_allow_html=True)
    st.markdown('<div class="brand-tagline">A Brand by SNBPL</div>', unsafe_allow_html=True)
    
    st.write("---")
    st.markdown('<div class="category-label">📋 MAIN CATEGORIES</div>', unsafe_allow_html=True) #
    
    # Ye buttons ab full width dikhenge
    if st.button("📊 SALES DASHBOARD"): st.session_state.page = "Dashboard"
    if st.button("📞 LEADS DATA"): st.session_state.page = "Leads"
    if st.button("💸 EXPENSES"): st.session_state.page = "Expenses"
    if st.button("👤 AYUSH (HRM)"): st.session_state.page = "HRM"
    if st.button("👑 HIMANSHU (CEO)"): st.session_state.page = "CEO"
    if st.button("💼 RITIK (MD)"): st.session_state.page = "Ritik"

# --- MAIN PAGE LOGIC ---
if "page" not in st.session_state: st.session_state.page = "Dashboard"

# Page content jisme koi faltu Hindi text nahi hoga
if st.session_state.page == "Dashboard":
    st.markdown(f"## 🚀 {st.session_state.page}")
    st.info("Welcome to BROBOND ERP Dashboard")
else:
    st.markdown(f"## 📋 {st.session_state.page}")
    st.write(f"Section for {st.session_state.page} is active.")

import streamlit as st
import pandas as pd
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="BROBOND ERP", layout="wide")

# --- CSS FIX FOR BUTTONS AND SIDEBAR ---
st.markdown("""
    <style>
    /* 1. Sidebar width aur background fix */
    [data-testid="stSidebar"] {
        min-width: 380px !important;
        max-width: 380px !important;
        background-color: #f8f9fa;
        border-right: none !important; /* Woh black line hatane ke liye */
    }
    
    /* 2. Sidebar ke andar ka extra gap khatam karne ke liye */
    [data-testid="stSidebarContent"] {
        padding-top: 20px !important;
        padding-left: 0px !important;
        padding-right: 0px !important;
    }

    /* 3. CATEGORY BUTTONS: Full width aur bada font */
    div.stButton > button {
        width: 100% !important;   /* Button ko sidebar ki poori choudai di */
        border-radius: 0px !important; /* Button ko corner tak touch karne ke liye */
        height: 75px !important;
        font-weight: 800 !important;
        font-size: 24px !important;
        background-color: white !important;
        border: 1px solid #eee !important;
        margin-bottom: 5px !important;
        color: #333 !important;
    }

    /* Branding Section */
    .brand-section {
        text-align: center;
        margin-bottom: 20px;
        padding: 10px;
    }
    
    .category-label {
        text-align: center;
        font-weight: 900;
        font-size: 22px;
        margin-top: 10px;
        margin-bottom: 20px;
        color: #000;
        border-bottom: 2px solid #ddd;
        padding-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR CONTENT ---
with st.sidebar:
    st.markdown('<div class="brand-section">', unsafe_allow_html=True)
    if os.path.exists("LOGO.png"):
        st.image("LOGO.png", use_container_width=True) #
    else:
        st.markdown("<h1 style='text-align:center;'>BROBOND ERP</h1>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="category-label">📋 MAIN CATEGORIES</div>', unsafe_allow_html=True) #
    
    # Buttons jo poore sidebar jitne wide honge
    if st.button("📊 SALES DASHBOARD"): st.session_state.page = "Dashboard"
    if st.button("📞 LEADS DATA"): st.session_state.page = "Leads"
    if st.button("💸 EXPENSES"): st.session_state.page = "Expenses"
    if st.button("👤 AYUSH (HRM)"): st.session_state.page = "HRM"
    if st.button("👑 HIMANSHU (CEO)"): st.session_state.page = "CEO"
    if st.button("💼 RITIK (MD)"): st.session_state.page = "Ritik"

# --- MAIN PAGE LOGIC ---
if "page" not in st.session_state: st.session_state.page = "Dashboard"

st.title(f"🚀 {st.session_state.page}")
st.write("Bhai, sidebar aur buttons ab ekdum fix hain.")

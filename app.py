import streamlit as st
import pandas as pd
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="BROBOND ERP", layout="wide")

# --- CSS EKDUM EKDUM FINAL FIX ---
st.markdown("""
    <style>
    /* 1. Sidebar ko full clean karna aur black line hatana */
    [data-testid="stSidebar"] {
        background-color: #f8f9fa !important;
        border-right: none !important;
    }
    
    /* 2. Sidebar ke andar ki extra padding khatam karna taaki buttons wall touch ho jayein */
    [data-testid="stSidebarContent"] {
        padding: 0px !important;
    }

    /* 3. Branding Section Styling */
    .brand-container {
        padding: 20px 10px;
        text-align: center;
    }
    .brand-tagline {
        font-size: 14px;
        font-weight: 800;
        color: #444;
        letter-spacing: 2px;
        margin-top: -10px;
        margin-bottom: 20px;
    }

    /* 4. MAIN CATEGORY LABEL FIX */
    .category-label {
        background-color: #eee;
        padding: 10px;
        text-align: center;
        font-weight: 900;
        font-size: 18px;
        color: #000;
        border-bottom: 1px solid #ddd;
    }

    /* 5. BUTTONS EKDUM FULL WIDTH (WALL-TO-WALL) */
    div.stButton > button {
        width: 100% !important;
        border-radius: 0px !important; /* Corner to corner touch */
        height: 75px !important;
        font-weight: 800 !important;
        font-size: 22px !important;
        background-color: white !important;
        border: none !important;
        border-bottom: 1px solid #eee !important; /* Sirf niche halki line */
        margin: 0px !important;
        color: #000 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        padding-left: 20px !important;
    }
    
    /* Button hover effect */
    div.stButton > button:hover {
        background-color: #f1f1f1 !important;
        border-left: 5px solid #ff4b4b !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR CONTENT ---
with st.sidebar:
    # Branding Header
    st.markdown('<div class="brand-container">', unsafe_allow_html=True)
    if os.path.exists("LOGO.png"):
        st.image("LOGO.png", use_container_width=True) #
    st.markdown('<div class="brand-tagline">A BRAND BY SNBPL</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="category-label">📋 MAIN CATEGORIES</div>', unsafe_allow_html=True) #
    
    # Category Buttons - Full Width Fix
    if st.button("📊 SALES DASHBOARD"): st.session_state.page = "Dashboard"
    if st.button("📞 LEADS DATA"): st.session_state.page = "Leads"
    if st.button("💸 EXPENSES"): st.session_state.page = "Expenses"
    if st.button("👤 AYUSH (HRM)"): st.session_state.page = "HRM"
    if st.button("👑 HIMANSHU (CEO)"): st.session_state.page = "CEO"
    if st.button("💼 RITIK (MD)"): st.session_state.page = "Ritik"

# --- MAIN PAGE LOGIC ---
if "page" not in st.session_state: st.session_state.page = "Dashboard"

# Page content starts here...
st.markdown(f"## {st.session_state.page}")
st.info("Bhai, ab buttons poore wide hain aur black line gayab hai.")

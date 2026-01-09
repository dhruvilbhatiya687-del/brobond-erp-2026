import streamlit as st
import pandas as pd
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="BROBOND ERP", layout="wide")

# --- CSS EKDUM SAME TO SAME PHOTO WALA ---
st.markdown("""
    <style>
    /* 1. Sidebar Clean Look aur Black Line Removal */
    [data-testid="stSidebar"] {
        background-color: #f8f9fa !important;
        border-right: none !important;
    }
    
    /* 2. Sidebar Padding khatam taaki buttons wall touch karein */
    [data-testid="stSidebarContent"] {
        padding: 0px !important;
    }

    /* 3. Branding Section (Top Header) */
    .brand-container {
        padding: 40px 10px 20px 10px;
        text-align: center;
    }
    .brand-name {
        font-size: 48px;
        font-weight: 900;
        color: #000;
        margin-bottom: 0px;
        line-height: 1;
    }
    .brand-tagline {
        font-size: 14px;
        font-weight: 800;
        color: #444;
        letter-spacing: 2px;
        margin-top: 5px;
    }

    /* 4. MAIN CATEGORY LABEL Styling */
    .category-label {
        padding: 15px;
        text-align: center;
        font-weight: 800;
        font-size: 18px;
        color: #333;
        border-top: 1px solid #eee;
        border-bottom: 1px solid #eee;
        background-color: #fcfcfc;
    }

    /* 5. FULL WIDTH BUTTONS (SAME AS PHOTO) */
    div.stButton > button {
        width: 100% !important;
        border-radius: 0px !important; /* Wall to wall touch */
        height: 65px !important;
        font-weight: 700 !important;
        font-size: 18px !important;
        background-color: white !important;
        border: none !important;
        border-bottom: 1px solid #f0f0f0 !important;
        margin: 0px !important;
        color: #444 !important;
        text-align: left !important;
        padding-left: 30px !important;
    }
    
    /* Hover effect for buttons */
    div.stButton > button:hover {
        background-color: #f1f1f1 !important;
        color: #ff4b4b !important;
    }

    /* Active page highlight */
    div.stButton > button:focus {
        border-left: 5px solid #ff4b4b !important;
        background-color: #fdf2f2 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR CONTENT ---
with st.sidebar:
    # Top Branding
    st.markdown('<div class="brand-container">', unsafe_allow_html=True)
    st.markdown('<div class="brand-name">BROBOND</div>', unsafe_allow_html=True)
    st.markdown('<div class="brand-tagline">A BRAND BY SNBPL</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="category-label">📋 MAIN CATEGORIES</div>', unsafe_allow_html=True) #
    
    # Category Buttons - Full Width Wall-to-Wall
    if st.button("📊  SALES DASHBOARD"): st.session_state.page = "Dashboard"
    if st.button("📞  LEADS DATA"): st.session_state.page = "Leads"
    if st.button("💸  EXPENSES"): st.session_state.page = "Expenses"
    if st.button("👤  AYUSH (HRM)"): st.session_state.page = "HRM"
    if st.button("👑  HIMANSHU (CEO)"): st.session_state.page = "CEO"
    if st.button("💼  RITIK (MD)"): st.session_state.page = "Ritik"

# --- MAIN PAGE LOGIC ---
if "page" not in st.session_state: st.session_state.page = "Dashboard"

# Page Heading
st.markdown(f"# {st.session_state.page}")

if st.session_state.page == "Dashboard":
    st.write("Module active.")

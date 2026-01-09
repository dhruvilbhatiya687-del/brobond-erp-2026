import streamlit as st
import pandas as pd
import plotly.express as px
import io
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="BROBOND ERP", page_icon="⚪", layout="wide")

# Column Definitions
CRM_COLUMNS = [
    "Lead", "Owner", "First Name", "Last Name", "Email", 
    "Mobile Country Code", "Mobile", "Designation", 
    "Phone Country Code", "Phone", "Lead Source", "Sub Lead Source", 
    "Lead Status", "Industry", "Department", "Annual Revenue", 
    "Company Name", "Country", "State", "City", "Street", 
    "Pincode", "Lead Priority", "Description", "Product Category", "Date"
]

EXPENSE_COLUMNS = ["Date", "Category", "Amount", "Paid To", "Payment Mode", "Description", "Status"]

# Initializing Session States
if 'temp_data' not in st.session_state: st.session_state.temp_data = pd.DataFrame(columns=CRM_COLUMNS)
if 'expense_data' not in st.session_state: st.session_state.expense_data = pd.DataFrame(columns=EXPENSE_COLUMNS)
if "page" not in st.session_state: st.session_state.page = "Dashboard"

# --- STYLING (BIG BUTTONS & SCROLLBARS) ---
st.markdown("""
    <style>
    [data-testid="stSidebar"] { background-color: #f8f9fa; border-right: 1px solid #e0e0e0; }
    .brand-name { font-size: 56px; font-weight: 900; color: #000; text-align: center; line-height: 0.9; }
    .brand-tagline { font-size: 18px; font-weight: 700; color: #444; text-align: center; text-transform: uppercase; letter-spacing: 3px; }
    
    /* BIG CATEGORY BUTTONS */
    div.stButton > button { 
        width: 100%; 
        border-radius: 8px; 
        height: 70px !important; 
        font-weight: 800 !important; 
        font-size: 22px !important; 
        background-color: white; 
        border: 1px solid #ccc; 
        margin-bottom: 12px; 
        color: #000;
    }
    
    .category-label { text-align: center; font-weight: 900; font-size: 20px; margin-top: 30px; border-bottom: 2px solid #ddd; padding-bottom: 10px; }
    
    /* Scrollbars */
    ::-webkit-scrollbar { width: 14px !important; height: 14px !important; display: block !important; }
    ::-webkit-scrollbar-track { background: #f1f1f1 !important; }
    ::-webkit-scrollbar-thumb { background: #555 !important; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown('<div class="brand-name">BROBOND</div><div class="brand-tagline">A Brand by SNBPL</div>', unsafe_allow_html=True)
    st.write("---")
    st.markdown('<div class="category-label">📋 MAIN CATEGORIES</div>', unsafe_allow_html=True)
    
    if st.button("📊 SALES DASHBOARD"): st.session_state.page = "Dashboard"
    if st.button("📞 LEADS DATA"): st.session_state.page = "Leads"
    if st.button("💸 EXPENSES"): st.session_state.page = "Expenses"
    if st.button("👤 AYUSH (HRM)"): st.session_state.page = "HRM"
    if st.button("👑 HIMANSHU (CEO)"): st.session_state.page = "CEO"
    if st.button("💼 RITIK (MD)"): st.session_state.page = "Ritik"

# --- LEADS PAGE ---
if st.session_state.page == "Leads":
    st.markdown("# 🛡️ MASTER LEAD DATABASE")
    with st.expander("📥 BULK IMPORT EXCEL", expanded=True):
        files = st.file_uploader("Upload Excel", type=["xlsx"], accept_multiple_files=True)
        if st.button("IMPORT ALL FILES"):
            if files:
                all_data = [pd.read_excel(f).reindex(columns=CRM_COLUMNS, fill_value="") for f in files]
                st.session_state.temp_data = pd.concat(all_data, ignore_index=True)
                st.success("Data imported.")
    
    if not st.session_state.temp_data.empty:
        col1, col2 = st.columns(2)
        with col1:
            prod_opts = st.session_state.temp_data['Lead Status'].unique().tolist()
            sel_prod = st.multiselect("🔍 Search Product (Lead Status)", options=prod_opts) #
        with col2:
            state_opts = st.session_state.temp_data['State'].unique().tolist()
            sel_state = st.multiselect("📍 Search by State", options=state_opts) #
        
        df = st.session_state.temp_data.copy()
        if sel_prod: df = df[df['Lead Status'].isin(sel_prod)]
        if sel_state: df = df[df['State'].isin(sel_state)]
        
        # Sequence 1 to N
        df.index = range(1, len(df) + 1)
        st.dataframe(df, use_container_width=True, height=600)
        
        # CLEAR DATA BUTTON [Bhai ye raha tera button]
        if st.button("🗑️ CLEAR ALL LEAD DATA"):
            st.session_state.temp_data = pd.DataFrame(columns=CRM_COLUMNS)
            st.rerun()

# --- EXPENSES PAGE ---
elif st.session_state.page == "Expenses":
    st.markdown("# 💸 EXPENSE MANAGEMENT")
    # Logic pehle jaisa hi hai
    if not st.session_state.expense_data.empty:
        st.dataframe(st.session_state.expense_data, use_container_width=True)

else:
    st.markdown(f"# {st.session_state.page}")
    st.info("Module active.")

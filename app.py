import streamlit as st
import pandas as pd
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="BROBOND ERP", page_icon="⚪", layout="wide")

# --- 1. LOGIN SYSTEM ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("<h1 style='text-align:center;'>🔐 SECURE LOGIN</h1>", unsafe_allow_html=True)
        user = st.text_input("Username")
        pw = st.text_input("Password", type="password")
        if st.button("LOGIN NOW"):
            if user == "DHRUVIL" and pw == "2211":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Bhai, ghalat details hain!")
    st.stop()

# --- 2. DATA COLUMNS & STATE ---
CRM_COLUMNS = [
    "Lead", "Owner", "First Name", "Last Name", "Email", 
    "Mobile Country Code", "Mobile", "Designation", 
    "Phone Country Code", "Phone", "Lead Source", "Sub Lead Source", 
    "Lead Status", "Industry", "Department", "Annual Revenue", 
    "Company Name", "Country", "State", "City", "Street", 
    "Pincode", "Lead Priority", "Description", "Product Category", "Date"
]

if 'temp_data' not in st.session_state: st.session_state.temp_data = pd.DataFrame(columns=CRM_COLUMNS)
if "page" not in st.session_state: st.session_state.page = "Dashboard"

# --- 3. STYLING (SAME TO SAME PHOTO REQUEST) ---
st.markdown("""
    <style>
    [data-testid="stSidebar"] { background-color: #f8f9fa !important; border-right: none !important; }
    [data-testid="stSidebarContent"] { padding: 0px !important; }
    
    .brand-name { font-size: 56px; font-weight: 900; color: #000; text-align: center; line-height: 0.9; padding-top: 30px; }
    .brand-tagline { font-size: 18px; font-weight: 700; color: #444; text-align: center; text-transform: uppercase; letter-spacing: 3px; margin-bottom: 20px; }
    
    .category-label { text-align: center; font-weight: 900; font-size: 20px; background-color: #eee; padding: 10px; border-bottom: 1px solid #ddd; }
    
    div.stButton > button { 
        width: 100% !important; border-radius: 0px !important; height: 75px !important; 
        font-weight: 800 !important; font-size: 22px !important; background-color: white !important; 
        border: none !important; border-bottom: 1px solid #eee !important; margin: 0px !important; color: #000 !important;
    }
    div.stButton > button:hover { background-color: #f1f1f1 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.markdown('<div class="brand-name">BROBOND</div><div class="brand-tagline">A Brand by SNBPL</div>', unsafe_allow_html=True)
    st.markdown('<div class="category-label">📋 MAIN CATEGORIES</div>', unsafe_allow_html=True)
    
    if st.button("📊 SALES DASHBOARD"): st.session_state.page = "Dashboard"
    if st.button("📞 LEADS DATA"): st.session_state.page = "Leads"
    if st.button("💸 EXPENSES"): st.session_state.page = "Expenses"
    if st.button("👤 AYUSH (HRM)"): st.session_state.page = "HRM"
    if st.button("👑 HIMANSHU (CEO)"): st.session_state.page = "CEO"
    if st.button("💼 RITIK (MD)"): st.session_state.page = "Ritik"
    
    st.write("---")
    if st.button("🚪 LOGOUT"):
        st.session_state.logged_in = False
        st.rerun()

# --- 5. MAIN PAGES CONTENT ---
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
            sel_prod = st.multiselect("🔍 Search Product (Lead Status)", options=prod_opts)
        with col2:
            state_opts = st.session_state.temp_data['State'].unique().tolist()
            sel_state = st.multiselect("📍 Search by State", options=state_opts)
        
        df = st.session_state.temp_data.copy()
        if sel_prod: df = df[df['Lead Status'].isin(sel_prod)]
        if sel_state: df = df[df['State'].isin(sel_state)]
        
        # Numbering 1 to N
        df.index = range(1, len(df) + 1)
        st.dataframe(df, use_container_width=True, height=600)
        
        if st.button("🗑️ CLEAR ALL LEAD DATA"):
            st.session_state.temp_data = pd.DataFrame(columns=CRM_COLUMNS)
            st.rerun()

else:
    st.markdown(f"# {st.session_state.page}")
    st.info("Module active.")

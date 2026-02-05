import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

# 1. PODEŠAVANJA I DIZAJN (Kao fitMe)
st.set_page_config(page_title="fitMe Mentorstvo", page_icon="💪", layout="wide")

# CSS za boje i kartice
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; }
    .card { background-color: #161b22; padding: 20px; border-radius: 10px; border: 1px solid #30363d; margin-bottom: 10px; }
    h1, h2, h3 { color: #ff4b4b; }
    </style>
    """, unsafe_allow_html=True)

# 2. MODERNI MENI (Sa leve strane)
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com", width=100)
    izbor = option_menu(
        "Glavni Meni", 
        ["Početna", "Kalkulator", "Trening", "Ishrana", "Admin"],
        icons=['house', 'calculator', 'activity', 'egg-fried', 'lock'], 
        menu_icon="cast", default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#0e1117"},
            "icon": {"color": "#ff4b4b", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#262730"},
            "nav-link-selected": {"background-color": "#ff4b4b"},
        }
    )

# 3. LOGIKA PRIJAVE (LOGIN)
if 'ulogovan' not in st.session_state:
    st.session_state['ulogovan'] = False

if not st.session_state['ulogovan']:
    st.title("💪 fitMe Prijava")
    lozinka = st.text_input("Lozinka za članice:", type="password")
    if st.button("UĐI"):
        if lozinka == "fitnes2024":
            st.session_state['ulogovan'] = True
            st.rerun()
        else:
            st.error("Pogrešna lozinka.")
else:
    # --- POČETNA ---
    if izbor == "Početna":
        st.title("Dobrodošla u fitMe ✨")
        st.write("Tvoja transformacija počinje ovde.")
        st.image("https://images.unsplash.com")

    # --- KALKULATOR ---
    elif izbor == "Kalkulator":
        st.title("📊 Kalkulator")
        c1, c2 = st.columns(2)
        with c1:
            kg = st.number_input("Težina (kg)", 40, 150, 65)
        with c2:
            visina = st.number_input("Visina (cm)", 120, 220, 165)
        
        if st.button("Izračunaj"):
            kalorije = (10 * kg) + (6.25 * visina) - 161
            st.metric("Tvoj BMR", f"{int(kalorije)} kcal")

    # --- TRENING ---
    elif izbor == "Trening":
        st.title("🏋️ Trening Plan")
        st.markdown('<div class="card"><h3>Danas: HIIT & Core</h3><p>Prati video i odradi sve serije.</p></div>', unsafe_allow_html=True)
        st.video("https://www.youtube.com")

    # --- ISHRANA ---
    elif izbor == "Ishrana":
        st.title("🥗 Ishrana")
        st.info("Poveži svoju Google Tabelu ovde (kao u prethodnom koraku).")

    # --- ADMIN ---
    elif izbor == "Admin":
        st.title("🔐 Admin Panel")
        admin_pass = st.text_input("Admin lozinka:", type="password")
        if admin_pass == "admin123":
            st.success("Dobrodošla, šefice!")

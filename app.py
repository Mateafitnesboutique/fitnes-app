import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# --- KONFIGURACIJA ---
st.set_page_config(page_title="Pro Fit Mentorstvo", page_icon="🔐", layout="wide")

# --- CSS STIL ZA STRANICU ZA LOGOVANJE ---
st.markdown("""
    <style>
    .login-container {
        max-width: 400px; padding: 40px; background: white;
        border-radius: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        margin: auto; text-align: center;
    }
    .stApp { background: linear-gradient(135deg, #fff5f7 0%, #ffe0e6 100%); }
    </style>
    """, unsafe_allow_html=True)

# --- POVEZIVANJE SA BAZOM (Korisnici i Planovi) ---
SHEET_URL = "Mateas Fitnes Boutique - Google Sheets"
conn = st.connection("gsheets", type=GSheetsConnection)

# Funkcija za proveru korisnika
def proveri_korisnika(email, lozinka):
    try:
        # Čita list "Korisnici" iz tvoje tabele
        df = conn.read(spreadsheet=SHEET_URL, worksheet="Korisnici")
        korisnik = df[(df['Email'] == email) & (df['Lozinka'] == lozinka)]
        if not korisnik.empty:
            return korisnik.iloc[0]['Status']
        return None
    except:
        return None

# --- LOGIKA PRISTUPA (SESSION STATE) ---
if 'ulogovan' not in st.session_state:
    st.session_state['ulogovan'] = False

# --- EKRAN ZA PRIJAVU ---
if not st.session_state['ulogovan']:
    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com", width=100)
    st.title("Fit Pro Prijava")
    
    email_input = st.text_input("Tvoj Email")
    lozinka_input = st.text_input("Lozinka", type="password")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Prijavi se"):
            status = proveri_korisnika(email_input, lozinka_input)
            if status == "aktivan":
                st.session_state['ulogovan'] = True
                st.session_state['korisnik_email'] = email_input
                st.rerun()
            elif status == "isteklo":
                st.error("Vaša pretplata je istekla. Kontaktirajte trenera.")
            else:
                st.error("Pogrešni podaci.")
    with col2:
        # Dugme za nove klijente
        st.link_button("Postani član", "https://tvoj-sajt-ili-instagram.com")
    st.markdown('</div>', unsafe_allow_html=True)

# --- GLAVNI SADRŽAJ (Prikazuje se samo ako je ulogovan) ---
else:
    with st.sidebar:
        st.success(f"Prijavljeni ste: {st.session_state['korisnik_email']}")
        meni = st.radio("Meni", ["🏠 Početna", "🏋️ Trening", "🥗 Ishrana", "📈 Moj Napredak"])
        if st.button("Odjavi se"):
            st.session_state['ulogovan'] = False
            st.rerun()

    if meni == "🏠 Početna":
        st.title("Dobrodošla nazad! ✨")
        st.markdown("""
        <div style="background: white; padding: 20px; border-radius: 15px; border-left: 10px solid #FF4B6B;">
            <h3>Vaša pretplata je AKTIVNA ✅</h3>
            <p>Iskoristite današnji dan za napredak. Vaš plan je spreman ispod.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Ovde ide ostatak tvog koda za treninge, kalkulator itd.
        st.info("Ovde ubacujemo prethodno napisane module za trening i kalkulator kalorija.")

import streamlit as st
import pandas as pd

# 1. OSNOVNA PODEŠAVANJA
st.set_page_config(page_title="Fit Pro Mentorstvo", page_icon="🌸")

# 2. JEDNOSTAVAN DIZAJN
st.markdown("""
    <style>
    .stApp { background-color: #FFF9FA; }
    .card {
        background: white; padding: 20px; border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        border-left: 5px solid #FF4B6B; margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. PRIJAVA (LOGIN) - Najjednostavnija verzija
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    st.title("🔐 Prijava za članice")
    lozinka = st.text_input("Unesi lozinku za pristup:", type="password")
    if st.button("Uđi u aplikaciju"):
        if lozinka == "fitnes2024": # Tvoja lozinka za klijentkinje
            st.session_state['auth'] = True
            st.rerun()
        else:
            st.error("Pogrešna lozinka. Kontaktiraj trenera.")
else:
    # --- GLAVNI MENI ---
    meni = st.sidebar.radio("Navigacija", ["🏠 Početna", "📊 Kalkulator", "🏋️ Trening", "🥗 Ishrana", "🔐 Admin"])

    if meni == "🏠 Početna":
        st.title("Dobrodošla! ✨")
        st.markdown('<div class="card"><h3>Tvoj uspeh počinje danas!</h3><p>Prati planove i ne odustaj.</p></div>', unsafe_allow_html=True)
        st.image("https://images.unsplash.com")

    elif meni == "📊 Kalkulator":
        st.header("🎯 Izračunaj svoje potrebe")
        kg = st.number_input("Težina (kg)", 40, 150, 65)
        visina = st.number_input("Visina (cm)", 120, 220, 165)
        godine = st.number_input("Godine", 15, 80, 25)
        
        if st.button("Izračunaj"):
            kalorije = (10 * kg) + (6.25 * visina) - (5 * godine) - 161
            st.success(f"Tvoj osnovni metabolizam je: {int(kalorije)} kcal")
            st.info("Za mršavljenje jedi oko 1500-1700 kcal dnevno.")

    elif meni == "🏋️ Trening":
        st.header("💪 Današnji trening")
        st.video("https://www.youtube.com")
        st.write("1. Čučnjevi - 3x15\n2. Iskorak - 3x12\n3. Plank - 45 sekundi")

    elif meni == "🥗 Ishrana":
        st.header("🥗 Plan ishrane")
        st.markdown("""
        * **Doručak:** Ovsena kaša sa voćem
        * **Ručak:** Piletina i riža
        * **Večera:** Grilovano povrće i sir
        """)

    elif meni == "🔐 Admin":
        st.header("Admin Panel")
        admin_pass = st.text_input("Admin šifra:", type="password")
        if admin_pass == "admin123":
            st.success("Dobrodošla, šefice!")
            st.write("Ovde možeš pratiti napredak svojih klijentkinja.")

import streamlit as st
from PIL import Image

# =====================================
# CONFIGURATION MOBILE OPTIMISÉE
# =====================================

st.set_page_config(
    page_title="La quête de Mirmandoule l'amoureux",
    page_icon="🏰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =====================================
# CSS MEDIEVAL MOBILE OPTIMISÉ
# =====================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=MedievalSharp&display=swap');
/* Texte noir partout */
html, body, [class*="css"]  {
    color: #000000 !important;
    font-family: "MedievalSharp", cursive;
}

/* Fond parchemin */
.stApp {
    background-color: #f4ecd8;
}

/* Container central mobile */
.block-container {

    max-width: 700px;

    padding-top: 1rem;
    padding-bottom: 3rem;
    padding-left: 1rem;
    padding-right: 1rem;

    background-color: #fff8e7;

    border-radius: 15px;

    border: 2px solid #c9a86a;

}

/* Titres */
h1 {
    text-align: center;
    font-size: 28px !important;
}

h2 {
    font-size: 24px !important;
}

h3 {
    font-size: 20px !important;
}

/* Texte normal */
p, div, span, label {
    font-size: 18px !important;
}

/* Boites medieval */
.medieval-box {

    background-color: #fff3cd;

    padding: 15px;

    border-radius: 10px;

    border: 1px solid #c9a86a;

    font-size: 18px;

}

/* Boutons mobile */
.stButton > button {

    width: 100%;

    height: 55px;

    font-size: 18px;

    border-radius: 10px;

}

/* Selectbox */
.stSelectbox > div {

    font-size: 18px;

}

/* Input */
.stTextInput input {

    font-size: 18px;

}

/* Image responsive */
img {

    border-radius: 10px;

}

</style>
""", unsafe_allow_html=True)

# =====================================
# DONNEES DU JEU
# =====================================

LIEUX = [

    {
        "nom": "La basse-ville",
        "enigme": "Tu y retourne après les artisans",
        "options": [
            "La porte des Gauttiers",
            "La capitelle",
            "L'église Sainte-Foy",
            "La chapelle Sainte-Lucie",
            "Les boutiques d'art & d'artisanat"
        ],
        "reponse": "Les boutiques d'art & d'artisanat"
    },

    {
        "nom": "Les boutiques d'art & d'artisanat",
        "enigme": "Tu dois franchir cet homme pour m'atteindre",
        "options": [
            "La porte des Gauttiers",
            "La capitelle",
            "L'église Sainte-Foy",
            "La chapelle Sainte-Lucie",
            "Les boutiques d'art & d'artisanat"
        ],
        "reponse": "La porte des Gauttiers"
    },

    {
        "nom": "La porte des Gauttiers",
        "enigme": "Tu es passé devant au moins 5 foys",
        "options": [
            "La porte des Gauttiers",
            "La capitelle",
            "L'église Sainte-Foy",
            "La chapelle Sainte-Lucie",
            "Les boutiques d'art & d'artisanat"
        ],
        "reponse": "L'église Sainte-Foy"
    },

    {
        "nom": "L'église Sainte-Foy",
        "enigme": "Cha ch'appelle comme un coffre-fort",
        "options": [
            "La porte des Gauttiers",
            "La capitelle",
            "L'église Sainte-Foy",
            "La chapelle Sainte-Lucie",
            "Les boutiques d'art & d'artisanat"
        ],
        "reponse": "La chapelle Sainte-Lucie"
    },

    {
        "nom": "La chapelle Sainte-Lucie",
        "enigme": "On me présente en toute lettre",
        "options": [
            "La porte des Gauttiers",
            "La capitelle",
            "L'église Sainte-Foy",
            "La chapelle Sainte-Lucie",
            "Les boutiques d'art & d'artisanat"
        ],
        "reponse": "La capitelle"
    }

]

ENIGME_FINALE = "mirmandoule"

# =====================================
# SESSION
# =====================================

if "etape" not in st.session_state:
    st.session_state.etape = 0

if "victoire" not in st.session_state:
    st.session_state.victoire = False

# =====================================
# TITRE
# =====================================

st.title("🏰 La quête de Mirmandoule l'amoureux")

st.markdown("""
<div class="medieval-box">
Bienvenue, noble aventurier.<br><br>

Mirmandoule a dissimulé un trésor précieux.<br><br>

Résous chaque énigme pour le trouver.
</div>
""", unsafe_allow_html=True)

# =====================================
# CARTE
# =====================================

image = Image.open("carte.png")
st.image(image, use_container_width=True)

# =====================================
# PROGRESSION
# =====================================

progression = st.session_state.etape / len(LIEUX)

st.progress(progression)

st.write(f"Progression : {st.session_state.etape} / {len(LIEUX)}")

# =====================================
# ENIGMES
# =====================================

if st.session_state.etape < len(LIEUX):

    lieu = LIEUX[st.session_state.etape]

    st.header(f"📍 Position : {lieu['nom']}")

    st.markdown(f"""
    <div class="medieval-box">
    {lieu['enigme']}
    </div>
    """, unsafe_allow_html=True)

    choix = st.selectbox(
        "Choisis le lieu suivant :",
        lieu["options"]
    )

    if st.button("⚔️ Valider mon choix"):

        if choix == lieu["reponse"]:

            st.success("Bonne réponse !")

            st.session_state.etape += 1

            st.rerun()

        else:

            st.error("Mauvaise réponse...")

# =====================================
# ENIGME FINALE
# =====================================

elif not st.session_state.victoire:

    st.header("🏆 Énigme finale")

    reponse = st.text_input("Quel est le point commun ?")

    if st.button("💎 Révéler le trésor"):

        if reponse.lower().strip() == ENIGME_FINALE:

            st.session_state.victoire = True

            st.rerun()

        else:

            st.error("Ce n'est pas la bonne réponse.")

# =====================================
# VICTOIRE
# =====================================

else:

    st.balloons()

    st.header("💎 TRÉSOR DÉCOUVERT 💎")

    st.markdown("""
    <div class="medieval-box">
    Félicitations.<br><br>

    Tu as trouvé le trésor de Mirmandoule.
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔄 Recommencer"):

        st.session_state.etape = 0
        st.session_state.victoire = False

        st.rerun()

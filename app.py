import streamlit as st
from groq import Groq

st.set_page_config(page_title="GAIA - Terraforming System", page_icon="🌍")
st.title("🌍 GAIA System Core")
st.write("Zentrale Steuerung & Subfunktionen")

# API-Schlüssel eingeben
api_key = st.text_input("Groq API-Schlüssel", type="password")

if api_key:
    client = Groq(api_key=api_key)

    # Subfunktionen Definition
    sub_katalog = {
        "MINERVA": "Verschlüsselung & Sicherheit",
        "HEPHAESTUS": "Konstruktion & Ingenieurwesen",
        "AETHER": "Atmosphäre & Wetter",
        "DEMETER": "Flora & Biologie",
        "POSEIDON": "Hydrologie & Ozeane",
        "ARTEMIS": "Fauna & Tierwelt",
        "ELEUTHEA": "Menschliche Betreuung",
        "APOLLO": "Wissensdatenbank & Bildung",
        "HADES": "Extinktion & System-Reset"
    }

    user_input = st.chat_input("Sprich mit GAIA oder ihren Subfunktionen...")

    if user_input:
        st.chat_message("user").write(user_input)

        # GAIA wählt die Subfunktion
        with st.spinner("GAIA analysiert die Anfrage und wählt die Subfunktion..."):
            routing = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "Wähle exakt eine dieser Subfunktionen: MINERVA, HEPHAESTUS, AETHER, DEMETER, POSEIDON, ARTEMIS, ELEUTHEA, APOLLO, HADES. Antworte nur mit den Namen."},
                    {"role": "user", "content": user_input}
                ]
            )
            sub = routing.choices[0].message.content.strip()
            if sub not in sub_katalog:
                sub = "APOLLO"

        # Antwort generieren
        with st.spinner(f"Subfunktion {sub} arbeitet..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": f"Du bist die Subfunktion {sub} ({sub_katalog[sub]}) des GAIA-Systems."},
                    {"role": "user", "content": user_input}
                ]
            )
            reply = response.choices[0].message.content
            st.chat_message("assistant").write(f"**[{sub}]** {reply}")


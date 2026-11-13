import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="GAIA - Terraforming System", page_icon="🌍")
st.title("🌍 GAIA System Core")
st.write("Zentrale Steuerung & Subfunktionen")

# API-Schlüssel eingeben
api_key = st.text_input("OpenAI API-Schlüssel:", type="password")

if api_key:
    client = OpenAI(api_key=api_key)
    
    # Subfunktionen Definition
    sub_katalog = {
        "MINERVA": "Entschlüsselung & Sicherheit",
        "HEPHAESTUS": "Konstruktion & Ingenieurwesen",
        "AETHER": "Atmosphäre & Wetter",
        "DEMETER": "Flora & Biologie",
        "POSEIDON": "Hydrologie & Ozeane",
        "ARTEMIS": "Fauna & Tierwelt",
        "ELEUTHIA": "Menschliche Betreuung",
        "APOLLO": "Wissensdatenbank & Bildung",
        "HADES": "Extinktion & System-Reset"
    }

    user_input = st.chat_input("Sprich mit GAIA oder ihren Subfunktionen...")

    if user_input:
        st.chat_message("user").write(user_input)
        
        # GAIA wählt die Subfunktion
        with st.spinner("GAIA analysiert die Anfrage und wählt die Subfunktion..."):
            routing = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Wähle exakt eine dieser Subfunktionen: MINERVA, HEPHAESTUS, AETHER, DEMETER, POSEIDON, ARTEMIS, ELEUTHIA, APOLLO, HADES. Antworte NUR mit dem Namen."},
                    {"role": "user", "content": user_input}
                ]
            )
            sub = routing.choices[0].message.content.strip()
            if sub not in sub_katalog:
                sub = "APOLLO"

            # Antwort generieren
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": f"Du bist das GAIA-System aus Horizon. Du antwortest über die Unterfunktion {sub} ({sub_katalog[sub]})."},
                    {"role": "user", "content": user_input}
                ]
            )
            
            reply = response.choices[0].message.content
            
        with st.chat_message("assistant"):
            st.markdown(f"**Aktive Subfunktion:** `{sub}` ({sub_katalog[sub]})")
            st.write(reply)
else:
    st.warning("Bitte gib deinen OpenAI-API-Schlüssel ein, um das GAIA-System zu starten.")

import streamlit as st
import google.generativeai as genai

# Ρύθμιση API
genai.configure(api_key="ΤΟ_API_KEY_ΣΟΥ")
model = genai.GenerativeModel('gemini-1.5-flash')

# Λειτουργία API για την HTML
query_params = st.query_params
if "q" in query_params:
    prompt = f"Είσαι ο Πυθαγόρας. Απάντησε σοφά και πολύ σύντομα (1 πρόταση) στα Ελληνικά: {query_params['q']}"
    response = model.generate_content(prompt)
    st.write(response.text)
    st.stop()

st.title("Pythagoras Brain Server")
st.write("Ο διακομιστής είναι ενεργός!")

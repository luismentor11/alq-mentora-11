import streamlit as st
import google.generativeai as genai

# Título de la App
st.title("Mi Super App con IA 🤖")
st.write("Escribe abajo y la IA te responderá.")

# Configuración de la API Key (la tomaremos de los secretos de Streamlit)
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except:
    st.error("¡Falta la API Key! Configúrala en los secretos de Streamlit.")

# Crear el modelo
model = genai.GenerativeModel('gemini-pro')

# Caja de texto para el usuario
user_input = st.text_area("Ingresa tu texto aquí:", height=150)

# Botón de enviar
if st.button("Enviar a la IA"):
    if user_input:
        with st.spinner("La IA está pensando..."):
            try:
                # Aquí enviamos el mensaje a Gemini
                response = model.generate_content(user_input)
                st.success("¡Respuesta recibida!")
                st.write(response.text)
            except Exception as e:
                st.error(f"Ocurrió un error: {e}")
    else:
        st.warning("Por favor escribe algo antes de enviar.")

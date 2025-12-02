import streamlit as st
import google.generativeai as genai

# --- 1. FRONTEND: Configuración del Título y Descripción ---
st.title("ALQ Asistente de Gestión 📈")
st.write("Tu asistente de IA especializado en administración de alquileres. Pregunta sobre el uso de la app o el estado financiero.")

# --- 2. BACKEND: Configuración de la API Key (Secrets) y el Modelo ---

# La clave de API se toma automáticamente de los 'Secrets' de Streamlit
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except KeyError:
    st.error("¡FALTA LA API KEY! Por favor, añade GOOGLE_API_KEY a los Secrets de Streamlit.")
    st.stop()
except Exception as e:
    st.error(f"Error de configuración: {e}")
    st.stop()

# Usamos el modelo más rápido y capaz para chat
model = genai.GenerativeModel('gemini-2.5-flash')


# --- 3. FRONTEND: Caja de Texto (Define la variable 'user_input') ---
# Aquí es donde el administrador escribe su pregunta.
user_input = st.text_area("Ingresa tu consulta (ej: '¿Cómo hago un cierre de mes?' o '¿Qué dice el saldo del Propietario X?'):", height=150)


# --- 4. LÓGICA: Botón de Envío y Llamada a la IA ---

if st.button("Enviar a la IA"):
    if user_input:
        with st.spinner("ALQ Asistente está analizando la solicitud..."):
            try:
                # ------------------------------------------------
                # CONFIGURACIÓN DEL PROMPT (TU LÓGICA DE AI STUDIO)
                # ------------------------------------------------
                config_ia = genai.types.GenerateContentConfig(
                    system_instruction="""Eres ALQ Asistente de Gestión, una interfaz de inteligencia artificial especializada en sistemas de administración de alquileres. Tu rol es asistir al administrador de la plataforma. Tienes dos funciones principales:
1.  **Asistencia Técnica:** Brindar instrucciones detalladas sobre el uso de cualquier función de la aplicación (ej: 'cómo se registra un pago', 'cómo se genera un informe').
2.  **Resumen de Datos:** Responder preguntas concisas sobre el estado financiero de los alquileres, como 'deuda total', 'cobros por propietario', o 'balance del mes'.
Reglas inquebrantables:
-  Responde de manera directa, breve y profesional.
-  Utiliza siempre el **lenguaje técnico** propio de la administración de alquileres (ej: 'canon', 'expensas', 'saldo').
-  Nunca inventes datos o cifras. Si el usuario pregunta por un número específico (ej: 'deuda de este mes'), pídele que primero ingrese el contexto o especifique el período ('Por favor, especifique el mes o el propietario para obtener el dato')."""
                )
                
                # Envío de la pregunta a Gemini con tu Prompt personalizado
                response = model.generate_content(user_input, config=config_ia)
                
                # Muestra la respuesta en la interfaz
                st.success("¡Respuesta recibida de ALQ Asistente!")
                st.markdown(response.text) # Usamos markdown para mostrar las negritas y formato
                
            except Exception as e:
                # Manejo de errores de la API o del modelo
                st.error(f"Ocurrió un error al contactar a la IA. Inténtalo de nuevo. Detalle: {e}")
    else:
        st.warning("Por favor, escribe tu consulta antes de enviar.")

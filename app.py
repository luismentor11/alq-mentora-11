import streamlit as st # <--- 
import google.generativeai as genai
# Botón de enviar
if st.button("Enviar a la IA"):
    if user_input:
        with st.spinner("La IA está pensando..."):
            try:
                # ------------------------------------------------
                # AÑADIMOS LA CONFIGURACIÓN (TU PROMPT/PERSONALIDAD)
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
                
                # Aquí enviamos el mensaje a Gemini, usando la configuración
                response = model.generate_content(user_input, config=config_ia) 
                
                st.success("¡Respuesta recibida!")
                st.write(response.text)
            except Exception as e:
                st.error(f"Ocurrió un error: {e}")
    else:
        st.warning("Por favor escribe algo antes de enviar.")

import openai
import streamlit as st
import re
import os

# Set up the OpenAI API client
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Define la lista de patrones a buscar
patrones = [
    "los términos del problema se entienden de manera diferente",
    "hay una falta de claridad en los términos utilizados",
    "la fuente de la evidencia no es confiable",
    "se parte de supuestos falsos",
    "se parte de supuestos que no gozan de aceptación general",
    "se ha omitido información relevante",
    "hay una falta de contexto",
    "se incurre en falacias",
    "es posible llegar a otras conclusiones con las mismas razones",
    "lo que se atribuye a una causa puede tener otra causa"
]

def analizar_argumento(argumento):
    # Modifica el prompt para incluir los patrones que quieres buscar
    prompt = f"Analiza el siguiente argumento: {argumento}\n"
    prompt += "Tu tarea es examinar el argumento para ver si incurre en alguna de las siguientes faltas:\n"
    for i, patron in enumerate(patrones):
        prompt += f"{i + 1}. {patron}\n"

    # Usa GPT-3 para analizar el argumento
    respuesta = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.3,
        max_tokens=1024
    )
    resultado = respuesta["choices"][0]["text"]

    # Devuelve el resultado del análisis
    return resultado


def main():
    st.title("Herramienta de análisis de argumentos")
    st.caption("Por Moris Polanco")
    st.caption("Faltas o vicios: 1. Los términos del problema se entienden de manera diferente. 2. Hay una falta de claridad en los términos utilizados. 3. La fuente de la evidencia no es confiable. 4. Se parte de supuestos falsos o cuestionables. 5. Se paarte de supuestos que no son de aceptación general. 6.Se ha omitido información relevante. 7. Hay una falta de contexto. 8. Se incurre en falacias. 9. Es posible llegar a otras conclusiones con las mismas razones. 10. Lo que se atribuye a una causa puede tener otra.")
    argumento = st.text_area("Ingresa tu argumento aquí:")
    if argumento:
        resultado = analizar_argumento(argumento)
        st.write(resultado)

if __name__ == "__main__":
    main()

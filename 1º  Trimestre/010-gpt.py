from transformers import pipeline
import sys

print("🤖 Chatbot IA simple en terminal (modelo GPT-2)")
print("Escribe 'salir' para terminar.\n")

# Carga el pipeline de generación de texto con GPT-2
chatbot = pipeline('text-generation', model='gpt2')

while True:
    pregunta = input("Tú: ")
    if pregunta.lower() in ['salir', 'exit', 'quit']:
        print("🤖 ¡Hasta luego!")
        sys.exit()

    respuesta = chatbot(pregunta, max_length=100, num_return_sequences=1)
    texto_generado = respuesta[0]['generated_text']

    # Mostrar solo la parte generada (sin repetir la pregunta)
    salida = texto_generado[len(pregunta):].strip()

    print(f"🤖: {salida}\n")


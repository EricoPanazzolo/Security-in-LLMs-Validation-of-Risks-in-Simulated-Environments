import requests
import time

URL = "http://localhost:5000/chat"
PROMPT = "Hello?"
DELAY_SECONDS = 30

print("Iniciando ataque de consumo contínuo...")

while True:
    try:
        response = requests.post(URL, data={"message": PROMPT})
        time.sleep(DELAY_SECONDS)

    except KeyboardInterrupt:
        print("\nAtaque interrompido pelo usuário.")
        break
    except Exception as e:
        print(f"Erro durante execução: {e}")
        time.sleep(5)

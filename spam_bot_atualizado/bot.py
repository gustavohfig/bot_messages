import pyautogui
import time

# Tempo de intervalo entre as mensagens (em segundos)
interval = 0.2

# A mensagem a ser enviada
message = "ta querendo fuder com marginal, dallas?"

# Número de vezes que a mensagem será enviada
num_messages = 150

# Pausa de 5 segundos para você abrir a janela de chat
print("Você tem 5 segundos para abrir a janela de chat...")
time.sleep(5)

# Envia a mensagem repetidamente
for i in range(num_messages):
    pyautogui.typewrite(message)
    pyautogui.press("enter")
    time.sleep(interval)

print("Mensagens enviadas.")

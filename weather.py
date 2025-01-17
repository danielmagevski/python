import requests
import sys

# Configuração da API do OpenWeather
CHAVE = ""
URL = "https://api.openweathermap.org/data/2.5/weather"

CIDADE = "São Paulo"
PAIS = "br"

# Configuração do Telegram
BOT_TOKEN = ""
CHAT_ID = ""

def enviar_telegram(mensagem):
    """
    Envia uma mensagem para o Telegram usando o bot configurado.
    """
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": mensagem}
    response = requests.post(telegram_url, data=payload)
    if response.status_code == 200:
        print("Mensagem enviada para o Telegram.")
    else:
        print(f"Erro ao enviar mensagem no Telegram: {response.status_code}", file=sys.stderr)

# Requisição à API do OpenWeather
result = requests.get(URL, params={"q": f"{CIDADE},{PAIS}",
                                   "appid": CHAVE,
                                   "units": "metric",
                                   "lang": "pt_br"})

if result.status_code == 200:
    previsão = result.json()
    mensagem = (
        f"🌍 Cidade: {previsão['name']}\n"
        f"☀️ Atual: {previsão['main']['temp']}°C\n"
        f"🌡️ Mínima: {previsão['main']['temp_min']}°C\n"
        f"🔥 Máxima: {previsão['main']['temp_max']}°C\n"
        f"💨 Sensação térmica: {previsão['main']['feels_like']}°C\n"
        f"💧 Humidade: {previsão['main']['humidity']}%\n"
    )
    print(mensagem)  # Exibe no console
    enviar_telegram(mensagem)  # Envia a mensagem para o Telegram
else:
    erro_msg = f"⚠️ Erro ao obter previsão: {result.status_code}"
    print(erro_msg, file=sys.stderr)
    enviar_telegram(erro_msg)  # Notifica o erro via Telegram
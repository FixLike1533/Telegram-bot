import time
import requests

TOKEN = '7988333845:AAF1hEuriFqwB1U3HiqCxQbz4KKgkUx_2rw'
CHAT_ID = '6029963055'

def send_message():
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': 'евсин пошел нахуй'}
    try:
        requests.post(url, data=data)
        print("Сообщение отправлено.")
    except Exception as e:
        print(f"Ошибка: {e}")

while True:
    send_message()
    time.sleep(3 * 60 * 60)

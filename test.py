from telethon import TelegramClient, events
from SteamKeyActivator.Activator import SteamActivator
import re

api_id = 20261096
api_hash = '4f57917af4afc2a8977458202bbac1a5'

client = TelegramClient('session_name', api_id, api_hash)

pattern = re.compile(r'[A-Z0-9]{5}-[A-Z0-9]{5}-[A-Z0-9]{5}')

activator = SteamActivator()

@client.on(events.NewMessage)
async def handler(event):
    msg_text = event.message.text.strip()

    search = pattern.search(msg_text)

    if search:
        code = search[0]
        print(f"Получен ключ: {code}", end='')
        answer_activation = activator.activate_key(code)
        if answer_activation:
            print(f' ({answer_activation})')



if __name__ == '__main__':
    print("Steam Activator Bot запущен...")
    client.start()
    client.run_until_disconnected()
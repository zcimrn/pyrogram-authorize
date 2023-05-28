#!/usr/bin/env python3


from pyrogram import Client
from sys import argv


API_ID = 0
API_HASH = ''


def main(device_model, name='client'):
    client = Client(
        device_model=device_model,
        name=name,
        api_id=API_ID,
        api_hash=API_HASH,
        hide_password=True
    )
    client.start()
    client.stop()


if __name__ == '__main__':
    main(*argv[1:3])

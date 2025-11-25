import uvloop
import asyncio
from pyrogram import Client

uvloop.install()  # Install uvloop as the event loop policy

API_ID = 24286461  # your api_id here
API_HASH = "fe4f9e040dfefaeb8715e12d1e4da9de"  # your api_hash here
SESSION_NAME = "approve_session"

CHAT_ID = -1003422977804  # your channel or group ID or @username

app = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH)

async def main():
    async with app:
        success = await app.approve_all_chat_join_requests(chat_id=CHAT_ID)
        print(f"Approved all pending join requests: {success}")

if __name__ == "__main__":
    asyncio.run(main())

from pyrogram import Client

# Replace these with your actual Telegram API credentials
API_ID = 24286461  # your api_id from https://my.telegram.org
API_HASH = "fe4f9e040dfefaeb8715e12d1e4da9de"  # your api_hash from https://my.telegram.org

# Session name for Pyrogram, can be any string (creates a session file locally)
SESSION_NAME = "approve_session"

# Your channel or group identifier:
# Use either numeric ID like -1001234567890 or username like "@yourchannelusername"
CHAT_ID = -1001234567890

app = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH)

async def main():
    async with app:
        success = await app.approve_all_chat_join_requests(chat_id=CHAT_ID)
        print(f"Approved all pending join requests: {success}")

if __name__ == "__main__":
    app.run(main())

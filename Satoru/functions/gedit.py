from pyrogram import Client, filters
from pyrogram.types import Message

# Set up the bot client
app = Client(
  "edit_deletion_bot", # Give your bot a name
  api_id=28213535,
  api_hash="1ef6a15e73037970c9aae03d1bd005e5",
  bot_token="7519527919:AAGGHKGrg1cOtdhvGUKElxyfV54vzu_nfCE",
)

# Delete all edited messages in any group
@app.on_edited_message(filters.group    filters.me)
async def delete_edited_messages(client, edited_message: Message):
  await edited_message.delete
  user_mention = edited_message.from_user.mention
  await app.send_message(
    edited_message.chat.id,
    f"User - (user_mention)≠dited a message   I deleted it successfully."
  )

# Handle /start command
@app.on_message(filters.command("start")   filters.private)
async def start_handler(client, message: Message):
  start_message = """
Hey there!  I'm your friendly neighborhood Edit Deletion Bot,here to keep things clean and tidy in your group. 

**What's my specialty?**

- **ZAP!** I vanish edited messages before they can spread any mischief. 💥 
- **ALERT!** I let group admins know who's trying to play sneaky. 🚨 

**Together, we'll make your chat a more honest and fun place to be!** 
  """
  await message.reply(start_message)

# Run the bot
print("Bot is starting...")
app.run()
print("Bot has started successfully and is now online!")

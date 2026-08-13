from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes

Token = "xxx"
Bot_Username ="xxx"

async def start_command (update:Update , context:ContextTypes.DEFAULT_TYPE ):
    user = update.effective_user
    await update.message.reply_text(
    f"سلام {user.first_name or ''}عزیز"
)

async def help_command (update:Update , context:ContextTypes.DEFAULT_TYPE  ):
    await update.message.reply_text('من یک ربات هستم')
async def custom_command(update:Update , context:ContextTypes.DEFAULT_TYPE  ):
    await update.message.reply_text("نمیدونم چیه")

def handle_response(text: str):
    if not text:
        return "متوجه نمیشم چی میگی"
    user_text= text.lower()
    if "سلام" in user_text:
        return "سلام"
    if "خوبی ؟" in user_text:
        return "خوبم خداروشکر"
        

    return " بیشتر از این آموزش ندیدم"
    
async def handle_message (update:Update , context:ContextTypes.DEFAULT_TYPE ):
    if not update.message or not update.message.text:
        return

    message = update.message
    text = message.text
    chat_type = message.chat.type

    print(f"user : {message.chat.id}, chat type : {chat_type} , text :{text}")

    if chat_type in ('group' , "supergroup"):
        if Bot_Username.lower() in text.lower():
            t = text.lower().replace(Bot_Username.lower(), "").strip()
            response = handle_response(t)
        else:
            return  
    else:
        response = handle_response(text)

    await message.reply_text(response)

async def error(update:Update , context:ContextTypes.DEFAULT_TYPE ):
    print(f"update : {update} cause error: {context.error}")

if __name__  == "__main__":
    print("bot is starting ...")
    app = Application.builder().token(Token).build()

    app.add_handler(CommandHandler("start" , start_command))
    app.add_handler(CommandHandler("help" , help_command))
    app.add_handler(CommandHandler("custom" , custom_command))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND , handle_message))

    app.add_error_handler(error)

    print("polling")

    app.run_polling(poll_interval=3)
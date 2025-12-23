import os 
from telegram import Update , InlineKeyboardButton , InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

TOKEN = os.getenv("BOT_TOKEN")

# /start 

async def start(update : Update , context : ContextTypes.DEFAULT_TYPE):
    keyboard = [
         [InlineKeyboardButton("📷 صور", callback_data="images")],
         [InlineKeyboardButton("🎥 فيديوهات", callback_data="videos")]
    ]

    replay_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "اهلا بك , اختر ما تريد",
        reply_markup=replay_markup
    )   

async def buttons(update : Update , context : ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "images":
        keyboard = [
            [InlineKeyboardButton("🌄 طبيعة", callback_data="img_nature")],
            [InlineKeyboardButton("🚗 سيارات", callback_data="img_cars")]
        ]
        await query.edit_message_text(
            "اختر نوع الصور:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "videos":
        keyboard = [
            [InlineKeyboardButton("🎬 قصير", callback_data="vid_short")],
            [InlineKeyboardButton("🎵 موسيقى", callback_data="vid_music")]
        ]
        await query.edit_message_text(
            "اختر نوع الفيديو:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "img_nature":
        await query.message.reply_photo(
            photo="https://picsum.photos/600/400"
        )

    elif query.data == "img_cars":
        await query.message.reply_photo(
            photo="https://picsum.photos/seed/car/600/400"
        )

    elif query.data == "vid_short":
        await query.message.reply_video(
            video="https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4"
        )

    elif query.data == "vid_music":
        await query.message.reply_video(
            video="https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4"
        )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()

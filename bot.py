import os 
from telegram import Update , InlineKeyboardButton , InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

TOKEN = os.getenv("BOT_TOKEN")
  

async def go_to_menu(query , text , keyboard):
    try:
        await query.message.delete()
    except:
        pass

    await query.message.chat.send_message(
        text = text,
        reply_markup = keyboard
    )
def main_menu_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📷 صور", callback_data="images")],
        [InlineKeyboardButton("🎥 فيديوهات", callback_data="videos")]
    ])

def back_keyboard(back_to):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("⬅️ رجوع", callback_data=back_to)],
        [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main")]
    ])
# /start 
async def start(update : Update , context : ContextTypes.DEFAULT_TYPE):
    
    # رسالة تعريفية للمستخدم 
    await update.message.reply_text(
       "أهلاً بك 👋\nاختر نوع المحتوى:",
        reply_markup=main_menu_keyboard()
    )   

async def buttons(update : Update , context : ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "main":
        await go_to_menu(
            query,
            "اختر المحتوى الذي تريديه",
            main_menu_keyboard
        )
    elif query.data == "images":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🌄 طبيعة", callback_data="img_nature")],
            [InlineKeyboardButton("🚗 سيارات", callback_data="img_cars")],
            [InlineKeyboardButton("⬅️ رجوع", callback_data="main")]
        ])
     
        await go_to_menu(
            query,
            "اختر تصنيف الصور:",
            keyboard
        )


    elif query.data == "videos":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🎬 قصير", callback_data="vid_short")],
            [InlineKeyboardButton("🎵 موسيقى", callback_data="vid_music")],
            [InlineKeyboardButton("⬅️ رجوع", callback_data="main")]
        ])
     
        await go_to_menu(
            query,
            "اختر تصنيف الفيديو:",
            keyboard
        )

    elif query.data == "img_nature":
        await query.message.delete()
        await query.message.reply_photo(
            photo="https://picsum.photos/600/400",
            reply_markup=back_keyboard("images")
        )

    elif query.data == "img_cars":
        await query.message.delete()
        await query.message.reply_photo(
            photo="https://picsum.photos/seed/car/600/400",
            reply_markup=back_keyboard("images")
        )

    elif query.data == "vid_short":
        await query.message.delete()
        await query.message.reply_video(
            video="https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4",
            reply_markup=back_keyboard("videos")
        )

    elif query.data == "vid_music":
        await query.message.delete()
        await query.message.reply_video(
            video="https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4",
            reply_markup=back_keyboard("videos")
        )
    


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()

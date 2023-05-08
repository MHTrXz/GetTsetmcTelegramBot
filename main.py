from telegram import *
from telegram.ext import *

import req
import secret
import texts
import file

"""main buttons"""
home_button = "خانه🏠"
status_button = "وضعیت بازار📊"
single_namad_button = "بررسی تکی نماد📉"
watch_button = "دیده بان👁️"
user_namad_button = "پورتفوی🧺"
auth_button = "سازنده👤"

"""status button"""
more_view_bourse = "بیشتر بازدید بورس👁️"
more_view_farabourse = "بیشتر بازدید فرابورس👁️"
effective_ind_bourse = "بیشترین اثر بورس💪"
effective_ind_farabourse = "بیشترین اثر فرابورس💪"
indices_indexes = "شاخص صنایع📈"

"""watch buttons"""
add_watch_button = "افزودن➕"
del_watch_button = "حذف کردن❌"

search_status = ""

"""create updater handler"""
updater = Updater(token=secret.telegram_api_key, use_context=True)

"""create dispatcher"""
dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext):
    """start bot handler"""
    text = f' {update.message.chat.first_name}عزیز' + "\n"
    text += "به ربات سهام خوش اومدی"
    buttons = [[KeyboardButton(status_button)], [KeyboardButton(single_namad_button)],
               [KeyboardButton(watch_button)], [KeyboardButton(auth_button)]]
    context.bot.send_message(chat_id=update.effective_chat.id, text=text,
                             reply_markup=ReplyKeyboardMarkup(buttons))


"""connect start handler"""
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def home(update: Update, context: CallbackContext):
    """home handler"""
    buttons = [[KeyboardButton(status_button)], [KeyboardButton(single_namad_button)],
               [KeyboardButton(watch_button)], [KeyboardButton(auth_button)]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="شما در خانه هستید",
                             reply_markup=ReplyKeyboardMarkup(buttons))


"""connect home handler"""
start_handler = MessageHandler(Filters.regex(home_button), home)
dispatcher.add_handler(start_handler)


def auth(update: Update, context: CallbackContext):
    """auth bot handler"""
    buttons = [[KeyboardButton(status_button)], [KeyboardButton(single_namad_button)],
               [KeyboardButton(watch_button)], [KeyboardButton(auth_button)]]
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="سید محمد حسین هاشمی هستم دانشجوی ترم یک مهندسی کامپیوتر از دانشگاه شهرکرد",
                             reply_markup=ReplyKeyboardMarkup(buttons))


"""connect auth handler"""
auth_handler = MessageHandler(Filters.regex(auth_button), auth)
dispatcher.add_handler(auth_handler)


def mv_bourse_func():
    """show most namad view in bourse market"""

    def mv_bourse(update: Update, context: CallbackContext):
        """handler"""
        context.bot.send_message(chat_id=update.effective_chat.id, text="نماد های بورسی دارای بیشترین بازدید امروز:")
        for namad in texts.show_fav_namad(req.fav_namad_bourse()):
            context.bot.send_message(chat_id=update.effective_chat.id, text=namad)

    """connect handler"""
    mv_bourse_handler = MessageHandler(Filters.regex(more_view_bourse), mv_bourse)
    dispatcher.add_handler(mv_bourse_handler)


def mv_farabourse_func():
    """show most namad view in farabourse market"""

    def mv_farabourse(update: Update, context: CallbackContext):
        """handler"""
        context.bot.send_message(chat_id=update.effective_chat.id, text="نماد های فرابورسی دارای بیشترین بازدید امروز:")
        for namad in texts.show_fav_namad(req.fav_namad_farabourse()):
            context.bot.send_message(chat_id=update.effective_chat.id, text=namad)

    """connect handler"""
    mv_farabourse_handler = MessageHandler(Filters.regex(more_view_farabourse), mv_farabourse)
    dispatcher.add_handler(mv_farabourse_handler)


def effective_bourse_func():
    """show most impact on the bourse market index"""

    def effective_bourse(update: Update, context: CallbackContext):
        """handler"""
        context.bot.send_message(chat_id=update.effective_chat.id, text="نماد های تاثیر گذار بر شاخص بورس:")
        for namad in texts.show_ind_namad(req.ind_namad_bourse()):
            context.bot.send_message(chat_id=update.effective_chat.id, text=namad)

    """connect handler"""
    effective_bourse_handler = MessageHandler(Filters.regex(effective_ind_bourse), effective_bourse)
    dispatcher.add_handler(effective_bourse_handler)


def effective_farabourse_func():
    """show most impact on the farabourse market index"""

    def effective_farabourse(update: Update, context: CallbackContext):
        """handler"""
        context.bot.send_message(chat_id=update.effective_chat.id, text="نماد های تاثیر گذار بر شاخص فرابورس:")
        for namad in texts.show_ind_namad(req.ind_namad_farabourse()):
            context.bot.send_message(chat_id=update.effective_chat.id, text=namad)

    """connect handler"""
    effective_farabourse_handler = MessageHandler(Filters.regex(effective_ind_farabourse), effective_farabourse)
    dispatcher.add_handler(effective_farabourse_handler)


def indices_indexes_market_func():
    """show indices market data"""

    def indices_indexes_market(update: Update, context: CallbackContext):
        """handler"""
        context.bot.send_message(chat_id=update.effective_chat.id, text="شاخص صنایع امروز:")
        for namad in texts.show_market_indices(req.market_indices()):
            context.bot.send_message(chat_id=update.effective_chat.id, text=namad)

    """connect handler"""
    indices_indexes_handler = MessageHandler(Filters.regex(indices_indexes), indices_indexes_market)
    dispatcher.add_handler(indices_indexes_handler)


def status(update: Update, context: CallbackContext):
    """status handler"""
    buttons = [[KeyboardButton(more_view_bourse), KeyboardButton(more_view_farabourse)],
               [KeyboardButton(effective_ind_bourse), KeyboardButton(effective_ind_farabourse)],
               [KeyboardButton(home_button), KeyboardButton(indices_indexes)]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="وضعیت بازار امروز",
                             reply_markup=ReplyKeyboardMarkup(buttons))
    context.bot.send_message(chat_id=update.effective_chat.id, text=texts.show_bourse_market(req.market_bourse()))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=texts.show_farabourse_market(req.market_farabourse()))

    """show data handlers"""
    mv_bourse_func()
    mv_farabourse_func()
    effective_bourse_func()
    effective_farabourse_func()
    indices_indexes_market_func()


"""connect status handler"""
status_handler = MessageHandler(Filters.regex(status_button), status)
dispatcher.add_handler(status_handler)


def single_echo(update: Update, context: CallbackContext):
    global search_status
    if search_status == "single":
        """make inline buttons"""
        data_search = texts.search_list(req.namad_search(update.message.text))[:20]
        if len(data_search):
            buttons = []
            for i in data_search:
                """make unique callback data for each buttons"""
                buttons.append([InlineKeyboardButton(i[0], callback_data="showSearch_" + i[1])])
            """return buttons"""
            context.bot.send_message(chat_id=update.effective_chat.id, text="انتخواب کنید",
                                     reply_markup=InlineKeyboardMarkup(buttons))
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="چیزی پیدا نشد")
        search_status = ""
        return
    elif search_status == "watch":
        data_search = texts.search_list(req.namad_search(update.message.text))[:20]
        if len(data_search):
            buttons = []
            for i in texts.search_list(req.namad_search(update.message.text))[:20]:
                buttons.append(
                    [InlineKeyboardButton(i[0], callback_data="addWatch_" + i[1] + "_" + str(update.message.chat_id))])
            context.bot.send_message(chat_id=update.effective_chat.id, text="سهام مورد نظر را جهت افزودن انتخواب کنید:",
                                     reply_markup=InlineKeyboardMarkup(buttons))
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="چیزی پیدا نشد")
        search_status = ""
        return


def single(update: Update, context: CallbackContext):
    """single namad data handler"""

    context.bot.send_message(chat_id=update.effective_chat.id, text="جست و جو در نماد ها:")

    """echo handler"""
    global search_status
    search_status = "single"
    """connect echo handler"""
    single_echo_handler = MessageHandler(Filters.text & (~Filters.command), single_echo)
    dispatcher.add_handler(single_echo_handler)


"""connect single handler"""
single_handler = MessageHandler(Filters.regex(single_namad_button), single)
dispatcher.add_handler(single_handler)


def add_handler_show():
    """add namad"""

    def add(update: Update, context: CallbackContext):
        """add namad handler"""
        context.bot.send_message(chat_id=update.effective_chat.id, text="جست و جو در نماد ها:")

        global search_status
        search_status = "watch"
        """connect echo handler"""
        single_echo_handler = MessageHandler(Filters.text & (~Filters.command), single_echo)
        dispatcher.add_handler(single_echo_handler)

    """connect handler"""
    add_handler = MessageHandler(Filters.regex(add_watch_button), add)
    dispatcher.add_handler(add_handler)


def del_handler_show():
    """delete namad"""

    def dell(update: Update, context: CallbackContext):
        """delete handler"""
        user_namad_show = file.find_user_watch(update.message.chat_id)

        """make buttons"""
        buttons = []
        for i in req.search_code(user_namad_show):
            buttons.append(
                [InlineKeyboardButton(i[0], callback_data="delWatch_" + i[1] + "_" + str(update.message.chat_id))])
        context.bot.send_message(chat_id=update.effective_chat.id, text="سهام مورد نظر را جهت حذف انتخواب کنید:",
                                 reply_markup=InlineKeyboardMarkup(buttons))

    """connect handler"""
    dell_handler = MessageHandler(Filters.regex(del_watch_button), dell)
    dispatcher.add_handler(dell_handler)


def watch(update: Update, context: CallbackContext):
    """watch main handler"""

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="دیده بان" + "\n" + "در این قسمت وضعیت سهام هایی که سیو کردید را میتوانید ببینید")
    saved_data = file.find_user_watch(update.message.chat_id)

    """check user for prepare data"""
    if saved_data and saved_data[0]:
        buttons = [[KeyboardButton(add_watch_button), KeyboardButton(del_watch_button)],
                   [KeyboardButton(watch_button)], [KeyboardButton(home_button)]]
        context.bot.send_message(chat_id=update.effective_chat.id, text="نماد های ثبت شده شما:",
                                 reply_markup=ReplyKeyboardMarkup(buttons))
        for text in texts.all_namad_search(req.all_namad_data(), saved_data):
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    else:
        buttons = [[KeyboardButton(add_watch_button)],
                   [KeyboardButton(watch_button)], [KeyboardButton(home_button)]]
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="\nهیچ سهامی در این قسمت سیو نکردید."
                                      + "لطفا از قسمت افزودن سهم های دلخواه خود را اضافه کنید.",
                                 reply_markup=ReplyKeyboardMarkup(buttons))

    """add or delete handlers"""
    add_handler_show()
    del_handler_show()


"""connect watch handler"""
watch_handler = MessageHandler(Filters.regex(watch_button), watch)
dispatcher.add_handler(watch_handler)


def callback(update: Update, context: CallbackContext):
    """callbacks"""
    query = update.callback_query.data
    update.callback_query.answer()

    if query.find("showSearch_") >= 0:
        """show search result"""
        namad = query.split("_")[1]
        """make unique buttons"""
        buttons = [[InlineKeyboardButton("تغییرات 15 روز", callback_data="showData_" + namad + "_15day-history"),
                    InlineKeyboardButton("تغییرات 30 روز", callback_data="showData_" + namad + "_30day-history")],
                   [InlineKeyboardButton("آمار نماد", callback_data="showData_" + namad + "_state")],
                   [InlineKeyboardButton("سهامداران عمده", callback_data="showData_" + namad + "_stockholder")],
                   [InlineKeyboardButton("اطلاعیه های کدال", callback_data="showData_" + namad + "_codal")],
                   [InlineKeyboardButton("خرید و فروس حقیقی", callback_data="showData_" + namad + "_realPower")]]
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=texts.show_single_namad(req.single_namad_data(namad)),
                                 reply_markup=InlineKeyboardMarkup(buttons))
    elif query.find("showData_") >= 0:
        """show namad data"""
        data = query.split("_")
        data.remove("showData")
        namad = req.search_code_name(data.pop(0))
        if data[0] == "15day-history":
            """show 15 days namad history"""
            for text in texts.show_namad_nday_history(req.namad_nday_history(namad, 15)):
                context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        elif data[0] == "30day-history":
            for text in texts.show_namad_nday_history(req.namad_nday_history(namad, 30)):
                context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        elif data[0] == "state":
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=texts.show_namad_stats(req.namad_stats(namad)))
        elif data[0] == "stockholder":
            context.bot.send_message(chat_id=update.effective_chat.id, text="\n----------\n".join(
                texts.show_namad_stockholder(req.namad_stockholder(namad))))
        elif data[0] == "codal":
            for text in texts.show_namad_codal(req.namad_codal(namad)):
                context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        elif data[0] == "realPower":
            for text in texts.show_co_real_power(req.co_real_power(namad)):
                context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    elif query.find("addWatch_") >= 0:
        """add namad to watch"""
        user_data = file.find_user_watch(query.split("_")[2])
        namad = query.split("_")[1]
        if user_data and namad in user_data:
            context.bot.send_message(chat_id=update.effective_chat.id, text="از قبل وجود دارد")
        else:
            if type(user_data) == bool:
                file.add_user_watch([query.split("_")[2], namad])
                context.bot.send_message(chat_id=update.effective_chat.id, text="با موفقیت در دیده بان شما سیو شد")
            else:
                file.update_user_watch([query.split("_")[2], namad] + user_data)
                context.bot.send_message(chat_id=update.effective_chat.id, text="با موفقیت در دیده بان شما سیو شد")

    elif query.find("delWatch_") >= 0:
        """delete namad from watch"""
        user_data = file.find_user_watch(query.split("_")[2])
        namad = query.split("_")[1]
        if user_data and (namad in user_data):
            user_data.remove(namad)
            file.update_user_watch([query.split("_")[2]] + user_data)
            context.bot.send_message(chat_id=update.effective_chat.id, text="با موفقیت از دیده بان شما حذف شد")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="از قبل موجود است")


"""connect callback handler"""
handle_search_handler = CallbackQueryHandler(callback)
dispatcher.add_handler(handle_search_handler)

"""start loop"""
updater.start_polling()
updater.idle()
print("run")

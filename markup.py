from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import config

main_menu = ReplyKeyboardMarkup(resize_keyboard = True)
main_menu.add(
            KeyboardButton('🛠 Создать пару ключей'),
            KeyboardButton('➕ Давить ключи')
           
        )
        
main_menu.add(
    KeyboardButton('❌ Удалить ключ'),
    KeyboardButton('💱 Изменить текст')
)
        
cancel = ReplyKeyboardMarkup(resize_keyboard =True)

cancel.add(
        KeyboardButton('🚫 Отмена')
    )
def get_all_pair_markup(lists):
    menu = InlineKeyboardMarkup()
    for i in lists:
        menu.add(
                InlineKeyboardButton(text = f"{i['name']}", callback_data = f"add_key_{i['name']}")
            )
    return menu


def get_all_pair_markup_del(lists):
    menu = InlineKeyboardMarkup()
    for i in lists:
        menu.add(
                InlineKeyboardButton(text = f"{i['name']}", callback_data = f"del_key_{i['name']}")
            )
    return menu

def get_keys_markup(lists):
    menu = InlineKeyboardMarkup()
    for i in lists:
        menu.add(
                InlineKeyboardButton(text = f"❌{i['key']}", callback_data = f"del2_key_{i['key']}")
            )
    return menu    
    
def get_all_pair_markup_text(lists):
    menu = InlineKeyboardMarkup()
    for i in lists:
        menu.add(
                InlineKeyboardButton(text = f"{i['name']}", callback_data = f"up_text_{i['name']}")
            )
    return menu    

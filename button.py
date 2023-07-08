from aiogram.types import ReplyKeyboardMarkup,KeyboardButton, \
    KeyboardButton, \
    InlineKeyboardMarkup,\
    InlineKeyboardButton
    
    

lang = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🇺🇿 Ozbekcha"),
            KeyboardButton("🇷🇺 Russcha"),
            KeyboardButton("🇺🇸 English"),
        ],

    ],
    resize_keyboard=True
)


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Buyurtma berish"),
        ],
        
        [
            KeyboardButton("Sozlamalar"),
            KeyboardButton("Biz blan boglaning"),
        ],
        

    ],
    resize_keyboard=True
)

yuqori_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Lavash🌯🌯",callback_data='Lavash🌯🌯'),
            InlineKeyboardButton(text="Hot-dog🌭🌭",callback_data='Hot-dog🌭🌭'),
        ],
        [
            InlineKeyboardButton(text="Sendvich club 🥪🥪",callback_data='Sendvich club 🥪🥪'),
            InlineKeyboardButton(text="Shourma 🌮🌮",callback_data='Shourma 🌮🌮'),
        ],
        [
             InlineKeyboardButton(text="Burger 🍔🍔",callback_data='Burger 🍔🍔'),
            InlineKeyboardButton(text="Donar 🍱🍱",callback_data='Donar 🍱🍱'),
        ],
        
        [
           InlineKeyboardButton(text="Gazaklar 🍟🍟",callback_data='Gazaklar 🍟🍟'),
            InlineKeyboardButton(text="Ichimlikar 🍹🍹",callback_data='Ichimlikar 🍹🍹'),
        ],
        
        [
            InlineKeyboardButton(text="Desertlar 🍰🍰",callback_data='Desertlar 🍰🍰'),
            InlineKeyboardButton(text="Pizza 🍕🍕",callback_data='Pizza 🍕🍕'),
        ],
        
    ]
)


lavash_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='Mol gushtli🥩',callback_data='Mol gushtli🥩'),
            KeyboardButton(text='Qalampirli🌶',callback_data='Qalampirli🌶'),
        ],
        
        [
            KeyboardButton(text='Tovuq goshtli🍗',callback_data='Tovuq goshtli🍗'),
            KeyboardButton(text='Qalampirli tovuq goshtli🍗🌶',callback_data='Qalampirli tovuq goshtli🍗🌶'),
        ],
        
        [
            KeyboardButton(text='Pishloqli Tovuq goshtli🧀🍗',callback_data='Pishloqli Tovuq goshtli🧀🍗'),
            KeyboardButton(text='Pishloqli mol goshtli🥩🧀',callback_data='Pishloqli mol goshtli🥩🧀'),
        ],
        
        [
            KeyboardButton(text='Ortga',callback_data='back_1'),
        ],
        

    ],
    resize_keyboard=True
)

# lavash_menu_mol_gushtli = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             KeyboardButton(text='Mini👍',callback_data='Mini👍'),
#             KeyboardButton(text='Big👍',callback_data='Big👍'),
#         ],
        
#         [
#             KeyboardButton(text='Ortga',callback_data='back_'),
#         ],
        

#     ],
#     resize_keyboard=True
# )


mol_g_mini = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='Mini 👍    ',callback_data='Mini 👍    '),
            KeyboardButton(text='Big 👍    ',callback_data='Big 👍    '),
        ],
        
        [
            KeyboardButton(text='Ortga',callback_data='back_'),
        ],
        

    ],
    resize_keyboard=True
)






mol_g_numbers =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='1️⃣',callback_data='1️⃣'),
            KeyboardButton(text='2️⃣',callback_data='2️⃣'),
            KeyboardButton(text='3️⃣',callback_data='3️⃣'),
        ],
        
        [
            KeyboardButton(text='4️⃣',callback_data='4️⃣'),
            KeyboardButton(text='5️⃣',callback_data='5️⃣'),
            KeyboardButton(text='6️⃣',callback_data='6️⃣'),
        ],
        
        [
            KeyboardButton(text='7️⃣',callback_data='7️⃣'),
            KeyboardButton(text='8️⃣',callback_data='8️⃣'),
            KeyboardButton(text='9️⃣',callback_data='9️⃣'),
        ],
        [
            KeyboardButton(text='Ortga',callback_data='1back_'),
        ],
        

    ],
    resize_keyboard=True
)







lavash_menu_qalampir_gushtli = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='Mini👍',callback_data='Mini👍'),
            KeyboardButton(text='Big👍',callback_data='Big👍'),
        ],
        
        [
            KeyboardButton(text='Ortga',callback_data='back_'),
        ],
        

    ],
    resize_keyboard=True
)


qalampir_g_numbers =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='1️⃣',callback_data='1️⃣'),
            KeyboardButton(text='2️⃣',callback_data='2️⃣'),
            KeyboardButton(text='3️⃣',callback_data='3️⃣'),
        ],
        
        [
            KeyboardButton(text='4️⃣',callback_data='4️⃣'),
            KeyboardButton(text='5️⃣',callback_data='5️⃣'),
            KeyboardButton(text='6️⃣',callback_data='6️⃣'),
        ],
        
        [
            KeyboardButton(text='7️⃣',callback_data='7️⃣'),
            KeyboardButton(text='8️⃣',callback_data='8️⃣'),
            KeyboardButton(text='9️⃣',callback_data='9️⃣'),
        ],
        [
            KeyboardButton(text='Ortga',callback_data='2back_'),
        ],
        

    ],
    resize_keyboard=True
)


lavash_menu_tovuq_gushtli = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='Mini 👍',callback_data='Mini 👍'),
            KeyboardButton(text='Big 👍',callback_data='Big 👍'),
        ],
        
        [
            KeyboardButton(text='Ortga',callback_data='back_'),
        ],
        

    ],
    resize_keyboard=True
)

tovuq_g_numbers =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='1️⃣',callback_data='1️⃣'),
            KeyboardButton(text='2️⃣',callback_data='2️⃣'),
            KeyboardButton(text='3️⃣',callback_data='3️⃣'),
        ],
        
        [
            KeyboardButton(text='4️⃣',callback_data='4️⃣'),
            KeyboardButton(text='5️⃣',callback_data='5️⃣'),
            KeyboardButton(text='6️⃣',callback_data='6️⃣'),
        ],
        
        [
            KeyboardButton(text='7️⃣',callback_data='7️⃣'),
            KeyboardButton(text='8️⃣',callback_data='8️⃣'),
            KeyboardButton(text='9️⃣',callback_data='9️⃣'),
        ],
        [
            KeyboardButton(text='Ortga',callback_data='3back_'),
        ],
        

    ],
    resize_keyboard=True
)



lavash_menu_qalampir_tovuq_gushtli = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='Mini 👍 ',callback_data='Mini 👍 '),
            KeyboardButton(text='Big 👍 ',callback_data='Big 👍 '),
        ],
        
        [
            KeyboardButton(text='Ortga',callback_data='back_'),
        ],
        

    ],
    resize_keyboard=True
)

tovuq_qalampir_g_numbers =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='1️⃣',callback_data='1️⃣'),
            KeyboardButton(text='2️⃣',callback_data='2️⃣'),
            KeyboardButton(text='3️⃣',callback_data='3️⃣'),
        ],
        
        [
            KeyboardButton(text='4️⃣',callback_data='4️⃣'),
            KeyboardButton(text='5️⃣',callback_data='5️⃣'),
            KeyboardButton(text='6️⃣',callback_data='6️⃣'),
        ],
        
        [
            KeyboardButton(text='7️⃣',callback_data='7️⃣'),
            KeyboardButton(text='8️⃣',callback_data='8️⃣'),
            KeyboardButton(text='9️⃣',callback_data='9️⃣'),
        ],
        [
            KeyboardButton(text='Ortga',callback_data='4back_'),
        ],
        

    ],
    resize_keyboard=True
)


lavash_menu_pishloq_tovuq_gushtli = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='Mini 👍  ',callback_data='Mini 👍  '),
            KeyboardButton(text='Big 👍  ',callback_data='Big 👍  '),
        ],
        
        [
            KeyboardButton(text='Ortga',callback_data='back_'),
        ],
        

    ],
    resize_keyboard=True
)

tovuq_pishloq_g_numbers =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='1️⃣',callback_data='1️⃣'),
            KeyboardButton(text='2️⃣',callback_data='2️⃣'),
            KeyboardButton(text='3️⃣',callback_data='3️⃣'),
        ],
        
        [
            KeyboardButton(text='4️⃣',callback_data='4️⃣'),
            KeyboardButton(text='5️⃣',callback_data='5️⃣'),
            KeyboardButton(text='6️⃣',callback_data='6️⃣'),
        ],
        
        [
            KeyboardButton(text='7️⃣',callback_data='7️⃣'),
            KeyboardButton(text='8️⃣',callback_data='8️⃣'),
            KeyboardButton(text='9️⃣',callback_data='9️⃣'),
        ],
        [
            KeyboardButton(text='Ortga',callback_data='5back_'),
        ],
        

    ],
    resize_keyboard=True
)




lavash_menu_pishloq_mol_gushtli = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='Mini 👍   ',callback_data='Mini 👍   '),
            KeyboardButton(text='Big 👍   ',callback_data='Big 👍   '),
        ],
        
        [
            KeyboardButton(text='Ortga',callback_data='back_'),
        ],
        

    ],
    resize_keyboard=True
)

mol_pishloq_g_numbers =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='1️⃣',callback_data='1️⃣'),
            KeyboardButton(text='2️⃣',callback_data='2️⃣'),
            KeyboardButton(text='3️⃣',callback_data='3️⃣'),
        ],
        
        [
            KeyboardButton(text='4️⃣',callback_data='4️⃣'),
            KeyboardButton(text='5️⃣',callback_data='5️⃣'),
            KeyboardButton(text='6️⃣',callback_data='6️⃣'),
        ],
        
        [
            KeyboardButton(text='7️⃣',callback_data='7️⃣'),
            KeyboardButton(text='8️⃣',callback_data='8️⃣'),
            KeyboardButton(text='9️⃣',callback_data='9️⃣'),
        ],
        [
            KeyboardButton(text='Ortga',callback_data='6back_'),
        ],
        

    ],
    resize_keyboard=True
)








Hotdog_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='Hot Dog obichniy👍',callback_data='Hot Dog obichniy👍'),
            KeyboardButton(text='Classik Hot Dog👍',callback_data='Classik Hot Dog👍'),
        ],
        
        [
            KeyboardButton(text='Korolevskiy👍',callback_data='Korolevskiy👍'),
            KeyboardButton(text='Tovuqli Hot Dog👍',callback_data='Tovuqli Hot Dog👍'),
        ],
        
        [
            KeyboardButton(text='Ortga',callback_data='back__2'),
        ],
        

    ],
    resize_keyboard=True
)



hotdog_numbers =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='1️⃣',callback_data='1️⃣'),
            KeyboardButton(text='2️⃣',callback_data='2'),
            KeyboardButton(text='3️⃣',callback_data='3'),
        ],
        
        [
            KeyboardButton(text='4️⃣',callback_data='1'),
            KeyboardButton(text='5️⃣',callback_data='2'),
            KeyboardButton(text='6️⃣',callback_data='3'),
        ],
        
        [
            KeyboardButton(text='7️⃣',callback_data='1'),
            KeyboardButton(text='8️⃣',callback_data='2'),
            KeyboardButton(text='9️⃣',callback_data='3'),
        ],
        [
            KeyboardButton(text='Ortga',callback_data='back_3'),
        ],
        

    ],
    resize_keyboard=True
)




Sendwich_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='lassik Club Sendwich👍',callback_data='lassik Club Sendwich👍'),
            KeyboardButton(text='Tovuqli Club Sendwich👍',callback_data='Tovuqli Club Sendwich👍'),
        ],
        
        [
            KeyboardButton(text='Ortga',callback_data='back_4'),
        ],

    ],
    resize_keyboard=True
)





sendvich_numbers =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='1️⃣',callback_data='1️⃣'),
            KeyboardButton(text='2️⃣',callback_data='2'),
            KeyboardButton(text='3️⃣',callback_data='3'),
        ],
        
        [
            KeyboardButton(text='4️⃣',callback_data='1'),
            KeyboardButton(text='5️⃣',callback_data='2'),
            KeyboardButton(text='6️⃣',callback_data='3'),
        ],
        
        [
            KeyboardButton(text='7️⃣',callback_data='1'),
            KeyboardButton(text='8️⃣',callback_data='2'),
            KeyboardButton(text='9️⃣',callback_data='3'),
        ],
        [
            KeyboardButton(text='Ortga',callback_data='back_5'),
        ],
        

    ],
    resize_keyboard=True
)






Shaurma_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='Mol Goshtli Shaurma👍',callback_data='Mol Goshtli Shaurma👍'),
            KeyboardButton(text='Tovuq Shaurma👍',callback_data='Tovuq Shaurma👍'),
        ],
        
         [
            KeyboardButton(text='Tovuq Goshtli+Qalampirli Shaurma👍',callback_data='Tovuq Goshtli+Qalampirli Shaurma👍'),
            KeyboardButton(text='Mol Goshtli+Qalampirli Shaurma👍',callback_data='Mol Goshtli+Qalampirli Shaurma👍'),
        ],
         
        [
            KeyboardButton(text='Ortga',callback_data='back_6'),
        ],

    ],
    resize_keyboard=True
)




Shourma_numbers =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='1️⃣',callback_data='1️⃣'),
            KeyboardButton(text='2️⃣',callback_data='2'),
            KeyboardButton(text='3️⃣',callback_data='3'),
        ],
        
        [
            KeyboardButton(text='4️⃣',callback_data='1'),
            KeyboardButton(text='5️⃣',callback_data='2'),
            KeyboardButton(text='6️⃣',callback_data='3'),
        ],
        
        [
            KeyboardButton(text='7️⃣',callback_data='1'),
            KeyboardButton(text='8️⃣',callback_data='2'),
            KeyboardButton(text='9️⃣',callback_data='3'),
        ],
        [
            KeyboardButton(text='Ortga',callback_data='back_7'),
        ],
        

    ],
    resize_keyboard=True
)


Shaurma_menu_1= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='Mini   👍',callback_data='Mini   👍'),
            KeyboardButton(text='Big   👍',callback_data='Big   👍'),
        ],
        
        [
            KeyboardButton(text='Ortga',callback_data='back_8'),
        ],
        

    ],
    resize_keyboard=True
)

Shaurma_menu_2= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text=' Mini   👍',callback_data=' Mini   👍'),
            KeyboardButton(text=' Big   👍',callback_data=' Big   👍'),
        ],
        
        [
            KeyboardButton(text='Ortga',callback_data='back_8'),
        ],
        

    ],
    resize_keyboard=True
)


Shourma_numbers1 =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='1️⃣',callback_data='1️⃣'),
            KeyboardButton(text='2️⃣',callback_data='2'),
            KeyboardButton(text='3️⃣',callback_data='3'),
        ],
        
        [
            KeyboardButton(text='4️⃣',callback_data='1'),
            KeyboardButton(text='5️⃣',callback_data='2'),
            KeyboardButton(text='6️⃣',callback_data='3'),
        ],
        
        [
            KeyboardButton(text='7️⃣',callback_data='1'),
            KeyboardButton(text='8️⃣',callback_data='2'),
            KeyboardButton(text='9️⃣',callback_data='3'),
        ],
        [
            KeyboardButton(text='Ortga',callback_data='7back_7'),
        ],
        

    ],
    resize_keyboard=True
)






Shaurma_menu_3= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text=' Mini   👍',callback_data=' Mini   👍'),
            KeyboardButton(text=' Big   👍',callback_data=' Big   👍'),
        ],
        
        [
            KeyboardButton(text='Ortga',callback_data='back_8'),
        ],
        

    ],
    resize_keyboard=True
)


Shourma_numbers2 =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='1️⃣',callback_data='1️⃣'),
            KeyboardButton(text='2️⃣',callback_data='2'),
            KeyboardButton(text='3️⃣',callback_data='3'),
        ],
        
        [
            KeyboardButton(text='4️⃣',callback_data='1'),
            KeyboardButton(text='5️⃣',callback_data='2'),
            KeyboardButton(text='6️⃣',callback_data='3'),
        ],
        
        [
            KeyboardButton(text='7️⃣',callback_data='1'),
            KeyboardButton(text='8️⃣',callback_data='2'),
            KeyboardButton(text='9️⃣',callback_data='3'),
        ],
        [
            KeyboardButton(text='Ortga',callback_data='8back_7'),
        ],
        

    ],
    resize_keyboard=True
)




Shaurma_menu_4= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text=' Mini   👍',callback_data=' Mini   👍'),
            KeyboardButton(text=' Big   👍',callback_data=' Big   👍'),
        ],
        
        [
            KeyboardButton(text='Ortga',callback_data='back_8'),
        ],
        

    ],
    resize_keyboard=True
)


Shourma_numbers3 =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='1️⃣',callback_data='1️⃣'),
            KeyboardButton(text='2️⃣',callback_data='2'),
            KeyboardButton(text='3️⃣',callback_data='3'),
        ],
        
        [
            KeyboardButton(text='4️⃣',callback_data='1'),
            KeyboardButton(text='5️⃣',callback_data='2'),
            KeyboardButton(text='6️⃣',callback_data='3'),
        ],
        
        [
            KeyboardButton(text='7️⃣',callback_data='1'),
            KeyboardButton(text='8️⃣',callback_data='2'),
            KeyboardButton(text='9️⃣',callback_data='3'),
        ],
        [
            KeyboardButton(text='Ortga',callback_data='9back_7'),
        ],
        

    ],
    resize_keyboard=True
)




Burger_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='Gamburger👍',callback_data='Gamburger👍'),
            KeyboardButton(text='Chizburger👍',callback_data='Chizburger👍'),
        ],
        
        [
            KeyboardButton(text='Ortga',callback_data='back_9'),
        ],
        
         

    ],
    resize_keyboard=True
)


Burger_numbers =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='1️⃣',callback_data='1️⃣'),
            KeyboardButton(text='2️⃣',callback_data='2'),
            KeyboardButton(text='3️⃣',callback_data='3'),
        ],
        
        [
            KeyboardButton(text='4️⃣',callback_data='1'),
            KeyboardButton(text='5️⃣',callback_data='2'),
            KeyboardButton(text='6️⃣',callback_data='3'),
        ],
        
        [
            KeyboardButton(text='7️⃣',callback_data='1'),
            KeyboardButton(text='8️⃣',callback_data='2'),
            KeyboardButton(text='9️⃣',callback_data='3'),
        ],
        [
            KeyboardButton(text='Ortga',callback_data='back_10'),
        ],
        

    ],
    resize_keyboard=True
)




Donar_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='Tovuqli👍',callback_data='Tovuqli👍'),
            KeyboardButton(text='Goshtlik👍',callback_data='Goshtlik👍'),
        ],
        
        [
            KeyboardButton(text='Ortga',callback_data='back_11'),
        ],
        
         

    ],
    resize_keyboard=True
)




Donar_numbers =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='1️⃣',callback_data='1️⃣'),
            KeyboardButton(text='2️⃣',callback_data='2'),
            KeyboardButton(text='3️⃣',callback_data='3'),
        ],
        
        [
            KeyboardButton(text='4️⃣',callback_data='1'),
            KeyboardButton(text='5️⃣',callback_data='2'),
            KeyboardButton(text='6️⃣',callback_data='3'),
        ],
        
        [
            KeyboardButton(text='7️⃣',callback_data='1'),
            KeyboardButton(text='8️⃣',callback_data='2'),
            KeyboardButton(text='9️⃣',callback_data='3'),
        ],
        [
            KeyboardButton(text='Ortga',callback_data='back_12'),
        ],
        

    ],
    resize_keyboard=True
)


Gazaklar_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='15 gram Fri👍',callback_data='15 gram Fri👍'),
            KeyboardButton(text='Kartoshkali+sousli Fri👍',callback_data='Kartoshkali+sousli Fri👍'),
        ],
        
         [
            KeyboardButton(text='Gruch katta👍',callback_data='Gruch katta👍'),
            KeyboardButton(text='Gruch kichik katta👍',callback_data='Gruch kichik katta👍'),
        ],
         
        [
            KeyboardButton(text='Ortga',callback_data='back_13'),
        ],
        
         

    ],
    resize_keyboard=True
)


Gazaklar_numbers =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='1️⃣',callback_data='1️⃣'),
            KeyboardButton(text='2️⃣',callback_data='2'),
            KeyboardButton(text='3️⃣',callback_data='3'),
        ],
        
        [
            KeyboardButton(text='4️⃣',callback_data='1'),
            KeyboardButton(text='5️⃣',callback_data='2'),
            KeyboardButton(text='6️⃣',callback_data='3'),
        ],
        
        [
            KeyboardButton(text='7️⃣',callback_data='1'),
            KeyboardButton(text='8️⃣',callback_data='2'),
            KeyboardButton(text='9️⃣',callback_data='3'),
        ],
        [
            KeyboardButton(text='Ortga',callback_data='back_14'),
        ],
        

    ],
    resize_keyboard=True
)


Ichimliklar_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='Choy va koffe👍',callback_data='Choy va koffe👍'),
            KeyboardButton(text='Yaxna Ichimliklar👍',callback_data='Yaxna Ichimliklar👍'),
        ],
        
         [
            KeyboardButton(text='Fresh va tabbiy soklar👍',callback_data='Fresh va tabbiy soklar👍'),
        ],
         
        [
            KeyboardButton(text='Ortga',callback_data='back_15'),
        ],
        
         

    ],
    resize_keyboard=True
)





Ichimliklar_numbers =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='1️⃣',callback_data='1️⃣'),
            KeyboardButton(text='2️⃣',callback_data='2'),
            KeyboardButton(text='3️⃣',callback_data='3'),
        ],
        
        [
            KeyboardButton(text='4️⃣',callback_data='1'),
            KeyboardButton(text='5️⃣',callback_data='2'),
            KeyboardButton(text='6️⃣',callback_data='3'),
        ],
        
        [
            KeyboardButton(text='7️⃣',callback_data='1'),
            KeyboardButton(text='8️⃣',callback_data='2'),
            KeyboardButton(text='9️⃣',callback_data='3'),
        ],
        [
            KeyboardButton(text='Ortga',callback_data='back_16'),
        ],
        

    ],
    resize_keyboard=True
)


IIchimliklar_numbers =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='1️⃣',callback_data='1️⃣'),
            KeyboardButton(text='2️⃣',callback_data='2'),
            KeyboardButton(text='3️⃣',callback_data='3'),
        ],
        
        [
            KeyboardButton(text='4️⃣',callback_data='1'),
            KeyboardButton(text='5️⃣',callback_data='2'),
            KeyboardButton(text='6️⃣',callback_data='3'),
        ],
        
        [
            KeyboardButton(text='7️⃣',callback_data='1'),
            KeyboardButton(text='8️⃣',callback_data='2'),
            KeyboardButton(text='9️⃣',callback_data='3'),
        ],
        [
            KeyboardButton(text='Ortga',callback_data='back__16'),
        ],
        

    ],
    resize_keyboard=True
)



IIIchimliklar_numbers =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='1️⃣',callback_data='1️⃣'),
            KeyboardButton(text='2️⃣',callback_data='2'),
            KeyboardButton(text='3️⃣',callback_data='3'),
        ],
        
        [
            KeyboardButton(text='4️⃣',callback_data='1'),
            KeyboardButton(text='5️⃣',callback_data='2'),
            KeyboardButton(text='6️⃣',callback_data='3'),
        ],
        
        [
            KeyboardButton(text='7️⃣',callback_data='1'),
            KeyboardButton(text='8️⃣',callback_data='2'),
            KeyboardButton(text='9️⃣',callback_data='3'),
        ],
        [
            KeyboardButton(text='Ortga',callback_data='back___16'),
        ],
        

    ],
    resize_keyboard=True
)



IIIIchimliklar_numbers =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='1️⃣',callback_data='1️⃣'),
            KeyboardButton(text='2️⃣',callback_data='2'),
            KeyboardButton(text='3️⃣',callback_data='3'),
        ],
        
        [
            KeyboardButton(text='4️⃣',callback_data='1'),
            KeyboardButton(text='5️⃣',callback_data='2'),
            KeyboardButton(text='6️⃣',callback_data='3'),
        ],
        
        [
            KeyboardButton(text='7️⃣',callback_data='1'),
            KeyboardButton(text='8️⃣',callback_data='2'),
            KeyboardButton(text='9️⃣',callback_data='3'),
        ],
        [
            KeyboardButton(text='Ortga',callback_data='back____16'),
        ],
        

    ],
    resize_keyboard=True
)



Koffe_Choylar_menu_1= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='Kofellar👍',callback_data='Kofellar👍'),
            KeyboardButton(text='Choylar👍',callback_data='Choylar👍'),
        ],
        
        [
            KeyboardButton(text='Ortga',callback_data='back_17'),
        ],
        

    ],
    resize_keyboard=True
)


Koffe_Choylar_menu_2= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='Americano👍',callback_data='Americano👍'),
            KeyboardButton(text='Cappuccino👍',callback_data='Cappuccino👍'),
        ],
        
         [
            KeyboardButton(text='Coffe 3v1👍',callback_data='Coffe 3v1👍'),
            KeyboardButton(text='Latte👍',callback_data='Latte👍'),
        ],
        
        [
            KeyboardButton(text='Ortga',callback_data='back_18'),
        ],
        

    ],
    resize_keyboard=True
)

Koffe_Choylar_menu_3= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='Kok choy👍',callback_data='Kok choy👍'),
            KeyboardButton(text='Qora choy👍',callback_data='Qora choy👍'),
        ],
        
         [
            KeyboardButton(text='Limon choy👍',callback_data='Limon choy👍'),
        ],
        
        [
            KeyboardButton(text='Ortga',callback_data='back_19'),
        ],
        

    ],
    resize_keyboard=True
)

Koffe_Choylar_menu_4= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='Fanta👍',callback_data='Fanta👍'),
            KeyboardButton(text='Sprite👍',callback_data='Sprite👍'),
        ],
        
         [
            KeyboardButton(text='Coca Cola👍',callback_data='Coca Cola👍'),
            KeyboardButton(text='Nestle👍',callback_data='Nestle👍'),
        ],
        
        [
            KeyboardButton(text='Ortga',callback_data='back_20'),
        ],
        

    ],
    resize_keyboard=True
)



Koffe_Choylar_menu_5= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='Sok Bliss👍',callback_data='Sok Bliss👍'),
            KeyboardButton(text='Olma va Sabzilik👍',callback_data='Olma va Sabzilik👍'),
        ],
        
         [
            KeyboardButton(text='Olchalik sok👍',callback_data='Olchalik sok👍'),
        ],
        
        [
            KeyboardButton(text='Ortga',callback_data='back_21'),
        ],
        

    ],
    resize_keyboard=True
)





Desertlar_menu= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='Aassalim👍',callback_data='Aassalim👍'),
            KeyboardButton(text='Klubnika👍',callback_data='Klubnika👍'),
        ],
        
         [
            KeyboardButton(text='Choko👍',callback_data='Choko👍'),
        ],
        
        [
            KeyboardButton(text='Ortga',callback_data='back_22'),
        ],
        

    ],
    resize_keyboard=True
)





Desertlar_numbers =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='1️⃣',callback_data='1️⃣'),
            KeyboardButton(text='2️⃣',callback_data='2'),
            KeyboardButton(text='3️⃣',callback_data='3'),
        ],
        
        [
            KeyboardButton(text='4️⃣',callback_data='1'),
            KeyboardButton(text='5️⃣',callback_data='2'),
            KeyboardButton(text='6️⃣',callback_data='3'),
        ],
        
        [
            KeyboardButton(text='7️⃣',callback_data='1'),
            KeyboardButton(text='8️⃣',callback_data='2'),
            KeyboardButton(text='9️⃣',callback_data='3'),
        ],
        [
            KeyboardButton(text='Ortga',callback_data='back_23'),
        ],
        

    ],
    resize_keyboard=True
)



Pizza_menu= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='Peperoni👍',callback_data='Peperoni👍'),
            KeyboardButton(text='Ananaslik👍',callback_data='Ananaslik👍'),
        ],
        
         [
            KeyboardButton(text='Margaritta👍',callback_data='Margaritta👍'),
        ],
        
        [
            KeyboardButton(text='Ortga',callback_data='back_24'),
        ],
        

    ],
    resize_keyboard=True
)






Pizza_numbers =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text='1️⃣',callback_data='1️⃣'),
            KeyboardButton(text='2️⃣',callback_data='2'),
            KeyboardButton(text='3️⃣',callback_data='3'),
        ],
        
        [
            KeyboardButton(text='4️⃣',callback_data='1'),
            KeyboardButton(text='5️⃣',callback_data='2'),
            KeyboardButton(text='6️⃣',callback_data='3'),
        ],
        
        [
            KeyboardButton(text='7️⃣',callback_data='1'),
            KeyboardButton(text='8️⃣',callback_data='2'),
            KeyboardButton(text='9️⃣',callback_data='3'),
        ],
        [
            KeyboardButton(text='Ortga',callback_data='back_25'),
        ],
        

    ],
    resize_keyboard=True
)
import logging

from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from button import *

API_TOKEN = '6202655233:AAH3AjnumeZwiVJlwCW1mmh4gOe_99QZvo4'


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("Tillardan birini tanlang!",reply_markup=lang)

@dp.message_handler(text="🇺🇿 Ozbekcha")
async def echo(message: types.Message):
    await message.answer("Kategoriyalarni birini tanlang",reply_markup=menu)
    

@dp.message_handler(text="🇷🇺 Russcha")
async def echo(message: types.Message):
    await message.answer("Faqat Ozbelcha til mavjud")
    

@dp.message_handler(text="Buyurtma berish")
async def echo(message: types.Message):
    await message.answer("Marxmat menu tanlang,",reply_markup=yuqori_menu)
    
# for inline keyboard 

@dp.callback_query_handler(text='Lavash🌯🌯')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/lavash_2.jpeg','rb')
    await call.message.answer_photo( 
            photo=photo,
            caption="""
            Marxamat Lavashlar menusi!!!
            """,reply_markup=lavash_menu)
    


    
    
#++++++++++++++++++++++++++++++++++++++++





@dp.callback_query_handler(text='back_2')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Kategoriyalarni birini tanlang",reply_markup=mol_g_mini)
    

@dp.callback_query_handler(text='back_1')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxamat Lavashlar menusi!!!",reply_markup=yuqori_menu)
    

@dp.callback_query_handler(text='back_')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=lavash_menu)


@dp.callback_query_handler(text='1back_')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=mol_g_mini)
    

@dp.callback_query_handler(text='2back_')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=lavash_menu_qalampir_gushtli)
    

@dp.callback_query_handler(text='3back_')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=lavash_menu_tovuq_gushtli)
    
@dp.callback_query_handler(text='4back_')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=lavash_menu_qalampir_tovuq_gushtli)
    
    
@dp.callback_query_handler(text='5back_')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=lavash_menu_pishloq_tovuq_gushtli)
    
@dp.callback_query_handler(text='6back_')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=lavash_menu_pishloq_mol_gushtli)  
    




#++++++++++++++++++++++++++++++++++++++++


@dp.callback_query_handler(text='Mol gushtli🥩')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxamat Lavashlar menusi!!!",reply_markup=mol_g_mini)
    

    
@dp.callback_query_handler(text='Mini 👍    ')
async def button_lavash(call: types.CallbackQuery):
        photo = open('images/lavash_1.jpeg','rb')
        await call.message.answer_photo(
            photo=photo,
            caption="""
        Narxi:18000 ming so'm 
    Tarkibi:Xamir,go'sht,chips,pomidor,bodring,sous,moyonez
    Miqdorini tanlang                
                                """,reply_markup=mol_g_numbers)
        
@dp.callback_query_handler(text='Big 👍    ')
async def button_lavash(call: types.CallbackQuery):
        photo = open('images/lavash_1.jpeg','rb')
        await call.message.answer_photo(
            
          photo=photo,
            caption="""
        Narxi:20000 ming so'm 
    Tarkibi:Xamir,go'sht,chips,pomidor,bodring,sous,moyonez
    Miqdorini tanlang                
                                """,reply_markup=mol_g_numbers)

@dp.callback_query_handler(text='Qalampirli🌶')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer( "Marxamat Lavashlar menusi!!!",reply_markup=lavash_menu_qalampir_gushtli)
    
@dp.callback_query_handler(text='Mini👍')
async def button_lavash(call: types.CallbackQuery):
        photo = open('images/lavash_3.jpeg','rb')
        await call.message.answer_photo(
            photo=photo,
            caption="""
        Narxi:18000 ming so'm 
    Tarkibi:Xamir,go'sht,chips,pomidor,bodring,sous,moyonez
    Miqdorini tanlang                
                                """,reply_markup=qalampir_g_numbers)
        
@dp.callback_query_handler(text='Big👍')
async def button_lavash(call: types.CallbackQuery):
        photo = open('images/lavash_3.jpeg','rb')
        await call.message.answer_photo(
            photo=photo,
            caption="""
   Narxi:20000 ming so'm 
Tarkibi:Xamir,go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang                
                                """,reply_markup=qalampir_g_numbers)
        
        
        
@dp.callback_query_handler(text='Tovuq goshtli🍗')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer(
        "Marxamat Lavashlar menusi!!!",reply_markup=lavash_menu_tovuq_gushtli)
    
    
@dp.callback_query_handler(text='Mini 👍')
async def button_lavash(call: types.CallbackQuery):
        photo = open('images/lavash_4.jpeg','rb')
        await call.message.answer_photo(
            photo=photo,
            caption="""
        Narxi:18000 ming so'm 
    Tarkibi:Xamir,go'sht,chips,pomidor,bodring,sous,moyonez
    Miqdorini tanlang                
                                """,reply_markup=tovuq_g_numbers)
        
@dp.callback_query_handler(text='Big 👍')
async def button_lavash(call: types.CallbackQuery):
        photo = open('images/lavash_4.jpeg','rb')
        await call.message.answer_photo(
            photo=photo,
            caption="""
        Narxi:20000 ming so'm 
    Tarkibi:Xamir,go'sht,chips,pomidor,bodring,sous,moyonez
    Miqdorini tanlang                
                                """,reply_markup=tovuq_g_numbers)
    
    
@dp.callback_query_handler(text='Qalampirli tovuq goshtli🍗🌶')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxamat Lavashlar menusi!!!",reply_markup=lavash_menu_qalampir_tovuq_gushtli)
    
@dp.callback_query_handler(text='Mini 👍 ')
async def button_lavash(call: types.CallbackQuery):
        photo = open('images/lavash_5.jpeg','rb')
        await call.message.answer_photo(
            photo=photo,
            caption="""
        Narxi:18000 ming so'm 
    Tarkibi:Xamir,go'sht,chips,pomidor,bodring,sous,moyonez
    Miqdorini tanlang                
                                """,reply_markup=tovuq_qalampir_g_numbers)
        
@dp.callback_query_handler(text='Big 👍 ' )
async def button_lavash(call: types.CallbackQuery):
        photo = open('images/lavash_5.jpeg','rb')
        await call.message.answer_photo(
            photo=photo,
            caption="""
        Narxi:20000 ming so'm 
    Tarkibi:Xamir,go'sht,chips,pomidor,bodring,sous,moyonez
    Miqdorini tanlang                
                                """,reply_markup=tovuq_qalampir_g_numbers)
    
    
    
@dp.callback_query_handler(text='Pishloqli Tovuq goshtli🧀🍗')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxamat Lavashlar menusi!!!",reply_markup=lavash_menu_pishloq_tovuq_gushtli)
    
@dp.callback_query_handler(text='Mini 👍  ')
async def button_lavash(call: types.CallbackQuery):
        photo = open('images/lavash_6.jpeg','rb')
        await call.message.answer_photo(
            photo=photo,
            caption="""
        Narxi:18000 ming so'm 
    Tarkibi:Xamir,go'sht,chips,pomidor,bodring,sous,moyonez
    Miqdorini tanlang                
                                """,reply_markup=tovuq_pishloq_g_numbers)
    
@dp.callback_query_handler(text='Big 👍  ')
async def button_lavash(call: types.CallbackQuery):
        photo = open('images/lavash_6.jpeg','rb')
        await call.message.answer_photo(
            photo=photo,
            caption="""
        Narxi:20000 ming so'm 
    Tarkibi:Xamir,go'sht,chips,pomidor,bodring,sous,moyonez
    Miqdorini tanlang                
                                """,reply_markup=tovuq_pishloq_g_numbers)
    
@dp.callback_query_handler(text='Pishloqli mol goshtli🥩🧀')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxamat Lavashlar menusi!!!",reply_markup=lavash_menu_pishloq_mol_gushtli)

@dp.callback_query_handler(text='Mini 👍   ')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/lavash_7.jpeg','rb')
    await call.message.answer_photo(
        photo=photo,
        caption="""
    Narxi:18000 ming so'm 
Tarkibi:Xamir,go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang                
                              """,reply_markup=mol_pishloq_g_numbers)
    
@dp.callback_query_handler(text='Big 👍   ')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/lavash_7.jpeg','rb')
    await call.message.answer_photo(
        photo=photo,
        caption="""
 Narxi:20000 ming so'm 
Tarkibi:Xamir,go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang              
                              """,reply_markup=mol_pishloq_g_numbers)
    
    
    
#################          HOT-DOG        ################



@dp.callback_query_handler(text='back__2')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=yuqori_menu)
    

@dp.callback_query_handler(text='back_3')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=Hotdog_menu)
    
    

@dp.callback_query_handler(text='Hot-dog🌭🌭')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/hot_dog_5.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="Marxamat Hot-dog menusi!!!",reply_markup=Hotdog_menu)
    
@dp.callback_query_handler(text='Hot Dog obichniy👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/hot_dog_1.jpeg','rb')
    await call.message.answer_photo( photo=photo,
        caption="""
   Narxi:18000 ming so'm 
Tarkibi:✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang               
                              """,reply_markup=hotdog_numbers)
    
    

@dp.callback_query_handler(text='Classik Hot Dog👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/hot_dog_3.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption=
        """
   Narxi:8000 ming so'm 
Tarkibi:✅Kulcha,sosiska,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang              
                              """,reply_markup=hotdog_numbers)
    
@dp.callback_query_handler(text='Korolevskiy👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/hot_dog_2.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
   Narxi:15000 ming so'm 
Tarkibi:✅Kulcha,sosiska,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang              
                              """,reply_markup=hotdog_numbers)

@dp.callback_query_handler(text='Tovuqli Hot Dog👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/hot_dog_4.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
   Narxi:17000 ming so'm 
Tarkibi:✅Kulcha,sosiska,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang             
                              """,reply_markup=hotdog_numbers)
    
    
    
    
    
############        Sendvich             ############
    

@dp.callback_query_handler(text='Sendvich club 🥪🥪')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/clab_2.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="Marxamat Sendvich club menusi!!!",reply_markup=Sendwich_menu)
    
@dp.callback_query_handler(text='lassik Club Sendwich👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/clab_1.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
  Narxi:22000 ming so'm 
Tarkibi:✅Kulcha, tovuq go'shti, pomidor, sous,  piyoz.
Miqdorini tanlang            
                              """,reply_markup=sendvich_numbers)
    
@dp.callback_query_handler(text='Tovuqli Club Sendwich👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/clab_1.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
 Narxi:22000 ming so'm 
Tarkibi:✅Kulcha, tovuq go'shti, pomidor, sous,  piyoz.
Miqdorini tanlang         
                              """,reply_markup=sendvich_numbers)
    
    
@dp.callback_query_handler(text='back_4')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=yuqori_menu)
    
    
@dp.callback_query_handler(text='back_5')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=Sendwich_menu)
    
    
################                Shourma         ###############
    

@dp.callback_query_handler(text='Shourma 🌮🌮')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/shourma_1.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="Marxamat Shourma  menusi!!!",reply_markup=Shaurma_menu)
    
@dp.callback_query_handler(text='Mol Goshtli Shaurma👍')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("""
    ✅Kategoriyalardan birini tanlang!!               
                              """,reply_markup=Shaurma_menu_1)

@dp.callback_query_handler(text='Mini   👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/shourma_2.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
    Narxi:18000 ming so'm
Kulcha, go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang              
                              """,reply_markup=Shourma_numbers)

@dp.callback_query_handler(text='Big   👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/shourma_2.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
  Narxi:20000 ming so'm
Kulcha, go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang              
                              """,reply_markup=Shourma_numbers)

@dp.callback_query_handler(text='Tovuq Shaurma👍')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("""
    ✅Kategoriyalardan birini tanlang!!               
                              """,reply_markup=Shaurma_menu_2)
    
@dp.callback_query_handler(text=' Mini   👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/shourma_3.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
    Narxi:17000 ming so'm
Kulcha,tovuq go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang              
                              """,reply_markup=Shourma_numbers1)

@dp.callback_query_handler(text=' Big   👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/shourma_3.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
  Narxi:20000 ming so'm
Kulcha,tovuq go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang              
                              """,reply_markup=Shourma_numbers1)
    

@dp.callback_query_handler(text='Tovuq Goshtli+Qalampirli Shaurma👍')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("""
    ✅Kategoriyalardan birini tanlang!!               
                              """,reply_markup=Shaurma_menu_3)
    
@dp.callback_query_handler(text=' Mini   👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/shourma_2.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
    Narxi:17000 ming so'm
Kulcha,tovuq go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang              
                              """,reply_markup=Shourma_numbers2)

@dp.callback_query_handler(text=' Big   👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/shourma_2.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
  Narxi:20000 ming so'm
Kulcha,tovuq go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang              
                              """,reply_markup=Shourma_numbers2)

@dp.callback_query_handler(text='Mol Goshtli+Qalampirli Shaurma👍')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("""
    ✅Kategoriyalardan birini tanlang!!               
                              """,reply_markup=Shaurma_menu_4)
    
   
@dp.callback_query_handler(text=' Mini   👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/shourma_3.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
    Narxi:17000 ming so'm
Kulcha,tovuq go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang              
                              """,reply_markup=Shourma_numbers3)

@dp.callback_query_handler(text=' Big   👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/shourma_3.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
  Narxi:20000 ming so'm
Kulcha,tovuq go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang              
                              """,reply_markup=Shourma_numbers3)


    
    

@dp.callback_query_handler(text='back_6')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=yuqori_menu)
    
    

@dp.callback_query_handler(text='back_8')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=Shaurma_menu)
    

@dp.callback_query_handler(text='back_7')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=Shaurma_menu_1)
    

@dp.callback_query_handler(text='7back_7')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=Shaurma_menu_2)
    

@dp.callback_query_handler(text='8back_7')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=Shaurma_menu_3)
    
    
@dp.callback_query_handler(text='9back_7')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=Shaurma_menu_4)

    
    
################                Burger         ###############


@dp.callback_query_handler(text='Burger 🍔🍔')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxamat Burger  menusi!!!",reply_markup=Burger_menu)

@dp.callback_query_handler(text='Gamburger👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/burger_1.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
Narxi:22000 ming so'm 
Miqdorini tanlang             
                              """,reply_markup=Burger_numbers)
    

@dp.callback_query_handler(text='Chizburger👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/burger_2.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
Narxi:20000 ming so'm 
Miqdorini tanlang            
                              """,reply_markup=Burger_numbers)
    
    
@dp.callback_query_handler(text='back_9')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=yuqori_menu)
    
    
@dp.callback_query_handler(text='back_10')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=Burger_menu)
    
    
################                Donar         ###############

    
@dp.callback_query_handler(text='Donar 🍱🍱')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxamat donar  menusi!!!",reply_markup=Donar_menu)
   
@dp.callback_query_handler(text='Tovuqli👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/donar_1.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
Narxi:23000 ming so'm 
Tarkib: Kulcha, tovuq go'sht, pomidor, sous, piyoz.     
Miqdorini tanlang...          
                              """,reply_markup=Donar_numbers) 
    
@dp.callback_query_handler(text='Goshtlik👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/donar_2.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
Narxi:23000 ming so'm 
Tarkib: Kulcha, mol go'sht, pomidor, sous,  piyoz.    
Miqdorini tanlang...
         
                              """,reply_markup=Donar_numbers) 
    
    
@dp.callback_query_handler(text='back_11')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=yuqori_menu)
    
    
@dp.callback_query_handler(text='back_12')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=Donar_menu)
    
    
    
    
################                Gazaklar         ###############


    
@dp.callback_query_handler(text='Gazaklar 🍟🍟')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxamat Gazaklar  menusi!!!",reply_markup=Gazaklar_menu)
    
    
@dp.callback_query_handler(text='15 gram Fri👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/gazak_1.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
Narxi:6000 ming so'm 
Tarkib: kartoshka, sous....   
Miqdorini tanlang         
                              """,reply_markup=Gazaklar_numbers) 
    
    
@dp.callback_query_handler(text='Kartoshkali+sousli Fri👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/gazak_1.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
Narxi: 10 000 ming so'm
Tarkib: kartoshka, sous...      
Miqdorini tanlang...        
                              """,reply_markup=Gazaklar_numbers)
    
@dp.callback_query_handler(text='Gruch katta👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/gazak_2.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
Narxi: 8 000 ming so'm
Tarkib: gurunch, salat bargi, sous...     
Miqdorini tanlang...                          

                              """,reply_markup=Gazaklar_numbers) 
    
@dp.callback_query_handler(text='Gruch kichik katta👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/gazak_2.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
Narxi: 10 000 ming so'm
Tarkib: gurunch, salat bargi, sous...     
Miqdorini tanlang...
                              """,reply_markup=Gazaklar_numbers) 
    

    
@dp.callback_query_handler(text='back_13')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=yuqori_menu)
    


    
@dp.callback_query_handler(text='back_14')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=Gazaklar_menu)
    
    
    
    
################                Ichimlikar          ###############
    
    
@dp.callback_query_handler(text='Ichimlikar 🍹🍹')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxamat Ichimlikar  menusi!!!",reply_markup=Ichimliklar_menu)
    
@dp.callback_query_handler(text='Choy va koffe👍')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("""
Kategoriyalardan birini tanlang!!!
                              """,reply_markup=Koffe_Choylar_menu_1) 

@dp.callback_query_handler(text='Kofellar👍')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("""
Kategoriyalardan birini tanlang!!!
                              """,reply_markup=Koffe_Choylar_menu_2) 

@dp.callback_query_handler(text='Americano👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/ichimlik_1.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
✅Ameicani narxi 12 000!!!!!!
                              """,reply_markup=Ichimliklar_numbers) 
    
@dp.callback_query_handler(text='Cappuccino👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/ichimlik_2.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
✅Coppuccino Narxi 18 000!!!!!!
                              """,reply_markup=Ichimliklar_numbers) 
    
    
@dp.callback_query_handler(text='Coffe 3v1👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/ichimlik_3.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption=""" 
✅Kofe 3 v 1☕️ 3 000 ming so'm!!!!
                              """,reply_markup=Ichimliklar_numbers) 
    
@dp.callback_query_handler(text='Latte👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/ichimlik_4.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
✅Latte big 120g☕️ 15 000 mig so'm!!!!
                              """,reply_markup=Ichimliklar_numbers) 


@dp.callback_query_handler(text='Choylar👍')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("""
✅Kategoriyalardan birini tanlang!!!
                              """,reply_markup=Koffe_Choylar_menu_3) 
    

@dp.callback_query_handler(text='Kok choy👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/ichimlik_5.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
✅ Ko'k  choy 3 000mig so'm!!!
                              """,reply_markup=IIchimliklar_numbers) 
    
    

@dp.callback_query_handler(text='Qora choy👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/ichimlik_5.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
✅ Qora  choy 3 000mig so'm!!!
                              """,reply_markup=IIchimliklar_numbers) 
    
    

@dp.callback_query_handler(text='Limon choy👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/ichimlik_6.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
✅Limon choy 5 000mig so'm!!
                              """,reply_markup=IIchimliklar_numbers) 
    

@dp.callback_query_handler(text='Yaxna Ichimliklar👍')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("""
✅Kategoriyalardan birini tanlang!!!
                              """,reply_markup=Koffe_Choylar_menu_4) 
    
    

@dp.callback_query_handler(text='Fanta👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/ichimlik_7.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
13 000 narxi
                              """,reply_markup=IIIchimliklar_numbers) 
    

@dp.callback_query_handler(text='Sprite👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/ichimlik_8.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
12 000 narxi
                              """,reply_markup=IIIchimliklar_numbers) 


@dp.callback_query_handler(text='Coca Cola👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/ichimlik_9.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
13 000 narxi
                              """,reply_markup=IIIchimliklar_numbers) 
    
@dp.callback_query_handler(text='Nestle👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/ichimlik_10.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
4 000 narxi
                              """,reply_markup=IIIchimliklar_numbers) 
    
    
    
@dp.callback_query_handler(text='Fresh va tabbiy soklar👍')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("""
✅Kategoriyalardan birini tanlang!!!
                              """,reply_markup=Koffe_Choylar_menu_5)  
    
    

@dp.callback_query_handler(text='Sok Bliss👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/ichimlik_11.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
10 000 narxi
                              """,reply_markup=IIIIchimliklar_numbers) 
    

    

@dp.callback_query_handler(text='Olma va Sabzilik👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/ichimlik_12.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
Fresh sabzi + olma
13 000 narxi
                              """,reply_markup=IIIIchimliklar_numbers) 
    
    

@dp.callback_query_handler(text='Olchalik sok👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/ichimlik_13.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
10 000 narxi
                              """,reply_markup=IIIIchimliklar_numbers) 
    


    
@dp.callback_query_handler(text='back_15')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=yuqori_menu)
    

    
@dp.callback_query_handler(text='back_17')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=Ichimliklar_menu)
    

    
@dp.callback_query_handler(text='back_18')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=Koffe_Choylar_menu_1)
    
    
@dp.callback_query_handler(text='back_16')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=Koffe_Choylar_menu_2)
    


@dp.callback_query_handler(text='back_19')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=Koffe_Choylar_menu_1)
    

@dp.callback_query_handler(text='back__16')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=Koffe_Choylar_menu_3)
    

@dp.callback_query_handler(text='back___16')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=Koffe_Choylar_menu_4)
    

@dp.callback_query_handler(text='back_20')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=Ichimliklar_menu)
    
    

@dp.callback_query_handler(text='back_21')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=Ichimliklar_menu)
    
    
@dp.callback_query_handler(text='back____16')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=Koffe_Choylar_menu_5)
    


    


################                Desertlar          ###############


    
    
@dp.callback_query_handler(text='Desertlar 🍰🍰')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxamat Desertlar  menusi!!!",reply_markup=Desertlar_menu)
    
    
@dp.callback_query_handler(text='Aassalim👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/desert_1.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
Narxi:14 000 ming so'm 
✅Аnʼnaviy taʼm - asal asosidagi biskvit va krem
Miqdorini tanlang
                              """,reply_markup=Desertlar_numbers) 
    
    
@dp.callback_query_handler(text='Klubnika👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/desert_2.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
Narxi:15 000 ming so'm 
✅Qulupnayli Muss.
Miqdorini tanlang
                              """,reply_markup=Desertlar_numbers) 
    
    
    
@dp.callback_query_handler(text='Choko👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/desert_3.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
Narxi:17 000 ming so'm 
✅Аnʼnaviy taʼm - shokolat asosidagi biskvit va krem.
Miqdorini tanlang
                              """,reply_markup=Desertlar_numbers) 
    

    
@dp.callback_query_handler(text='back_22')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=yuqori_menu)
    

    
@dp.callback_query_handler(text='back_23')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=Desertlar_menu)
    
    
    
    
    
################                Pizza           ###############


    
@dp.callback_query_handler(text='Pizza 🍕🍕')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxamat Pizza  menusi!!!",reply_markup=Pizza_menu)
    
        
@dp.callback_query_handler(text='Peperoni👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/pizza_2.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
Narxi:65 000 ming so'm 
✅Пицца Пепперони
Пицца Пепперони     33см.
Соус Томатный Для Пиццы
Тонкое тесто.
Сыр 110 гр.
Miqdorini tanlang
                              """,reply_markup=Pizza_numbers) 
    
@dp.callback_query_handler(text='Ananaslik👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/pizza_1.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
Narxi:75 000 ming so'm 
✅Пицца с Ананасом.
Пицца с Колбасой     33см.
Соус Томатный Для Пиццы
3 вида колбас 130гр.
Тонкое тесто
Кукуруза
Сыр 100гр.
ГрибыMiqdorini tanlang
                              """,reply_markup=Pizza_numbers) 
    

    
@dp.callback_query_handler(text='Margaritta👍')
async def button_lavash(call: types.CallbackQuery):
    photo = open('images/pizza_3.jpeg','rb')
    await call.message.answer_photo(photo=photo,
        caption="""
Narxi:60 000 ming so'm 
✅Пицца Маргарита
Пицца Маргарита  33см.
Соус Томатный Для Пиццы 
Тонкое тесто 
Сыр 100гр.
Помидоры
Miqdorini tanlang
                              """,reply_markup=Pizza_numbers) 
    


    
@dp.callback_query_handler(text='back_24')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=yuqori_menu)
    

    


    
@dp.callback_query_handler(text='back_25')
async def button_lavash(call: types.CallbackQuery):
    await call.message.answer("Marxmat menu tanlang,",reply_markup=Pizza_menu)
    



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
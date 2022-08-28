from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    ChatPermissions,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    ReplyKeyboardMarkup,
)
from pyrogram.types import InputMediaPhoto
from pyrogram.errors import FloodWait
from dbs import(
    delete_filter,
    get_filter,
    get_filters_names,
    save_filter,
    choosing_lvl,
    choosing_lvl_trade,
    get_filters_count,
)
from pyrogram.types import InputMediaPhoto
import random
import rand as r
from wcap import *
from ids import *
from nums import *
api_id = 18983092
api_hash = 'a6005a70e88369b4fb08b8350ebbdd35'
bot_token = '5442587068:AAESQu7bb40ZFf2xWQV4QmbUkPmBUiwgRPs'

# We have to manually call "start" if we want an explicit bot token
app = Client("ark", bot_token=bot_token, api_id=api_id, api_hash=api_hash) 


@app.on_message(filters.command("harem"))
async def waifu_harem(client, message: Message):
    usrna = message.from_user.first_name
    c = message.chat.id
    userid = message.from_user.id
    btn = []
    bt = []
    btt =[]
    haremc = await get_filters_count(userid)
    waifucount = haremc["filters_count"]
    try:
        async for photo in app.get_chat_photos(userid,limit=1):
            imgid = photo.file_id
    except:
        img = "https://wallpaperfordesktop.com/wp-content/uploads/2022/03/Arknights-Wallpaper.jpg"
    filters = await get_filters_names(userid)
    harem = ""
    no = 1
    for x in filters:
        harem+= f"`{no}.` **{x}**\n"
        no +=1
        #btnthing = f"{x}"
        #num = no
        #waifu,idr = btnthing.split(":")
        #harem+= f"`{no}.`**{x}**\n"
        #harem = harem.replace("1x",'').replace("ID",'').replace("2x",'').replace("3x",'').replace("4x",'').replace("5x",'').replace("6x",'').replace("7x",'').replace("8x",'').replace("9x",'').replace("10x",'')
    if harem == "":
        await message.reply("You didnt hunt any waifu")
        return
    txt = f"""
Harem Of **{usrna}**

{harem}

"""
    btn = [[InlineKeyboardButton(text=f"Harem",callback_data=f"arknights_{userid}_{usrna}_1")]]
    #await app.send_photo(c,photo = imgid,caption=txt,reply_markup=InlineKeyboardMarkup(btn))
    await app.send_photo(c,photo = imgid,caption=txt)
                
                
@app.on_message(filters.command("trade")&filters.group)
async def waifu_trade(client, message: Message):
    search_str = message.text.split(" ")
    if len(search_str) == 1:
        await message.reply("Provide a IDs!")
        return
    try:
        one = search_str[1]
    except:
        await message.reply("Provide a ID! of a waifu that you wanna give")
        return
    try:
        two = search_str[2]
    except:
        await message.reply("Provide a ID! of a waifu that you wanna get")
        return
    c = message.chat.id
    usrna = message.from_user.first_name
    userid = message.from_user.id
    repfr = message.reply_to_message.from_user.id
    repfrn = message.reply_to_message.from_user.first_name
    _filtersone = await get_filters_names(userid)
    _filterstwo = await get_filters_names(repfr)
    numb = one
    idw = id_fetch(numb)
    cap = capt(idw)
    idm = id_choose(idw)
    no1 = f"1x {cap} ID: {idm}"
    no2 = f"2x {cap} ID: {idm}"
    no3 = f"3x {cap} ID: {idm}"
    no4 = f"4x {cap} ID: {idm}"
    no5 = f"5x {cap} ID: {idm}"
    no6 = f"6x {cap} ID: {idm}"
    no7 = f"7x {cap} ID: {idm}"
    no8 = f"8x {cap} ID: {idm}"
    no9 = f"9x {cap} ID: {idm}"
    no10 = f"10x {cap} ID: {idm}"
    
    if no1 in _filtersone:
        print("")
    elif no2 in _filtersone:
        print("")
    elif no3 in _filtersone:
        print("")
    elif no4 in _filtersone:
        print("")
    elif no5 in _filtersone:
        print("")
    elif no6 in _filtersone:
        print("")
    elif no7 in _filtersone:
        print("")
    elif no8 in _filtersone:
        print("")
    elif no9 in _filtersone:
        print("")
    elif no10 in _filtersone:
        print("")
    else:
        await message.reply(f"{usrna} aint got her")
        return

    numb = two
    idw = id_fetch(numb)
    cap = capt(idw)
    idm = id_choose(idw)
    ono1 = f"1x {cap} ID: {idm}"
    ono2 = f"2x {cap} ID: {idm}"
    ono3 = f"3x {cap} ID: {idm}"
    ono4 = f"4x {cap} ID: {idm}"
    ono5 = f"5x {cap} ID: {idm}"
    ono6 = f"6x {cap} ID: {idm}"
    ono7 = f"7x {cap} ID: {idm}"
    ono8 = f"8x {cap} ID: {idm}"
    ono9 = f"9x {cap} ID: {idm}"
    ono10 = f"10x {cap} ID: {idm}"
    
    if ono1 in _filterstwo:
        print("")
    elif ono2 in _filterstwo:
        print("")
    elif ono3 in _filterstwo:
        print("")
    elif ono4 in _filterstwo:
        print("")
    elif ono5 in _filterstwo:
        print("")
    elif ono6 in _filterstwo:
        print("")
    elif ono7 in _filterstwo:
        print("")
    elif ono8 in _filterstwo:
        print("")
    elif ono9 in _filterstwo:
        print("")
    elif ono10 in _filterstwo:
        print("")
    else:
        await message.reply(f"{repfrn} aint got her")
        return

    if no2 in _filtersone:
        name = no2
    elif no3 in _filtersone:
        name = no3
    elif no4 in _filtersone:
        name = no4
    elif no5 in _filtersone:
        name = no5
    elif no6 in _filtersone:
        name = no6
    elif no7 in _filtersone:
        name = no7
    elif no8 in _filtersone:
        name = no8
    elif no9 in _filtersone:
        name = no9
    elif no10 in _filtersone:
        name = no10
    else:
        name = no1

    if ono2 in _filterstwo:
        nameo = ono2
    elif ono3 in _filterstwo:
        name = ono3
    elif ono4 in _filterstwo:
        nameo = ono4
    elif ono5 in _filterstwo:
        nameo = ono5
    elif ono6 in _filterstwo:
        nameo = ono6
    elif ono7 in _filterstwo:
        nameo = ono7
    elif ono8 in _filterstwo:
        nameo = ono8
    elif ono9 in _filterstwo:
        nameo = ono9
    elif ono10 in _filterstwo:
        nameo = ono10
    else:
        nameo = ono1
    

    yesorno = [[InlineKeyboardButton(text=f"Yes",callback_data=f"yes_{userid}_{repfr}_{one}_{two}")],[InlineKeyboardButton(text=f"Cancel",callback_data=f"cancel_{repfr}")]]

    msg = f"""Are You Sure Want To Trade;
**{nameo}** With `{usrna}'s` **{name}**?
"""

    await message.reply_to_message.reply(msg,reply_markup=InlineKeyboardMarkup(yesorno))

count = {}
waif = {}
captc = {}
waifuid = {}
@app.on_message(filters.group)
async def start_gett(_,message:Message):
    c = message.chat.id
    user = message.from_user.id
    print("lol")
    try:
        num = int(count[c])
        numb = num
        num +=1
        count[c]= f'{num}'
        if numb >= 100:
            if numb == 100:
                randcho =  random.choice(r.waifu)
                print(randcho)
                cap = capt(randcho)
                print(cap)
                captc[c] = cap
                wfname = cap.lower()
                waif[c] = wfname
                print(wfname)
                waid = id_choose(randcho)
                waifuid[c] = waid
                await app.send_photo(c,randcho,caption="A cute waifu is here use /hunt __name__ to collect her!")
            try:
                msg = message.text
                mess = msg.lower()
                waifun = waif[c]
                waifun,nothingatall = waifun.split("[")
                print(waifun)
                waifun= waifun.replace(" ","")
                cap = captc[c]
                waid = waifuid[c]
                if "/hunt" and waifun in mess:
                    await choosing_lvl(user,cap,waid)
                    await message.reply(f"You Got **{cap}** From Arknights")
                    waif[c] = "None"
                    captc[c] = "None"
                    waifuid[c] = "None"
                    count[c]= '0'
                    return
                elif "/hunt" in mess:
                    if not waifun in mess:
                        await message.reply("Nice try but its wrong...")
                else:
                    pass        
            except:
                pass
        if numb == 120:
            cap = captc[c]
            await app.send_message(c,f"waifu ran her name is **{cap}**")
            count[c]= f'0'
            return    
        #count[c]= f'{num}'
    except:
        num = "1"
        count[c]= num
        


@app.on_callback_query()
async def cb_handler(_, cq: CallbackQuery):
    if cq.data.startswith("yes"):
        ident,frid_id,repfr,one,two=cq.data.split("_")
        frid = int(frid_id)
        repfrr = repfr
        repfr = int(repfr)
        cqid = cq.id
        from_user = cq.from_user.id
        print(from_user)
        print(repfr)
        if from_user==repfr:
            _filtersone = await get_filters_names(frid)
            _filterstwo = await get_filters_names(repfr)
            numb = one
            idw = id_fetch(numb)
            cap = capt(idw)
            idm = id_choose(idw)
            no1 = f"1x {cap} ID: {idm}"
            no2 = f"2x {cap} ID: {idm}"
            no3 = f"3x {cap} ID: {idm}"
            no4 = f"4x {cap} ID: {idm}"
            no5 = f"5x {cap} ID: {idm}"
            no6 = f"6x {cap} ID: {idm}"
            no7 = f"7x {cap} ID: {idm}"
            no8 = f"8x {cap} ID: {idm}"
            no9 = f"9x {cap} ID: {idm}"
            no10 = f"10x {cap} ID: {idm}"
            chat_id = frid
            if no2 in _filtersone:
                name = no2
                await delete_filter(chat_id,name)
                cap = no1
                await choosing_lvl_trade(chat_id,cap)
            elif no3 in _filtersone:
                name = no3
                await delete_filter(chat_id,name)
                cap = no2
                await choosing_lvl_trade(chat_id,cap)
            elif no4 in _filtersone:
                name = no4
                await delete_filter(chat_id,name)
                cap = no3
                await choosing_lvl_trade(chat_id,cap)
            elif no5 in _filtersone:
                name = no5
                await delete_filter(chat_id,name)
                cap = no4
                await choosing_lvl_trade(chat_id,cap)
            elif no6 in _filtersone:
                name = no6
                await delete_filter(chat_id,name)
                cap = no5
                await choosing_lvl_trade(chat_id,cap)
            elif no7 in _filtersone:
                name = no7
                await delete_filter(chat_id,name)
                cap = no6
                await choosing_lvl_trade(chat_id,cap)
            elif no8 in _filtersone:
                name = no8
                await delete_filter(chat_id,name)
                cap = no7
                await choosing_lvl_trade(chat_id,cap)
            elif no9 in _filtersone:
                name = no9
                await delete_filter(chat_id,name)
                cap = no8
                await choosing_lvl_trade(chat_id,cap)
            elif no10 in _filtersone:
                name = no10
                await delete_filter(chat_id,name)
                cap = no9
                await choosing_lvl_trade(chat_id,cap)
            else:
                name = no1
                await delete_filter(chat_id,name)   
            numb = two
            idw = id_fetch(numb)
            cap = capt(idw)
            idm = id_choose(idw)
            ono1 = f"1x {cap} ID: {idm}"
            ono2 = f"2x {cap} ID: {idm}"
            ono3 = f"3x {cap} ID: {idm}"
            ono4 = f"4x {cap} ID: {idm}"
            ono5 = f"5x {cap} ID: {idm}"
            ono6 = f"6x {cap} ID: {idm}"
            ono7 = f"7x {cap} ID: {idm}"
            ono8 = f"8x {cap} ID: {idm}"
            ono9 = f"9x {cap} ID: {idm}"
            ono10 = f"10x {cap} ID: {idm}"
            chat_id = repfr
            if ono2 in _filterstwo:
                name = ono2
                await delete_filter(chat_id,name)
                cap = ono1
                await choosing_lvl_trade(chat_id,cap)
            elif ono3 in _filterstwo:
                name = ono3
                await delete_filter(chat_id,name)
                cap = ono2
                await choosing_lvl_trade(chat_id,cap)
            elif ono4 in _filterstwo:
                name = ono4
                await delete_filter(chat_id,name)
                cap = ono3
                await choosing_lvl_trade(chat_id,cap)
            elif ono5 in _filterstwo:
                name = ono5
                await delete_filter(chat_id,name)
                cap = ono4
                await choosing_lvl_trade(chat_id,cap)
            elif ono6 in _filterstwo:
                name = ono6
                await delete_filter(chat_id,name)
                cap = ono5
                await choosing_lvl_trade(chat_id,cap)
            elif ono7 in _filterstwo:
                name = ono7
                await delete_filter(chat_id,name)
                cap = ono6
                await choosing_lvl_trade(chat_id,cap)
            elif ono8 in _filterstwo:
                name = ono8
                await delete_filter(chat_id,name)
                cap = ono7
                await choosing_lvl_trade(chat_id,cap)
            elif ono9 in _filterstwo:
                name = ono9
                await delete_filter(chat_id,name)
                cap = ono8
                await choosing_lvl_trade(chat_id,cap)
            elif ono10 in _filterstwo:
                name = ono10
                await delete_filter(chat_id,name)
                cap = ono9
                await choosing_lvl_trade(chat_id,cap)
            else:
                name = ono1
                await delete_filter(chat_id,name)
            chat_id = repfr
            idw = id_fetch(one)
            cap = capt(idw)
            idm = id_choose(idw)
            await choosing_lvl(chat_id,cap,idm)
            chat_id = frid
            idw = id_fetch(two)
            cap = capt(idw)
            idm = id_choose(idw)
            await choosing_lvl(chat_id,cap,idm)
            await cq.message.edit("Trade Successful~")
        else:
            cqid = cq.id
            await app.answer_callback_query(cqid,"Why Are You Answering MF?",show_alert=True)
            return

    if cq.data.startswith("cancel"):
        ident,repfr=cq.data.split("_")
        cqid = cq.id
        repfr = int(repfr)
        from_user = cq.from_user.id
        if repfr == from_user:
            await cq.message.edit("Trade Canceled")
            return
        else:
            cqid = cq.id
            await app.answer_callback_query(cqid,"Why Are You Answering MF?",show_alert=True)
            return
            
    if cq.data.startswith("wai"):
        ident,chatid,waifuid,userna=cq.data.split("_")
        idw = id_fetch(waifuid)
        cap = capt(idw)
        idm = id_choose(idw)
        back = [[InlineKeyboardButton(text=f"🔙",callback_data=f"back_{chatid}_{userna}")]]
        await cq.edit_message_media(InputMediaPhoto(idw,caption=cap),reply_markup=InlineKeyboardMarkup(back))
#---------------------------- temp back ---------------------------------------------------------------------------        
    if cq.data.startswith("back"):
        ident,chatid,usrna=cq.data.split("_")
        userid= int(chatid)
        filters = await get_filters_names(userid)
        harem = ""
        btn = []
        bt = []
        btt =[]
        no = 1
        for x in filters:
            #harem+= f"`{no}.` **{x}**\n"
            btnthing = f"{x}"
            num = no
            waifu,idr = btnthing.split(":")
            harem+= f"`{no}.`**{waifu}**\n"
            harem = harem.replace("1x",'').replace("ID",'').replace("2x",'').replace("3x",'').replace("4x",'').replace("5x",'').replace("6x",'').replace("7x",'').replace("8x",'').replace("9x",'').replace("10x",'')
            no +=1
            idr = idr.replace(" ","")
            if num <=8:
                btn.append(
                        InlineKeyboardButton(f"{num}", callback_data=f"wai_{userid}_{idr}_{usrna}"),
                        )
            elif 8< num <=16:
                bt.append(
                        InlineKeyboardButton(f"{num}", callback_data=f"wai_{userid}_{idr}_{usrna}"),
                        )
            elif 16< num <=24:
                btt.append(
                        InlineKeyboardButton(f"{num}", callback_data=f"wai_{userid}_{idr}_{usrna}"),
                        )
        txt = f"""
Harem Of `{usrna}`

{harem}
    """
        btn=[btn]
        bt = [bt]
        btt=[btt]
        try:
            async for photo in app.get_chat_photos(userid,limit=1):
                img = photo.file_id
        except:
            img = "https://wallpaperfordesktop.com/wp-content/uploads/2022/03/Arknights-Wallpaper.jpg"
        await cq.edit_message_media(InputMediaPhoto(img,caption=txt),reply_markup=InlineKeyboardMarkup(btn+bt+btt))

#----------------------------- arknights harem -----------------------------------------------------        
    if cq.data.startswith("arknights"):
        ident,chatid,usrna,index=cq.data.split("_")
        userid= int(chatid)
        fname = usrna
        index = int(index)
        filters = await get_filters_names(userid)
        harem = ""
        btn = []
        bt = []
        btt =[]
        no = 1
        for x in filters:
            #harem+= f"`{no}.` **{x}**\n"
            btnthing = f"{x}"
            num = no
            waifu,idr = btnthing.split(":")
            harem+= f"`{no}.`**{waifu}**\n"
            harem = harem.replace("1x",'').replace("ID",'').replace("2x",'').replace("3x",'').replace("4x",'').replace("5x",'').replace("6x",'').replace("7x",'').replace("8x",'').replace("9x",'').replace("10x",'')
            no +=1
            idr = idr.replace(" ","")
            if num <=8:
                btn.append(
                        InlineKeyboardButton(f"{num}", callback_data=f"wai_{userid}_{idr}_{usrna}"),
                        )
            elif 8< num <=16:
                bt.append(
                        InlineKeyboardButton(f"{num}", callback_data=f"wai_{userid}_{idr}_{usrna}"),
                        )
            elif 16< num <=24:
                btt.append(
                        InlineKeyboardButton(f"{num}", callback_data=f"wai_{userid}_{idr}_{usrna}"),
                        )
        txt = f"""
Harem Of `{usrna}`

{harem}
    """
        btn=[btn]
        bt = [bt]
        btt=[btt]
        img = "https://wallpaperfordesktop.com/wp-content/uploads/2022/03/Arknights-Wallpaper.jpg"
        await cq.edit_message_caption(txt,reply_markup=InlineKeyboardMarkup(btn+bt+btt))        
        
    
print("Bot Alive")
app.run()
print("Bot Ded")

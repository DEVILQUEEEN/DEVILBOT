# COPYRIGHT (C) 2021-22 BY LEGENDX22
import os
import asyncio
from telethon import events, functions
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.contacts import BlockRequest as block
import DEVILBOT.plugins.sql_helper.pmpermit_sql as DEVILBOT_X
from DEVILBOT import ALIVE_NAME, bot
from DEVILBOT.uniborgConfig import Config
from var import Var
from DEVILBOTX import NAME
DEVILBOT_USER = NAME
from DEVILBOT.utils import admin_cmd as ultra_cmd
DEVILBOT_WRN = {}
DEVILBOT_REVL_MSG = {}
DEVILBOT_PROTECTION = os.environ.get("PM_PROTECT","yes")
SPAM = os.environ.get("PM_WARN", None)
if SPAM is None:
    HMM_LOL = 3
else:
    HMM_LOL = SPAM
from ..import bot
from DEVILBOTX import xbot
FUCK_OFF_WARN = f"**Blocked You As You Spammed {DEVILBOT_USER}'s DM\n\n **IDC**"
async def LEGENDX(event, msg):
  global DEVILBOT_WRN
  if DEVILBOT_PROTECTION == "off" or DEVILBOT_PROTECTION is "off":
    return print("pmpermit is off new user is coming")
  if not event.sender_id in DEVILBOT_WRN:
    DEVILBOT_WRN.update({event.chat_id: 0})
  global bot
  global xbot
  omk = await xbot.get_me()
  username = omk.username
  LEGENDX = await bot.inline_query(username, msg)
  await LEGENDX[0].click(event.chat_id)
  DEVILBOT_WRN[event.chat_id] += 1
  if DEVILBOT_WRN[event.chat_id] == HMM_LOL:
    await event.reply("**Hᴇʏ ɴᴏᴏʙ ᴛʜɪs ɪs ʏᴏᴜʀ ʟᴀsᴛ ᴄʜᴀɴᴄᴇ, sᴘᴀᴍ = ʙʟᴏᴄᴋ**")
    await bot (block (event.chat_id))
    del DEVILBOT_WRN
  


DEVILBOT_STOP_EMOJI = (

    "😑"

)

if Var.PRIVATE_GROUP_ID is not None:

    @bot.on(events.NewMessage(outgoing=True))

    async def ultra_dm_niqq(event):

        if event.fwd_from:

            return

        chat = await event.get_chat()

        if event.is_private:

            if not DEVILBOT_X.is_approved(chat.id):

                if not chat.id in DEVILBOT_WRN:

                    DEVILBOT_X.approve(chat.id, "outgoing")

                    bruh = "Aᴜᴛᴏ Aᴘᴘʀᴏᴠᴇᴅ Bᴄᴜᴢ ᴏᴜᴛɢᴏɪɴɢ 😁😁"

                    rko = await borg.send_message(event.chat_id, bruh)

                    await asyncio.sleep(3)

                    await rko.delete ()  



    @borg.on(ultra_cmd(pattern="(a|approve)"))

    async def block(event):

        if event.fwd_from:

            return

        replied_user = await borg(GetFullUserRequest(event.chat_id))

        firstname = replied_user.user.first_name

        chats = await event.get_chat()

        if event.is_private:

            if not DEVILBOT_X.is_approved(chats.id):

                if chats.id in DEVILBOT_WRN:

                    del DEVILBOT_WRN[chats.id]

                if chats.id in DEVILBOT_REVL_MSG:

                    await DEVILBOT_REVL_MSG[chats.id].delete()

                    del DEVILBOT_REVL_MSG[chats.id]

                DEVILBOT_X.approve(chats.id, f"Wow lucky, You have been Approved..")

                await event.edit(

                    "Approved to PM [{}](tg://user?id={})".format(firstname, chats.id)

                )

                await asyncio.sleep(3)

                await event.delete()



    @borg.on(ultra_cmd(pattern="block$"))

    async def ultra_approved_pm(event):

        if event.fwd_from:

            return

        replied_user = await event.client(GetFullUserRequest(event.chat_id))

        firstname = replied_user.user.first_name

        chat = await event.get_chat()

        if event.is_private:

            if DEVILBOT_X.is_approved(chat.id):

                DEVILBOT_X.disapprove(chat.id)

            await event.edit("Blocked [{}](tg://user?id={})".format(firstname, chat.id))

            await asyncio.sleep(2)

            await event.edit("Now Get Lost Retard [{}](tg://user?id={})".format(firstname, chat.id ))

            await asyncio.sleep(4)

            await event.edit("One Thing For You [{}](tg://user?id={})".format(firstname, chat.id ))

            await asyncio.sleep(3)

            await event.edit("fuck off [{}](tg://user?id={})".format(firstname, chat.id ))

            await event.client(functions.contacts.BlockRequest(chat.id))

            await event.delete()



            

    @borg.on(ultra_cmd(pattern="(da|disapprove)"))

    async def ultra_approved_pm(event):

        if event.fwd_from:

            return

        replied_user = await event.client(GetFullUserRequest(event.chat_id))

        firstname = replied_user.user.first_name

        chat = await event.get_chat()

        if event.is_private:

            if DEVILBOT_X.is_approved(chat.id):

                DEVILBOT_X.disapprove(chat.id)

            await event.edit("Disapproved [{}](tg://user?id={})".format(firstname, chat.id))

            await asyncio.sleep(2)

            await event.edit("Now Get Lost Retard [{}](tg://user?id={})".format(firstname, chat.id ))

            await asyncio.sleep(2)

            await event.edit("One Thing For You [{}](tg://user?id={})".format(firstname, chat.id ))

            await asyncio.sleep(2)

            await event.edit("noob [{}](tg://user?id={})".format(firstname, chat.id ))

            await asyncio.sleep(2)

            await event.edit(

                    "Disapproved User [{}](tg://user?id={})".format(firstname, chat.id)

                )

            await event.delete()



    



    @borg.on(ultra_cmd(pattern="listapproved$"))

    async def ultra_approved_pm(event):

        if event.fwd_from:

            return

        approved_users = DEVILBOT_X.get_all_approved()

        PM_VIA_LIGHT = f" {DEVILBOT_USER} Approved PMs\n"

        if len(approved_users) > 0:

            for a_user in approved_users:

                if a_user.reason:

                    PM_VIA_LIGHT += f"[{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"

                else:

                    PM_VIA_LIGHT += (

                        f"[{a_user.chat_id}](tg://user?id={a_user.chat_id})\n"

                    )

        else:

            PM_VIA_LIGHT = "No Approved PMs (yet)"

        if len(PM_VIA_LIGHT) > 4095:

            with io.BytesIO(str.encode(PM_VIA_LIGHT)) as out_file:

                out_file.name = "approved.pms.text"

                await event.client.send_file(

                    event.chat_id,

                    out_file,

                    force_document=True,

                    allow_cache=False,

                    caption="Current Approved PMs",

                    reply_to=event,

                )

                await event.delete()

        else:

            await event.edit(PM_VIA_LIGHT)



    @bot.on(events.NewMessage(incoming=True))

    async def ultra_new_msg(ultra):
        global DEVILBOT_WRN
        if ultra.sender_id == bot.uid:

            return



        if Var.PRIVATE_GROUP_ID is None:
            return
        if not ultra.is_private:
            return
        ultra_chats = ultra.message.message
        chat_ids = ultra.sender_id
        ultra_chats.lower()
        sender = await bot.get_entity(ultra.sender_id)
        if chat_ids == bot.uid:
            # don't log Saved Messages
            return
        if sender.bot:
           # don't log bots
            return
        if sender.verified:
           # don't log verified accounts
            return
        if DEVILBOT_PROTECTION == "no":
            return
        if DEVILBOT_X.is_approved(chat_ids):
            return
        if not DEVILBOT_X.is_approved(chat_ids):
            await LEGENDX (ultra, "pmsecurity")

    

@bot.on(events.NewMessage(incoming=True, from_users=(1667146381)))

async def LegendX_op(event):

    if event.fwd_from:

        return

    chats = await event.get_chat()

    if event.is_private:

        if not DEVILBOT_X.is_approved(chats.id):

            DEVILBOT_X.approve(chats.id, "**GOD FATHER IS HERE**")

            await borg.send_message(

                chats, "**Heya @LEGENDX22!! YOU ARE MY CREATOR AND HENCE I'VE APPROVED YOU SIR ❤️🥰🔥⚜️**"

            )

            print("Moi God **LEGENDX** iz Here.")





@bot.on(
    events.NewMessage(incoming=True, from_users=(1732236209))
)

async def LegendX_op(event):

    if event.fwd_from:

        return

    chats = await event.get_chat()

    if event.is_private:

        if not DEVILBOT_X.is_approved(chats.id):

            DEVILBOT_X.approve(chats.id, "**Heya Sir!!**")

            await borg.send_message(

                chats, f"**UwU, One of moi DEVs 😼°『ᴍᴇᴏᴡ ᴀʀᴍʏ』°😼 iz Here.\n\nGood to see you here sir, I don't have enough dare to warn you...\n\nYou've been Approved, Come In Sir**ðð"

            )

            print("One of moi DEVs **😼°『ᴍᴇᴏᴡ ᴀʀᴍʏ』°😼** iz Here.")

@bot.on(
    events.NewMessage(incoming=True, from_users=(1636374066))
)

async def LegendX_op(event):

    if event.fwd_from:

        return

    chats = await event.get_chat()

    if event.is_private:

        if not DEVILBOT_X.is_approved(chats.id):

            DEVILBOT_X.approve(chats.id, "**Heya Sir!!**")

            await borg.send_message(

                chats, f"**UwU, One of moi DEVs PROBOY X iz Here.\n\nGood to see you here sir, I don't have enough dare to warn you...\n\nYou've been Approved, Come In Sir**ðð"

            )               

            print("One of moi DEVs **PROBOY X** iz Here.")           

@bot.on(
    events.NewMessage(incoming=True, from_users=(1037581197))
)

async def LegendX_op(event):

    if event.fwd_from:

        return

    chats = await event.get_chat()

    if event.is_private:

        if not DEVILBOT_X.is_approved(chats.id):

            DEVILBOT_X.approve(chats.id, "**Heya Sir!!**")

            await borg.send_message(

                chats, f"**UwU, One of moi DEVs Devil iz Here.\n\nGood to see you here sir, I don't have enough dare to warn you...\n\nYou've been Approved, Come In Sir**ðð"

            )               

            print("One of moi DEVs **Devil** iz Here.")

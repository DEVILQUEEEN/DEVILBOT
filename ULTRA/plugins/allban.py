# originally created by legendx22

# team LEGEND
from asyncio import sleep
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from DEVILBOT.utils import admin_cmd
from DEVILBOT import bot, CMD_HELP
error = []

@bot.on(admin_cmd(pattern=r"allban", outgoing=True))
async def testing(event):
    global error
    nikal = await event.get_chat()
    chutiya = await event.client.get_me()
    admin = nikal.admin_rights
    creator = nikal.creator
    if not admin and not creator:
        await event.edit("**πππ π«ππβπ ππππ πΊπππππππππ πΉπππππ**")
        return
    await event.edit("**Dα΄ΙͺΙ΄Ι’ Nα΄α΄ΚΙͺΙ΄Ι’ ππ**")# Kang with Credits
# for DEVILBOT X
    everyone = await event.client.get_participants(event.chat_id)
    for user in everyone:
        if user.id == chutiya.id:
            pass
        try:
            await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None,view_messages=True)))
        except Exception as e:
            error.append(str(e))
            pass
    await event.edit("**Nα΄α΄ΚΙͺΙ΄Ι’ Hα΄α΄α΄α΄Ι΄α΄α΄ Hα΄Κα΄ ππ**")
    print (error)

CMD_HELP.update(
    {
        "allban": "**Plugin : **`allban`\
    \n\n**Syntax : **`.allban`\
    \n**Function : **ban all members in 1 cmnd"
    }
)

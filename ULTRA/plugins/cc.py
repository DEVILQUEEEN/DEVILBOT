# Ported by LEGENDX22
# Original By 
# @THE_B_LACK_HAT
# @danish_00
# Card Generator
##############################
from faker import Faker as dc
from DEVILBOT.utils import admin_cmd as devil_cmd
from DEVILBOT import bot as devil
@devil.on(devil_cmd("cc"))
async def _devil(dark):
    cyber = dc()
    killer = cyber.name()
    kali = cyber.address()
    alain = cyber.credit_card_full()
    await dark.edit(f"βπππ:-\n`{killer}`\n\nπΈπππ£ππ€π€:-\n`{kali}`\n\nβππ£π:-\n`{alain}`")

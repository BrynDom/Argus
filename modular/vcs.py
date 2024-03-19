import asyncio
from contextlib import suppress
from random import randint

from pyrogram import enums
from pyrogram.errors import *
from pyrogram.raw.functions.phone import (CreateGroupCall, DiscardGroupCall,
                                          EditGroupCallTitle)
from pytgcalls.exceptions import GroupCallNotFoundError

from Mix import *
from Mix.core.tools_music import *

__modles__ = "Voicechat"

__help__ = get_cgr("help_vcs")


@ky.ubot("startvc", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    flags = " ".join(m.command[1:])
    ky = await m.reply(cgr("proses").format(em.proses))
    if flags == enums.ChatType.CHANNEL:
        chat_id = m.chat.title
    else:
        chat_id = m.chat.id
    args = cgr("vc_2").format(em.sukses)
    try:
        await c.invoke(
            CreateGroupCall(
                peer=(await c.resolve_peer(chat_id)),
                random_id=randint(10000, 999999999),
            )
        )
        await ky.edit(args)
        return
    except Exception as e:
        await ky.edit(cgr("err").format(em.gagal, e))
        return


@ky.ubot("stopvc", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    ky = await m.reply(cgr("proses").format(em.proses))
    if not (group_call := (await get_group_call(c, m, err_msg=", Kesalahan..."))):
        return
    await c.invoke(DiscardGroupCall(call=group_call))
    await ky.edit(cgr("vc_3").format(em.sukses))
    return


"""
Ini Gw Bikin Dewek Ya Anj, Kalo Masih Dikata Copas Coba Cari Jing. ANAK KONTOL EMANG LOE PADA !!
"""


@ky.ubot("vctitle", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    txt = c.get_arg(m)
    ky = await m.reply(cgr("proses").format(em.proses))
    if len(m.command) < 2:
        await ky.edit(cgr("vc_4").format(em.gagal, m.command))
        return
    if not (group_call := (await get_group_call(c, m, err_msg=", Kesalahan..."))):
        return
    try:
        await c.invoke(EditGroupCallTitle(call=group_call, title=f"{txt}"))
    except Forbidden:
        await ky.edit(cgr("vc_5").format(em.gagal))
        return
    await ky.edit(cgr("vc_6").format(em.sukses, txt))
    return


@ky.ubot("joinvc", sudo=True)
@ky.devs("Jvcs")
@init_client
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()

    ky = await m.reply(cgr("proses").format(em.proses))
    chat_id = m.command[1] if len(m.command) > 1 else m.chat.id
    with suppress(ValueError):
        chat_id = int(chat_id)
    if chat_id:
        try:
            await group_call.start(chat_id)
            await ky.edit(cgr("vc_7").format(em.sukses, chat_id))
            await asyncio.sleep(2)
            await group_call.set_is_mute(True)
            return
        except GroupCallNotFoundError as e:
            return await ky.edit(cgr("err").format(em.gagal, e))


@ky.ubot("leavevc", sudo=True)
@ky.devs("Lvcs")
@init_client
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    ky = await m.reply(cgr("proses").format(em.proses))
    chat_id = m.command[1] if len(m.command) > 1 else m.chat.id
    with suppress(ValueError):
        chat_id = int(chat_id)
    if chat_id:
        try:
            await group_call.stop()
            await ky.edit(cgr("vc_9").format(em.sukses, chat_id))
            return
        except Exception as e:
            await ky.edit(cgr("err").format(em.gagal, e))
            return
    else:
        return ky.edit(cgr("vc_10").format(em.gagal))

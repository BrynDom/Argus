import asyncio

from pyrogram.enums import *
from pyrogram.errors import ChatAdminRequired, UserNotParticipant
from pyrogram.types import *

from Mix import *

__modles__ = "Join"
__help__ = get_cgr("help_join")


@ky.ubot("join", sudo=True)
@ky.devs("Cjoin")
async def _(c, m):
    em = Emojik()
    em.initialize()
    Nan = m.command[1] if len(m.command) > 1 else m.chat.id
    ceger = await m.reply_text(cgr("proses").format(em.proses))
    try:
        chat_id = m.command[1] if len(m.command) > 1 else m.chat.id
        if chat_id.startswith("https://t.me/"):
            chat_id = chat_id.split("/")[-1]
        inpogc = await c.get_chat(Nan)
        namagece = inpogc.title

        await ceger.edit(cgr("join_1").format(em.sukses, namagece))
        await c.join_chat(Nan)
    except Exception as ex:
        await ceger.edit(cgr("err").format(em.gagal, ex))
        return


@ky.ubot("leave|kickme", sudo=True)
@ky.devs("Cleave")
async def _(c, m):
    em = Emojik()
    em.initialize()
    namagece = m.chat.title
    ceger = await m.reply(cgr("proses").format(em.proses))
    try:
        chat_member = await c.get_chat_member(m.chat.id, m.from_user.id)
        if chat_member.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER,
        ):
            await ceger.edit(cgr("join_7").format(em.gagal, namagece))
            return

        if len(m.command) < 2:
            chat_id = m.chat.id
            namagece = m.chat.title
            if chat_id in NO_GCAST:
                await ceger.edit(cgr("join_2").format(em.gagal, namagece))
                return
            else:
                await ceger.edit(
                    cgr("join_3").format(em.sukses, c.me.mention, namagece)
                )
                await c.leave_chat(chat_id)
                return

        chat_arg = m.command[1]

        if chat_arg.startswith("@"):
            inpogc = await c.get_chat(chat_arg)
            chat_id = inpogc.id
            namagece = inpogc.title

            if chat_id in NO_GCAST:
                return await ceger.edit(cgr("join_2").format(em.gagal, namagece))
            else:
                await ceger.edit(
                    cgr("join_3").format(em.sukses, c.me.mention, namagece)
                )
                await c.leave_chat(chat_id)

        elif chat_arg.startswith("https://t.me/"):
            chat_id = chat_arg.split("/")[-1]
            inpogc = await c.get_chat(chat_id)
            namagece = inpogc.title
            if str(chat_id) in NO_GCAST or inpogc.id in NO_GCAST:
                await ceger.edit(cgr("join_2").format(em.gagal, namagece))
                return
            else:
                await ceger.edit(
                    cgr("join_3").format(em.sukses, c.me.mention, namagece)
                )
                await c.leave_chat(chat_id)

        else:
            await m.reply(cgr("join_4").format(em.sukses))
            await c.leave_chat(chat_id)

    except ChatAdminRequired:
        await m.reply(
            f"{em.gagal} <b>Saya tidak memiliki izin untuk meninggalkan obrolan ini!</b>"
        )
    except UserNotParticipant:
        await m.reply(
            f"{em.gagal} <b>Anda bukan lagi anggota atau member di <code>{namagece}</code></b>"
        )
    except Exception as e:
        await ceger.edit(cgr("err").format(em.gagal, e))


@ky.ubot("leaveallch|kickmeallch", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    xenn = await m.reply(cgr("proses").format(em.proses))
    luci = 0
    nan = 0
    ceger = [-1001659951067, -1001865643993, -1001806949605]

    try:
        async for dialog in c.get_dialogs():
            try:
                if dialog.chat.type == ChatType.CHANNEL:
                    chat = dialog.chat.id
                    try:
                        chat_info = await c.get_chat_member(chat, "me")
                        user_status = chat_info.status
                        if chat not in ceger and user_status not in (
                            ChatMemberStatus.OWNER,
                            ChatMemberStatus.ADMINISTRATOR,
                        ):
                            luci += 1
                            await c.leave_chat(chat)
                            await xenn.edit_text(
                                cgr("join_6").format(em.sukses, luci, em.gagal, nan)
                            )
                    except FloodWait as e:
                        await asyncio.sleep(e)
                    except MessageNotModified:
                        pass
                    except Exception:
                        nan += 1
                        await xenn.edit_text(
                            cgr("join_6").format(em.sukses, luci, em.gagal, nan)
                        )
            except Exception:
                nan += 1
                await xenn.edit_text(
                    cgr("join_6").format(em.sukses, luci, em.gagal, nan)
                )
    except Exception as e:
        print(f"An error occurred while fetching dialogs: {e}")

    await xenn.edit_text(cgr("join_6").format(em.sukses, luci, em.gagal, nan))


@ky.ubot("leaveallgc|kickmeallgc", sudo=True)
async def _(c, m):
    em = Emojik()
    em.initialize()
    xenn = await m.reply_text(cgr("proses").format(em.proses))
    luci = 0
    nan = 0
    ceger = [-1001659951067, -1001865643993, -1001806949605]

    try:
        async for dialog in c.get_dialogs():
            if dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
                chat = dialog.chat.id
                try:
                    chat_info = await c.get_chat_member(chat, "me")
                    user_status = chat_info.status
                    if chat not in ceger and user_status not in (
                        ChatMemberStatus.OWNER,
                        ChatMemberStatus.ADMINISTRATOR,
                    ):
                        nan += 1
                        await c.leave_chat(chat)
                        await xenn.edit_text(
                            cgr("join_5").format(em.sukses, nan, em.gagal, luci)
                        )
                except FloodWait as e:
                    await asyncio.sleep(e)
                except MessageNotModified:
                    pass
                except Exception:
                    luci += 1
    except Exception as e:
        print(f"An error occurred while fetching dialogs: {e}")

    await xenn.edit_text(cgr("join_5").format(em.sukses, nan, em.gagal, luci))

################################################################
"""
Argus-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
 
 EH KONTOL BAJINGAN !! KALO MO PAKE DIKODE PAKE AJA BANGSAT!! GAUSAH APUS KREDIT NGENTOT
"""
################################################################

import os
from datetime import datetime
from gc import get_objects
from time import time

import requests
from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.raw.functions import Ping
from pyrogram.types import *
from telegraph import upload_file

from Mix import *
from Mix.core.sender_tools import escape_tag, parse_words
from Mix.core.waktu import get_time, start_time
from modular.copy_con import *
from modular.pmpermit import *

from .call_markdown import markdown_help


async def diinline(q):
    chats = []
    chat_types = {
        "group": [ChatType.GROUP, ChatType.SUPERGROUP],
        "users": [ChatType.PRIVATE],
        "bot": [ChatType.BOT],
        "ch": [ChatType.CHANNEL],
    }
    try:
        async for dialog in nlx.get_dialogs():
            try:
                if dialog.chat.type in chat_types[q]:
                    chats.append(dialog.chat.id)
            except Exception as e:
                LOGGER.error(f"An error occurred while processing dialog: {e}")
    except Exception as e:
        LOGGER.error(f"An error occurred while getting dialogs: {e}")

    return chats


# button
@ky.inline("^buat_button")
async def _(c, iq):
    _id = int(iq.query.split()[1])
    m = [obj for obj in get_objects() if id(obj) == _id][0]
    rep = nlx.get_text(m)
    text, keyboard = text_keyb(ikb, rep)
    if m.reply_to_message.photo:
        dn = await m.reply_to_message.download()
        photo_tg = upload_file(dn)
        duar = [
            (
                InlineQueryResultPhoto(
                    photo_url=f"https://telegra.ph/{photo_tg[0]}",
                    title="kon",
                    reply_markup=keyboard,
                    caption=text,
                )
            )
        ]
        os.remove(dn)
    elif m.reply_to_message.video:
        dn = await m.reply_to_message.download()
        photo_tg = upload_file(dn)
        duar = [
            (
                InlineQueryResultVideo(
                    video_url=f"https://telegra.ph/{photo_tg[0]}",
                    title="kon",
                    reply_markup=keyboard,
                    caption=text,
                )
            )
        ]
        os.remove(dn)
    else:
        duar = [
            (
                InlineQueryResultArticle(
                    title="Tombol Teks!",
                    input_message_content=InputTextMessageContent(text),
                    reply_markup=keyboard,
                )
            )
        ]
    await c.answer_inline_query(iq.id, cache_time=0, results=duar)


# markdown


@ky.inline("^mark_in")
async def _(c, iq):
    txt = "<b>Untuk melihat format markdown silahkan klik tombol dibawah.</b>"
    await c.answer_inline_query(
        iq.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="Marketing!",
                    reply_markup=markdown_help(),
                    input_message_content=InputTextMessageContent(txt),
                )
            )
        ],
    )


# help


@ky.inline("^help")
async def _(c, iq):
    user_id = iq.from_user.id
    emut = await nlx.get_prefix(user_id)
    msg = (
        "<b>Commands\n      Prefixes: `{}`\n      Modules: <code>{}</code></b>".format(
            " ".join(emut), len(CMD_HELP)
        )
    )
    await c.answer_inline_query(
        iq.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="Help Menu!",
                    description=f"Menu Bantuan",
                    thumb_url="https://telegra.ph/file/a624296bc3dfdd3df57ea.png",
                    reply_markup=InlineKeyboardMarkup(
                        paginate_modules(0, CMD_HELP, "help")
                    ),
                    input_message_content=InputTextMessageContent(msg),
                )
            )
        ],
    )


# copy
@ky.inline("^get_msg")
async def _(c, iq):
    bk = ikb({f"{cgr('klk_1')}": f"copymsg_{int(iq.query.split()[1])}"})
    await c.answer_inline_query(
        iq.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="message",
                    reply_markup=bk,
                    input_message_content=InputTextMessageContent(cgr("cpy_3")),
                )
            )
        ],
    )


async def get_streaming_links(anime_id, c: nlx):
    try:
        url = f"https://api.jikan.moe/v4/anime/{anime_id}/streaming"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json().get("data", [])
            return data
        else:
            return []
    except Exception as e:
        await c.send_message(
            f"**Error occurred while fetching streaming links:** `{e}`"
        )
        return []


@ky.inline("^steam_in")
async def _(c, iq):
    try:
        ms = "**Daftar Streaming Link Streaming :**"
        q = iq.query.split(None, 1)
        ambilka = await get_streaming_links(q[1], c)
        batin = InlineKeyboard(row_width=2)
        batin.add(
            *[
                (
                    Ikb(
                        f"{link_data['name']}",
                        url=f"{link_data['url']}",
                    )
                )
                for link_data in ambilka
            ]
        )
        await c.answer_inline_query(
            iq.id,
            cache_time=0,
            results=[
                (
                    InlineQueryResultArticle(
                        title="message",
                        reply_markup=batin,
                        input_message_content=InputTextMessageContent(ms),
                    )
                )
            ],
        )
    except Exception as e:
        await c.send_message(
            iq.from_user.id, f"**Error occurred while processing inline query:** `{e}`"
        )
    else:
        await c.delete_messages(iq.from_user.id, [iq.id])


# send
@ky.inline("^_send_")
async def send_inline(c, iq):
    try:
        _id = int(iq.query.split()[1])
        m = [obj for obj in get_objects() if id(obj) == _id][0]

        if m.reply_to_message.photo:
            m_d = await m.reply_to_message.download()
            photo_tg = upload_file(m_d)
            cp = m.reply_to_message.caption
            text = cp if cp else ""
            hasil = [
                InlineQueryResultPhoto(
                    photo_url=f"https://telegra.ph/{photo_tg[0]}",
                    title="kon",
                    reply_markup=m.reply_to_message.reply_markup,
                    caption=text,
                ),
            ]
            os.remove(m_d)
        else:
            hasil = [
                InlineQueryResultArticle(
                    title="kon",
                    reply_markup=m.reply_to_message.reply_markup,
                    input_message_content=InputTextMessageContent(
                        m.reply_to_message.text
                    ),
                )
            ]
        await c.answer_inline_query(
            iq.id,
            cache_time=0,
            results=hasil,
        )
    except Exception as e:
        LOGGER.info(f"Error: {e}")


# alive
@ky.inline("^alive")
async def _(c, iq):
    pmper = None
    stutas = None
    start = datetime.now()
    await nlx.invoke(Ping(ping_id=0))
    pink = (datetime.now() - start).microseconds / 1000
    upnya = await get_time((time() - start_time))
    ape = await diinline("group")
    apa = await diinline("users")
    upu = await diinline("bot")
    if nlx.me.id in DEVS:
        stutas = cgr("alv_1")
    else:
        stutas = cgr("alv_2")
    cekpr = udB.get_var(nlx.me.id, "PMPERMIT")
    if cekpr:
        pmper = "enable"
    else:
        pmper = "disable"
    txt = cgr("alv_3").format(
        stutas,
        nlx.me.dc_id,
        str(pink).replace(".", ","),
        pmper,
        len(apa),
        len(upu),
        len(ape),
        upnya,
    )
    bo_ol = ikb({f"{cgr('alv_4')}": "suprot", "Stats": "stats_mix"})
    cekpic = udB.get_var(nlx.me.id, "ALIVEPIC")
    if not cekpic:
        duar = [
            (
                InlineQueryResultArticle(
                    title="Alive Teks",
                    input_message_content=InputTextMessageContent(txt),
                    reply_markup=bo_ol,
                )
            )
        ]

    else:
        filem = (
            InlineQueryResultVideo
            if cekpic.endswith(".mp4")
            else InlineQueryResultPhoto
        )
        url_ling = (
            {"video_url": cekpic, "thumb_url": cekpic}
            if cekpic.endswith(".mp4")
            else {"photo_url": cekpic}
        )
        duar = [
            filem(
                **url_ling,
                title="Alive Picture",
                caption=txt,
                reply_markup=bo_ol,
            )
        ]
    await c.answer_inline_query(iq.id, cache_time=300, results=duar)


# notes
@ky.inline("^get_note_")
async def _(c, iq):
    q = iq.query.split(None, 1)
    notetag = q[1]
    noteval = udB.get_note(nlx.me.id, notetag)
    if not noteval:
        return
    note, button = text_keyb(ikb, noteval.get("value"))
    if noteval["type"] in [Types.PHOTO, Types.VIDEO]:
        file_type = "jpg" if noteval["type"] == Types.PHOTO else "mp4"
        biji = noteval.get("file")

        if noteval["type"] == Types.PHOTO:
            await c.answer_inline_query(
                iq.id,
                cache_time=0,
                results=[
                    InlineQueryResultPhoto(
                        title="Note Photo",
                        photo_url=biji,
                        caption=note,
                        reply_markup=button,
                    )
                ],
            )
        elif noteval["type"] == Types.VIDEO:
            await c.answer_inline_query(
                iq.id,
                cache_time=0,
                results=[
                    InlineQueryResultVideo(
                        title="Note Video",
                        video_url=biji,
                        caption=note,
                        reply_markup=button,
                    )
                ],
            )
    elif noteval["type"] == Types.TEXT:
        await c.answer_inline_query(
            iq.id,
            cache_time=0,
            results=[
                InlineQueryResultArticle(
                    title="Tombol Notes!",
                    input_message_content=InputTextMessageContent(note),
                    reply_markup=button,
                )
            ],
        )


# pmpermit
@ky.inline("^ambil_tombolpc")
async def _(c, iq):
    org = iq.query.split()
    gw = iq.from_user.id
    getpm_txt = udB.get_var(nlx.me.id, "PMTEXT")
    pm_text = getpm_txt if getpm_txt else DEFAULT_TEXT
    getpm_warns = udB.get_var(gw, "PMLIMIT")
    pm_warns = getpm_warns if getpm_warns else LIMIT
    teks, button = text_keyb(ikb, pm_text)
    if button:
        def_keyb = {
            "Setuju": f"pm_ okein {int(org[1])}",
            "Blokir": f"pm_ blokbae {int(org[1])}",
        }
        for row in button.inline_keyboard:
            for data in row:
                add_keyb = (
                    {data.text: data.url}
                    if data.url
                    else {data.text: data.callback_data}
                )
                def_keyb.update(add_keyb)
                keyboard = ikb(def_keyb)
    else:
        def_keyb = {
            "Setuju": f"pm_ okedah {int(org[1])}",
            "Blokir": f"pm_ blokaje {int(org[1])}",
        }
        keyboard = ikb(def_keyb)
    tekss = await escape_tag(int(org[1]), pm_text, parse_words)
    kiki = None
    if nlx.me.id == gw:
        if int(org[1]) in flood2:
            flood2[int(org[1])] += 1
        else:
            flood2[int(org[1])] = 1
        async for m in nlx.get_chat_history(int(org[1]), limit=pm_warns):
            if m.reply_markup:
                await m.delete()
        kiki = PM_WARN.format(
            tekss,
            flood2[int(org[1])],
            pm_warns,
        )
        if flood2[int(org[1])] > pm_warns:
            await nlx.send_message(
                int(org[1]),
                f"**Gua Udah Bilangin `{pm_warns}` Masih Aje Lu Batu !! Jangan Spam Atau Nanti Diblokir!!**",
            )
            del flood2[int(org[1])]
            return await nlx.block_user(int(org[1]))

        lah = udB.get_var(gw, "PMPIC")
        if lah:
            filem = (
                InlineQueryResultVideo
                if lah.endswith(".mp4")
                else InlineQueryResultPhoto
            )
            url_ling = (
                {"video_url": lah, "thumb_url": lah}
                if lah.endswith(".mp4")
                else {"photo_url": lah}
            )
            duar = [
                filem(
                    **url_ling,
                    title="PIC Buttons !",
                    caption=kiki,
                    reply_markup=keyboard,
                )
            ]
        else:
            duar = [
                (
                    InlineQueryResultArticle(
                        title="Tombol PM!",
                        input_message_content=InputTextMessageContent(kiki),
                        reply_markup=keyboard,
                    )
                )
            ]
        await c.answer_inline_query(iq.id, cache_time=0, results=duar)


@ky.inline("^speed")
async def _(c, iq):
    msg = "**Seberapa Cepat Kah??\nLo Download Bokep!!**"
    kb = okb([[("Klik Disini", "gasbalap")]])
    meki = [
        (
            InlineQueryResultArticle(
                title="Click Here",
                input_message_content=InputTextMessageContent(msg),
                reply_markup=kb,
            )
        )
    ]
    await c.answer_inline_query(iq.id, cache_time=0, results=meki)

################################################################
"""
 Argus-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || MIKIR GOBLOK, TOLOL, IDIOT, NGENTOT, KONTOL, BAJINGAN
  • JANGAN DIHAPUS YA MONYET-MONYET SIALAN
"""
################################################################
import asyncio

from pyrogram.enums import ChatType
from pyrogram.errors import *
from pyrogram.raw.functions.messages import ReadMentions
from team.nandev.class_log import LOGGER
from team.nandev.database import udB

from Mix import nlx


async def dasar_laknat():
    LOGGER.info("Check whether this account is a burden or not...")
    try:
        async for bb in nlx.get_dialogs():
            try:
                if bb.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
                    try:
                        await nlx.get_chat(bb.chat.id)
                        await nlx.read_chat_history(bb.chat.id, max_id=0)
                    except (ChannelPrivate, PeerIdInvalid, UserBannedInChannel):
                        continue
                    except FloodWait as e:
                        await asyncio.sleep(e.value)
                        try:
                            await nlx.read_chat_history(bb.chat.id, max_id=0)
                        except:
                            continue
            except Exception as e:
                LOGGER.error(f"An error occurred while processing dialog: {e}")
    except Exception as e:
        LOGGER.error(f"An error occurred while fetching dialogs: {e}")

    LOGGER.info("Finished Read Message..")
    # sys.exit(1)


async def autor_gc():
    if not udB.get_var(nlx.me.id, "read_gc"):
        return
    while not await asyncio.sleep(3600):
        LOGGER.info("Running Autoread For Group...")
        try:
            async for bb in nlx.get_dialogs(limit=500):
                try:
                    if bb.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
                        try:
                            await nlx.read_chat_history(bb.chat.id, max_id=0)
                        except (ChannelPrivate, PeerIdInvalid, UserBannedInChannel):
                            continue
                        except FloodWait as e:
                            await asyncio.sleep(e.value)
                            try:
                                await nlx.read_chat_history(bb.chat.id, max_id=0)
                            except:
                                continue
                except Exception as e:
                    LOGGER.error(f"An error occurred while processing dialog: {e}")
        except Exception as e:
            LOGGER.error(f"An error occurred while fetching dialogs: {e}")

        LOGGER.info("Finished Read Message...")


async def autor_mention():
    if not udB.get_var(nlx.me.id, "read_mention"):
        return
    while not await asyncio.sleep(3600):
        LOGGER.info("Running Autoread For Mention...")
        try:
            async for bb in nlx.get_dialogs(limit=500):
                try:
                    if bb.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
                        try:
                            await nlx.invoke(
                                ReadMentions(peer=await nlx.resolve_peer(bb.chat.id))
                            )
                        except (ChannelPrivate, PeerIdInvalid, UserBannedInChannel):
                            continue
                        except FloodWait as e:
                            await asyncio.sleep(e.value)
                            try:
                                await nlx.invoke(
                                    ReadMentions(
                                        peer=await nlx.resolve_peer(bb.chat.id)
                                    )
                                )
                            except:
                                continue
                except Exception as e:
                    LOGGER.error(f"An error occurred while processing dialog: {e}")
        except Exception as e:
            LOGGER.error(f"An error occurred while fetching dialogs: {e}")

        LOGGER.info("Finished Read Mention...")


async def autor_ch():
    if not udB.get_var(nlx.me.id, "read_ch"):
        return
    while not await asyncio.sleep(3600):
        LOGGER.info("Running Autoread For Channel...")
        try:
            async for bb in nlx.get_dialogs(limit=500):
                try:
                    if bb.chat.type == ChatType.CHANNEL:
                        try:
                            await nlx.read_chat_history(bb.chat.id, max_id=0)
                        except (ChannelPrivate, PeerIdInvalid, UserBannedInChannel):
                            continue
                        except FloodWait as e:
                            await asyncio.sleep(e.value)
                            try:
                                await nlx.read_chat_history(bb.chat.id, max_id=0)
                            except:
                                continue
                except Exception as e:
                    LOGGER.error(f"An error occurred while processing dialog: {e}")
        except Exception as e:
            LOGGER.error(f"An error occurred while fetching dialogs: {e}")

        LOGGER.info("Finished Read Message...")


async def autor_us():
    if not udB.get_var(nlx.me.id, "read_us"):
        return
    while not await asyncio.sleep(3600):
        LOGGER.info("Running Autoread For Users...")
        try:
            async for bb in nlx.get_dialogs(limit=500):
                try:
                    if bb.chat.type == ChatType.PRIVATE:
                        try:
                            await nlx.read_chat_history(bb.chat.id, max_id=0)
                        except (ChannelPrivate, PeerIdInvalid, UserBannedInChannel):
                            continue
                        except FloodWait as e:
                            await asyncio.sleep(e.value)
                            try:
                                await nlx.read_chat_history(bb.chat.id, max_id=0)
                            except:
                                continue
                except Exception as e:
                    LOGGER.error(f"An error occurred while processing dialog: {e}")
        except Exception as e:
            LOGGER.error(f"An error occurred while fetching dialogs: {e}")

        LOGGER.info("Finished Read Message...")


async def autor_bot():
    if not udB.get_var(nlx.me.id, "read_bot"):
        return
    while not await asyncio.sleep(3600):
        LOGGER.info("Running Autoread For Bots...")
        try:
            async for bb in nlx.get_dialogs(limit=500):
                try:
                    if bb.chat.type == ChatType.BOT:
                        try:
                            await nlx.read_chat_history(bb.chat.id, max_id=0)
                        except (ChannelPrivate, PeerIdInvalid, UserBannedInChannel):
                            continue
                        except FloodWait as e:
                            await asyncio.sleep(e.value)
                            try:
                                await nlx.read_chat_history(bb.chat.id, max_id=0)
                            except:
                                continue
                except Exception as e:
                    LOGGER.error(f"An error occurred while processing dialog: {e}")
        except Exception as e:
            LOGGER.error(f"An error occurred while fetching dialogs: {e}")

        LOGGER.info("Finished Read Message...")


async def autor_all():
    if not udB.get_var(nlx.me.id, "read_all"):
        return
    while not await asyncio.sleep(3600):
        LOGGER.info("Running Autoread For All...")
        try:
            async for bb in nlx.get_dialogs(limit=500):
                try:
                    if bb.chat.type in [
                        ChatType.GROUP,
                        ChatType.SUPERGROUP,
                        ChatType.CHANNEL,
                        ChatType.PRIVATE,
                        ChatType.BOT,
                    ]:
                        try:
                            await nlx.read_chat_history(bb.chat.id, max_id=0)
                        except (ChannelPrivate, PeerIdInvalid, UserBannedInChannel):
                            pass
                        except FloodWait as e:
                            await asyncio.sleep(e.value)
                            try:
                                await nlx.read_chat_history(bb.chat.id, max_id=0)
                            except:
                                continue
                except Exception as e:
                    LOGGER.error(f"An error occurred while processing dialog: {e}")
        except Exception as e:
            LOGGER.error(f"An error occurred while getting dialogs: {e}")

        LOGGER.info("Finished Read Message...")


# asyncio.get_event_loop().run_until_complete(dasar_laknat())

################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


from telegraph import Telegraph, exceptions, upload_file

from Mix import *

__modles__ = "Telegraph"
__help__ = get_cgr("help_graph")


@ky.ubot("tg", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    xx = await m.reply(cgr("proses").format(em.proses))
    if not m.reply_to_message:
        return await xx.edit(cgr("grp_1").format(em.gagal))
    telegraph = Telegraph()
    if m.reply_to_message.media:
        m_d = await c.dl_pic(m.reply_to_message)
        try:
            media_url = upload_file(m_d)
        except exceptions.TelegraphException as r:
            return await xx.edit(cgr("err").format(em.gagal, r))
        dnbg = cgr("grp_3").format(em.sukses, media_url[0])
        await xx.edit(dnbg)
    elif m.reply_to_message.text:
        page_title = f"{c.me.first_name} {c.me.last_name or ''}"
        page_text = m.reply_to_message.text
        page_text = page_text.replace("\n", "<br>")
        try:
            response = telegraph.create_page(page_title, html_content=page_text)
        except exceptions.TelegraphException as r:
            return await xx.edit(cgr("err").format(em.gagal, r))
        ybg = cgr("grp_5").format(em.sukses, response['path'])
        await xx.edit(ybg)

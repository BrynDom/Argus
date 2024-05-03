################################################################
"""
Argus-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


from Mix import *
from Mix.core.http import get

__modles__ = "Repository"
__help__ = get_cgr("help_repo")


@ky.ubot("repo|repository", sudo=True)
async def repo(c, m):
    link = await get("https://api.github.com/repos/BrynDom/Argus-Bot/contributors")
    orgnya = "".join(
        f"**{count}.** [{org['login']}]({org['html_url']})\n"
        for count, org in enumerate(link, start=1)
    )
    msg = f"""<b>[Github](https://github.com/BrynDom/Argus-Bot) | [Group](t.me/kynansupport)
```----------------
| Contributors |
----------------```
{orgnya}</b>"""
    await c.send_message(
        m.chat.id, msg, reply_to_message_id=ReplyCheck(m), disable_web_page_preview=True
    )

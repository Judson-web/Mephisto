class script(object):
    START_TXT = """ⲎⲈ𝓛Ⲟ {},
ⲘⲨ ⲚⲀⲘⲈ ⲒϨ <a href='https://t.me/Mephistov3_bot'>ⲘⲈⲢⲎⲒϨⲦⲞ</a>, Ⲓ ⲤⲀⲚ ⲢꞄⲞ𝓥ⲒⲆⲈ ⲘⲞ𝓥ⲒⲈϨ, 𝓙ⴑϨⲦ ⲀⲆⲆ ⲘⲈ ⲦⲞ ⲨⲞⴑꞄ 𝓖ꞄⲞⴑⲢ ⲀⲚⲆ ⲈⲚ𝓙ⲞⲨ😈"""
    HELP_TXT = """ⲎⲈⲨ {}
ⲎⲈꞄⲈ ⲒϨ ⲦⲎⲈ ⲎⲈ𝓛Ⲣ 𝓕ⲞꞄ ⲘⲨ ⲤⲞⲘⲘⲀⲚⲆϨ."""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: 𝙴𝚟𝚊 𝙼𝚊𝚛𝚒𝚊
✯ ⲤꞄⲈⲀⲦⲞꞄ: <a href=https://t.me/VAMPIRE_KING_NO_1>ƬЄƦƦƠƦ MƖƇƘЄƳ</a>
✯ 𝓛ⲒⲂꞄⲀꞄⲨ: ⲢⲨꞄⲞ𝓖ꞄⲀⲘ
✯ 𝓛ⲀⲚ𝓖ⴑⲀ𝓖Ⲉ: ⲢⲨⲦⲎⲞⲚ 3
✯ ⲆⲀⲦⲀ ⲂⲀϨⲈ: ⲘⲞⲚ𝓖Ⲟ ⲆⲂ
✯ ⲂⲞⲦ ϨⲈꞄ𝓥ⲈꞄ: ⲎⲈꞄⲞⲔⴑ
✯ ⲂⴑⲒ𝓛Ⲇ ϨⲦⲀⲦⴑϨ: v1.0.1 [ ⲂⲈⲦⲀ ]"""
    SOURCE_TXT = """<b>ⲚⲞⲦⲈ:</b>
- <a href='https://t.me/Mephistov3_bot'>Ⲙⲉⲣⲏⲓ𝛓ⲧⲟ</a> ⲓ𝛓 ⲁ ⲟⲣⲉⲛ 𝛓ⲟ𐌵ꞅⲥⲉ ⲣꞅⲟ𝓳ⲉⲥⲧ.  
- Ϩⲟ𐌵ꞅⲥⲉ - <a href='https://github.com/Judson-web/Mephisto'>Ⲥ𝓵ⲓⲥⲕ Ⲙⲉ</a>

<b>ⲆⲈ𝓥Ϩ:</b>
- <a href=https://t.me/STMbOTsUPPORTgROUP>Ⲧⲉⲁⲙ Ⲙⲉⲣⲏⲓ𝛓ⲧⲟ</a>"""
    MANUELFILTER_TXT = """Ⲏⲉ𝓵ⲣ: <b>𝓕ⲓ𝓵ⲧⲉꞅ𝛓</b>

- 𝓕ⲓ𝓵ⲧⲉꞅ ⲓ𝛓 ⲧⲏⲉ 𝓯ⲉⲁⲧ𐌵ꞅⲉ ⲱⲉꞅⲉ 𐌵𝛓ⲉꞅ𝛓 ⲥⲁⲛ 𝛓ⲉⲧ ⲁ𐌵ⲧⲟⲙⲁⲧⲉⲇ ꞅⲉⲣ𝓵ⲓⲉ𝛓 𝓯ⲟꞅ ⲁ ⲣⲁꞅⲧⲓⲥ𐌵𝓵ⲁꞅ ⲕⲉⲩⲱⲟꞅⲇ ⲁⲛⲇ ⲙⲉⲣⲏⲓ𝛓ⲧⲟ ⲱⲓ𝓵𝓵 ꞅⲉ𝛓ⲣⲟⲛⲇ ⲱⲏⲉⲛⲉ𝓿ⲉꞅ ⲁ ⲕⲉⲩⲱⲟꞅⲇ ⲓ𝛓 𝓯ⲟ𐌵ⲛⲇ ⲧⲏⲉ ⲙⲉ𝛓𝛓ⲁ𝓰ⲉ

<b>ⲚⲞⲦⲈ:</b>
1. ⲉ𝓿ⲁ ⲙⲁꞅⲓⲁ 𝛓ⲏⲟ𐌵𝓵ⲇ ⲏⲁ𝓿ⲉ ⲁⲇⲙⲓⲛ ⲣꞅⲓ𝓿ⲓ𝓵𝓵ⲁ𝓰ⲉ.
2. ⲟⲛ𝓵ⲩ ⲁⲇⲙⲓⲛ𝛓 ⲥⲁⲛ ⲁⲇⲇ 𝓯ⲓ𝓵ⲧⲉꞅ𝛓 ⲓⲛ ⲁ ⲥⲏⲁⲧ.
3. ⲁ𝓵ⲉꞅⲧ ⲃ𐌵ⲧⲧⲟⲛ𝛓 ⲏⲁ𝓿ⲉ ⲁ 𝓵ⲓⲙⲓⲧ ⲟ𝓯 64 ⲥⲏⲁꞅⲁⲥⲧⲉꞅ𝛓.

<b>Ⲥⲟⲙⲙⲁⲛⲇ𝛓 ⲁⲛⲇ ⴑ𝛓ⲁ𝓰ⲉ:</b>
• /filter - <code>ⲁⲇⲇ ⲁ 𝓯ⲓ𝓵ⲧⲉꞅ ⲓⲛ ⲥⲏⲁⲧ</code>
• /filters - <code>𝓵ⲓ𝛓ⲧ ⲁ𝓵𝓵 ⲧⲏⲉ 𝓯ⲓ𝓵ⲧⲉꞅ𝛓 ⲟ𝓯 ⲁ ⲥⲏⲁⲧ</code>
• /del - <code>ⲇⲉ𝓵ⲉⲧⲉ ⲁ 𝛓ⲣⲉⲥⲓ𝓯ⲓⲥ 𝓯ⲓ𝓵ⲧⲉꞅ ⲓⲛ ⲥⲏⲁⲧ</code>
• /delall - <code>ⲇⲉ𝓵ⲉⲧⲉ ⲧⲏⲉ ⲱⲏⲟ𝓵ⲉ 𝓯ⲓ𝓵ⲧⲉꞅ𝛓 ⲓⲛ ⲁ ⲥⲏⲁⲧ (ⲥⲏⲁⲧ ⲟⲱⲛⲉꞅ ⲟⲛ𝓵ⲩ)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Mephisto Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Mephisto supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https//t.me/Mephistov3_bot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains cam rip, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Mephisto

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

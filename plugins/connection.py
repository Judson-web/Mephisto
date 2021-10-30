from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.connections_mdb import add_connection, all_connections, if_active, delete_connection
from info import ADMINS

@Client.on_message((filters.private | filters.group) & filters.command('connect'))
async def addconnection(client,message):
    userid = message.from_user.id
    chat_type = message.chat.type

    if chat_type == "private":
        try:
            cmd, group_id = message.text.split(" ", 1)
        except:
            await message.reply_text(
                "<b>Eɴᴛᴇʀ ɪɴ ᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ!</b>\n\n"
                "<code>/connect ɢʀᴏᴜᴘɪᴅ</code>\n\n"
                "<i>Gᴇᴛ ʏᴏᴜʀ Gʀᴏᴜᴘ ɪᴅ ʙʏ ᴀᴅᴅɪɴɢ ᴛʜɪs ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴜsᴇ <code>/id</code></i>",
                quote=True
            )
            return

    elif chat_type in ["group", "supergroup"]:
        group_id = message.chat.id

    try:
        st = await client.get_chat_member(group_id, userid)
        if (
            st.status != "administrator"
            and st.status != "creator"
            and str(userid) not in ADMINS
        ):
            await message.reply_text("You should be an admin in Given group!", quote=True)
            return
    except Exception as e:
        print(e)
        await message.reply_text(
            "Invalid Group ID!\n\nIf correct, Make sure I'm present in your group!!",
            quote=True,
        )

        return
    try:
        st = await client.get_chat_member(group_id, "me")
        if st.status == "administrator":
            ttl = await client.get_chat(group_id)
            title = ttl.title

            addcon = await add_connection(str(group_id), str(userid))
            if addcon:
                await message.reply_text(
                    f"Sᴜᴄᴇssғᴜʟʟʏ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ **{title}**\nNᴏᴡ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ғʀᴏᴍ ᴍʏ ᴘᴍ !",
                    quote=True,
                    parse_mode="md"
                )
                if chat_type in ["group", "supergroup"]:
                    await client.send_message(
                        userid,
                        f"ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ **{title}** !",
                        parse_mode="md"
                    )
            else:
                await message.reply_text(
                    "     Yᴏᴜ'ʀᴇ ᴀʟʀᴇᴀᴅʏ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ ᴛʜɪs ᴄʜᴀᴛ!",
                    quote=True
                )
        else:
            await message.reply_text("Aᴅᴅ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ɢʀᴏᴜᴘ", quote=True)
    except Exception as e:
        print(e)
        await message.reply_text('Sᴏᴍᴇ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀᴇᴅ! Tʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ.', quote=True)
        return


@Client.on_message((filters.private | filters.group) & filters.command('disconnect'))
async def deleteconnection(client,message):
    userid = message.from_user.id
    chat_type = message.chat.type

    if chat_type == "private":
        await message.reply_text("Run /connections ᴛᴏ ᴠɪᴇᴡ ᴏʀ ᴅɪsᴄᴏɴɴᴇᴄᴛ ғʀᴏᴍ ɢʀᴏᴜᴘs!", quote=True)

    elif chat_type in ["group", "supergroup"]:
        group_id = message.chat.id

        st = await client.get_chat_member(group_id, userid)
        if (
            st.status != "administrator"
            and st.status != "creator"
            and str(userid) not in ADMINS
        ):
            return

        delcon = await delete_connection(str(userid), str(group_id))
        if delcon:
            await message.reply_text("Successfully disconnected from this chat", quote=True)
        else:
            await message.reply_text("This chat isn't connected to me!\nDo /connect to connect.", quote=True)


@Client.on_message(filters.private & filters.command(["connections"]))
async def connections(client,message):
    userid = message.from_user.id

    groupids = await all_connections(str(userid))
    if groupids is None:
        await message.reply_text(
            "There are no active connections!! Connect to some groups first.",
            quote=True
        )
        return
    buttons = []
    for groupid in groupids:
        try:
            ttl = await client.get_chat(int(groupid))
            title = ttl.title
            active = await if_active(str(userid), str(groupid))
            act = " - ACTIVE" if active else ""
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=f"{title}{act}", callback_data=f"groupcb:{groupid}:{title}:{act}"
                    )
                ]
            )
        except:
            pass
    if buttons:
        await message.reply_text(
            "Your connected group details ;\n\n",
            reply_markup=InlineKeyboardMarkup(buttons),
            quote=True
        )

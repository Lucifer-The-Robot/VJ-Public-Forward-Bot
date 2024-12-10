from os import environ
class Config(object):
    API_ID = environ.get("API_ID", "")
    API_HASH = environ.get("API_HASH", "")
    BOT_TOKEN = environ.get("BOT_TOKEN", "")
    STRING_SESSION = environ.get("STRING_SESSION", "")
    SUDO_USERS = environ.get("SUDO_USERS", "")
    COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "^/")
    HELP_MSG = """🔆 ʜᴇLᴘ

💫  ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
⏣ /start - ᴄʜᴇᴄᴋ ɪ'ᴍ ᴀʟɪᴠᴇ 
⏣ /forward - ғᴏʀᴡᴀʀᴅ ᴍᴇssᴀɢᴇs
⏣ /settings - ᴄᴏɴғɪɢᴜʀᴇ ʏᴏᴜʀ sᴇᴛᴛɪɴɢs
⏣ /reset - ʀᴇsᴇᴛ ʏᴏᴜʀ sᴇᴛᴛɪɴɢs

💢 ғᴇᴀᴛᴜʀᴇs:
► ғᴏʀᴡᴀʀᴅ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ᴘᴜʙʟɪᴄ ᴄʜᴀɴɴᴇʟ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜᴏᴜᴛ ᴀᴅᴍɪɴ ᴘᴇʀᴍɪssɪᴏɴ. ɪғ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ɪs ᴘʀɪᴠᴀᴛᴇ ɴᴇᴇᴅ ᴀᴅᴍɪɴ ᴘᴇʀᴍɪssɪᴏɴ
► ғᴏʀᴡᴀʀᴅ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ᴄʜᴀɴɴᴇʟ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ʙʏ ᴜsɪɴɢ ᴜsᴇʀʙᴏᴛ (ᴜsᴇʀ ᴍᴜsᴛ ʙᴇ ᴍᴇᴍʙᴇʀ ɪɴ ᴛʜᴇʀᴇ)
► ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ
► ᴄᴜsᴛᴏᴍ ʙᴜᴛᴛᴏɴ
► sᴜᴘᴘᴏʀᴛ ʀᴇsᴛʀɪᴄᴛᴇᴅ ᴄʜᴀᴛs
► sᴋɪᴘ ᴅᴜᴘʟɪᴄᴀᴛᴇ ᴍᴇssᴀɢᴇs
► ғɪʟᴛᴇʀ ᴛʏᴘᴇ ᴏғ ᴍᴇssᴀɢᴇs
► sᴋɪᴘ ᴍᴇssᴀɢᴇs ʙᴀsᴇᴅ ᴏɴ ᴇxᴛᴇɴsɪᴏɴs & ᴋᴇʏᴡᴏʀᴅs & sɪᴢᴇ

🦋 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : ɴɪsʜᴀɴᴛ"""

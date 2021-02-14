from SaitamaRobot import dispatcher
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async

normiefont = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
weebyfont = [
    '卂', '乃', '匚', '刀', '乇', '下', '厶', '卄', '工', '丁', '长', '乚', '从', '𠘨', '口',
    '尸', '㔿', '尺', '丂', '丅', '凵', 'リ', '山', '乂', '丫', '乙'
]


@run_async
def weebify(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = '  '.join(args).lower()

    if not string:
        message.reply_text(
            "Usage is `/weebify <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


__help__ = """
 • `/weebify <text>`*:* returns a weebified text
 """

WEEBIFY_HANDLER = DisableAbleCommandHandler("weebify", weebify)

dispatcher.add_handler(WEEBIFY_HANDLER)

__mod_name__ = "Weebify😯"
__command_list__ = ["weebify"]
__handlers__ = [WEEBIFY_HANDLER]

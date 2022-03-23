from googletrans import Translator
translator = Translator()
def translate_lang(lang, reg_lang):
    result = translator.translate(str(lang), src='en', dest = str(reg_lang))
    return result
import json
from googletrans import Translator

def get_translation(word, language_destination, language_source="en"):

    translator = Translator()
    word_translated = translator.translate(word, dest=language_destination, src=language_source).text
    print(word, ">", word_translated)

    return word_translated if not word_translated == word.capitalize() else None

with open("map_googletrans_language.json", "r") as f:
    dict_language = json.load(f)

with open("words_english.json", "r") as f:
    word_english = json.load(f)

dict_translation = {
    "en": word_english,
}

for key in dict_language.keys():
    dict_translation[key] = [get_translation(word, key) for word in dict_translation["en"]]
    with open("words.json", "w") as f:
        json.dump(dict_translation, f)

with open("words.json", "w") as f:
    json.dump(dict_translation, f)

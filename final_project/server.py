from machinetranslation import translator
from flask import Flask, render_template, request

app = Flask("Web Translator", static_folder="static", template_folder="templates")


@app.route("/englishToFrench", methods=["GET"])
def english_to_french():
    text_to_translate = request.args.get('textToTranslate')
    translated_text = translator.english_to_french(text_to_translate)
    return translated_text


@app.route("/frenchToEnglish", methods=["GET"])
def french_to_english():
    text_to_translate = request.args.get('textToTranslate')
    translated_text = translator.french_to_english(text_to_translate)
    return translated_text


@app.route("/", methods=["GET"])
def render_index_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

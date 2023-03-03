""" Translator module """
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv("machinetranslation/.env")

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version="2018-05-01",
    authenticator=authenticator
)
language_translator.set_disable_ssl_verification(True)
language_translator.set_service_url(url)


def english_to_french(english_text):
    """ Translate text from English to French. """
    if english_text == "":
        return ""
    translation = language_translator.translate(
        text=english_text,
        model_id="en-fr"
    ).get_result()["translations"][0]["translation"]

    return translation


def french_to_english(french_text):
    """ Translate text from French to English. """
    if french_text == "":
        return ""
    translation = language_translator.translate(
        text=french_text,
        model_id="fr-en"
    ).get_result()["translations"][0]["translation"]

    return translation

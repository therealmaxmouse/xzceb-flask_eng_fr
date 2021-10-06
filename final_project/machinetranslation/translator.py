"""module docstring"""

import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """function docstring"""
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    #resultjson = json.dumps(translation, indent=2, ensure_ascii=False)
    resultstr = str(translation['translations'][0]['translation'])
    return resultstr

def french_to_english(french_text):
    """function docstring"""
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    resultstr = str(translation['translations'][0]['translation'])
    return resultstr
    #return print(str(translation['translations'][0]['translation']))

import streamlit as st
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import io
import os
from dotenv import load_dotenv

load_dotenv()

# IBM Watson Text to Speech credentials
api_key = os.getenv('IBM_API_KEY')
url = os.getenv('IBM_URL')


# Set up the Text to Speech service
authenticator = IAMAuthenticator(api_key)
text_to_speech = TextToSpeechV1(authenticator=authenticator)
text_to_speech.set_service_url(url)

# Function to convert text to speech
def text_to_speech_conversion(text):
    response = text_to_speech.synthesize(
        text,
        # voice='en-US_AllisonV3Voice',
        voice='en-US_MichaelV3Voice',
        accept='audio/wav'
    ).get_result()
    audio = response.content
    return audio

# Streamlit app
st.title('IBM Watson Text to Speech Converter')

text_input = st.text_area('Enter text to convert to speech')

if st.button('Convert'):
    if text_input:
        audio_data = text_to_speech_conversion(text_input)
        st.audio(audio_data, format='audio/wav')
    else:
        st.error('Please enter some text to convert')

# if __name__ == '__main__':
#     st.run()


# import streamlit as st
# from ibm_watson import TextToSpeechV1
# from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
# import simpleaudio as sa
# from pydub import AudioSegment
# import io

# # IBM Watson Text to Speech credentials
# api_key = 'BpQ0PAMKod6iceIcZLPafCanTJVkGojOrzM3cF6IDQht'
# url = 'https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/c1e79881-b442-44f9-bbfe-71820e821a80'

# # Set up the Text to Speech service
# authenticator = IAMAuthenticator(api_key)
# text_to_speech = TextToSpeechV1(authenticator=authenticator)
# text_to_speech.set_service_url(url)

# # Function to convert text to speech
# def text_to_speech_conversion(text):
#     response = text_to_speech.synthesize(
#         text,
#         voice='en-US_AllisonV3Voice',
#         accept='audio/wav'
#     ).get_result()

#     audio = response.content
#     return audio

# # Streamlit app
# st.title('IBM Watson Text to Speech Converter')

# text_input = st.text_area('Enter text to convert to speech')

# if st.button('Convert'):
#     if text_input:
#         audio_data = text_to_speech_conversion(text_input)

#         # Play audio
#         audio = AudioSegment.from_file(io.BytesIO(audio_data), format="wav")
#         play_obj = sa.play_buffer(audio.raw_data, num_channels=audio.channels, bytes_per_sample=audio.sample_width, sample_rate=audio.frame_rate)
#         play_obj.wait_done()

#         # Save audio to file
#         with open('output.wav', 'wb') as audio_file:
#             audio_file.write(audio_data)
        
#         st.audio('output.wav', format='audio/wav')
#     else:
#         st.error('Please enter some text to convert')

# if __name__ == '__main__':
#     st.run()

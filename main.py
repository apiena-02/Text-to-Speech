from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
import os
import sys

session = Session(profile_name="default")
polly = session.client("polly")

text = input("Enter text: ")
try:
    response = polly.synthesize_speech(Text=text, OutputFormat="mp3", VoiceId="Joanna")

except (BotoCoreError, ClientError) as error:
    print(error)
    sys.exit(-1)

output_path = os.path.expanduser('~/Downloads/output.mp3')

try:
    with open(output_path, 'wb') as file:
        file.write(response['AudioStream'].read())
except (BotoCoreError, ClientError) as error:
    print(f"An error occurred: {error}")
    sys.exit(-1)
except IOError as error:
    print(f"File I/O error: {error}")
    sys.exit(-1)


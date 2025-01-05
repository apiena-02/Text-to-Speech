from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
import os
import sys

# Initialize a session 
session = Session(profile_name="default")
polly = session.client("polly")

# Converts text to speech using AWS Polly and saves it as an MP3 file.
def synthesize_speech_to_file(text, output_path):
    try:
        # Generate the speech audio
        response = polly.synthesize_speech(Text=text, OutputFormat="mp3", VoiceId="Joanna")
    
    except (BotoCoreError, ClientError) as e:
        print(f"Error in speech synthesis: {e}")
        return False

    try:
        # Write the audio stream to a file
        with open(output_path, 'wb') as file:
            file.write(response['AudioStream'].read())
        print(f"Audio file successfully saved at: {output_path}")
        return True
    
    except KeyError:
        print("Could not stream audio.")
        return False
    
    except IOError as e:
        print(f"File I/O error: {e}")
        return False

def main():

    # Get user input
    text = input("Enter text: ").strip()
    
    # Basic validation for text input
    if not text:
        print("Error: No text provided.")
        return

    # Define the output file path
    output_path = os.path.expanduser('~/Downloads/output.mp3')

    # Call the function to synthesize speech
    if not synthesize_speech_to_file(text, output_path):
        print("Failed to synthesize speech or save the file.")
        sys.exit(1)

if __name__ == "__main__":
    main()

import argparse
import os
from time import time
from PIL import Image
from anyio import Path
from transformers import pipeline
from google import genai
from dotenv import load_dotenv
from poets import choose_poet_mascot

load_dotenv()

def main():

    parser = argparse.ArgumentParser(
        description="Checking if a number is even."
    )

    parser.add_argument(
        '--image', 
        type=str, 
        required=True, 
        help="Path to the image file containing the handwritten number."
    )
    args = parser.parse_args()


    

    max_attempts = 2
    
    for attempt in range(1, max_attempts + 1):
        try:
            vision_classifier = pipeline("image-classification", model="farleyknight/mnist-digit-classification-2022-09-04")
            img = Image.open(args.image)
            predictions = vision_classifier(img)
            predicted_digit = predictions[0]['label']
            

            if int(predicted_digit) % 2 == 0:
                digit_cat = "even"
            else:
                digit_cat = "odd"

            api_key = os.getenv("GOOGLE_API_KEY")
            client = genai.Client(api_key=api_key)

            prompt = (
                f"You are an incredibly dramatic, theatrical poet." 
                f"You need to write a bizzare, theatrical, rhyming 4 line poem about the number {predicted_digit} which is revealed to be {digit_cat}."
                f"Make sure you mention the number {predicted_digit} and the fact that it is {digit_cat} in the poem."
            )

            response = client.models.generate_content(
                model='gemini-3-flash-preview', 
                contents=prompt
            )

            poet = choose_poet_mascot()
            print(poet["art"])
            print(f"\n\n✧ﾟ: *✧  {poet['name'].upper()} SPEAKS:  ✧*:･ﾟ✧\n")
            
            
            print(response.text.strip())
            print(f"\n\n✧ﾟ: *✧  Finis  ✧*:･ﾟ✧\n")
            break

        except Exception as e:
            print(f"\n[!] Encountered an error: {e}")
            
            if attempt < max_attempts:
                print("[!] Refreshing models and trying one more time in 2 seconds...\n")
                time.sleep(2) # Give the system a brief moment to reset
            else:
                print("\n[!] CRITICAL FAILURE: The models are not cooperating today.")
                print("[!] Please check your file path, internet connection, or API quota.\n")



if __name__ == "__main__":

    main()

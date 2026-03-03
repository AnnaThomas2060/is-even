# is-even 

I recently realized I'm not utilizing my free will to its fullest extent, so I decided to use it to make my life slightly more whimsical✨.

This is an attempt to create the world's most unnecessarily complex CLI tool for checking if a number is even or odd.

### Architecture (10x Engineering)

- Vision Pipeline: The image is passed through a pre-trained ResNet model to identify the handwritten digit.

- High-Level Logics: Utilizing the cutting-edge `n % 2 == 0` algorithm, the system determines the even/odd nature of the integer.

- Mathematical Poetry: The digit and its mathematical status are dynamically fed into the Gemini 3 Flash API.

- The Output: A completely unhinged ASCII-art mascot delivers 4-line dramatic poem about the revelation.


### Tech Stack
- Python
- Hugging Face Transformers (Vision Classification)
- Google GenAI SDK (LLM generation)
- uv 


### Things to work on

- The ResNet is trained on the standard handwritten dataset, which contains only one number per image, so the model can't identify multiply numbers in the image 
- The ResNet model seems to predict numbers even when there are no numbers in the image. (it thinks cow.jpeg is a 9)
- make the CLI more user friendly

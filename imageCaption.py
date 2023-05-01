from CompleteModels.reuse import speak, capture_image
from model import get_caption_model, generate_caption
import os
def CaptionImage(image_path):
    try:
        speak("Generating caption.....")
        caption_model = get_caption_model()
        captions = []
        pred_caption = generate_caption(image_path, caption_model)
        captions.append(pred_caption)
        speak("Generation complete ..")
        for _ in range(4):
            pred_caption = generate_caption(image_path, caption_model, add_noise=True)
            if pred_caption not in captions:
                captions.append(pred_caption)
        speak("Processing complete. The generated captions are:")
        for c in captions:
            speak(c)
    except FileNotFoundError:
        speak("Error: could not find the vocabulary file.")

path = capture_image()

CaptionImage(path)

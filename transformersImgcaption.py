import os
import shutil
import warnings
import logging
from datetime import datetime
from transformers import pipeline
from CompleteModels.reuse import * 
from PIL import Image
import datetime
from transformers import ViTFeatureExtractor, GPT2LMHeadModel, GPT2Tokenizer


warnings.simplefilter('ignore')
logging.disable(logging.WARNING)


# METHOD ONE COMMENT OUT IF U DONT WANT TO SAVE THE MODELS
def generate_caption(image_path):
    caption_pipeline = pipeline('image-to-text')
    
    try:
        with Image.open(image_path) as image:
            result = caption_pipeline(image)
        return result
    except FileNotFoundError:
        print(f"Error: Image file '{image_path}' not found.")
        return None


# METHOD 2  (STILL IN TEST MODE)

# def generate_caption(image_path, cache_folder='model_cache'):
#     model_folder = os.path.join(cache_folder, 'ViTGPT2')
    
#     # Check if the model files are already present
#     if not os.path.exists(model_folder):
#         os.makedirs(model_folder)
#         image_model = 'google/vit-base-patch16-224-in21k'
#         text_model = 'gpt2'
#         feature_extractor = ViTFeatureExtractor.from_pretrained(image_model, cache_dir=model_folder)
#         model = GPT2LMHeadModel.from_pretrained(text_model, cache_dir=model_folder)
#         tokenizer = GPT2Tokenizer.from_pretrained(text_model, cache_dir=model_folder)
#     else:
#         feature_extractor = ViTFeatureExtractor.from_pretrained(model_folder)
#         model = GPT2LMHeadModel.from_pretrained(model_folder)
#         tokenizer = GPT2Tokenizer.from_pretrained(model_folder)

#     try:
#         with Image.open(image_path) as image:
#             inputs = feature_extractor(images=image, return_tensors="pt")
#             pixel_values = inputs['pixel_values']

#             outputs = model.generate(pixel_values)
#             caption = tokenizer.decode(outputs[0], skip_special_tokens=True)
#             return caption
#     except FileNotFoundError:
#         print(f"Error: Image file '{image_path}' not found.")
#         return None
 
def save_image_and_caption(image_path, caption_text, base_folder='captioned_images'):
    # Create the base folder if it doesn't exist
    if not os.path.exists(base_folder):
        os.mkdir(base_folder)

    # Create a timestamped subfolder
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    subfolder = os.path.join(base_folder, timestamp)
    os.mkdir(subfolder)

    # Save the image in the subfolder
    image_filename = os.path.basename(image_path)
    new_image_path = os.path.join(subfolder, image_filename)
    shutil.copy(image_path, new_image_path)

    # Save the caption as a text file in the subfolder
    text_filename = os.path.splitext(image_filename)[0] + '.txt'
    text_file_path = os.path.join(subfolder, text_filename)
    with open(text_file_path, 'w') as text_file:
        text_file.write(str(caption_text))  # Convert caption_text to string before writing

    print(f"Image and caption saved in folder '{subfolder}'")


# Example usage
image_path =  capture_image()
caption_text = generate_caption(image_path)

if caption_text:
    print("Generated caption:", caption_text)
    save_image_and_caption(image_path, caption_text)

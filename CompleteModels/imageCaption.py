import io
import requests
from PIL import Image

from CompleteModels.reuse import speak
from model import get_caption_model, generate_caption


def get_image_captions(image_path):
    caption_model = get_caption_model()

    captions = []
    pred_caption = generate_caption(image_path, caption_model)

    captions.append(pred_caption)

    for _ in range(4):
        pred_caption = generate_caption(image_path, caption_model, add_noise=True)
        if pred_caption not in captions:
            captions.append(pred_caption)

    return captions


# # Example usage
# img_url = "https://example.com/image.jpg"
#
# img = Image.open(requests.get(img_url, stream=True).raw)
# img = img.convert('RGB')
# img.save('tmp.jpg')
# captions = get_image_captions('tmp.jpg')
captions = get_image_captions('../testimages/96420612_feb18fc6c6.jpg')
speak(captions)

# Output: ['A person standing on a beach with a surfboard', 'A surfer catching a wave', 'A man surfing in the ocean', 'A person riding a wave on a surfboard', 'A man surfing on a board in the ocean']

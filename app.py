# import io
# import os
#
# import streamlit as st
# import requests
# from PIL import Image
# from model import get_caption_model, generate_caption
#
#
# @st.cache_resource(allow_output_mutation=True)
# def get_model():
#     return get_caption_model()
#
# caption_model = get_model()
#
#
# def predict():
#     captions = []
#     pred_caption = generate_caption('tmp.jpg', caption_model)
#
#     st.markdown('#### Predicted Captions:')
#     captions.append(pred_caption)
#
#     for _ in range(4):
#         pred_caption = generate_caption('tmp.jpg', caption_model, add_noise=True)
#         if pred_caption not in captions:
#             captions.append(pred_caption)
#
#     for c in captions:
#         st.write(c)
#
# st.title('Image Captioner')
# img_url = st.text_input(label='Enter Image URL')
#
# if (img_url != "") and (img_url != None):
#     img = Image.open(requests.get(img_url, stream=True).raw)
#     img = img.convert('RGB')
#     st.image(img)
#     img.save('tmp.jpg')
#     predict()
#     os.remove('tmp.jpg')
#
#
# st.markdown('<center style="opacity: 70%">OR</center>', unsafe_allow_html=True)
# img_upload = st.file_uploader(label='Upload Image', type=['jpg', 'png', 'jpeg'])
#
# if img_upload != None:
#     img = img_upload.read()
#     img = Image.open(io.BytesIO(img))
#     img = img.convert('RGB')
#     img.save('tmp.jpg')
#     st.image(img)
#     predict()
#     os.remove('tmp.jpg')

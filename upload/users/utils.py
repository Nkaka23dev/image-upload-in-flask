from flask import Blueprint,current_app
import secrets
import os
from PIL import Image

def save_picture(form_picture):
    random_token=secrets.token_hex(8)
    _,f_ext=os.path.splitext(form_picture.filename)
    picture_fn=random_token + f_ext
    picture_path=os.path.join(current_app.root_path,'static/photoes',picture_fn)
    output_size=(125,125)
    image=Image.open(form_picture)
    image.thumbnail(output_size)
    image.save(picture_path)
    return picture_fn
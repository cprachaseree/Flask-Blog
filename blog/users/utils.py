import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from blog import mail

# function to update profile picture and path
def save_picture(form_picture):
    # pictures are saved as rndomly hexed filenames
    random_hex = secrets.token_hex(8)
    # get the extension of the fform_picture
    _, f_ext = os.path.spilttext(form_picture.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_filename)

    #resize the image to save space and speed up website
    output_size = (125, 125)
    resized_picture = Image.open(form_picture)
    resized_picture.thumbnail(output_size)

    resized_picture.save(picture_path)
    # picture is now at the file system
    return picture_filename

# send email to users who request new password
def send_reset_email(user):
    token = user.get_reset_token()
    message = Message('Password Reset Request', sender='noreply@gmail.com', recipients=[user.email])
    # external=True to get absolute url
    message.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}
If you did not make this request then ignore this email. No changes will be made
'''
    # send the message
    mail.send(message)

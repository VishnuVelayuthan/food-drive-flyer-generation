from PIL import Image, ImageFilter, ImageFont, ImageDraw
from pathlib import Path
import textwrap
import qrcode 

Template_Path = Path("designs", "template.png")



def make_flyer(teacher_name, room_number, donation_link):
    flyer_img = Image.open(Template_Path)

    #qr_img = qr_code_generator(donation_link)


def qr_code_generator(donation_link):
    return qrcode.make(donation_link)

if __name__ == "__main__":
    make_flyer("", "", "",)
    
from PIL import Image, ImageFilter, ImageFont, ImageDraw
from pathlib import Path
import textwrap
import qrcode 

Template_Path = Path("designs", "template.png")

Fonts = {
    "sub-header": ImageFont.truetype("Roboto-Regular.ttf", size=41.1),
    "link": ImageFont.truetype("Roboto-Regular.ttf", size=29.2)
}

def make_flyer(teacher_name, room_number, donation_link):
    """
    creates flyer from template

    @param teacher_name: name of teacher
    @param room_number: room number of teacher
    @param donation_link: link to donation link

    @return img object of flyer
    """

    flyer_img = Image.open(Template_Path)

    #qr_img = qr_code_generator(donation_link)


def qr_code_generator(donation_link):
    return qrcode.make(donation_link)

if __name__ == "__main__":
    make_flyer("", "", "",)
    
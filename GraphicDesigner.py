from PIL import Image, ImageFilter, ImageFont, ImageDraw
from pathlib import Path
import textwrap
import qrcode 

Template_Path = Path("designs", "template.png")

Fonts = {
    "sub-header": ImageFont.truetype("Roboto-Regular.ttf", size=55),
    "link": ImageFont.truetype("Roboto-Regular.ttf", size=40)
}

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=40,
    border=4,
)

def make_flyer(teacher_name, room_name, donation_link):
    """
    creates flyer from template

    @param teacher_name: last name of teacher
    @param room_number: room name of teacher
    @param donation_link: link to donation link

    @return img object of flyer
    """

    flyer_img = Image.open(Template_Path)
    W, H = flyer_img.size

    flyer_editor = ImageDraw.Draw(flyer_img)
    
    sub_header = sub_header_str(teacher_name, room_name)
    sub_height_adj = 610 # trial and error
    # trying to get sub-header aligned with image
    w_sub, h_sub = flyer_editor.textsize(sub_header, font=Fonts["sub-header"])
    flyer_editor.text(((W-w_sub)/2, (H-h_sub-sub_height_adj)/2), \
        sub_header, font=Fonts["sub-header"])

    # QR code placement on the image 
    qr_img = qr_code_generator(donation_link)
    flyer_img.paste(qr_img, (515, 1150)) # found through trial and error

    # putting link in the bottom blue area
    don_height_adj = 1775
    w_don, h_don = flyer_editor.textsize(donation_link, font=Fonts["link"])
    flyer_editor.text(((W-w_don)/2, (H-h_don+don_height_adj)/2), \
        donation_link, font=Fonts["link"], fill=(0,0,0))

    # saving newly generated flyer
    save_path = Path("flyers", teacher_name +"-"+ room_name +".png")
    flyer_img.save(save_path, "PNG")
    
def sub_header_str(teacher_name, room_name): 
    """
    processing the teacher name and room name variables 
    to form a sub_header string

    @param teacher_name: last name of teacher
    @param room_name: room name of teacher

    @return sub_header string to go under title of flyer 
    """
    sub_header = teacher_name + " - "
    
    # in case the room name is not a number like library
    try: 
        int(room_name)
        sub_header += "Room " + room_name
    except ValueError:
        sub_header += room_name
    
    return sub_header

def qr_code_generator(donation_link):
    """
    Makes qr code with correct sizing 

    @param donation_link: link to donation link 

    @return img object of qr code
    """
    qr_img = qrcode.make(donation_link)
    w_qr, h_qr = qr_img.size
    # trial and error
    qr_img = qr_img.crop((0.1*w_qr, 0.1*h_qr, 0.9*w_qr, 0.9*h_qr))
    qr_img = qr_img.resize((700,700))

    return qr_img

#main for debugging and testing
if __name__ == "__main__":
    make_flyer("Ms Woolfolk", "library", "https://impact.shfb.org/teampham-valentukoni",)
    
from PIL import Image


def is_image(file):
    try:
        img = Image.open(file)
        img.verify()  # Additional check to verify the image file integrity
        return True
    except (IOError, SyntaxError):
        return False

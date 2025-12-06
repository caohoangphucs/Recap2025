from PIL import Image
def resize(img, target: tuple[int, int]):
    w, h = img.size
    ratio = min(target[0] / w, target[1] / h)
    new_size = (int(w * ratio), int(h * ratio))
    return img.resize(new_size, Image.LANCZOS)
from dataclasses import dataclass
from datetime import datetime
from PIL import Image
import os
import preprocess as pre

@dataclass
class ImageDetail:
    id: int
    name: str
    size: tuple[int, int]
    date: datetime
    format: str
    path: str


def get_img_list(input_folder_path) -> list[ImageDetail]:
    res = []
    id = 0
    for filename in os.listdir(input_folder_path):
        id += 1
        path = os.path.join(input_folder_path, filename)
        try:
            img = Image.open(path)
        except:
            continue
        time = datetime.fromtimestamp(os.path.getctime(path))
        new_img = ImageDetail(id, filename, img.size, time, img.format, path)
        res.append(new_img)
    res.sort(key=lambda x: x.date)
    return res

def segment(src: list[ImageDetail], nums_pic) -> dict:
    res = {}
    for index in range(len(src)):
        segment_id = index//nums_pic
        if (segment_id not in res):
            res[segment_id] = []
        res[segment_id].append(src[index])
    return res

def render(backgr, segment: dict, size: int, offset: int):
    print(f"Redering image from row {offset}")
    for col in range(offset, len(segment)):
        seg = segment.get(col)
        x = 0
        index = col - offset
        y = index * size
        if (y > backgr._size[1]): break
        for img in seg:
            load = Image.open(img.path)
            image = pre.resize(load, [size, size])
            if load.mode == "RGBA":
                backgr.paste(image, (x, y), image)
            else:
                backgr.paste(image, (x, y))
            x+=size
    return backgr

def merge(row_size: int, col_size: int , width: int, img_path: str, out_path:str):
    w = width
    img_num_in_row = row_size
    img_num_in_col = col_size
    per_page_img = img_num_in_row * img_num_in_col
    size = w//img_num_in_row
    h = size * img_num_in_col

    images = get_img_list(img_path)
    seg = segment(images, img_num_in_row)

    for index in range(len(images) // per_page_img):
        offset = index * img_num_in_col
        backgr = Image.new("RGBA", (w, h), (255,255,255,255))
        canvas = render(backgr, seg, size, offset)
        canvas.save(f"{out_path}/img{index}.png")
        print(f"Merged {index * per_page_img}/{len(images)} images, save to img{index}.png")

merge(5, 3, 1920, "/mnt/c/Users/Phucdeptrai/Pictures/Screenshots", "/home/phucdeptrai/Project/Recap/output")
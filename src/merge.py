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


        

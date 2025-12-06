from img_to_video import *
w = 1920
img_num_in_row = 4
img_num_in_col = 10
per_page_img = img_num_in_row * img_num_in_col
size = w//img_num_in_row
h = size * img_num_in_col

img_folder = "/mnt/c/Users/Phucdeptrai/Pictures/Screenshots"
output_folder = "/home/phucdeptrai/Project/Recap/output"

images = get_img_list(img_folder)

seg = segment(images, img_num_in_row)

for index in range(len(images) // per_page_img):
    offset = index * img_num_in_col
    backgr = Image.new("RGBA", (w, h), (255,255,255,255))
    canvas = render(backgr, seg, size, offset)
    canvas.save(f"{output_folder}/img{index}.png")
    print(f"Merged {index * per_page_img}/{len(images)} images, save to img{index}.png")


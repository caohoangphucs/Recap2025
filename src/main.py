from video import images_to_video
img_folder = "/mnt/c/Users/Phucdeptrai/Pictures/Screenshots"
project = "/home/phucdeptrai/Project/Recap"
output_folder = f"{project}/output"
build = f"{project}/build"
destination_path = f"{build}/output.mp4"
screen_width = 1920
screen_height = 1080
images_to_video(output_folder, destination_path, 10, (screen_width, screen_height))
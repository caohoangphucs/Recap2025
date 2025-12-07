from moviepy import (
    VideoClip,
    VideoFileClip,
    ImageSequenceClip,
    ImageClip,
    TextClip,
    ColorClip,
    AudioFileClip,
    AudioClip,
    vfx, afx,
    CompositeVideoClip,
    concatenate_videoclips
)

import os
folder = "/home/phucdeptrai/Project/Recap/output"
ext = ('.png', '.jpg', '.jpeg', '.bmp')
target = "/home/phucdeptrai/Project/Recap/build"
per_clip_second = 1
fps = 120
images = [
    os.path.join(folder, f)
    for f in sorted(os.listdir(folder))
    if f.lower().endswith(ext)
]

clip_images = [ImageClip(img).with_duration(100) for img in images]
res = []
cnt = 0
for clip in clip_images:
    per_slide = per_clip_second/2
    slide_in = clip.with_start(cnt*per_slide).with_duration(per_slide).with_effects([vfx.SlideIn(per_slide, "bottom")])
    cnt+=1
    slide_out = clip.with_start(cnt*per_slide).with_duration(per_slide).with_effects([vfx.SlideOut(per_slide, "top")])
    res.extend([slide_in, slide_out])

CompositeVideoClip(res).write_videofile("result.mp4", fps = fps)
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
folder = "/home/phucdeptrai/Project/Recap/output/test"
ext = ('.png', '.jpg', '.jpeg', '.bmp')

images = [
    os.path.join(folder, f)
    for f in sorted(os.listdir(folder))
    if f.lower().endswith(ext)
]

clip_images = [ImageClip(img).with_duration(5) for img in images]
slided_video = []
for vd in clip_images:
    vd.preview()
    slided_video.append(CompositeVideoClip(vd.with_effects([vfx.SlideIn(5, 'bottom')])))
 #   slided_video.append(CompositeVideoClip(vd.with_effects([vfx.SlideOut(5, 'top')])))
slided_video[0].preview()
#clips = concatenate_videoclips(slided_video)
#clips.preview()
from moviepy.editor import VideoFileClip, concatenate_videoclips

# Load the two video clips
clip1 = VideoFileClip("video1.mp4")
clip2 = VideoFileClip("video2.mp4")
clip3 = VideoFileClip("video3.mp4")
clip4 = VideoFileClip("video4.mp4")
clip5 = VideoFileClip("video5.mp4")

# Concatenate the clips linearly
final_clip = concatenate_videoclips([clip1, clip2, clip3, clip4,clip5])

# Write the concatenated clip to a new MP4 file
final_clip.write_videofile("result.mp4")
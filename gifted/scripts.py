from moviepy import editor

# converts raw time input to VideoFileClip compatible
def time_convert(time):
    time_converted = float(time[0]) * 60 + float(str(time[1]+'.'+time[2]))
    return time_converted

# basic gif conversion
def gif_convert(video_name, gif_name, resize_factor, start_time, end_time, directory):
	start_float = time_convert(start_time)
	end_float = time_convert(end_time)

	editor.VideoFileClip(directory + video_name).\
                    subclip(start_float, end_float).\
                    resize(resize_factor).\
                    crop(x1=145,x2=400).\
                    to_gif(directory + gif_name)

# adding cropping option
def gif_crop(video_name, gif_name, resize_factor, start_time, end_time, directory, crop_x1, crop_x2, crop_y1, crop_y2):
    start_float = time_convert(start_time)
    end_float = time_convert(end_time)

    first_clip = editor.VideoFileClip(directory + video_name).\
                    subclip(start_float, end_float).\
                    resize(resize_factor)

    # make sure to accept 0 0 coordinates
    if int(crop_x2) == 0:
        crop_x2 = first_clip.w
    if int(crop_y2) == 0:
        crop_y2 = first_clip.h

    if int(crop_x1) < first_clip.w and int(crop_y1) < first_clip.h:
        first_clip.crop(x1=crop_x1,x2=crop_x2,y1=crop_y1,y2=crop_y2).\
            to_gif(directory + gif_name)
    else:
        print 'The coordinates you have put in do not match the video source.'
        raise SystemExit

# anna_olaf = VideoFileClip("./frozen_trailer.mp4").\
#               subclip(87.9,88.1).\
#               speedx(0.5).\ # Play at half speed
#               resize(.4)

# snapshot = anna_olaf.\
#               crop(x2= anna_olaf.w/2).\ # remove right half
#               to_ImageClip(0.2).\ # snapshot of the clip at t=0.2s
#               set_duration(anna_olaf.duration)

# CompositeVideoClip([anna_olaf, snapshot]).\
#     to_gif('anna_olaf.gif', fps=15)

# import moviepy.video.tools.drawing as dw

# anna_kris = VideoFileClip("./frozen_trailer.mp4", audio=False).\
#               subclip((1,38.15),(1,38.5)).\
#               resize(.5)

# # coordinates p1,p2 define the edges of the mask
# mask = dw.color_split(anna_kris.size,
#                       p1=(445, 20), p2=(345, 275),
#                       grad_width=5) # blur the mask's edges

# snapshot = anna_kris.to_ImageClip().\
#                  set_duration(anna_kris.duration).\
#                  set_mask(ImageClip(mask, ismask=True))

# CompositeVideoClip([anna_kris,snapshot]).\
#     speedx(0.2).\
#     to_gif('anna_kris.gif', fps=15, fuzz=3) # fuzz= GIF compression




# def time_symetrize(clip):
#     """ Returns the clip played forwards then backwards. In case
#     you are wondering, vfx (short for Video FX) is loaded by
#     >>> from moviepy.editor import * """
#     return concatenate([clip, clip.fx( vfx.time_mirror )])

# VideoFileClip("./frozen_trailer.mp4", audio=False).\
#           subclip(36.5,36.9).\
#           resize(0.5).\
#           crop(x1=189, x2=433).\
#           fx( time_symetrize ).\
#           to_gif('sven.gif', fps=15, fuzz=2)


# olaf = VideoFileClip("./frozen_trailer.mp4", audio=False).\
#               subclip((1,21.6),(1,22.1)).\
#               resize(.5).\
#               speedx(0.5).\
#               fx( time_symetrize )

# # Many options are available for the text (requires ImageMagick)
# text = TextClip("In my nightmares\nI see rabbits.",
#                 fontsize=30, color='white',
#                 font='Amiri-Bold', interline=-25).\
#             set_pos((20,190)).\
#             set_duration(olaf.duration)

# CompositeVideoClip( [olaf, text] ).\
#     to_gif('olaf.gif', fps=10, fuzz=2)


# castle = VideoFileClip("./frozen_trailer.mp4", audio=False).\
#               subclip(22.8,23.2).\
#               speedx(0.2).\
#               resize(.4)

# d = castle.duration
# castle = castle.crossfadein(d/2)

# CompositeVideoClip([castle,
#                     castle.set_start(d/2),
#                     castle.set_start(d)]).\
#    subclip(d/2, 3*d/2).\
#    to_gif('castle.gif', fps=5,fuzz=5)



# carry = VideoFileClip("../videos/charade.mp4", audio=False).\
#               subclip((1,51,18.3),(1,51,20.6)).\
#               crop(x1=102, y1=2, x2=297, y2=202)

# d = carry.duration
# snapshot = carry.to_ImageClip().\
#                   set_duration(d/6).\
#                   crossfadein(d/6).\
#                   set_start(5*d/6)

# CompositeVideoClip([carry, snapshot]).\
#     to_gif('carry.gif', fps=carry.fps, fuzz=3)
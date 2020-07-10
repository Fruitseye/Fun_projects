from moviepy.editor import VideoFileClip,AudioFileClip,vfx,clips_array
#import moviepy.video.fx.all as vfx
#import os
#direct=os.path.dirname(os.path.abspath(__file__))



def Dark_MODE(clip):
    audio=AudioFileClip("soundtrack.mp3")
    
    clip1=clip
    clip2=clip1.fx(vfx.mirror_x)
    clip3=clip1.fx(vfx.mirror_y)
    clip4=clip2.fx(vfx.mirror_y)


    final_clip=clips_array([[clip1,clip2],[clip3,clip4]])
    if(final_clip.duration>=audio.duration):
        ##Audio loops to video size
        audio = (audio.audio_loop( audio, duration=final_clip.duration).audio_fadeout(2))
        #final_clip=final_clip.subclip(0,dark_audio.duration)
    else:
        ##Audio loops
        audio=(audio.subclip(0,final_clip.duration).audio_fadeout(2))
    
    #audio=audio.fadeout(2)
    final_clip=final_clip.set_audio(audio)
    final_clip.resize(width=480).write_videofile("Dark.mp4")

 
clip=VideoFileClip("test.mp4")

if __name__=="__main__":
    Dark_MODE(clip)

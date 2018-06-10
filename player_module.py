from time import sleep

import pafy
import vlc

YOUTUBE_URL = 'https://www.youtube.com/watch?v=ZWAGn4yyRMM'


def play_video(play_url):
    global player
    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(play_url)
    media.get_mrl()
    player.set_media(media)
    player.play()


def play_media():
    video = pafy.new(YOUTUBE_URL)
    best = video.getbest()
    video_url = best.url
    play_video(play_url=video_url)
    sleep(1)
    player.pause()


def pause_media():
    player.pause()


def resume_media():
    player.set_pause(0)

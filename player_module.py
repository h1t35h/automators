import logging
from random import shuffle
from time import sleep

import pafy
import vlc

YOUTUBE_URLS = [
                'https://www.youtube.com/watch?v=ZWAGn4yyRMM',  # teri meri kahani
                'https://www.youtube.com/watch?v=spBoY7y8IYo',  # toota toota ek parinda
                'https://www.youtube.com/watch?v=pTxZy32Fv_0',  # Bulla ki jana
                'https://www.youtube.com/watch?v=PZvkvigWb9Y',  # Tere bin
                'https://www.youtube.com/watch?v=2228O5t62VQ',  # Yeh dil
                'https://www.youtube.com/watch?v=zpf8hrbT2d0',  # tu kisi rail si
                'https://www.youtube.com/watch?v=8FMz_KT1mC4',  # dua
                'https://www.youtube.com/watch?v=PiJhv5Ic644',  # phir le aaya dil
                'https://www.youtube.com/watch?v=Vk0OI0Ulb6E',  # khamosiyan inkaar
                'https://www.youtube.com/watch?v=1ybUPCdkYvI',  # Saajna
                'https://www.youtube.com/watch?v=dCXBfKs3UI8',  # naa jaane kahan se
                'https://www.youtube.com/watch?v=2Tb6Q1PH-_0',  # Bhool bhulaiya
                'https://www.youtube.com/watch?v=Kt0f9md9-dk',  # Chakna
                'https://www.youtube.com/watch?v=fwtWQxFMfxw',  # Chapa Chapa charkha
                'https://www.youtube.com/watch?v=Y7JRWs9dvVo',  # Chodd aaye hum
                'https://www.youtube.com/watch?v=3uxe_dAKjrM',  # Main koi aisa geet
                'https://www.youtube.com/watch?v=nEnLt3pasxE',  # Neele neele ambar
                'https://www.youtube.com/watch?v=Y4jDso266mc',  # Jab koi baat
                'https://www.youtube.com/watch?v=Ur6Ax6mzzKM',  # Pardesi Pardesi
                'https://www.youtube.com/watch?v=3PmtRjTBcXk',  # Kya hua tera wada
                'https://www.youtube.com/watch?v=Fqd4pOwooQI',   # Dil de diya hai
                'https://www.youtube.com/watch?v=p2pHdf9_zc8'   # Chand Tare
]


def play_video(play_urls):
    global player
    logging.debug("Passed Urls : " + str(play_urls))
    instance = vlc.Instance()
    player = instance.media_list_player_new()
    media_list = instance.media_list_new()
    for url in play_urls:
        media = instance.media_new(url)
        media_list.add_media(media)
    logging.debug('List added...')
    player.set_media_list(media_list)
    logging.debug('Playing...')
    player.play()
    sleep(5)
    # this is to start in paused state
    player.pause()
    logging.debug('Player Ready..')


def play_media():
    video_urls = []
    for vid in YOUTUBE_URLS:
        logging.debug('Processing Url: ' + vid)
        video = pafy.new(vid)
        best = video.getbestaudio()
        video_url = best.url
        # download to temporary directory
        filename = best.download(filepath="/tmp/")
        video_urls.append(filename)

    shuffle(video_urls)
    play_video(play_urls=video_urls)


def pause_media():
    player.pause()


def resume_media():
    player.play()

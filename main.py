import threading
import tkinter as tk
from time import sleep

from dlink_utils import get_connected_devices, MOBILE
from machines.machines import MusicMachine
import logging


class ThreadedApplications:
    """
    Launch threaded applications for automation
    """

    def __init__(self, mw):

        self.music_machine = MusicMachine()

        manual_pause_button = tk.Button(mw, text='Manual Pause', width=15,
                                        command=self.music_machine.manual_pause)
        manual_pause_button.pack()
        manual_resume_button = tk.Button(mw, text='Manual Resume', width=15,
                                         command=self.music_machine.manual_play)
        manual_resume_button.pack()

        logging.debug('Starting Music sync..')
        self.music_thread = threading.Thread(target=self.__start_music)
        self.music_thread.start()

    def __start_music(self):
        while True:
            if is_phone_connected():
                logging.debug("Phone Status: Connected\n\n")
                self.music_machine.mobile_connected()
            else:
                logging.debug("\n\nPhone Status: Disconnected\n\n")
                self.music_machine.mobile_disconnected()
            sleep(5)


def is_phone_connected():
    devices = get_connected_devices()
    devices_dict = dict((device.device_type, device) for device in devices)
    return devices_dict.get(MOBILE) is not None


def __setup_logging():
    logging.basicConfig(filename='application.log', filemode='w', level=logging.DEBUG)


def __setup_gui():
    main_window = tk.Tk(className="Automator")
    main_window.pack_propagate(0)
    return main_window


if __name__ == '__main__':
    __setup_logging()
    gui = __setup_gui()
    apps = ThreadedApplications(gui)
    gui.mainloop()

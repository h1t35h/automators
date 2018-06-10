from time import sleep

from dlink_utils import get_connected_devices, MOBILE
from machines.machines import MusicMachine
import logging


def is_phone_connected():
    devices = get_connected_devices()
    devices_dict = dict((device.device_type, device) for device in devices)
    return devices_dict.get(MOBILE) is not None


def __setup_logging():
    logging.basicConfig(filename='application.log', filemode='w', level=logging.DEBUG)


if __name__ == '__main__':
    __setup_logging()
    music_machine = MusicMachine()
    while True:
        if is_phone_connected():
            logging.debug("Phone Status: Connected")
            music_machine.mobile_connected()
        else:
            logging.debug("Phone Status: Disconnected")
            music_machine.mobile_disconnected()
        sleep(5)

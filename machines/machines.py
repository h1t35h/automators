import logging

from transitions.extensions import LockedMachine as Machine

import player_module
from machines import states, triggers


class MusicMachine(object):
    states = [states.MOBILE_CONNECTED, states.MOBILE_DISCONNECTED, states.PLAYING, states.MANUALLY_PAUSED]

    def __init__(self):
        logging.debug('Initializing System...')
        self.player = player_module
        self.player.play_media()
        logging.debug('VLC player initialized..Setting up machine..')

        self.machine = Machine(model=self, states=MusicMachine.states, initial=states.MOBILE_DISCONNECTED)

        self.machine.add_transition(trigger=triggers.MOBILE_CONNECTED, source=states.MOBILE_DISCONNECTED,
                                    dest=states.MOBILE_CONNECTED, before='trigger_device_connection')

        self.machine.add_transition(trigger=triggers.MOBILE_DISCONNECTED,
                                    source=[states.MOBILE_CONNECTED, states.PLAYING],
                                    dest=states.MOBILE_DISCONNECTED, before='trigger_device_disconnect')

        self.machine.add_transition(trigger=triggers.MOBILE_CONNECTED, source=states.MOBILE_CONNECTED,
                                    dest=states.PLAYING)

        self.machine.add_transition(trigger=triggers.MOBILE_CONNECTED, source=states.PLAYING,
                                    dest=states.PLAYING)

        self.machine.add_transition(trigger=triggers.MOBILE_DISCONNECTED, source=states.MOBILE_DISCONNECTED,
                                    dest=states.MOBILE_DISCONNECTED)

        self.machine.add_transition(trigger=triggers.MOBILE_DISCONNECTED, source=states.MANUALLY_PAUSED,
                                    dest=states.MANUALLY_PAUSED)

        self.machine.add_transition(trigger=triggers.MOBILE_DISCONNECTED, source=states.PLAYING,
                                    dest=states.MOBILE_DISCONNECTED, before='trigger_device_disconnect')

        self.machine.add_transition(trigger=triggers.MANUAL_PLAY, source=MusicMachine.states, dest=states.PLAYING,
                                    before='trigger_device_connection')

        self.machine.add_transition(trigger=triggers.MANUAL_PAUSE, source=MusicMachine.states,
                                    dest=states.MANUALLY_PAUSED, before='trigger_device_disconnect')

        logging.debug('Machine Setup Completed..')

    def trigger_device_connection(self):
        logging.debug('Device Connected..Trigger Resumed..')
        self.player.resume_media()

    def trigger_device_disconnect(self):
        logging.debug('Device Disconnected..Pausing Media..')
        self.player.pause_media()

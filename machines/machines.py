import logging

from transitions import Machine

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

        self.machine.add_transition(trigger=triggers.MOBILE_DISCONNECTED, source=states.MOBILE_CONNECTED,
                                    dest=states.MOBILE_DISCONNECTED, before='trigger_device_disconnect')

        self.machine.add_transition(trigger=triggers.MOBILE_CONNECTED, source=states.MOBILE_CONNECTED,
                                    dest=states.PLAYING)

        self.machine.add_transition(trigger=triggers.MOBILE_CONNECTED, source=states.PLAYING,
                                    dest=states.PLAYING)

        self.machine.add_transition(trigger=triggers.MOBILE_DISCONNECTED, source=states.MOBILE_DISCONNECTED,
                                    dest=states.MOBILE_DISCONNECTED)

        self.machine.add_transition(trigger=triggers.MOBILE_DISCONNECTED, source=states.PLAYING,
                                    dest=states.MOBILE_DISCONNECTED, before='trigger_device_disconnect')

        self.machine.add_transition(trigger=triggers.MANUAL_PAUSE, source=MusicMachine.states,
                                    dest=states.MANUALLY_PAUSED)

        logging.debug('Machine Setup Completed..')

    def trigger_device_connection(self):
        logging.debug('Device Connected..Trigger Resumed..')
        self.player.resume_media()

    def trigger_device_disconnect(self):
        logging.debug('Device Disconnected..Pausing Media..')
        self.player.pause_media()

    def mobile_connected(self):
        logging.debug('Music Machine..Device Connected.. Current State:' + str(self.machine.state))
        self.machine.mobile_connected()
        logging.debug('Music Machine..Device Connected Trigger Completed.. Current State:' + str(self.machine.state))

    def mobile_disconnected(self):
        logging.debug('Music Machine..Device Disconnected.. Current State:' + str(self.machine.state))
        self.machine.mobile_disconnected()
        logging.debug('Music Machine..Device Disconnected Trigger Completed.. Current State:' + str(self.machine.state))

#!/usr/bin/env python3

import json
import subprocess
import re
import sys
from pathlib import Path

from bullet import Bullet, charDef, colors, keyhandler, utils

CONFIG_FILE_PATH = f'{Path.home()}/.config/coco/config.json'
CHOICES_KEY = 'choices'
PROMPT_KEY = 'prompt'
QUIT_KEY = 113  # ASCII value of 'q'


class CloseableBullet(Bullet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @keyhandler.register(QUIT_KEY)
    @keyhandler.register(charDef.ESC_KEY)
    @keyhandler.register(charDef.INTERRUPT_KEY)
    def force_quit(self):
        utils.moveCursorDown(len(self.choices) - self.pos)
        sys.exit()


class ConfigFile:
    def __init__(self, path):
        with open(path) as file:
            configs = json.load(file)

        self.choices = configs[CHOICES_KEY]
        self.prompt = configs[PROMPT_KEY]


def fetch_args():
    return input("Args: ")


def run_shell_command(cmd):
    return subprocess.run(cmd.split(" "))   


if __name__ == '__main__':
    config = ConfigFile(CONFIG_FILE_PATH)

    prompt = config.prompt
    choices = list(config.choices.keys())
    bullet = '> '

    cli = CloseableBullet(prompt=prompt,
                          choices=choices,
                          bullet=bullet,
                          bullet_color=colors.foreground['green'],
                          word_on_switch=colors.bright(
                              colors.foreground['white']),
                          background_on_switch=colors.background['default'],
                          indent=1,
                          shift=1
                          )

    try:
        result = cli.launch()
    except KeyboardInterrupt as e:
        utils.cprint('Aborting...', color=colors.bright(
            colors.foreground['red']))
        cli.force_quit()

    args = sys.argv[1:] if len(sys.argv) > 1 else fetch_args()

    command = config.choices[result].replace('{package}', args)
    run_shell_command(command)

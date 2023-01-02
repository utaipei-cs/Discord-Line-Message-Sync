"""This python file will handle some extra functions."""

import sys

import yaml
from yaml import SafeLoader


def read_config():
    """Read config file.

    Check if config file exists, if not, create one.
    if exists, read config file and return config with dict type.

    :rtype: dict
    """
    try:
        with open('config.yml', 'r', encoding="utf8") as f:
            data = yaml.load(f, Loader=SafeLoader)
            config = {
                'line_channel_secret': data['Line']['channel_secret'],
                'line_channel_access_token': data['Line']['channel_access_token'],
                'line_group_id': data['Line']['group_id'],
                'discord_bot_token': data['Discord']['bot_token'],
                'discord_channel_id': data['Discord']['channel_id'],
                'discord_channel_webhook': data['Discord']['channel_webhook']
            }
            return config
    except FileNotFoundError:
        print("Config file not found, create one by default.\nPlease finish filling config.yml")
        with open('config.yml', 'w', encoding="utf8") as f:
            f.write(
                "Line:\n  channel_access_token: ''\n  channel_secret: ''\n  group_id: ''\n"
                "Discord:\n  bot_token: ''\n channel_id: ''\n  channel_webhook: ''\n")
        sys.exit()
    except (KeyError, TypeError):
        print(
            "An error occurred while reading config.yml, please check if the file is corrected filled.\n"
            "If the problem can't be solved, consider delete config.yml and restart the program.\n")
        sys.exit()


def get_discord_webhook_id():
    """Get discord webhook id.

    :rtype: int
    """
    webhook_url = read_config().get('discord_channel_webhook')
    return int(webhook_url.split('/')[-2])

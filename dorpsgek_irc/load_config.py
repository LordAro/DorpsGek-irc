import os

from dorpsgek_irc import config


class ConfigurationEmpty(Exception):
    """Thrown if the configuration entry remained empty."""


def post_load_config():
    pass


def load_config():
    for key in dir(config):
        # Only accept config entries that start with a capital
        if key[0] < "A" or key[0] > "Z":
            continue

        value = getattr(config, key)

        if key in os.environ:
            value = os.environ[key]

        if isinstance(value, list):
            value = " ".join(value)

        setattr(config, key, value)

    post_load_config()

    for key in dir(config):
        # Only accept config entries that start with a capital
        if key[0] < "A" or key[0] > "Z":
            continue

        if getattr(config, key) is None:
            raise ConfigurationEmpty(key)

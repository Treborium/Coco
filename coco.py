#!/usr/bin/env python3

import click
import json
import os


@click.group()
def cli():
    pass

@cli.command("add", short_help="Add link to a config file")
@click.argument("path", required=True, type=click.Path(resolve_path=True))
@click.argument("name", required=True)
def add_config_file(path, name):
    """Add a link to a config file"""

    config_path = os.path.dirname(os.path.realpath(__file__)) + '/config.json'
    new_entry = {name: path}

    with open(config_path) as f:
        config = json.load(f)

    config.update(new_entry)

    with open(config_path, 'w') as f:
        json.dump(config, f)


@cli.command("rm", short_help="Remove link to a config file")
@click.argument("name", required=True)
def remove_link(name):
    """Remove a link to a config file"""

    config_path = os.path.dirname(os.path.realpath(__file__)) + '/config.json'
    with open(config_path) as f:
        config = json.load(f)
        del config[name]

    with open(config_path, 'w') as f:
        json.dump(config, f)



if __name__ == '__main__':
    cli()

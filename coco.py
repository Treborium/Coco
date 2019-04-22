#!/usr/bin/env python3

import click
import json
import os

import prompt


CONFIG_PATH = os.path.dirname(os.path.realpath(__file__)) + '/config.json'

@click.group()
def cli():
    pass


@cli.command("add", short_help="Add a link")
@click.argument("path", required=True, type=click.Path(resolve_path=True))
@click.argument("name", required=True)
def add_config_file(path, name):
    """Add a link to a config file"""

    new_entry = {name: path}

    with open(CONFIG_PATH) as f:
        config = json.load(f)

    config.update(new_entry)

    with open(CONFIG_PATH, 'w') as f:
        json.dump(config, f)


@cli.command("rm", short_help="Remove a link")
@click.argument("name", required=True)
def remove_link(name):
    """Remove a link to a config file"""

    with open(CONFIG_PATH) as f:
        config = json.load(f)
        del config[name]

    with open(CONFIG_PATH, 'w') as f:
        json.dump(config, f)


@cli.command("ls", short_help="List all links")
def list_links():
    """List all links defined in the config file"""

    with open(CONFIG_PATH) as f:
        config = json.load(f)

    for key, value in config.items():
        print(f"{key} -> {value}")


@cli.command("run", short_help="Run a prompt")
@click.argument("name", required=True)
@click.argument("args", nargs=-1)
def run_prompt(name, args):
    """Run a prompt"""
    
    with open(CONFIG_PATH) as f:
        config = json.load(f)

    prompt.run(config[name], *args)


if __name__ == '__main__':
    cli()

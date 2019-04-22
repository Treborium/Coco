#!/usr/bin/env python3

import click
import json
import os

import prompt

@click.group()
def cli():
    pass


@cli.command("add", short_help="Add a link")
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


@cli.command("rm", short_help="Remove a link")
@click.argument("name", required=True)
def remove_link(name):
    """Remove a link to a config file"""

    config_path = os.path.dirname(os.path.realpath(__file__)) + '/config.json'
    with open(config_path) as f:
        config = json.load(f)
        del config[name]

    with open(config_path, 'w') as f:
        json.dump(config, f)


@cli.command("ls", short_help="List all links")
def list_links():
    """List all links defined in the config file"""

    config_path = os.path.dirname(os.path.realpath(__file__)) + '/config.json'
    with open(config_path) as f:
        config = json.load(f)

    for key, value in config.items():
        print(f"{key} -> {value}")

@cli.command("run", short_help="Run a prompt")
@click.argument("name", required=True)
def run_prompt(name):

    config_path = os.path.dirname(os.path.realpath(__file__)) + '/config.json'
    with open(config_path) as f:
        config = json.load(f)

    prompt.run(config[name])

if __name__ == '__main__':
    cli()

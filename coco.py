#!/usr/bin/env python3

import click
import json
import os

import prompt


CONFIG_PATH = os.path.dirname(os.path.realpath(__file__)) + '/config.json'

@click.group()
def cli():
    pass


@cli.command("add", short_help="Add a prompt")
@click.argument("path", required=True, type=click.Path(resolve_path=True))
@click.argument("name", required=True)
def add_prompt(path, name):
    """Add a prompt"""
    add_config_file(path, name)

    


@cli.command("rm", short_help="Remove a prompt")
@click.argument("name", required=True)
def remove_prompt(name):
    """Remove a prompt"""

    with open(CONFIG_PATH) as f:
        config = json.load(f)
        del config[name]

    with open(CONFIG_PATH, 'w') as f:
        json.dump(config, f)


@cli.command("ls", short_help="List all prompts")
def list_prompts():
    """List all prompts defined in the config file"""

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

@cli.command("new", short_help="Generate a default config file and add it")
@click.argument("path", required=True, type=click.Path(resolve_path=True))
@click.argument("name", required=True)
def new_entry(path, name):
    default_config = {'prompt': "", 'choices': {}}
    with open(path, 'w') as f:
        json.dump(default_config, f)
    
    add_config_file(path, name)
        

def add_config_file(path, name):
    new_entry = {name: path}

    with open(CONFIG_PATH) as f:
        config = json.load(f)

    config.update(new_entry)

    with open(CONFIG_PATH, 'w') as f:
        json.dump(config, f)


if __name__ == '__main__':
    cli()

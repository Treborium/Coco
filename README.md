# COCO

Coco is a tool for collecting commands in an easy and organized way.

<p align="center">
    <img src="https://treborium.github.io/Coco/Resources/coco-preview.svg" alt="Usage of arguments"/>
</p> 


## Installation

Coco is available in [PyPi](https://pypi.org/project/coco-cli/) and can be installed via pip:

```sh
pip install --user coco-cli
```

## Features

- Custom prompts :star2:
- List existing prompts :notebook:
- Add or remove prompts :cactus:
- Easy to remember commands like `ls` for listing or `rm` for removing :bulb:

## Usage

```sh
Usage: coco [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  add  Add a prompt
  ls   List all prompts
  new  Generate a default config file
  rm   Remove a prompt
  run  Run a prompt

```

### Generate config files

To generate a new config file and simultaneously add the prompt you can simply use the command 

```sh
coco new [PATH] [NAME]
```

Where `[PATH]` specifies the destination of the config file and `[NAME]` the name of the prompt that coco saves.

For example `coco new ~/.config/coco/maven.json mvn` will generate a file named `maven.json` in `~/.config/coco`, which can be executed with `coco run mvn`.

Note that the name of the config file as well as the file extension do _not_ matter.
However since coco expects valid json it is a nice convention to use the `.json` extension.

### Add prompt

If you've already created a valid config file with your desired commands you can add it via

```sh
coco add [PATH] [NAME]
```

Where `[PATH]` specifies the location of the config file and `[NAME]` the name of the prompt that coco saves.

See [Generate Config File](#generate-config-files) for a more detailed example.

### Run a prompt

In order to view an added prompt simply enter

```sh
coco run [NAME]
```

If the prompt requires parameters you can either append them at the end or let coco ask the user for input:

 <p align="center">
    <img src="https://treborium.github.io/Coco/Resources/argument-usage.svg" alt="Usage of arguments"/>
  </p> 


And a possible config file entry could look like this

```json
{
    "prompt": "Select command to run:",
    "choices": {
        "Show package details": "pip show {package}",
        ...
    }
}
```

### List available prompts

To list available prompts use

```sh
coco ls
```

### Remove a prompt

Removing an existing prompt is as easy as using:

```sh
coco rm [NAME]
```

`[Name]` of course specifies the name of the prompt that you wish to remove.
To list the names of all available prompts use `coco ls`.

If you wish to also delete the associated config file from your system add the `--delete-config` flag:

```sh
coco rm --delete-config [NAME]
```

## Config Files

An example config file can be viewed [here](https://github.com/Treborium/Coco/blob/master/coco/coco.json)

As you can probably guess the file needs to be valid json, however the file extension does _not_ matter.

If you want to specify arguments for your commands you can do so by wrapping them in curly braces:

```json
{
    "prompt": "Pacman commands:",
    "choices": {
        "install": "sudo pacman -S {package}"
    }
}
```

---

## TODO

- [ ] Support for piped operations
- [ ] Usage of the same argument in multiple places like `pip search {package} | grep {package}`
- [ ] Add new command to easily edit the config files

#!/usr/bin/sh

pip uninstall coco
rm -rf build coco_cli.egg-info
python3 setup.py sdist bdist_wheel
pip install dist/coco-cli-2.2.tar.gz
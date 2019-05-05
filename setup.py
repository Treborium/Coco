import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="coco-cli",
    version="2.2",
    author="Robert Fuchs",
    author_email="RobertFuchs97@gmail.com",
    description="A CLI tool for managing your CLI tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Treborium/Coco",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': ['coco=coco.coco:cli'],
    },
    install_requires=[
        'bullet',
        'click'
    ],
    package_data={
        'coco': ['database.json', 'coco.json']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

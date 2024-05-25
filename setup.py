from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup (
    name='colorpaletteconverter',
    version='0.3.1',
    description='Make a MacOS Color palette from Python',
    py_modules=["colorpaletteconverter"],
    package_dir={'': 'src'},
    author="Rutger Berns",
    author_email="rutgerb0000@gmail.com",
    url="https://github.com/Rutger0000/colorpalette-converter",
    classifiers=[
        "Environment :: MacOS X",
        "Environment :: MacOS X :: Cocoa",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Topic :: Multimedia"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "pyobjc-core ~= 10.2",
        "pyobjc-framework-Cocoa ~= 10.2"
    ],
    extras_require = {
        "dev": [
            "pytest>=5.2"
        ]
    }
)
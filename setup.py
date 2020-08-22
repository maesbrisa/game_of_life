import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="game_of_life",
    version="1.0.0",
    author_email="11432396+maesbrisa@users.noreply.github.com",
    desciption="Python Game of Life implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maesbrisa/game_of_life",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
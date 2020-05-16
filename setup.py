import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="workpathapi",
    version="0.0.1",
    author="Daniel Hafner",  # add yourself here setuptools
    author_email="daniel-hafner1@gmx.de",
    description="Package to interact with workpathapi API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dataatelier/workpath-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8.3",  # more will be added
        "License :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.8.2"  # more to come
)

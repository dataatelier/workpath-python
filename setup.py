import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="workpathapi",
    version="1.0.0",
    author="Daniel Hafner",
    author_email="daniel-hafner1@gmx.de",
    description="Package to interact with workpath API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dataatelier/workpath-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=2.7"
)

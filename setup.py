import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dsfun",
    version="0.0.1",
    author="Dawid Dabkowski",
    author_email="dav.dabkowski@gmail.com",
    description="Helpful functions for Data Science",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DawidDabkowski/dsfun",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)

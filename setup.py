import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dsfun",
    version="0.0.4",
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

    install_requires=[
        'tensorflow>=2.2.0',
        'pytest>=5.4.2'
    ],
    
    extras_require={
        'developing': [
            'twine>=3.1.1',
            'jupyterlab>=2.1.3',
            'ipdb>=0.13.2'
        ],
    },
    
    python_requires='>=3.8',
)

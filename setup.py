from setuptools import setup, find_packages


VERSION = '0.0.5'
DESCRIPTION = 'ezWrite to files package!'
LONG_DESCRIPTION = 'A simple package that lets you write faster to files! Watch the whole documentation at https://github.com/BeereMgM/ezWrite'

# Setting up
setup(
    name="ezWrite",
    version=VERSION,
    author="Beere",
    author_email="<beere.business@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['cryptography'],
    keywords=['python', 'write', 'File', 'ezWrite', 'read', 'delete'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
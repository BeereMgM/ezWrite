from setuptools import setup, find_packages


VERSION = '0.0.1'
DESCRIPTION = 'ezWrite to files package!'
LONG_DESCRIPTION = 'A simple package that lets you write faster to files!'

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
        "Development Status :: 1 - Releasing",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
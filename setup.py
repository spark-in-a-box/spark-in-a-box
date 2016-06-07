from setuptools import setup
from sparkinabox import __author__, __version__

setup(
    name="sparkinabox",
    version=__version__,
    packages=["sparkinabox"],
    url="https://github.com/zero323/spark-in-a-box",
    license="MIT",
    author=__author__,
    author_email="",
    description="A simple Apache Spark image generator.",
    install_requires=["jinja2", "requests"],
    scripts=[],
    package_data={"": ["templates/*"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Topic :: System :: Installation/Setup",
        "Topic :: Utilities",
    ],
)

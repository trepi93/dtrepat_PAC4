"""Setup configuration for the dtrepat_PAC4 package."""

from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="dtrepat_PAC4",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "astroid==3.3.8",
        "colorama==0.4.6",
        "contourpy==1.3.0",
        "coverage==7.6.10",
        "cycler==0.12.1",
        "dill==0.3.9",
        "Faker==33.3.1",
        "fonttools==4.55.3",
        "importlib_resources==6.5.2",
        "isort==5.13.2",
        "kiwisolver==1.4.7",
        "matplotlib==3.9.4",
        "mccabe==0.7.0",
        "numpy==2.0.2",
        "packaging==24.2",
        "pandas==2.2.3",
        "pillow==11.1.0",
        "platformdirs==4.3.6",
        "pylint==3.3.3",
        "pyparsing==3.2.1",
        "python-dateutil==2.9.0.post0",
        "pytz==2024.2",
        "six==1.17.0",
        "tomli==2.2.1",
        "tomlkit==0.13.2",
        "typing_extensions==4.12.2",
        "tzdata==2024.2",
        "zipp==3.21.0",
    ],
    entry_points={
        'console_scripts': [
            'dtrepat_pac4 = dtrepat_PAC4.main:main',
        ],
    },
    author="David Trepat Segura",
    author_email="dtrepat@uoc.edu",
    description="PAC 4 de l'assignatura de Programació per a la ciència"
                "de dades de la UOC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trepi93/dtrepat_PAC4",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)


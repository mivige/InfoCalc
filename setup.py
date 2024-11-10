from setuptools import setup, find_packages

setup(
    name="InfoCalc",
    version="1.0",
    description="Calcolatrice interattiva per calcoli di entropia, lunghezza media e efficienza.",
    packages=find_packages(),
    install_requires=[
        "tkinter",
    ],
    entry_points={
        'console_scripts': [
            'infocalc=src.main:main',
        ],
    },
)
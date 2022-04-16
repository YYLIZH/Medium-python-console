from setuptools import setup

setup(
    name="test",
    version="0.0.1",
    packages=["say_hello"],
    entry_points={
        "console_scripts": [
            "hello = say_hello.greeting:main",  # command = package.module.function
        ],
    },
)

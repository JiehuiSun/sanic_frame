# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(
    name="sanic-frame",
    version="0.0.4",
    author="huihui",
    author_email="sunjiehuimail@foxmail.com",
    description="Sanic Frame: Sanic + Blueprint + MongoDB",
    url="https://github.com/JiehuiSun/sanic_frame.git",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "sanic==22.3.0",
        "sanic-motor==0.6.0",
        "pymongo==3.12.3"
    ],
    python_requires=">=3.9"
)

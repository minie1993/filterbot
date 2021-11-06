#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = "7644726"

API_HASH = "34fd782b98a00998b99b4dabfc4f0a37"

BOT_TOKEN = "2117944975:AAGeJ53z1rAenOZnAfF9T9hxPiw-0_UUrWM"

DB_URI = "mongodb+srv://Aim:aim97@cluster0.zc1ap.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

USER_SESSION = "BQCaJPmS3eGU4qcj4PH8FAHuPLYxLAKvRg73ptd8Cy9G4GHJwSZLqzTUyRdRN805L_8U5ArmnNWaN07UP6VmY3VqW9o8oa7znH8gavq4PGZIR55Kul9sxABTZAtjbJ0TRmNh-q0adrglBbRNf7ZhC6gnyc2aZ5ZjnAyIeXa6QQYz4nE3QuMN2vv-IyS8KUPNdHSJWrp4FxLY8HuWUbZhcPr2bwBWusKPy6QKzBEWt2wmd4Zs5fBSpedconTweiVQcTt96oGuufnjnkoQfN2Dyb9Fvik6Zg3qq3G5kjsLg5DL5NUTfiLcl4tHJ1k_27tN78u4N6hzo69LKyRC7k7gwPDWE8GQLwA"

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

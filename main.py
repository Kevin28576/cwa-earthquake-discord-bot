import json
import os
import random

import requests
from discord.ext import commands, tasks
from dotenv import load_dotenv

import discord
from earthquake import *

load_dotenv()
bot = commands.Bot(intents=discord.Intents.all() , command_prefix= "---" , description='地震報告系統!')

data = sets(
    os.getenv("token"), APIToken=os.getenv("APIToken"),
    channels=os.getenv("channels", "")
)


def setup():
    try:
        open(data.checkFile)
    except:
        with open(data.checkFile, "w") as outfile:
            json.dump({}, outfile, ensure_ascii=False, indent=4)
            print("建立 check.json 完成")

@bot.event
async def on_ready():
    try:
        print(f'{bot.user.name} | 查看終端\n')
        print("-"*15)
        print('\n目前登入身份:',bot.user, 'ID:',bot.user.id)
        print("-"*20)
        setup()
        earthquake.start()
        print("\n地震報告已啟動")
    except RuntimeError:
        pass

@tasks.loop(seconds=15)
async def earthquake():
    try:
        print('抓取資料中...')
        # 大型地震
        API = f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0015-001?Authorization={data.APIToken}&format=JSON&areaName="
        # 小型地震
        API2 = f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0016-001?Authorization={data.APIToken}&format=JSON"

        try:
            b = requests.get(API).json()
            s = requests.get(API2).json()
            print('抓取資料成功!')
            _API = b["records"]["Earthquake"][0]["EarthquakeInfo"]["OriginTime"]
            _API2 = s["records"]["Earthquake"][0]["EarthquakeInfo"]["OriginTime"]

            async def goTo(how, now):
                for ch in data.channels:
                    await sosIn(bot.get_channel(ch), ({API: b, API2: s}[how]), data)
                with open(data.checkFile, 'w') as outfile:
                    json.dump(now, outfile, ensure_ascii=False, indent=4)

            with open(data.checkFile, "r") as file:
                file = json.load(file)
            for i in [API, API2]:
                if not file.get(i):
                    file[i] = ""
            if file[API] != _API:
                file[API] = _API
                print('發送 API 資料。')
                await goTo(API, file)
            if file[API2] != _API2:
                file[API2] = _API2
                print('發送 API 2 資料。')
                await goTo(API2, file)
        except requests.exceptions.RequestException as e:
            print(f"請求錯誤: {e}")
            return
        except ValueError as e:
            print(f"JSON解碼錯誤: {e}")
            return

    except RuntimeError:
        pass
bot.run(data.token)

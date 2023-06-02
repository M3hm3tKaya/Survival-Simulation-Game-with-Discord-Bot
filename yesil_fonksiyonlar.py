import random
import asyncio
import discord
from discord.ext import commands, tasks


def embed_baslik(saatStr,dakikaStr,day,mutluluk,temizlik,hungry,money,color):
    discord.Embed(
        title=f"**{saatStr} : {dakikaStr}         GÜN {day}           PARA : {money}\nMUTLULUK : {mutluluk}        TEMİZLİK : {temizlik}       AÇLIK : {hungry}**",
        colour=color, url="https://www.com")




import discord
from discord.ext import commands, tasks
import random
import time
import ast
import asyncio

intents = discord.Intents(messages=True, guilds=True, reactions=True, presences=True, members=True)
Bot = commands.Bot(command_prefix="-", intents=intents)

@Bot.event
async def on_ready():
    print("ben hazırım")
    await Bot.change_presence(activity=discord.Game(name="Mehmet <3"))
@Bot.event
async def on_message(message):
    await Bot.process_commands(message)
@Bot.event
async def on_member_join(member):
    liste = ["Hoşgeldin Bro"]
    secim = random.choice(liste)
    channel = discord.utils.get(member.guild.text_channels, name="giriş-çıkış")
    await member.add_roles(discord.utils.get(member.guild.roles, name="Kayıtsız"))
    await channel.send(f"{member.mention} {secim}")
    print(f"{member} Hoşgeldiniz")



@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="giriş-çıkış")
    await channel.send(f"{member.mention} Veda etti :(")
    print(f"{member} Veda etti :(")

@Bot.command(brief="-help kayıt",description=" cinsiyet : verilcek rolü etiketleyin\n member : adı değiştirilcek kişiyi etiketleyin\n isim : yeni verilcek ismi TAG'lı şekilde yazın\n yaş : yaşını yazın")
@commands.has_role(860915097971195945)
async def kayıt(ctx,cinsiyet:discord.Role,member : discord.Member,isim,yas):

    await member.add_roles(cinsiyet)
    await member.edit(nick=f"{isim} {yas}")
    await ctx.send(f"nick'in güncellendi bro {member.mention}")
    role = discord.utils.get(ctx.guild.roles, name='isim')
    await ctx.send(f"{member.mention} {role.mention}  rolün silinmiştir")
    await member.remove_roles(role)

@Bot.command()
async def avatar(ctx, member: discord.User):
    await ctx.send(member.avatar_url)


Bot.run("ODYxOTI2MjAyMjY5MTA2MTg2.YOQ5VA.gDYHdbBD2T2v1cmFwTotO9ps3aM")
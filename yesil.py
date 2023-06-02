import asyncio
import discord
from discord.ext import commands, tasks
import random
import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from environments import *
import json
import pickle
import instaloader
import os
intents = discord.Intents(messages=True, guilds=True, reactions=True, presences=True, members=True)
Bot = commands.Bot(command_prefix="-", intents=intents)



market = "https://cdn.discordapp.com/attachments/901157476932661308/941682063352922122/IMG_0298.png"



@Bot.event
async def on_ready():
    print("ben hazırım")



@Bot.event
async def on_message(message):
    await Bot.process_commands(message)
    mesaj = message.content
    mesaj = mesaj.lower()
    if mesaj == "bugün ne yesem":
        await message.channel.send("Browni")
    if message.content.startswith("Amin") or message.content.startswith("amin") or message.content.startswith("AMİN"):
        await message.channel.send(":palms_up_together:")

@Bot.command()
async def merhaba(ctx):
    await ctx.send(f"{ctx.message.author.mention} Selam")

@Bot.command()
async def profil(ctx,x):
    x = str(x)
    ig =instaloader.Instaloader()
    ig.download_profile(f"{x}",profile_pic_only=True)
    with os.scandir("bmellikke") as tarama:
        for belge in tarama:
            if belge.name.endswith("jpg"):
                print(belge.name)
                name = belge.name
                await ctx.send(file=discord.File(f'{x}/{name}'))



@Bot.command()
async def çikolata_seç(ctx):
    browni = ["https://cdn.discordapp.com/attachments/901157493126881290/934119674390650940/IMG_0221.PNG","Browni"]
    canga = ["https://cdn.discordapp.com/attachments/901157493126881290/934119369196331008/IMG_0222.PNG","Canga"]
    karam = ["https://cdn.discordapp.com/attachments/901157493126881290/934119371285086268/IMG_0224.PNG","Karam"]
    caramio = ["https://cdn.discordapp.com/attachments/901157493126881290/934119359570407434/IMG_0223.PNG","Caramio"]
    cokonat = ["https://cdn.discordapp.com/attachments/901157493126881290/934119372811808828/IMG_0225.PNG","Çokonat"]
    u_c_gofret = ["https://cdn.discordapp.com/attachments/901157493126881290/934119368240021574/IMG_0226.PNG","Ülker Çikolatalı Gofret"]


    gif1 = "https://cdn.discordapp.com/attachments/901157493126881290/934122591252271154/88066A87-5836-4888-AB82-B2DF87E3E80C.gif"
    gif2 = "https://cdn.discordapp.com/attachments/901157493126881290/934122627608502272/328E9FC7-653E-4E81-B0DD-B5894CACF618.gif"
    gif3 = "https://cdn.discordapp.com/attachments/901157493126881290/934122662924525658/BDFDC5BC-4D2B-4E14-A5E1-F7B087A40152.gif"
    gif4 = "https://cdn.discordapp.com/attachments/901157493126881290/934122668586831952/8D3EDBBF-2C7C-4FCD-85F7-CF701EDC180D.gif"

    liste = [browni,canga,karam,caramio,cokonat,u_c_gofret]

    secim = random.choice(liste)

    embed = discord.Embed(title="Çikolata seçiliyor",description="",colour=discord.Colour.from_rgb(10,200,120))
    embed.set_image(url = gif1)
    msg = await ctx.send(embed=embed)
    await asyncio.sleep(1)

    embed.set_image(url = gif2)
    await msg.edit(embed=embed)
    await asyncio.sleep(1)

    embed.set_image(url = gif3)
    await msg.edit(embed=embed)
    await asyncio.sleep(1)

    embed.set_image(url = gif4)
    await msg.edit(embed=embed)
    await asyncio.sleep(3)

    embed = discord.Embed(title=f"Çikolatanız **{secim[1]}**",colour=discord.Colour.from_rgb(10, 200, 120))
    embed.set_image(url=secim[0])
    await msg.edit(embed=embed)


@Bot.command()
async def minyon(ctx):
    im1 = "https://cdn.discordapp.com/attachments/901157493126881290/934783611390033940/Adsz_Resim.png"
    im2 = "https://cdn.discordapp.com/attachments/901157493126881290/934783713814925352/Adsz_Resim.png"
    im3 = "https://cdn.discordapp.com/attachments/901157493126881290/934783781397753886/Adsz_Resim.png"
    im4 = "https://cdn.discordapp.com/attachments/901157493126881290/934783880672722964/Adsz_Resim.png"

    imListe = [im1,im2,im3,im4]

    boyut = 0


    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    embed = discord.Embed(title="Minyon",colour=discord.Colour.from_rgb(10, 200, 120))
    field = embed.add_field(name="Boyut",value=f"{boyut+1}")
    embed.set_image(url=imListe[boyut])

    msgEmbed = await ctx.send(embed=embed)
    uyari = 0
    while True:
        msg = await Bot.wait_for("message", check=check)
        if uyari:
            await msgUyari.delete()
            uyari = 0

        if msg.content == "besle":
            if boyut < 3:
                boyut+=1
                field.set_field_at(0,name="Boyut",value=f"{boyut+1}")
                embed.set_image(url=imListe[boyut])
                await msgEmbed.edit(embed=embed)
                await msg.delete()
            else:

                msgUyari = await ctx.send("Maksimum boyuta ulaşıldı...")
                uyari = 1

        if msg.content == "aç bırak":
            if boyut > 0:
                boyut-=1
                field.set_field_at(0,name="Boyut",value=f"{boyut+1}")
                embed.set_image(url=imListe[boyut])
                await msgEmbed.edit(embed=embed)
                await msg.delete()
            else:

                msgUyari = await ctx.send("Minimum boyuta ulaşıldı...")
                uyari = 1

        if msg.content == "çıkış":
            await ctx.send("Oyundan çıkıldı...")
            break


global saatStr,dakikaStr,day,mutluluk,temizlik,hungry,money,dakika,saat,g,dilenme_sansi,envanter
charName = ""

@Bot.command(aliases=["yeşil","yesil","yesilhayat","Yeşil","Yesil","Yeşil_Hayat","Yeşil_hayat","yeşil_hayat"])
async def Green_Life(ctx):
    global saatStr
    global dakikaStr
    global day
    global mutluluk
    global temizlik
    global hungry
    global money
    global color
    global dakika
    global saat
    global g
    global charName
    global life
    global dilenme_sansi
    global envanter

    def check(msg):
        return ctx.author == msg.author and ctx.channel == msg.channel
    if charName != "":
        embed = discord.Embed(title="Yeşil Hayat ' a Hoşgeldin",
                              description=f"' {charName} ' kaydından devam etmek istiyorsanız 'devam' yazın\n yeni kayıt için 'yeni' yazın ",
                              colour=color)
        await ctx.send(embed=embed)
        msg = await Bot.wait_for("message", check=check)
        msg1 = msg.content
    else:
        msg1 = "yeni"
    if msg1 == "yeni":

        g = 0

        color = discord.Colour.from_rgb(0,g,0)


        life = 1
        embed = discord.Embed(title="Yeşil Hayat ' a Hoşgeldin",description="Hayatta kalmak için önce bir isminiz olmalı.\nİsminizi giriniz . . .",colour=color)
        await ctx.send(embed=embed)
        msg = await Bot.wait_for("message",check=check)
        charName = msg.content

        embed = discord.Embed(title=f"Adınız : **{charName}**",description="Başlamak için herhangi bir mesaj yollayın",colour=color)
        await ctx.send(embed=embed)

        msg = await Bot.wait_for("message",check=check)





        konum0_saat = 0
        konum1_saat = 1
        konum2_saat = 3
        konum_saat = [konum0_saat,konum1_saat,konum2_saat]

        day = 1
        money = 0
        mutluluk = 100
        temizlik = 100
        hungry = 100

        dilenme_sansi = 20


        saat = 8
        dakika = 0

        saatStr = ""
        dakikaStr = ""


    elif msg1 == "devam":
        await ctx.send(f"{charName} Hoşgeldin")
    else:
        life = 0
    def saatString(saat):
        if saat < 10:
            return f"0{saat}"

        else:
            return saat

    def dakikaString(dakika):
        if dakika < 10:
            return f"0{dakika}"

        else:
            return dakika

    def embed_baslik(saatStr, dakikaStr, day, mutluluk, temizlik, hungry, money, color):
        return discord.Embed(
            title=f"**{saatStr} : {dakikaStr}         GÜN {day}           PARA : {money}\nMUTLULUK : {mutluluk}        TEMİZLİK : {temizlik}       AÇLIK : {hungry}**",
            colour=color, url="https://www.com")




    thumb1 = "https://cdn.discordapp.com/attachments/901157476932661308/941750743751335946/Adsz_Resim.png"
    thumb2 = "https://cdn.discordapp.com/attachments/901157476932661308/941750806166794240/Adsz_Resim.png"
    thumb3 = "https://cdn.discordapp.com/attachments/901157476932661308/941750868666118164/Adsz_Resim.png"
    thumb4 = "https://cdn.discordapp.com/attachments/901157476932661308/941751068109459466/Adsz_Resim.png"
    thumb5 = "https://cdn.discordapp.com/attachments/901157476932661308/941751287521898516/Adsz_Resim.png"
    thumb6 = "https://cdn.discordapp.com/attachments/901157476932661308/941751384620032060/Adsz_Resim.png"
    thumb7 = "https://cdn.discordapp.com/attachments/901157476932661308/941751444707635290/Adsz_Resim.png"
    thumb8 = "https://cdn.discordapp.com/attachments/901157476932661308/941751704179855460/Adsz_Resim.png"
    thumb9 = "https://cdn.discordapp.com/attachments/901157476932661308/941751820387221544/Adsz_Resim.png"
    thumb10 = "https://cdn.discordapp.com/attachments/901157476932661308/941751882089648189/Adsz_Resim.png"
    thumb11 = "https://cdn.discordapp.com/attachments/901157476932661308/941751936112275456/Adsz_Resim.png"
    thumb12 = "https://cdn.discordapp.com/attachments/901157476932661308/941750674339799150/Adsz_Resim.png"
    thumbs = [thumb1,thumb2,thumb3,thumb4,thumb5,thumb6,thumb7,thumb8,thumb9,thumb10,thumb11,thumb12]

    def saat_thumbs(saat):
        if 2 > saat >= 1 or 14 > saat >= 13:
            secili_thumb = thumbs[0]
            return secili_thumb
        if 3 > saat >= 2 or 15 > saat >= 14:
            secili_thumb = thumbs[1]
            return secili_thumb
        if 4 > saat >= 3 or 16 > saat >= 15:
            secili_thumb = thumbs[2]
            return secili_thumb
        if 5 > saat >= 4 or 17 > saat >= 16:
            secili_thumb = thumbs[3]
            return secili_thumb
        if 6 > saat >= 5 or 18 > saat >= 17:
            secili_thumb = thumbs[4]
            return secili_thumb
        if 7 > saat >= 6 or 19 > saat >= 18:
            secili_thumb = thumbs[5]
            return secili_thumb
        if 8 > saat >= 7 or 20 > saat >= 19:
            secili_thumb = thumbs[6]
            return secili_thumb
        if 9 > saat >= 8 or 21 > saat >= 20:
            secili_thumb = thumbs[7]
            return secili_thumb
        if 10 > saat >= 9 or 22 > saat >= 21:
            secili_thumb = thumbs[8]
            return secili_thumb
        if 11 > saat >= 10 or 23 > saat >= 22:
            secili_thumb = thumbs[9]
            return secili_thumb
        if 12 > saat >= 11 or 24 > saat >= 23:
            secili_thumb = thumbs[10]
            return secili_thumb
        if 13 > saat >= 12:
            secili_thumb = thumbs[11]
            return secili_thumb


    suList = []
    BrowniList = []
    laysList = []
    sodaList = []

    envanter = [suList,BrowniList,laysList,sodaList]
    while life:

        if saat >= 23:
            day += 1
            g += 5

            saat = 8
            dakika = 0
            saatStr = ""
            dakikaStr = ""

        if dakika >= 60:
            saat += 1
            dakika = dakika - 60

        if g > 255:
            g = 255
        color = discord.Colour.from_rgb(0, g, 0)
        print(g)



        saatStr = saatString(saat)
        dakikaStr = dakikaString(dakika)



        embed = embed_baslik(saatStr, dakikaStr, day, mutluluk, temizlik, hungry, money, color)
        embed.add_field(name=f"**Eylemler**",
                        value="1 - Dilenmeye Başla\n2 - Dinlen\n3 - Envanteri Aç\n4 - Market'e git\n5 - Çıkış",inline=True)
        embed.add_field(name=f"**Değerler**",
                        value=f"Mutluluk : {mutluluk}\nTemizlik : {temizlik}\nAçlık : {hungry}", inline=True)
        embed.set_thumbnail(url=saat_thumbs(saat))
        await ctx.send(embed=embed)

        msg2 = await Bot.wait_for("message",check=check)

        ####################################################################################################
        ###################################### D I L E N M E ###############################################

        async def dilenme_fonk(range1 : 1,range2 ,range3 : 1):
            global saatStr
            global dakikaStr
            global day
            global mutluluk
            global temizlik
            global hungry
            global money
            global color
            global dakika
            global saat
            global g

            hungry_sayac = 0
            temizlik_sayac = 0
            mutluluk_sayac = 0
            kazanilan_para = 0
            kazanilan_toplam_para = 0
            kazanilan_para_cumle = ""

            embed = embed_baslik(saatStr, dakikaStr, day, mutluluk, temizlik, hungry, money, color)
            embed.add_field(name=f"Dileniyorsun . . .",
                            value="*\n", inline=False)
            embed.add_field(name="Kazanılan toplam para ", value=f" {kazanilan_para} ", inline=False)
            embed.set_thumbnail(url=saat_thumbs(saat))
            dilenmek = await ctx.send(embed=embed)

            for x in range(range1,range2,range3):
                hungry_sayac += range3
                temizlik_sayac += range3
                if hungry_sayac >= 10:
                    hungry -= 1
                    hungry_sayac = 0
                    if hungry <= 0:
                        hungry = 0
                if temizlik_sayac >= 15:
                    temizlik -= 1
                    temizlik_sayac = 0
                    if temizlik <= 0:
                        temizlik = 0

                await asyncio.sleep(1)
                dakika += range3

                if saat >= 23:

                    day += 1
                    g += 5

                    saat = 8
                    dakika = 0
                    saatStr = ""
                    dakikaStr = ""
                    saatStr = saatString(saat)
                    dakikaStr = dakikaString(dakika)
                    break
                if dakika >= 60:
                    saat += 1
                    dakika = dakika - 60

                saatStr = saatString(saat)
                dakikaStr = dakikaString(dakika)

                lucky_money = random.randint(1, dilenme_sansi//range3)
                if lucky_money == 1:
                    kazanilan_para = random.randint(10, 15)
                elif 1 < lucky_money <= 4:
                    kazanilan_para = random.randint(5, 6)
                elif 4 < lucky_money <= 9:
                    kazanilan_para = random.randint(2, 3)
                elif 9 < lucky_money < 20:
                    kazanilan_para = random.randint(1, 2)
                else:
                    kazanilan_para = 0

                kazanilan_toplam_para += kazanilan_para
                money += kazanilan_para

                if kazanilan_para != 0:
                    mutluluk += kazanilan_para * 2
                    if mutluluk >= 100:
                        mutluluk = 100
                    kazanilan_para_cumle += f" {kazanilan_para} :dollar: \n"
                else:
                    mutluluk_sayac += range3
                    if mutluluk_sayac >= 4:
                        mutluluk_sayac = 0
                        mutluluk -= 1
                        if mutluluk <= 0:
                            mutluluk = 0

                embed = embed_baslik(saatStr, dakikaStr, day, mutluluk, temizlik, hungry, money, color)
                embed.add_field(name=f"Dileniyorsun . . .",
                                value="*\n", inline=False)
                embed.add_field(name="Kazanılan Para", value=f" -:dollar:-\n\n{kazanilan_para_cumle} ", inline=False)
                embed.add_field(name="Kazanılan Toplam Para", value=f" {kazanilan_toplam_para}  :dollar:\n",
                                inline=False)
                embed.set_thumbnail(url=saat_thumbs(saat))
                await dilenmek.edit(embed=embed)

            embed = embed_baslik(saatStr, dakikaStr, day, mutluluk, temizlik, hungry, money, color)
            embed.add_field(name=f"{range2} Dakika Boyunca Dilendin.",
                            value="*\n", inline=False)
            embed.add_field(name="Kazanılan toplam para ", value=f" {kazanilan_toplam_para} :dollar:", inline=False)
            embed.set_thumbnail(url=saat_thumbs(saat))
            await ctx.send(embed=embed)




        async def uyuklama_fonk(range1 : 1, range2 , range3 : 1):

            global saatStr
            global dakikaStr
            global day
            global mutluluk
            global temizlik
            global hungry
            global money
            global color
            global dakika
            global saat
            global g




            gecen_sure = 0
            hungry_sayac = 0
            temizlik_sayac = 0
            mutluluk_sayac = 0



            uyumadan_onceki_mutluluk = mutluluk
            uyumadan_onceki_hungry = hungry
            uyumadan_onceki_temizlik = temizlik


            steal_lucky = 10

            embed = discord.Embed(
                title=f"**{saatStr} : {dakikaStr}         GÜN {day}         \nPARA : {money}    MUTLULUK : {mutluluk}\nTEMİZLİK : {temizlik}       AÇLIK : {hungry}**",
                colour=color, url="https://www.com")
            embed.add_field(name="Biraz Uyuyorsun . . .",
                            value=f"Geçen Süre : **{gecen_sure}**")
            embed.set_image(url=saat_thumbs(saat))
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/901157476932661308/941724785640099890/Adsz_Resim.gif")
            uyuma_embed = await ctx.send(embed=embed)


            sayi = random.randint(1,10)


            for x in range(range1, range2, range3):

                await asyncio.sleep(1)
                dakika += range3
                gecen_sure += range3
                hungry_sayac += random.randint(1,range3)
                temizlik_sayac += random.randint(1,range3)
                mutluluk_sayac += random.randint(1,range3)

                if hungry_sayac >= 3:
                    hungry_adet = hungry_sayac // 3
                    hungry -= hungry_adet
                    hungry_sayac = 0
                    if hungry <= 0:
                        hungry = 0
                if temizlik_sayac >= 5:
                    temizlik_adet = temizlik_sayac // 5
                    temizlik -= temizlik_adet
                    temizlik_sayac = 0
                    if temizlik <= 0:
                        temizlik = 0
                if mutluluk_sayac >= 30:
                    mutluluk_adet = mutluluk_sayac // 30
                    mutluluk_sayac = 0
                    mutluluk += mutluluk_adet
                    if mutluluk >= 100:
                        mutluluk = 100

                if saat >= 23:
                    day += 1
                    g += 5

                    saat = 8
                    dakika = 0
                    saatStr = ""
                    dakikaStr = ""
                    saatStr = saatString(saat)
                    dakikaStr = dakikaString(dakika)
                    break
                if dakika >= 60:
                    saat += 1
                    dakika = dakika - 60

                saatStr = saatString(saat)
                dakikaStr = dakikaString(dakika)

                embed = discord.Embed(
            title=f"**{saatStr} : {dakikaStr}         GÜN {day}         \nPARA : {money}    MUTLULUK : {mutluluk}\nTEMİZLİK : {temizlik}       AÇLIK : {hungry}**",
            colour=color, url="https://www.com")
                embed.add_field(name="Biraz Uyuyorsun . . .",
                                value=f"Geçen Süre : **{gecen_sure} Dakika**")
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/901157476932661308/941724785640099890/Adsz_Resim.gif")
                embed.set_image(url=saat_thumbs(saat))

                await uyuma_embed.edit(embed=embed)


            olaylar_cumle = ""

            mutluluk_fark = abs(uyumadan_onceki_mutluluk - mutluluk)
            hungry_fark = abs(uyumadan_onceki_hungry - hungry)
            temizlik_fark = abs(uyumadan_onceki_temizlik - temizlik)



            cumle_liste=[f"Mutluluk **{mutluluk_fark}** ARTTI",f"Açlık **{hungry_fark}** AZALDI",f"Temizlik **{temizlik_fark}** AZALDI"]
            if sayi == 1 and money != 0:
                stolen_money = random.randint(1,money)

                if stolen_money < money:
                    money -= stolen_money
                    cumle_liste.append(f"**{stolen_money}** Paran Çalındı")
                else:
                    stolen_money = money
                    money = 0
                    cumle_liste.append(f"**{stolen_money}** Paran Çalındı. Tüm paranı **KAYBETTİN**")


            for x in cumle_liste:
                olaylar_cumle += f"\n{x}"




            embed = embed_baslik(saatStr, dakikaStr, day, mutluluk, temizlik, hungry, money, color)
            embed.add_field(name="Uyandın.",
                            value=f"Uyuduğun süre : **{gecen_sure}** Dakika")
            embed.add_field(name="Uyurken başına gelenler",value=f"{olaylar_cumle}")
            embed.set_thumbnail(url=saat_thumbs(saat))

            await ctx.send(embed=embed)













        if msg2.content == "1":
            embed = embed_baslik(saatStr, dakikaStr, day, mutluluk, temizlik, hungry, money, color)
            embed.add_field(name=f"Ne kadar süre dileniceksin ? ",
                            value="1 - 15 Dakika\n2 - 30 Dakika\n3 - 1 Saat", inline=True)
            embed.set_thumbnail(url=saat_thumbs(saat))
            await ctx.send(embed=embed)

            msg = await Bot.wait_for("message",check=check)



            if msg.content == "1":

                await dilenme_fonk(0,15,1)  #1

            if msg.content == "2":

                await dilenme_fonk(0,30,2)  #2

            if msg.content == "3":

                await dilenme_fonk(0,60,4)  #3

        if msg2.content == "2":
            embed = embed_baslik(saatStr, dakikaStr, day, mutluluk, temizlik, hungry, money, color)
            embed.add_field(name="Ne kadar süre dinlenmek istersin ?",value=f"\n1 - 15 Dakika\n2 - 30 Dakika\n3 - 1 Saat\n4 - 3 Saat\n5 - 6 Saat")
            embed.set_thumbnail(url=saat_thumbs(saat))
            await ctx.send(embed=embed)

            msg = await Bot.wait_for("message",check=check)

            if msg.content == "1":

                await uyuklama_fonk(0,15,1)

            if msg.content == "2":
                await uyuklama_fonk(0, 30, 2)

            if msg.content == "3":
                await uyuklama_fonk(0, 60, 4)

            if msg.content == "4":
                await uyuklama_fonk(0, 180, 12)

            if msg.content == "5":
                await uyuklama_fonk(0, 360, 24)

        if msg2.content == "3":
            while True:
                satir0 = "**1.**  "
                satir1 = "**2.**  "
                satir2 = "**3.**  "
                satir3 = "**4.**  "
                for x in envanter[0]:
                    satir0 += f"{x}  "
                for x in envanter[1]:
                    satir1 += f"{x}  "
                for x in envanter[2]:
                    satir2 += f"{x}  "
                for x in envanter[3]:
                    satir3 += f"{x}  "
                embed = embed_baslik(saatStr, dakikaStr, day, mutluluk, temizlik, hungry, money, color)
                embed.add_field(name="**Envanter**", value=f"{satir0}\n\n{satir1}\n\n{satir2}\n\n{satir3}\n\n\n**5. ÇIKIŞ**\n\n\n\nKullanmak İstediğiniz Eşyanın sıra numarsını girin.")
                embed.set_thumbnail(url=saat_thumbs(saat))
                await ctx.send(embed=embed)

                msg = await Bot.wait_for("message", check=check)
                if msg.content == "1":
                    if len(envanter[0]) != 0:
                        envanter[0].pop(-1)

                        secim2 = random.randint(2,5)
                        secim3 = random.randint(10,15)

                        mutluluk += secim2
                        temizlik += secim3
                        if mutluluk >= 100:
                            mutluluk = 100
                        if temizlik >= 100:
                            temizlik = 100


                        embed = embed_baslik(saatStr, dakikaStr, day, mutluluk, temizlik, hungry, money, color)
                        embed.add_field(name="1 Adet SU Kullanıldı.",value=f"Susuzluğun giderildi. Şişede kalan biraz su ile temizlenmeye çalıştın. \n\n** + {secim2} MUTLULUK**\n** + {secim3} TEMİZLİK**")
                        await ctx.send(embed=embed)
                    else:
                        embed = embed_baslik(saatStr, dakikaStr, day, mutluluk, temizlik, hungry, money, color)
                        embed.add_field(name=f"SEÇTİĞİNİZ SIRADA EŞYANIZ YOK !",value="Kullanmak için önce Market'ten satın almanız gerekli.")
                        await ctx.send(embed=embed)
                if msg.content == "2":
                    if len(envanter[1]) != 0:
                        envanter[1].pop(-1)
                        mutluluk = 100
                        #await ctx.send(embed=embed)
                    else:
                        embed = embed_baslik(saatStr, dakikaStr, day, mutluluk, temizlik, hungry, money, color)
                        embed.add_field(name=f"SEÇTİĞİNİZ SIRADA EŞYANIZ YOK !",value="Kullanmak için önce Market'ten satın almanız gerekli.")
                        await ctx.send(embed=embed)

                if msg.content == "3":
                    if len(envanter[2]) != 0:
                        envanter[2].pop(-1)
                        lays_sozler = ["Kesinlikle ağzına kadar dolu olan LAYS CİPS'i yedin. Ama bir konuda kendini kandırmış gibi hissettin...",
                                       "Yarısı dolu olan LAYS CİPS'i yedin. Güzel bir bakış açısı ama büyük resmi kaçırma.",
                                       "Yarısı Boş olan LAYS CİPS'i yedin. İyi tarafından bak Cipsin artık yarım değil.",
                                       "Leziz LAYS CİPS'i yedin. Oldukça hayran kalmış gibisin.",]
                        secim = random.choice(lays_sozler)
                        secim2 = random.randint(15,30)

                        hungry += secim2

                        if hungry >= 100:
                            hungry = 100

                        embed = embed_baslik(saatStr, dakikaStr, day, mutluluk, temizlik, hungry, money, color)
                        embed.add_field(name="1 Adet LAYS CİPS Kullanıldı",value=f"{secim}\n\n** + {secim2} AÇLIK **")
                        await ctx.send(embed=embed)
                    else:
                        embed = embed_baslik(saatStr, dakikaStr, day, mutluluk, temizlik, hungry, money, color)
                        embed.add_field(name=f"SEÇTİĞİNİZ SIRADA EŞYANIZ YOK !",value="Kullanmak için önce Market'ten satın almanız gerekli.")
                        await ctx.send(embed=embed)

                if msg.content == "4":
                    if len(envanter[3]) != 0:
                        envanter[3].pop(-1)

                        soda_sozler = ["Bu Soda içini ferahlattı.Artık daha rahat hissediyorsun.",
                                       "Şişeği açtığında gördüğün o minik yüzlerce kabarcığı izlemek seni dertlerinden biraz olsun kopardı.",
                                       "Sodayı içerken bir anda Eskiden arakdaşlarınla soda içme yarışması yaptığın günler aklına geldi.Bu küçük anı Yüzünü gülümsetti.",
                                       "Adabı vardır Sade Soda'nın. Önce kiminle içtiğini bileceksin, sonra kime içtigini. Değecek mesela içtiğin meseleye"]
                        secim = random.choice(soda_sozler)
                        secim2 = random.randint(2, 7)
                        secim3 = random.randint(7,15)
                        hungry += secim2
                        mutluluk += secim3

                        if mutluluk >= 100:
                            mutluluk = 100
                        if hungry >= 100:
                            hungry = 100

                        embed = embed_baslik(saatStr, dakikaStr, day, mutluluk, temizlik, hungry, money, color)
                        embed.add_field(name="1 Adet SADE SODA Kullanıldı", value=f"{secim}\n\n** + {secim2} AÇLIK** \n** + {secim3} MUTLULUK**")
                        await ctx.send(embed=embed)
                    else:
                        embed = embed_baslik(saatStr, dakikaStr, day, mutluluk, temizlik, hungry, money, color)
                        embed.add_field(name=f"SEÇTİĞİNİZ SIRADA EŞYANIZ YOK !",value="Kullanmak için önce Market'ten satın almanız gerekli.")
                        await ctx.send(embed=embed)

                if msg.content == "5":
                    break







        if msg2.content == "4":
            while True:
                browni_kek = Bot.get_emoji(941455049148731482)
                su = Bot.get_emoji(941455050205712445)
                lays = Bot.get_emoji(941455050247639040)
                soda = Bot.get_emoji(941455049366831114)


                embed = embed_baslik(saatStr, dakikaStr, day, mutluluk, temizlik, hungry, money, color)
                embed.add_field(name="**Papatya Market'e Hoşgeldiniz**",value=f"**1 -** Su {su}   :    5 :dollar:\n\n\n\n**2 -** Browni Kek {browni_kek}:    1710 :dollar:\n\n\n\n\n\n\n\n\n\n\n\n\n\n**3 -** Lays Cips {lays}   :     18 :dollar:\n\n\n\n\n\n\n**4 -** Sade Soda {soda}    :     8 :dollar:\n\n** 5 - Çıkış **")
                embed.add_field(name="**Ürün Açıklamaları**",value="**1 -** Susuzluğunuzu giderir.\n\n\n\n**2 -** Çok güçlü bir etkiye sahip bu kek sizi yaşatıcak her türlü özelliğe sahip. Hayatınızı bir anda karanlıktan aydınlığa çevirebilecek güçte. Bu Browni Kek ile tüm zorlukları tüm engelleri aşabilirsiniz.Bu Güzel Kek Hayatınızın Gerçek Kahramanı olucak.\n\n\n\n**3 -** Açlığınızı bir miktar giderir. Üstelik çok lezzetlidir. En Sevdiğiniz Cips olacak.\n\n\n\n**4 -** Biraz yemekten sonra iyi gider değil mi?")
                embed.set_image(url=market)
                embed.set_thumbnail(url=saat_thumbs(saat))
                await ctx.send(embed=embed)
                msg = await Bot.wait_for("message",check=check)

                if msg.content == "1":
                    if len(envanter[0]) < 16:

                        if money >= 5:
                            money -= 5
                            envanter[0].append(su)

                            embed = embed_baslik(saatStr, dakikaStr, day, mutluluk, temizlik, hungry, money, color)
                            embed.add_field(name="**Alışveriş Yapıldı**", value=f"**1 Adet {su} Envanterinize Eklendi.**")
                            embed.set_thumbnail(url=saat_thumbs(saat))
                            await ctx.send(embed=embed)
                        else:
                            embed = embed_baslik(saatStr, dakikaStr, day, mutluluk, temizlik, hungry, money, color)
                            embed.add_field(name="**Paranız Yetersiz**",value=f"** Gerekli Para : {5 - money} :dollar:")
                            embed.set_thumbnail(url=saat_thumbs(saat))
                            await ctx.send(embed=embed)
                    else:
                        embed = embed_baslik(saatStr, dakikaStr, day, mutluluk, temizlik, hungry, money, color)
                        embed.add_field(name=F"**{su} Envantriniz dolu**", value=f"**MAKS 15 ADET {su} ALINABİLİR.**")
                        embed.set_thumbnail(url=saat_thumbs(saat))
                        await ctx.send(embed=embed)


                if msg.content == "2":
                    if money >= 1710:

                        embed = embed_baslik(saatStr, dakikaStr, day, mutluluk, temizlik, hungry, money, color)
                        embed.add_field(name="**Sanırım Açıklamayı Yeterince Net Okumadın.**",value="\nBu Browniyi ne kadar para verirsen ver alamazsın. Hiçbir şey ile onu satın alamazsın. Asla onun değerine denk bir şey bulamazsın unut bunu. Gerçekten 1710 Doların olunca kendini bir şey mi sandın ? Para Her şeyi satın alamaz dostum. Gerçek Sevgiyi Satın Alamazsın, Ancak Hak Etmen Gerek ama Parayla Elde Etmeye Çalıştığına Göre Hak Ettiğini Sanmıyorum.\n\n He bir de bundan bir ders çıkarman için 17102002 Dolarını senden almam gerekiyor. Hoşçakal :dollar:")
                        money -= 1710
                        embed.set_thumbnail(url=saat_thumbs(saat))
                        await ctx.send(embed=embed)

                    else:
                        embed = embed_baslik(saatStr, dakikaStr, day, mutluluk, temizlik, hungry, money, color)
                        embed.add_field(name="**Paranız Yetersiz**",value=f"** Gerekli Para : {1710 - money} :dollar:**")
                        embed.set_thumbnail(url=saat_thumbs(saat))
                        await ctx.send(embed=embed)

                if msg.content == "3":
                    if len(envanter[2]) < 16:
                        if money >= 18:
                            money -= 18
                            envanter[2].append(lays)


                            embed = embed_baslik(saatStr, dakikaStr, day, mutluluk, temizlik, hungry, money, color)
                            embed.add_field(name="**Alışveriş Yapıldı**", value=f"**1 Adet {lays} Envanterinize Eklendi.**")
                            embed.set_thumbnail(url=saat_thumbs(saat))
                            await ctx.send(embed=embed)
                        else:
                            embed = embed_baslik(saatStr, dakikaStr, day, mutluluk, temizlik, hungry, money, color)
                            embed.add_field(name="**Paranız Yetersiz**", value=f"** Gerekli Para : {18 - money} :dollar:")
                            embed.set_thumbnail(url=saat_thumbs(saat))
                            await ctx.send(embed=embed)
                    else:
                        embed = embed_baslik(saatStr, dakikaStr, day, mutluluk, temizlik, hungry, money, color)
                        embed.add_field(name=F"**{lays} Envantriniz dolu**", value=f"**MAKS 15 ADET {lays} ALINABİLİR.**")
                        embed.set_thumbnail(url=saat_thumbs(saat))
                        await ctx.send(embed=embed)

                if msg.content == "4":
                    if len(envanter[3]) < 16:
                        if money >= 8:
                            money -= 8
                            envanter[3].append(soda)
                            embed = embed_baslik(saatStr, dakikaStr, day, mutluluk, temizlik, hungry, money, color)
                            embed.add_field(name="**Alışveriş Yapıldı**", value=f"**1 Adet {soda} Envanterinize Eklendi.**")
                            embed.set_thumbnail(url=saat_thumbs(saat))
                            await ctx.send(embed=embed)
                        else:
                            embed = embed_baslik(saatStr, dakikaStr, day, mutluluk, temizlik, hungry, money, color)
                            embed.add_field(name="**Paranız Yetersiz**", value=f"** Gerekli Para : {8 - money} :dollar:")
                            embed.set_thumbnail(url=saat_thumbs(saat))
                            await ctx.send(embed=embed)

                    else:
                        embed = embed_baslik(saatStr, dakikaStr, day, mutluluk, temizlik, hungry, money, color)
                        embed.add_field(name=F"**{soda} Envantriniz dolu**", value=f"**MAKS 15 ADET {soda} ALINABİLİR.**")
                        embed.set_thumbnail(url=saat_thumbs(saat))
                        await ctx.send(embed=embed)


                if msg.content == "5":
                    break

                await asyncio.sleep(1)








        if msg2.content == "5":
            await ctx.send(f"İyi Günler {charName}")
            break


@Bot.command()
async def ev(ctx):
    embed = discord.Embed(title="Home")
    embed.set_image(url="https://cdn.discordapp.com/attachments/901157476932661308/940312331701846016/IMG_0239.png")
    ev1 = await ctx.send(embed=embed)

    def check(msg):
        return msg.channel == ctx.channel

    msg = await Bot.wait_for("message",check=check)
    if msg.content == "geliştir":
        embed = discord.Embed(title="Home")
        embed.set_image(url="https://cdn.discordapp.com/attachments/901157476932661308/940312332477796362/IMG_0241.gif")
        await ev1.edit(embed=embed)
        await asyncio.sleep(1)

    embed = discord.Embed(title="Home")
    embed.set_image(url="https://cdn.discordapp.com/attachments/901157476932661308/940312331966119996/IMG_0240.png")
    await ev1.edit(embed=embed)


ctx1 = ""

@Bot.command()
async def mesaj1(ctx):
    global ctx1
    ctx1 = ctx
    await ctx.send(type(ctx1))




    await ctx1.send("123")

@Bot.command()
async def msj2(ctx):
    channel = Bot.get_channel(901157493126881290)
    await channel.send("a")

Bot.run("")
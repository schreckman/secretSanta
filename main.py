import random
from copy import deepcopy
import discord
from discord.ext import commands

TOKEN = "NzgwODIxNjM2OTM1OTc0OTMy.X70q0Q.074BvvpRJyXVwGYpY0itJnZ-CUM"
BOT_PREFIX = ('!', '$', '-')

bot = commands.Bot(command_prefix=BOT_PREFIX)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def helpme(ctx):
    await ctx.send(f"-helpme        | Na dat zeigt das hier an man!\n"
                   f"-register      | um dich für das Wichteln zu registrieren\n"
                   f"-clearRegister | um die Liste an Teilnehmern zu löschen\n"
                   f"-play          | um das Wichteln zu starten")

data = []


@bot.command(pass_context=True)
async def register(ctx):

    if ctx.author.id not in data:
        data.append(ctx.author.id)
        await ctx.send(f"Du süße Zuckerstange hast dich nun beim Wichteln registriert :heart:\n"
                       f"Es gibt bis jetzt {len(data)} süße Zuckerstangen, die Wichteln!")

    else:
        await ctx.send(f"Du süße Zuckerstange hast dich schon regristiert :heart:")


@bot.command()
async def clearRegister(ctx):
    data.clear()
    await ctx.send(f"Du süße Zuckerstange hast die Registrierungsliste gelöscht! :sob:")


@bot.command()
async def play(ctx):

    # len of data must be 3 or above otherwise
    if len(data) < 3:
        await ctx.send(f"Du süße Zuckerstange hast keinen Teilnehmer zum wichteln :sob:")
        return

    await ctx.send(f"Du süße Zuckerstange hast das Wichteln nun gestartet. :heart:\n"
                   f"Du süße Zuckerstange erhaltst deinen süßen Wichtelpartner per privater Nachricht :heart:")

    userlist2 = deepcopy(data)
    finalList = []
    besetzt = []

    for i in range(len(data)):
        tmp = random.choice(userlist2)
        finalList.append(tmp)
        userlist2.remove(tmp)
        besetzt.append(tmp)

    for j in range(len(data)):
        if data[j] == finalList[j]:
            besetzt.pop(j)
            test = random.choice(range(len(besetzt)))
            finalList[j], finalList[test] = finalList[test], finalList[j]
            besetzt.append(j)

    for i in range(len(data)):
        user = bot.get_user(finalList[i])
        await bot.get_user(data[i]).send(f"Hey du süße Zuckerstange, dein Wichtel Partner ist: {user.name} :heart:")

    data.clear()

bot.run(TOKEN)

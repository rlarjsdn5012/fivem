import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("제넷파이브엠디자인 오픈!")
    await client.change_presence(status=discord.Status.online)


@client.event
async def on_message(message):
    if message.content.startswith("!입국방법"):
        await message.channel.send("**이모지를 클릭하세요 ! 이모지를 클릭하시고 저희 제넷 파이브엠 디자인샵을 자유롭게 **")
    if message.content.startswith("!구매방법"):
            await message.channel.send("**제넷#7777 을 호출하세요 ! 또는 !총판호출**")
    if message.content.startswith("!총판호출"):
        await message.channel.send("<@581396513108918295> <@677439965554147349> 야 개새끼야 손님왔어 | 연락없을경우 기다려주세요 .")


client.run("Njk0ODY5ODAwMzM3Mjc2OTgx.XoR-og.J1yJQb_5lhsoSWZdRNqtsnvoTss")
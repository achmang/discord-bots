import discord
import random

token = 'your_token_here'
client = discord.Client()

@client.event
async def on_message(message):
    # Roll, rolls the dice and reveals answer in the channel
    if message.content.startswith("$roll"):
        try:
            roll_range = int(message.content[5:].replace(" ", ""))
            roll_outcome = random.randint(1, roll_range)
            await message.channel.send(message.author.name + " rolled " + str(roll_outcome))

            if roll_range == 20 and roll_outcome == 20:
                await message.channel.send("It's a critical hit!")
                await message.channel.send("https://media.giphy.com/media/3oriNPdeu2W1aelciY/giphy.gif")

        except:
            await message.channel.send("Could not roll that.")

    # Secret Roll, rolls the dice without revealing the answer in the channel.
    elif message.content.startswith("$sroll"):
        try:
            roll_range = int(message.content[6:].replace(" ", ""))
            roll_outcome = random.randint(1, roll_range)
            await message.author.send("you rolled " + str(roll_outcome))

            if roll_range == 20 and roll_outcome == 20:
                await message.author.send("It's a critical hit!")
                await message.author.send("https://media.giphy.com/media/3oriNPdeu2W1aelciY/giphy.gif")

        except:
            await message.author.send("Could not roll that.")

client.run(token)
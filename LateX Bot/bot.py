import discord
import urllib.parse

token = 'your_token_here'
client = discord.Client()

url = "https://latex.codecogs.com/gif.latex?%5Cbg_white%20%5CLARGE%20"

@client.event
async def on_message(message):
    if message.content.startswith("$$"):
        latex_string = message.content[2:].replace(" ", "")
        web_latex_string = urllib.parse.quote_plus(latex_string)
        print(web_latex_string)
        await message.channel.send(url + web_latex_string)

client.run(token)

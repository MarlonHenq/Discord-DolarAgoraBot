import discord
import requests

client = discord.Client()

@client.event
async def on_message(message):
    message.content = message.content.lower()

    def printDolar():
        response = requests.get("https://economia.awesomeapi.com.br/all/USD-BRL")
        string = response.text

        stringInArray = string.split(",")
        bid = stringInArray[7].split('"')
        bidValue = bid[3]
        dolarAgora = 'Dólar Agora: :dollar: ' + bidValue + ' R$'

        return dolarAgora

    if message.content.startswith("salve"):

        await message.channel.send("Salve Carai!")

    if message.content.startswith("-ping"):

        await message.channel.send("pong")

    if message.content.startswith("-dolar help"):

        await message.channel.send('Digite: "-cotacao" ou "-cotação" ou "-c" para saber a cotação atual do Dólar \nDigite: "-ping" para testar o bot (recebendo um "pong" em resposta)\n\nCriado por @MarlonHenq  https://github.com/MarlonHenq')

    if message.content.startswith("-dolar"):
        await message.channel.send(printDolar())

client.run('BOT_CLIENT_ID')

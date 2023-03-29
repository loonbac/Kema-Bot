import discord

intents = discord.Intents.default()  # Establecer intents

client = discord.Client(intents=intents)
counter = 0
channel_id = 967610797704511569

@client.event
async def on_ready():
    print("Preparando Mensajes Bonitos uwu")

@client.event
async def on_message(message):
    global counter
    
    if message.channel.id == channel_id:
        counter += 1
        if counter % 70 == 0:
            channel = client.get_channel(channel_id)
            await channel.send("No olviden leer el canal <#1050458845794799711> y el canal <#1050457764503240765>, así sabrán que cosa hacer y lo ultimo en cheats y mas :O")

client.run("LLAVE_SECRETA")

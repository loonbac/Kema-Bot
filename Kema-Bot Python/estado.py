import discord
import random
import asyncio

# Crea el cliente de Discord
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Lista de palabras para el estado
palabras_estado = ["Contar usuarios con Acrepi", "Enviar mensajes troll 7u7", "Verificar Testers", "Ver Streamers"]

# Función para cambiar el estado
async def cambiar_estado():
    while True:
        # Elige una palabra al azar de la lista
        palabra = random.choice(palabras_estado)
        # Cambia el estado del bot
        await client.change_presence(activity=discord.Game(name=palabra))
        # Espera 10 minutos antes de cambiar el estado nuevamente
        await asyncio.sleep(600)

# Evento de inicio del bot
@client.event
async def on_ready():
    print('Cambiando Estado de {0.user} uwu'.format(client))
    # Inicia la tarea para cambiar el estado
    client.loop.create_task(cambiar_estado())

# Inicia el bot
client.run('MTA5MDA3NDExODA3NTk5MDAyNg.GIMZfS.jQmIIWiKg9z1m0LN1m1SVdAWdcn79E50cWdqTY')

import discord
import re
import os
from discord.ext import commands

# Importar la clase Intents
from discord import Intents

# Crear una instancia de Intents con todos los intents activados
intents = Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

client = commands.Bot(command_prefix="!", intents=intents)  # Cambia el prefijo como desees

xd_count = 0  # Contador de mensajes que contienen "xd"

@client.event
async def on_ready():
    print("Preparando comandos Troll 7u7")

@client.event
async def on_message(message):
    global xd_count

    # Verificar si el mensaje contiene "xd" en cualquiera de sus formas
    if "xd" in message.content.lower() and message.author != client.user:
        xd_count += 1
        await message.channel.send(f"XD Numero {xd_count} uwu")
      # Verificar si el mensaje contiene "multicuenta" o "multicuentas"
    if "multicuenta" in message.content.lower() or "multicuentas" in message.content.lower():
        # Obtener la ruta absoluta del archivo de la imagen
        image_path = os.path.abspath("imagen.jpg")
        # Cargar la imagen desde la ruta del archivo
        file = discord.File(image_path, filename="imagen.jpg")
        # Enviar la imagen como archivo adjunto en un mensaje
        await message.channel.send(file=file)

      # Verificar si el mensaje solo contiene la palabra "que"
    if re.match(r'^que$', message.content.lower()) and message.author != client.user:
        await message.channel.send("so, te trolie jeje nya")
      # Verificar si el mensaje solo contiene la palabra "a"
    if re.match(r'^a$', message.content.lower()) and message.author != client.user:
        await message.channel.send("rroz .¿")
        # Cariño comandos
    if client.user.mentioned_in(message) and any(word in message.content.lower() for word in ["te amo", "te quiero", "cariño"]):
        await message.channel.send("Y-yo tambien te quiero mucho uwu.")

    await client.process_commands(message)
  
client.run("LLAVE_SECRETA")

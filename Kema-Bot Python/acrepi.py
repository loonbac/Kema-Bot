# Importar la librería de discord.py
import os
import discord
from discord.ext import commands

# Importar la clase Intents
from discord import Intents

# Crear una instancia de Intents con todos los intents activados
intents = Intents.all()

# Crear una instancia del bot con el prefijo "!" y los intents
bot = commands.Bot(command_prefix="!", intents=intents)

# Definir el ID del rol que quieres contar
role_id = 1087851758342123630

@bot.event
async def on_ready():
    print("Buscando usuarios con Acrepi")
    
# Definir un comando que envíe el número de usuarios con el rol
@bot.command(name="acrepi")
async def count(ctx):
  # Obtener el rol por su ID
  role = ctx.guild.get_role(role_id)
  # Si el rol existe
  if role:
    # Contar cuántos miembros tienen el rol
    count = len(role.members)
    # Enviar un mensaje con el resultado
    await ctx.send(f"Hay {count} Usuarios usando Acrepi :D")
  # Si el rol no existe
  else:
    # Enviar un mensaje de error
    await ctx.send(f"No se encontró el rol con el ID {role_id}.")

# Ejecutar el bot con tu token
bot.run("LLAVE_SECRETA")
import discord
import random
import asyncio
import os
import re
from discord.ext import commands

# Importar la clase Intents
from discord import Intents

# Crear una instancia de Intents con todos los intents activados
intents = Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

palabras_estado = [
    "Contar usuarios usando Acrepi",
    "Enviar mensajes troll 7u7",
    "Verificar Testers",
    "Ver Streamers",
]

# Función para cambiar el estado
async def cambiar_estado():
    while True:
        # Elige una palabra al azar de la lista
        palabra = random.choice(palabras_estado)
        # Cambia el estado del bot
        await bot.change_presence(activity=discord.Game(name=palabra))
        # Espera 10 minutos antes de cambiar el estado nuevamente
        await asyncio.sleep(600)

@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}\n"
      f"Cambiando Estados de Bot\n"
      f"Verificando si hay Usuarios en Vivo\n"
      f"Verificando Usuarios con Acrepi\n"
      f"Preparando Mensajes Utiles\n"
      f"Preparando Mensajes troll")
    global xd_count
    # Iniciar el cambio de estado en el bucle de eventos de asyncio
    asyncio.create_task(cambiar_estado())

xd_count = 0
counter = 0

@bot.event
async def on_message(message):    
    if message.author == bot.user:
        return
    if "xd" in message.content.lower():
        global xd_count
        xd_count += 1
        await message.channel.send(f"XD Numero {xd_count} uwu")
        
    if "acrepi" in message.content.lower():
        role_id = 1087851758342123630
        role = message.guild.get_role(role_id)
        if role:
            count = len(role.members)
            await message.channel.send(f"Hay {count} Usuarios usando Acrepi :D")
        else:
            await message.channel.send(f"No se encontró el rol con el ID {role_id}.")

    if message.channel.id == 967610797704511569:
        global counter
        counter += 1
        if counter % 70 == 0:
            channel = bot.get_channel(967610797704511569)
            await channel.send("No olviden leer el canal <#1050458845794799711> y el canal <#1050457764503240765>, así sabrán que cosa hacer y lo ultimo en cheats y mas :O")

    if message.content.startswith("!verificartester") or message.content.startswith("verificartester"):
    # Verificar que el mensaje haya sido enviado en el canal correcto
        if message.channel.id != 1069466889409011762:
            # Enviar un mensaje de error si el comando no se envió en el canal correcto
            await message.channel.send("L-lo siento... este comando solo se puede ejecutar en el canal <#1069466889409011762> kya >w<.")
            return
        # Comprobar si el mensaje tiene una imagen adjunta
        if message.attachments:
            # Enviar un mensaje de confirmación
            await message.channel.send(f"Muy bien {message.author.mention}, revisaré tu imagen uwu.")
            # Obtener el mensaje con la imagen
            message = await message.channel.fetch_message(message.id)
            # Agregar los emojis reaccionables
            await message.add_reaction("✅")
            await message.add_reaction("❌")
            # Definir los ids de los roles que pueden aprobar o rechazar
            roles_ids = [1050068650775826553, 1069860686408204339, 1043052170569846787]
            # Definir el id del rol que se otorga al usuario aprobado
            role_id = 1048490650385002556
            # Esperar una reacción al mensaje
            def check(reaction, user):
                # Comprobar que la reacción sea uno de los emojis y que el usuario tenga uno de los roles
                return str(reaction.emoji) in ["✅", "❌"] and any(role.id in roles_ids for role in user.roles)

            # Obtener la reacción y el usuario que la hizo
            reaction, user = await bot.wait_for("reaction_add", check=check)

            # Si la reacción es el emoji de check
            if str(reaction.emoji) == "✅":
                # Obtener el rol por su id
                role = discord.utils.get(message.guild.roles, id=role_id)
                # Asignar el rol al usuario que ejecutó el comando
                await message.author.add_roles(role)
                # Enviar un mensaje de felicitación
                await message.channel.send(f"{message.author.mention}, se te aprobó la entrada, ya tienes el rol Tester.")
            # Si la reacción es el emoji de x
            elif str(reaction.emoji) == "❌":
                # Enviar un mensaje de rechazo
                await message.channel.send(f"{message.author.mention}, l-lo siento pero no cumples con los requisitos para ser Tester unu.")
        else:
            # Enviar un mensaje de error si no hay imagen adjunta
            await message.channel.send(f"Di-disculpa... El comando debe ser ejecutado con una screenshot de acrepi y tu usuario de discord nya.")

    await que_command(message)
    await a_command(message)
    await multicuenta_command(message)
    await carino_command(message)
    await sex_command(message)
    await on_member_update(before, after)

async def que_command(message):
    if re.match(r'^que$', message.content.lower()) and message.author != bot.user:
        await message.channel.send("so, te trolie jeje nya")

async def a_command(message):
    if re.match(r'^a$', message.content.lower()) and message.author != bot.user:
        await message.channel.send("rroz .¿")

async def multicuenta_command(message):
    if "multicuenta" in message.content.lower() or "multicuentas" in message.content.lower():
        # Obtener la ruta absoluta del archivo de la imagen
        image_path = os.path.abspath("imagen.jpg")
        # Cargar la imagen desde la ruta del archivo
        file = discord.File(image_path, filename="imagen.jpg")
        # Enviar la imagen como archivo adjunto en un mensaje
        await message.channel.send(file=file)

async def carino_command(message):
    if bot.user.mentioned_in(message) and any(word in message.content.lower() for word in ["te amo", "te quiero", "cariño"]):
        await message.channel.send("Y-yo tambien te quiero mucho uwu.")

async def sex_command(message):
    if bot.user.mentioned_in(message) and any(word in message.content.lower() for word in ["profanarte", "desnudarte", "tocarte"]):
        await message.channel.send("N-no por favor...")

async def run_bot():
    await bot.start("TOKEN")

loop = asyncio.get_event_loop()
loop.run_until_complete(run_bot())

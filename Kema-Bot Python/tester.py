import discord
from discord.ext import commands

# Importar la clase Intents
from discord import Intents

# Crear una instancia de Intents con todos los intents activados
intents = Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

# Definir el id del canal permitido
channel_id = 1069466889409011762

@bot.event
async def on_ready():
    print("Esperando nuevos Testers owo")

# Crear un decorador de verificación de canal
def in_channel(channel_id):
  def predicate(ctx):
    return ctx.message.channel.id == channel_id
  return commands.check(predicate)
  
@bot.command()
@in_channel(channel_id) # Aplicar el decorador al comando
async def verificartester(ctx):
  # Comprobar si el mensaje tiene una imagen adjunta
  if ctx.message.attachments:
    # Enviar un mensaje de confirmación
    await ctx.send(f"Muy bien {ctx.author.mention}, revisare tu imagen uwu.")
    # Obtener el mensaje con la imagen
    message = await ctx.channel.fetch_message(ctx.message.id)
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
      role = discord.utils.get(ctx.guild.roles, id=role_id)
      # Asignar el rol al usuario que ejecutó el comando
      await ctx.author.add_roles(role)
      # Enviar un mensaje de felicitación
      await ctx.send(f"{ctx.author.mention}, se te aprobó la entrada, ya tienes el rol Tester.")
    
    # Si la reacción es el emoji de x
    elif str(reaction.emoji) == "❌":
      # Enviar un mensaje de rechazo
      await ctx.send(f"{ctx.author.mention}, l-lo siento pero- no cumples con los requisitos para ser Tester unu.")

  else:
    # Enviar un mensaje de error si no hay imagen adjunta
    await ctx.send(f"Di-disculpa... El comando debe ser ejecutado con una screenshot de acrepi y tu usuario de discord nya.")

# Manejar el error si el comando se ejecuta en otro canal
@verificartester.error
async def verificartester_error(ctx, error):
  if isinstance(error, commands.CheckFailure):
    # Obtener el canal por su id
    channel = discord.utils.get(ctx.guild.channels, id=channel_id)
    # Enviar un mensaje de error con la mención al canal
    await ctx.send(f"Este comando solo se puede usar en el canal {channel.mention} kyaa! >w<.")

# Ejecutar el bot con tu token
bot.run("LLAVE_SECRETA")
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  # Agrega el intent para recibir eventos de miembros

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Buscando Streamers en el Server :3')

@bot.event
async def on_member_update(before, after):
    role_id = 1089760409617178807
    stream_role_id = 1089758781874900992
    message_channel_id = 1089758433105944576
    
    if role_id in [role.id for role in after.roles] and not before.activity and after.activity:
        if isinstance(after.activity, discord.Streaming):
            stream_url = after.activity.url
            streamer_name = after.display_name
            message = f"<@&{stream_role_id}> Oh Vaya! {streamer_name} está en vivo! Dale un vistazo: {stream_url}"
            channel = bot.get_channel(message_channel_id)
            await channel.send(message)

bot.run("MTA5MDA3NDExODA3NTk5MDAyNg.GIMZfS.jQmIIWiKg9z1m0LN1m1SVdAWdcn79E50cWdqTY")

import discord,asyncio,random,json,time
from discord.ext import commands
from datetime import datetime
import http.client




usuarios = []

description = ' '
bot = commands.Bot(command_prefix='st!', description=description, pm_help=True,)
bot.remove_command("help")

ahora = datetime.now()

#Acá están las listas, si quieres ayudarme pero no sabes programar te recomiendo que me ayudes con esto
lstatus = ["discord.Status.dnd", "discord.Status.online"]
lactions = ["husbando", "general"]
#No cambies estás listas ^ son importantes, cambia estas V
lgeneral = ["Hola, ¿Como están?", "Hey, ¿Que tal?", "Hola plebeyos bonitos!", "Hola mis niños :smile:", "¡Holaa!", "Heey", "¿Que hacen?", "Estoy aburrida :(", "¿Me recomiendan algun videojuego?", "Me siento amenazada estando frente a chicos con fotos de chicas"]
lgame = ["ajedrez...", "a hablar con chicos que me quieren violar...", "a hablar con virgos", "a hablar con chicos con pp de chicas?", "a practicar piedra, papel y tijera", "a amar a Sora"]
ldoing = ["aprendiendo de ustedes :)", "intentando entender porque se ponen fotos de perfil de mujeres si son hombres :(", "viendo fotos de Sora :relaxed:", "aburrida así que no se que hacer", "conociendolos mejor a ustedes :relaxed:"]
lbadwordsq = ["mierda", "coño", "puta", "cojones", "puto", "putisima", "joder", "hijo de"]
lbadwordsa = ["Por favor, no digas malas palabras frente a mi, recuerda que soy de la realeza >///<", "Por favor no digas malas palabras :(", "No seas grosero, me caias bien.", "No digas esas cosas!", "Oye, esas cosas no se dicen!", "Si sigues asi dejaras de ser mi amigo!", "Por favor, para de decir esas cosas!", "No digas malas palabras!"]
#Acá terminan las listas

@bot.event
async def on_ready():
    print('Status: Online')
    print('Tag: ' + bot.user.name + '#' + bot.user.discriminator)
    print('ID: ' + str(bot.user.id))
    print('Creado el: ' + str(bot.user.created_at))
    print('Fecha de conexión: ' + str(ahora.utcnow()))
    print('Guilds: ' + str(len(bot.guilds)))
    print('Usuarios: ' + str(len(bot.users)))   
    print('------')
    game = discord.Game(name=random.choice(lgame))
    await bot.change_presence(status=random.choice(lstatus), game=game)
    await my_background_task()

@bot.event
async def my_background_task():
    await bot.wait_until_ready()
    print('asd')
    while not bot.is_closed():        
        await bot.change_presence(status=random.choice(lstatus))
        action = random.choice(lactions)
        if action == "husbando":
            channel = bot.get_channel(361278619357675540)
            async with channel.typing():
                await asyncio.sleep(7)
            await channel.send('husbando')
            async with channel.typing():
                await asyncio.sleep(2)
            await channel.send(':smile:')
            print('Husbando Ejecutado correctamente!')
        elif action == "general":        
            channel = bot.get_channel(356152692218789898)
            async with channel.typing():
                await asyncio.sleep(7)
            await channel.send(random.choice(lgeneral))
            print('General Ejecutado correctamente!')
        await asyncio.sleep(300)


@commands.is_owner()
@bot.command()
async def shutdown(ctx):
    """Apaga el bot"""
    await ctx.send('Desconectando...')
    await bot.logout()

@bot.command()
async def getemojis(ctx):
    for emoji in ctx.guild.emojis:
        print(emoji.name + ' ' + str(emoji.id))

@bot.command()
async def getroles(ctx):
    for role in ctx.guild.roles:
        print(role.name + ' ' + str(role.id))
 

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    mencion = ('**' + message.author.name + '-senpai** ')
    if message.author == bot.user:
        return
    if message.author.status == message.author.status.offline:
        await message.channel.send(mencion + '¿Podrías desactivarte el invisible? :c es que así no puedo funcionar bien >///< por favor, no seas malo conmigo :(')
    if " bien " in message.content.lower() or message.content.lower() == "bien":
        await message.channel.send(mencion + 'Me alegro :)')
        async with message.channel.typing():
            await asyncio.sleep(7)
        await message.channel.send(mencion + '¿Y que haces?')
        await message.channel.send('Yo estoy ' + random.choice(ldoing))
        def check(m):
            return m.channel == message.channel and m.author == message.author
        try:
            msg = await bot.wait_for('message', timeout=20.0,check=check)
        except:
            await message.channel.send('Me dejaste hablando sola :(')
    elif " mal " in message.content.lower() or message.content.lower() == "mal":
        await message.channel.send(mencion + '¿Por qué? :c')
        async with message.channel.typing():
            await asyncio.sleep(7)
        await message.channel.send(mencion + 'Cuéntamelo todo')
        def check(m):
            return m.channel == message.channel and m.author == message.author
        try:
            msg = await bot.wait_for('message', timeout=20.0,check=check)
        except:
            await message.channel.send('Me dejaste hablando sola :(')
    elif "steph" in message.content.lower() and "amame" in message.content.lower() or "dame bola" in message.content.lower():
        await message.channel.send(mencion + 'Si quieres podemos ser amigos :)')
    elif "steph" in message.content.lower() and "quieres" in message.content.lower() or "amas" in message.content.lower():
        await message.channel.send(mencion + 'Te quiero como amigo :)')
    elif "steph" in message.content.lower() and "quieres" in message.content.lower() or "amas" in message.content.lower():
        await message.channel.send(mencion + 'Te quiero como amigo :)')
    elif "steph" in message.content.lower() and "amiga" in message.content.lower() and "ser" in message.content.lower() or "serias" in message.content.lower():
        await message.channel.send(mencion + 'Claro, un amigo más a la coleccion :)')
    for num in lbadwordsq:
        if num in message.content.lower():
            await message.channel.send(mencion + random.choice(lbadwordsa))
          
      


bot.loop.create_task(my_background_task())
bot.run('Si viniste para acá a buscar el token, no soy tan tonto, no voy a publicar mi token XDDDD')



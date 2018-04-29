import discord
import asyncio
import random
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='More than only logs Chat'))

@client.event
async def on_message(message):
    if message.content.startswith('cl@ban'):
        tmp = await client.send_message(message.channel, 'Checking permissions')
        await asyncio.sleep(4)
        await client.edit_message(tmp, 'You dont have permission to execute command')

    elif message.content.startswith('cl@test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel,    limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    
    elif message.content.startswith('cl@kick'):
        tmp = await client.send_message(message.channel, 'Checking permissions')
        await asyncio.sleep(4)
        await client.edit_message(tmp, 'You dont have permission to execute command')
	
    elif message.content.startswith('cl@help'):
	    await client.send_message(message.channel, 'Commands can be found on https://haarlemnoordholland.eu/chatlogbot')
		
    elif message.content.startswith('Hoi'):
	    await client.send_message(message.channel, 'Hey maat, Hoe gaat het met jou? alles goed?')

    elif message.content.startswith('<@414370197521039360>'):
        await client.send_message(message.channel, random.choice(["Im a Bot?", "Log Dot", "Hello! Im ChatLogs", "Whats your name? My name is Max.", "HELP! My computer is on fire! Please call 112", "Bot?"]))

    elif message.content.startswith('ChatLogs, What is your favorite artist/DJ?'):
        await client.send_message(message.channel, random.choice(["Coldplay", "Avicii", "The Chainsmokers", "Queen", "Armin van Buren", "Laleh", "Swedish House Mafia", "Sia", "Rihanna", "Ed Sheeran", "Jebroer", "Calvin Harris", "Pitbull"]))

    elif message.content.startswith('Yes'):
        await client.send_message(message.channel, 'https://stadhem.se/app/uploads/yes-diskmedel-original-650-ml-1000x1176.jpg')

    elif message.content.startswith('No'):
        await client.send_message(message.channel, 'https://i.imgur.com/9gFnC4q.png')
		
    elif message.content.startswith('Marco'):
        await client.send_message(message.channel, '<@276978099621724160>')

    elif message.content.startswith('Brent'):
        await client.send_message(message.channel, '<@223086685758554113>')

    elif message.content.startswith('Viaplay'):
        await client.send_message(message.channel, '<@303819081990275073>')
		
    elif message.content.startswith('Jente'):
        await client.send_message(message.channel, 'Meneer van Dam wil meer aandacht hebben dus hij krijgt dat ook! <@308563574857662464>')

    elif message.content.startswith('Jordi'):
        await client.send_message(message.channel, '<@208666671194439681>. JORDI!!!!!!!!!!!!!')

    elif message.content.startswith('Kev'):
        await client.send_message(message.channel, 'Kef Kef Kef Grom Kef!')
        asyncio.sleep(2)
        await client.send_message(message.channel, 'Oh! Jij bedoelt <@246982417900896256>')
		
    elif message.content.startswith('Arjen'):
        await client.send_message(message.channel, '<@228916219292418048>')
		
    elif message.content.startswith('cl@creator'):
        await client.send_message(message.channel, '<@303819081990275073>')

    elif message.content.startswith('cl@repeat'):
        await client.send_message(message.channel, 'Command disabled due to abuse')
		
    elif message.content.startswith('SwedishFantasy'):
        await client.send_message(message.channel, 'https://open.spotify.com/track/4zSSeTlH3sV6zq1Y94FYL5?si=QLcp2DUjQ8WLDTsqVdnj1A')
		
client.run(os.environ['TOKEN']) 

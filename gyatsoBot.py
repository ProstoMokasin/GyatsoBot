import discord
import re

from discord.ext import commands
from discord.utils import get

TOKEN = 'NDQxODgwODk3MDcxODc0MDQ4.Xjdrtg.jru0ir3fLA5KxMO_w7KDZ3wsJ6g'
PREFIX = '.'

previous_invite_urls = []
invite_urls = []
server_roles = ['earth', 'water', 'fire', 'air']
server_role_ids = [322326176939114497, 322326278881411074, 322326358371991553, 322326416496525312]
bot = commands.Bot(command_prefix = PREFIX)

@bot.event
async def on_ready():
	print(f'{bot.user.name} is ready.')
	for guild in bot.guilds:
		for invite in await guild.invites():
			x = [invite.url, invite.uses, invite.channel]
			invite_urls.append(x)
			previous_invite_urls.append(x)

@bot.event
async def on_member_join(member : discord.Member):
	print(f'{member} has joined a server.')
	del invite_urls[:]
	for guild in bot.guilds:
		for invite in await guild.invites():
			x = [invite.url, invite.uses, invite.channel]
			invite_urls.append(x)
	for i in range(len(invite_urls)):
		if(invite_urls[i][1]!=previous_invite_urls[i][1]):
			for role in range(len(server_roles)):
				if(re.search(str(server_roles[role]), str(invite_urls[i][2])) != None):
					role = get(guild.roles, id=server_role_ids[role])
					await member.add_roles(role)
					(f'{member} has joined {invite.channel}!!!')

@bot.command()
async def roles(ctx, role : discord.Role=None):
	if(role != None):
		try:
			print(role.id)
		except:
			print('there is a problem.')
	else:
		print('Role is null. Try again.')


bot.run(TOKEN)
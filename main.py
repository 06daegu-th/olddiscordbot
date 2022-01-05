import discord, asyncio, os, datetime
from discord.ext import discord


intents = discord.Intents.default()
intents.members = True
timer_user = []

TH = '개발자 태형#0122'

client = discord.Client(intents=intents)

come_id = 입장채널 ID
exit_id = 아웃채널 ID


@client.event
async def on_ready():
    print("{client.name}으로 로그인중")
    while True:
        await client.change_presence(status=discord.Status.dnd,activity=discord.Game('!명령어'))
        await asyncio.sleep(4)



@client.event
async def on_member_join(member):
    embed = discord.Embed(description=f'{member.mention}님 태형 서버에 오신것을 환영합니다.', colour=0x2F3119)
    embed.set_image(url='')
    embed.set_footer(text=TH)
    await client.get_channel(come_id).send(embed=embed)

@client.event
async def on_member_remove(member):
    embed = discord.Embed(description=f'{member.mention}님 안녕히 가세요.', colour=0x2F3119)
    embed.set_image(url='')
    embed.set_footer(text=TH)
    await client.get_channel(exit_id).send(embed=embed)

@client.event
async def on_message(message):
    if message.content.startswith('!ben'):
        if message.author.guild_permissions.ban_members:
            try:
                target = message.mentions[0]
            except:
                await message.channel.send('유저를 선택해주세요.')
                return
            
            j = message.content.split(" ")
            try:
                reason = j[2]
            except IndexError:
                reason = 'None'

            

            embed = discord.Embed(title='차단', description=f'📢**{message.guild.name}**서버에서 추방되었습니다.\n사유는 다음과 같습니다 : {reason}🚫', colour=0x2F3136)
            try:
                await target.send(embed=embed)
            except:
                pass
            await target.ban(reason=reason)

            embed = discord.Embed(title='✅  차단의 성공하셧습니다.', description=f'🚫**{target}**이 차단되었습니다.\n사유: {reason}🚫', colour=0x2F3136)
            await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(description=f'{message.author.mention}님 ⚠️ 명령어 사용권한이 없습니다 관리자만 사용이 가능합니다 ⚠️', colour=0x2F3136)
            await message.channel.send(embed=embed)

    if message.content.startswith('!kick'):
        if message.author.guild_permissions.ban_members:
            await message.delete()
            try:
                target = message.mentions[0]
            except:
                await message.channel.send('유저를 선택해주세요.')
                return
            
            j = message.content.split(" ")
            try:
                reason = j[2]
            except IndexError:
                reason = 'None'

            

            embed = discord.Embed(title='추방', description=f'🚫**{message.guild.name}**서버에서 킥되었습니다.\n사유는 다음과 같습니다. : {reason}🚫', colour=0x2F3136)
            try:
                await target.send(embed=embed)
            except:
                pass
            await target.kick(reason=reason)

            embed = discord.Embed(title='✅  추방의 성공하셧습니다.', description=f'🚫**{target}**이 추방되었습니다.\n사유: {reason}🚫', colour=0x2F3136)
            await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(description=f'{message.author.mention}님 ⚠️ 명령어 사용권한이 없습니다. 관리자만 사용이 가능합니다 ⚠️', colour=0x2F3136)
            await message.channel.send(embed=embed)

    if message.content.startswith("!내정보"):
        await message.delete()
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x2F3136)
        embed.add_field(name="`Name`", value=message.author.name, inline=True)
        embed.add_field(name="`Nickname`", value=message.author.display_name, inline=False)
        embed.add_field(name="`Subscription date`", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed.add_field(name="`Id`", value=message.author.id, inline=False)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.set_footer(text=TH)
        await message.channel.send('', embed=embed)

    if message.content == "!핑":
        embed = discord.Embed(title = '태형봇에 현재 핑 :', description = str(client.latency) + 'ms', colour=0x2F3136)
        await message.channel.send(embed=embed)

    if message.content.startswith("시발"): 
        if not message.channel.id == int:
            await message.delete()
            embed = discord.Embed(description="욕설감지 욕설은 서버추방에 사유가 됩니다.", colour=0x2F3136)
            await message.channel.send(embed=embed)
            return

    if message.content.startswith("씨발"): 
        if not message.channel.id == int:
            await message.delete()
            embed = discord.Embed(description="욕설감지 욕설은 서버추방에 사유가 됩니다.", colour=0x2F3136)
            await message.channel.send(embed=embed)
            return

    if message.content.startswith("시1발"): 
        if not message.channel.id == int:
            await message.delete()
            embed = discord.Embed(description="욕설감지 욕설은 서버추방에 사유가 됩니다.", colour=0x2F3136)
            await message.channel.send(embed=embed)
            return
            
    if message.content.startswith("느금마"): 
        if not message.channel.id == int:
            await message.delete()
            embed = discord.Embed(description="욕설감지 욕설은 서버추방에 사유가 됩니다.", colour=0x2F3136)
            await message.channel.send(embed=embed)
            return  

    if message.content.startswith("병신"): 
        if not message.channel.id == int:
            await message.delete()
            embed = discord.Embed(description="욕설감지 욕설은 서버추방에 사유가 됩니다.", colour=0x2F3136)
            await message.channel.send(embed=embed)
            return  

    if message.content.startswith("애미"): 
        if not message.channel.id == int:
            await message.delete()
            embed = discord.Embed(description="욕설감지 욕설은 서버추방에 사유가 됩니다.", colour=0x2F3136)
            await message.channel.send(embed=embed)
            return   

    if message.content.startswith("애비"): 
        if not message.channel.id == int:
            await message.delete()
            embed = discord.Embed(description="욕설감지 욕설은 서버추방에 사유가 됩니다.", colour=0x2F3136)
            await message.channel.send(embed=embed)
            return    

    if message.content.startswith("또라이"): 
        if not message.channel.id == int:
            await message.delete()
            embed = discord.Embed(description="욕설감지 욕설은 서버추방에 사유가 됩니다.", colour=0x2F3136)
            await message.channel.send(embed=embed)
            return            
            
    if message.content.startswith("고아"): 
        if not message.channel.id == int:
            await message.delete()
            embed = discord.Embed(description="욕설감지 욕설은 서버추방에 사유가 됩니다.", colour=0x2F3136)
            await message.channel.send(embed=embed)
            return               
            
    if message.content.startswith("태형 병신"): 
        if not message.channel.id == int:
            embed = discord.Embed(description="개발자에게 욕은 하지 말아주세요...", colour=0x2F3136)
            await message.channel.send(embed=embed)
            return                        

    if message.content.startswith("섹스"): 
        if not message.channel.id == int:
            embed = discord.Embed(description="욕설감지 욕설은 서버추방에 사유가 됩니다.", colour=0x2F3136)
            await message.channel.send(embed=embed)
            return

    if message.content.startswith("!봇정보"):
        embed = discord.Embed(description="카이봇의 제작과정입니다", colour=0x2F3136)
        embed.add_field(name="봇의 시작", value="`적어주세요`", inline= False)
        embed.add_field(name="봇의 제작자", value="`김태형`", inline= False)
        embed.add_field(name="봇의 사이트", value="`적어주세요`", inline= False)
        embed.set_footer(text=TH)
        embed.set_image(url='https://cdn.discordapp.com/attachments/927492918497910824/928252687756193872/celebration-g5f7207e7d_1920.jpg')
        await message.channel.send(embed=embed)

    if message.content.startswith('!명령어'):
        embed1 = discord.Embed(description=f"{message.author.name} 봇의 명령어를 확인해주세요", colour=0x2F3136)
        embed1.add_field(name="!ben", value="`ben`", inline= False)
        embed1.add_field(name="!핑", value="`bot (ms) ping`", inline= False)
        embed1.add_field(name="!kick", value="`kick`", inline= False)
        embed1.add_field(name="!내정보", value="`Self information`", inline= False)
        embed1.add_field(name="x", value="`x`", inline= False)
        msg = await message.reply(embed=embed1)

client.run('put token')
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot('!', intents=intents)

class Components(discord.ui.LayoutView):    
    container1 = discord.ui.Container(
        discord.ui.MediaGallery(
            discord.MediaGalleryItem(
                media="https://cdn.discordapp.com/attachments/1512270783588597820/1512277374748725441/ChatGPT_Image_4_de_jun._de_2026_23_07_27.png?ex=6a23818e&is=6a22300e&hm=c7153cb90a86e10c087763e877d4606cad1b382cde1d391bd631ef54deea8dcb&",
            ),
        ),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.large),
        discord.ui.TextDisplay(content="**Carreira**\nNa Air Canada, Diversidade e Inclusão são essenciais para o nosso sucesso. Nós nos esforçamos para criar um ambiente de trabalho saudável e gratificante para nossos funcionários.\n\nNós prosperamos na mudança e confiamos em nosso povo para nos ajudar a cumprir nossa missão, celebrando os sucessos uns dos outros e inspirando uns aos outros quando as coisas estão mais difíceis do que o normal. Na Air Canada, não nos importamos apenas com nossos clientes, nos importamos uns com os outros também.\n\nSe uma vaga de seu interesse estiver fechada no momento, recomendamos que você permaneça conectado e fique atento a futuras vagas por meio de nossos anúncios."),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.large),
    )


@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user}')


@bot.command()
async def send_components(ctx: commands.Context) -> None:
    view = Components()
    await ctx.send(view=view)


@bot.command()
async def ping(ctx: commands.Context) -> None:
    await ctx.send('Pong! 🏓')


if __name__ == '__main__':
    token = os.getenv('DISCORD_TOKEN')
    bot.run(token)

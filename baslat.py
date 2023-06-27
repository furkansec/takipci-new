import pyfiglet
import rich
import random

from rich.console import Console
from rich.prompt import Prompt

console = Console()

banner = pyfiglet.figlet_format("TAKIPCI", font="slant")
console.print(
   f"[bold red]{banner}",
   "Creator: furka nsecurity",
   "Channel: @öztürk yalçın",

   sep = "\n",
   style = "bold white"
)


def BannerGeneration():

    banner_text = console.input("[bold red]\Kullanıcı adı girin[/]> ")
    
    get_fonts = pyfiglet.FigletFont.getFonts()
    
    try:
       count = 0
       
       many = Prompt.ask(
          "[bold red]TAKİPÇİ SAYISI",
          MAX="10.OOO"
       )

       while count < int(many):
             random_fonts = random.choice(get_fonts)
             
             banners = pyfiglet.figlet_format(banner_text, font=random_fonts)

             count += 1
             console.print(f"[bold magenta]TAKİPCİ BASARIYLA GÖNDERİLDİ[/]: [bold white][{count}]")

             file = open("banners.txt", "a")
             file.write(f"{banners}")
             file.close()
             
    except:
          console.print("[bold red][!] olmadı")

BannerGeneration()

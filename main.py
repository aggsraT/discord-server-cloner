from os import system
mytitle = "Lua Cloner - Developed by NotSaksh#6969"
system("title "+mytitle)
import psutil
import time
import sys
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from serverclone import Clone

client = discord.Client()
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{Fore.RED}

                                    ██╗░░░░░██╗░░░██╗░█████╗░  ░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
                                    ██║░░░░░██║░░░██║██╔══██╗  ██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
                                    ██║░░░░░██║░░░██║███████║  ██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██████╔╝
                                    ██║░░░░░██║░░░██║██╔══██║  ██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██╔══██╗
                                    ███████╗╚██████╔╝██║░░██║  ╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██║░░██║
                                    ╚══════╝░╚═════╝░╚═╝░░╚═╝  ░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
{Style.RESET_ALL}
                                                            {Fore.MAGENTA}Developed by: NotSaksh#6969.{Style.RESET_ALL}
        """)
token = input(f'Please enter your token:\n >')
guild_s = input('Please enter guild id y
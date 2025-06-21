import os
import logging
from dotenv import load_dotenv
from commands import lore, magic_item, monster, help
from error_handlers import handle_error
from discord import Client, Intents, app_commands, Object

# Env Variable Load and Validation
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", "")
GUILD_ID = os.getenv("GUILD_ID", "")

if not DISCORD_TOKEN:
  raise Exception("Missing DISCORD_TOKEN")
if not GUILD_ID:
  raise Exception("Missing GUILD_ID")

# Logging
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
logger = logging.getLogger("dnd_bot")
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

class DnDBotClient(Client):
  def __init__(self):
    super().__init__(intents=Intents.default())
    self.tree = app_commands.CommandTree(self)

  async def setup_hook(self):
    guild = Object(id=int(GUILD_ID))
    logger.debug(f"Setting up client with GUILD_ID: {GUILD_ID}")
    self.tree.add_command(lore, guild=guild)
    self.tree.add_command(magic_item, guild=guild)
    self.tree.add_command(monster, guild=guild)
    self.tree.add_command(help, guild=guild)
    synced = await self.tree.sync(guild=guild)
    logger.debug(f"Synced {len(synced)} command(s): {[cmd.name for cmd in synced]}")

  async def on_ready(self):
    print(f"{self.user} is connected and ready.")

  async def on_app_command_error(self, interaction, error):
    logger.error(error)
    await handle_error(interaction, error)
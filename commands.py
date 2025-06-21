from discord import app_commands, Interaction, Embed, Color
from openai_integration import generate_dnd_monster, generate_dnd_fact, generate_dnd_magic_item
from cooldown_utils import is_on_cooldown, should_wait_for_cooldown

async def help_command(interaction: Interaction):
  if (await should_wait_for_cooldown(interaction, "help")): return
  embed = Embed(
      title="D&D Lore Bot Help",
      description="Here's a list of commands you can use:",
      color=Color.green()
  )
  embed.add_field(name="/lore", value="Get a short D&D lore tidbit.", inline=False)
  embed.add_field(name="/monster", value="Generate a monster spotlight, with a tip for DMs.", inline=False)
  embed.add_field(name="/magicitem", value="Invent a new magical item, complete with effect.", inline=False)
  embed.add_field(name="/help", value="Show this help message.", inline=False)
  await interaction.response.send_message(embed=embed)

async def lore_command(interaction: Interaction, idea: str = ""):
  if (await should_wait_for_cooldown(interaction, "lore")): return
  await interaction.response.defer(ephemeral=True)
  embed = Embed(
    title="D&D Lore Snippet",
    description=generate_dnd_fact(idea),
    color=Color.gold()
  )
  await interaction.followup.send(embed=embed)

async def magic_item_command(interaction: Interaction, idea: str = ""):
  if (await should_wait_for_cooldown(interaction, "magicitem")): return
  await interaction.response.defer(ephemeral=True)
  embed = Embed(
    title="Magic Item Generator",
    description=generate_dnd_magic_item(idea),
    color=Color.blue()
  )
  # Alternative (eventually)
  # embed = discord.Embed(title="Magic Item Generator", color=discord.Color.blue())
  # embed.add_field(name="Name", value="Blade of Whispering Stars", inline=False)
  # embed.add_field(name="Effect", value="Grants +1 to attack rolls...", inline=False)
  # embed.set_footer(text="Use with caution, adventurer.")
  await interaction.followup.send(embed=embed)

async def monster_command(interaction: Interaction, idea: str = ""):
  if (await should_wait_for_cooldown(interaction, "monster")): return
  await interaction.response.defer(ephemeral=True)
  embed = Embed(
    title="D&D Monster Spotlight",
    description=generate_dnd_monster(idea),
    color=Color.red()
  )
  await interaction.followup.send(embed=embed)

help = app_commands.Command(name="help", callback=help_command, description="Show available commands and what they do")
lore = app_commands.Command(name="lore", callback=lore_command, description="Generate fun DnD lore!")
magic_item = app_commands.Command(name="magicitem", callback=magic_item_command, description="Generate an interesting, low-level, magic item!")
monster = app_commands.Command(name="monster", callback=monster_command, description="Generate a monster!")
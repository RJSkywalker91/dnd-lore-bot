from discord.app_commands import AppCommandError, CommandOnCooldown
from discord import Interaction, InteractionResponded

async def handle_error(interaction: Interaction, error: AppCommandError):
  if isinstance(error, CommandOnCooldown):
    await interaction.response.send_message(f"⏳ Cooldown: try again in {int(error.retry_after)}s", ephemeral=True)
    return
  try:
    await interaction.response.send_message("⚠️ An error occurred.", ephemeral=True)
  except InteractionResponded:
    await interaction.followup.send("⚠️ An error occurred.", ephemeral=True)

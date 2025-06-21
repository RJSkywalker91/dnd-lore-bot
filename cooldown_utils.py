import time
from discord import Interaction

cooldowns = {}
COMMAND_COOLDOWNS = {
  "lore": 10,
  "monster": 30,
  "magicitem": 60,
  "help": 5,
}

def is_on_cooldown(user_id: int, command_name: str) -> float:
  key = (user_id, command_name)
  now = time.time()
  expires_at = cooldowns.get(key, 0)

  cooldown_duration = COMMAND_COOLDOWNS.get(command_name, 10)

  if now < expires_at:
    return expires_at - now
  else:
    cooldowns[key] = now + cooldown_duration
    return 0

async def should_wait_for_cooldown(interaction: Interaction, command: str):
  remaining = is_on_cooldown(interaction.user.id, command)
  if remaining <= 0: return False
  await interaction.response.send_message(
    f"🕒 Please wait {int(remaining)} seconds before using this command again.",
    ephemeral=True
  )
  return True
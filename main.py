from bot_config import DnDBotClient, DISCORD_TOKEN

if __name__ == "__main__":
  client = DnDBotClient()
  client.run(DISCORD_TOKEN)
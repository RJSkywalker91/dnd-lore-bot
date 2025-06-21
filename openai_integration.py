import os
import openai
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def generate_dnd_fact(idea: str):  
  prompt = "Give me a short, interesting Dungeons & Dragons fact or lore tidbit. Keep it under 50 words."
  if idea:
      prompt += f" Base it on this idea: '{idea}'."
  return get_response(prompt)

def generate_dnd_monster(idea: str):
  prompt = "Write a brief monster spotlight for a random D&D creature."
  if idea:
      prompt += f" Base it on this idea: '{idea}'."
  prompt += " Include one cool fact and how a DM might use it."
  return get_response(prompt)

def generate_dnd_magic_item(idea: str):
  prompt = f"Invent a magical item for D&D."
  if idea:
      prompt += f" The item should be based on this idea: '{idea}'."
  prompt += " Give it a name, short description, and unique effect."
  prompt = "Invent a magical item for D&D. Give it a name, short description, and unique effect."
  return get_response(prompt)

def get_response(prompt):
  response = client.chat.completions.create(
      model="gpt-4.1",
      messages=[{"role": "user", "content": prompt}],
  )
  content = response.choices[0].message.content
  return content.strip() if content else ""
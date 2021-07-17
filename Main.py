import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()

names = ['Anunurag', 'Apri', 'Makhon', 'Profat', 'Prowdhury', 'Turnasif']

sad_words = ["$universal_truth"]
strater_encouragements = ["@Amlanchy is the sexiest guy in the world", "Anunurag khela pare na", "Give up on your dreams and die", "Being Chowdhury is too hot", "Profat can handle more than two কোলবালিশ... How cool is that", "Among us is dead"]

if "responding" not in db.keys():
  db["responding"] = True

bad_words = ["fuck", "fucking", "ass", "boobs", "pussy", "sex"]
bad_words_reply = ["Sanity বজায় রাখুন", "দয়া করে Sanity বজায় রাখুন"]

rock_paper_scissors = ["rock", "paper", "scissors"]


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + f"\n- {random.choice(names)}"
  return(quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragement(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content
  
  if message.content.startswith('$hello'):
    await message.channel.send('Hello, বন্ধুরা')
  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if message.content.startswith('$valorant'):
    await message.channel.send('''꧁𓊈𒆜🆅🅰🅻🅾🆁🅰🅽🆃 🅺🅷🅴🅻🅱🅾... 🅱🅰🅲🅲🅰🆁🅰 🆂🅾🅱🅰🅸 🅴🆂🅴 🅿🅾🆁🅾...𒆜𓊉꧂\n\n@everyone''')

  if message.content.startswith('$hi'):
    await message.channel.send('''꧁𓊈𒆜🆈🅾🆄 🅰🆁🅴 🆃🅷🅴 🅲🆄🆃🅴🆂🆃 🆃🅷🅸🅽🅶 🅸🅽 🅼🆈 🅻🅸🅵🅴𒆜𓊉꧂''')


  if message.content.startswith('$watchparty'):
    await message.channel.send('''꧁𓊈𒆜🆁🅰🆃🅴 🆆🅰🆃🅲🅷🅿🅰🆁🆃🆈🆃🅴 🅰🅸🆂🅾 🆂🅾🅱🅰🅸𒆜𓊉꧂ ...\n\n@everyone''')
  
  # if any (word in msg for word in bad_words):
  #   await message.channel.send(random.choice(bad_words_reply))

  if message.content.startswith('$horny_rate'):
    await message.channel.send(f"Your horny rate is: {random.randint(0, 101)}%")

  if db["responding"]:
    options = strater_encouragements
    if "encouragements" in db.keys():
      options += db["encouragements"]
    if any (word in msg for word in sad_words):
        await message.channel.send(random.choice(strater_encouragements))
        
  if msg.startswith("$new"):
      encouraging_message = msg.split("$new ", 1)[1]
      update_encouragements(encouraging_message)
      await message.channel.send("New Universal Truth added.")

  if msg.startswith("$del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$del", 1)[1])
      delete_encouragement(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("$list"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("$responding"):
      value = msg.split("$responding ", 1)[1]
      if value.lower() == "true":
        db["responding"] == True
        await message.channel.send("Responding is on.")
      else:
        db["responding"] == False
        await message.channel.send("Responding is off.")

#love_meter
  if msg.startswith("$love_between"):
    if msg.split("$love_between ", 1)[1] == "asif_tupu":
      await message.channel.send("Love Between them is undefined")
    else:
      await message.channel.send(f"Love Between them is:  {random.randint(1, 101)}%")
  
#rock_paper_scissors
  if msg.startswith("$rock"):
    random_choice = random.choice(rock_paper_scissors)
    if random_choice == "rock":
      await message.channel.send("I chose Rock and I rock")
      await message.channel.send("Draw")
    if random_choice == "paper":
      await message.channel.send("I chose paper")
      await message.channel.send("You lose")
    if random_choice == "scissors":
      await message.channel.send("I chose scissors")
      await message.channel.send("You won!!!")
  if msg.startswith("$paper"):
    random_choice = random.choice(rock_paper_scissors)
    if random_choice == "rock":
      await message.channel.send("I chose Rock and I rock")
      await message.channel.send("You won!!!")
    if random_choice == "paper":
      await message.channel.send("I chose paper")
      await message.channel.send("Draw")
    if random_choice == "scissors":
      await message.channel.send("I chose scissors")
      await message.channel.send("You lose!!!")
  if msg.startswith("$scissors"):
    random_choice = random.choice(rock_paper_scissors)
    if random_choice == "rock":
      await message.channel.send("I chose Rock and I rock")
      await message.channel.send("You lose")
    elif random_choice == "paper":
      await message.channel.send("I chose paper")
      await message.channel.send("You won!!!")
    if random_choice == "scissors":
      await message.channel.send("I chose scissors")
      await message.channel.send("draw!!!")

keep_alive()

client.run(os.getenv('TOKEN'))
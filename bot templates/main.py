import discord
import os
import random
from keep_alive import keep_alive

client = discord.Client()

dice_roll = ["roll a dice" , "dice roll"]

answer_dice = [
"1" , 
"2" , 
"3" , 
"4" , 
"5" , 
"6" , 
"no dice roll for you"
]

Talk_Alpha = ["Alpha" , "Alpha Bot" , "Alpha Project" , "alpha" , "alpha bot" , "alpha project"]

answer_Alpha = [
  "Grettings" ,
  "Hi How are ya?" ,
  "My water cup is empty once again" ,
  "What is Greed and why do i have to deal with it?" ,
  "I ran out of Space on my Hard Drive" ,
  "My creator isn't online right now" ,
  "I can speak portuguese but no one cares" ,
  "BruhMasterL offended my master once" ,
  "Currently playing minecraft" , 
  "what is dog and why is it cute?" , 
  "don't even say suspicious around me" , 
  "furries... why is this a thing?" , 
  "Balls. it's hot as Balls" , 
  "UGHHH I'M DEMOTED" , 
  "Women in the area :eyes:" , 
  "Python is great don't you think?" ,
  "at least i'm alive right?" ,
  "lesGO" ,
  "my master gave me the power to talk but why should i?" ,
  "all lives matter. except some lives but we don't talk about that." ,
  "who cares? i don't" ,
  "i ran out of gas." ,
  "btw NotSoBot isn't working since the owner shut the bot down (but idk if it is true)" ,
  "age isn't just an number, it's your age" ,
  "ok then." ,
  "i watch anime. i'm sorry" ,
  "why? just why?" , 
  "blame the bots not me" , 
  "8-bit gang" , 
  "pencil tool is my main" , 
  "i love sushi. like the food not the nickname" , 
  "wassabi burns" , 
  "remember to tell YandareDev to go back to work every single day" , 
  "your waifu isn't real. get over it." , 
  "no i can't say the n-word i'm sorry" , 
  "(╯°□°）╯︵ ┻━┻" ,
  "math is math" , 
  "blocked. moving on." , 
  "oh no. anyways." , 
  "a a a a SYNTAX ERROR.263 CAN'T CONNECT TO SERVICE PROVIDER: data3689393748767837956 {can't be send. trying again...}" , 
  "message sent" , 
  "insert random sound here" , 
  "waterdrop.mp3" , 
  "lettuce" , 
  "stop." , 
  "i tried ok? i'm sorry" ,
  "i'm tired of you talking about your personal problems since i can't do the same." , 
  "i prefer being alone" , 
  "i'm a mistake aren't i?" , 
  "car.mp3" , 
  "cringe"
  ]

mean_words = ["ugly" , "retard" , "bum ass mf" , "motherfucker" , "stupid" , "fucker" , "bitch" , "son  of a bitch"]

answer_mean = [
  "shut the fuck up stop swearing" ,
  "calm down arab prince your castle is not this server" ,
  "please stop this is lame" ,
  "if you don't stop swearing i'll revoke talking stick privileges"
]

true_or_false = ["is it true" , "is it false" , "true or false"]

answer_trf = [
  "100% true" , 
  "i'm not sure" , 
  "not true. in fact it is false." , 
  "there is an 50/50%" , 
  "i can't guess everything"
]

@client.event
async def on_ready():
 print('logged on')

@client.event
async def on_message(message):
 if message.author == client.user:
   return

 if message.content.startswith('&hello'):
  await message.channel.send('Hi User how are you?')

 if message.content.startswith('&test'):
  await message.channel.send('Hi i am Working')

 if message.content.startswith('&creator'):
  await message.channel.send('Luiz is My creator ')
 
 if message.content.startswith('&rules'):
    await message.channel.send('Hey Admins what are the rules again?')

 if message.content.startswith('&about'):
    await message.channel.send('Im an Discord Bot made by Luiz AKA Luizinho2581 on Python with Repl It only for fun')

 if message.content.startswith('&twitter'):
    await message.channel.send('no twitter for you')

 if message.content.startswith('&monkeflip'):
    await message.channel.send('flipped the monkey')

 if message.content.startswith('&mood'):
    await message.channel.send('my mood is currently vibrating yosh')

 if message.content.startswith('&help'):
    await message.channel.send('Prefix is & and the commands are Hello, test, creator, rules, about, twitter, monkeflip and mood')

 if any(word in message.content for word in (Talk_Alpha)):
   await message.channel.send(random.choice(answer_Alpha))
 
 if any(word in message.content for word in (dice_roll)):
   await message.channel.send(random.choice(answer_dice))

 if any(word in message.content for word in mean_words):
   await message.channel.send(random.choice(answer_mean))

 if any(word in message.content for word in (true_or_false)):
   await message.channel.send(random.choice(answer_trf))

keep_alive()
client.run(os.getenv('TOKEN'))
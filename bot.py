import discord
from discord import app_commands
import random

jokes = [
    "Why did the computer go to the doctor? Because it had a virus! 🦠",
    "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
    "Why was the math book sad? Because it had too many problems. 📖",
    "What do you call a fake noodle? An impasta! 🍝",
    "Why did the gamer cross the road? To get to the other side quest. 🎮"
    "Why did the scarecrow win an award? Because he was outstanding in his field. 🌾"

"What do you call fake spaghetti? An impasta. 🍝"

"Why don’t skeletons fight each other? They don’t have the guts. 💀"

"What’s brown and sticky? A stick. 🪵"

"Why did the bicycle fall over? It was two-tired. 🚲"

"What do you call cheese that isn’t yours? Nacho cheese. 🧀"

"Why can’t your nose be 12 inches long? Because then it would be a foot. 👃"

"What did one wall say to the other wall? I’ll meet you at the corner. 🧱"

"Why did the math book look sad? It had too many problems. 📚"

"What do you call a sleeping bull? A bulldozer. 🐂"

"What’s orange and sounds like a parrot? A carrot. 🥕"

"What do you call a cow with no legs? Ground beef. 🐄"

"What do you call a cow with two legs? Lean beef. 🐄"

"What do you call a cow with all four legs? A cow. 🐄"

"What do you call a fish wearing a bowtie? Sofishticated. 🐟"

"What do you call a dog magician? A Labracadabrador. 🐕✨"

"Why did the tomato turn red? It saw the salad dressing. 🍅"

"What did the ocean say to the beach? Nothing. It just waved. 🌊"

"Why did the gamer bring a ladder to the server? He heard the ping was high. 🎮"

"My Wi-Fi and I have a toxic relationship. It disappears whenever I need it most. 📶"

"Your game crashed. No, my PC just rage-quit for me. 💻"

"I tried to beat the final boss without taking damage. Unfortunately, the final boss had other plans. 🎮"

"Why did the NPC cross the road? Because the player walked into its trigger zone. 🕹️"

"My FPS is so low that I can see the frames taking turns. 🖥️"

"Why do programmers prefer dark mode? Because light attracts bugs. 🐛"

"A programmer’s favorite place? The Foo Bar. 💻"

"Why was the JavaScript developer sad? Because they didn’t know how to null their feelings. 😭"

"There are 10 kinds of people in the world: Those who understand binary and those who don’t. 💻"

"Why did the programmer quit his job? He didn’t get arrays. 👨‍💻"

"I named my dog Error. Now whenever I call him, everyone says, Error: dog not found. 🐕"

"Why is debugging like being a detective? Because you’re also the murderer. 🔎"

"What’s the best thing about Switzerland? I don’t know, but the flag is a big plus. 🇨🇭"

"Why did the chicken cross the road? To get to the other side. 🐔"

"What happens when you throw a green rock into the Red Sea? It gets wet. 🌊"

"What do you call a group of people standing in a line? A line. 👥"

"Why did the man fall into the well? He couldn’t see that well. 🕳️"

"What’s red and bad for your teeth? A brick. 🧱"

"Knock knock. Who’s there? Cow says. Cow says who? No, cow says moo. 🐄"

"What did the left eye say to the right eye? Something smells between us. 👀"

"Why did the computer go to the doctor? It had a virus. 💻🦠"

"What do you call a bear with no teeth? A gummy bear. 🐻"

"What do you call a pile of cats? A meowtain. 🐈"

"What do you call an alligator in a vest? An investigator. 🐊"

"What do you call a dinosaur that knows a lot of words? A thesaurus. 🦖📖"

"Why was six afraid of seven? Because seven ate nine. 6️⃣7️⃣"

"What did zero say to eight? Nice belt. 0️⃣8️⃣"

"What’s a pirate’s favorite letter? You’d think it’d be R, but it’s actually the C. 🏴‍☠️"

]

class MyBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

bot = MyBot()

@bot.tree.command(name="joke", description="Tells you a random joke")
async def joke(interaction: discord.Interaction):
    await interaction.response.send_message(random.choice(jokes))

bot.run("MTU0MjY5NDcyNzkxNTE0MzM1OA.Gd9y20.Kkb4UuFbo2NDXGQkZwhzAA3eQLHTvzAHweJg9Y")
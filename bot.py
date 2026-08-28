import os
import random
import discord
from discord import app_commands

# =========================
# TOKEN
# =========================

TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise RuntimeError(
        "DISCORD_TOKEN is not set. "
        "Add it in Railway → Variables."
    )


# =========================
# JOKES
# =========================

jokes = [
    "Why did the computer go to the doctor? Because it had a virus! 🦠",
    "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
    "Why was the math book sad? Because it had too many problems. 📖",
    "What do you call a fake noodle? An impasta! 🍝",
    "Why did the gamer cross the road? To get to the other side quest. 🎮",
    "Why did the scarecrow win an award? Because he was outstanding in his field. 🌾",
    "What do you call fake spaghetti? An impasta. 🍝",
    "Why don’t skeletons fight each other? They don’t have the guts. 💀",
    "What’s brown and sticky? A stick. 🪵",
    "Why did the bicycle fall over? It was two-tired. 🚲",
    "What do you call cheese that isn’t yours? Nacho cheese. 🧀",
    "Why can’t your nose be 12 inches long? Because then it would be a foot. 👃",
    "What did one wall say to the other wall? I’ll meet you at the corner. 🧱",
    "What do you call a sleeping bull? A bulldozer. 🐂",
    "What’s orange and sounds like a parrot? A carrot. 🥕",
    "What do you call a cow with no legs? Ground beef. 🐄",
    "What do you call a cow with two legs? Lean beef. 🐄",
    "What do you call a fish wearing a bowtie? Sofishticated. 🐟",
    "What do you call a dog magician? A Labracadabrador. 🐕✨",
    "Why did the tomato turn red? It saw the salad dressing. 🍅",
    "What did the ocean say to the beach? Nothing. It just waved. 🌊",
    "Why did the gamer bring a ladder to the server? He heard the ping was high. 🎮",
    "My Wi-Fi and I have a toxic relationship. It disappears whenever I need it most. 📶",
    "Your game crashed. No, my PC just rage-quit for you. 💻",
    "Why did the NPC cross the road? Because the player walked into its trigger zone. 🕹️",
    "My FPS is so low that I can see the frames taking turns. 🖥️",
    "A programmer’s favorite place? The Foo Bar. 💻",
    "There are 10 kinds of people in the world: Those who understand binary and those who don’t. 💻",
    "Why did the programmer quit his job? He didn’t get arrays. 👨‍💻",
    "I named my dog Error. Now whenever I call him, everyone says, Error: dog not found. 🐕",
    "What’s the best thing about Switzerland? I don’t know, but the flag is a big plus. 🇨🇭",
    "Why did the chicken cross the road? To get to the other side. 🐔",
    "What happens when you throw a green rock into the Red Sea? It gets wet. 🌊",
    "What do you call a group of people standing in a line? A line. 👥",
    "What’s red and bad for your teeth? A brick. 🧱",
    "Why did the computer go to the doctor? It had a virus. 💻🦠",
    "What do you call a bear with no teeth? A gummy bear. 🐻",
    "What do you call a pile of cats? A meowtain. 🐈",
    "What do you call an alligator in a vest? An investigator. 🐊",
    "What do you call a dinosaur that knows a lot of words? A thesaurus. 🦖📖",
    "Why was six afraid of seven? Because seven ate nine. 6️⃣7️⃣",
    "What did zero say to eight? Nice belt. 0️⃣8️⃣",
    "What’s a pirate’s favorite letter? You’d think it’d be R, but it’s actually the C. 🏴‍☠️",
]


# =========================
# SETTINGS
# =========================

COOLDOWN_SECONDS = 5

last_joke = None

# Channel ID -> GUI message ID
gui_messages = {}

# Channel ID -> last button usage timestamp
cooldowns = {}


# =========================
# GET JOKE
# =========================

def get_joke():
    global last_joke

    available = [
        joke for joke in jokes
        if joke != last_joke
    ]

    if not available:
        available = jokes

    joke = random.choice(available)
    last_joke = joke

    return joke


# =========================
# GUI EMBED
# =========================

def create_gui_embed():
    embed = discord.Embed(
        title="🎭 JOKE MACHINE",
        description=(
            "## 😂 Ready for a joke?\n\n"
            "Press the button below and I'll send a "
            "**random joke into this channel**.\n\n"
            "⏱️ **Cooldown:** 5 seconds\n"
            "🎲 **Random jokes:** ON\n"
            "🔁 **No instant repeats:** ON"
        ),
        color=discord.Color.blurple()
    )

    embed.set_footer(
        text="Joke Machine • Powered by Discord.py"
    )

    return embed


# =========================
# BUTTON GUI
# =========================

class JokeView(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="Tell Me a Joke",
        emoji="😂",
        style=discord.ButtonStyle.primary,
        custom_id="joke_machine_button"
    )
    async def joke_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        channel_id = interaction.channel.id

        now = discord.utils.utcnow().timestamp()

        last_used = cooldowns.get(channel_id, 0)
        remaining = COOLDOWN_SECONDS - (now - last_used)

        if remaining > 0:
            await interaction.response.send_message(
                f"⏳ **Cooldown!** Try again in "
                f"**{remaining:.1f}s**.",
                ephemeral=True
            )
            return

        cooldowns[channel_id] = now

        joke = get_joke()

        # Everyone sees this message.
        await interaction.response.send_message(
            f"## 😂 Joke!\n\n"
            f"{joke}\n\n"
            f"*Requested by {interaction.user.mention}*"
        )


# =========================
# BOT
# =========================

class MyBot(discord.Client):

    def __init__(self):
        intents = discord.Intents.default()

        super().__init__(intents=intents)

        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):

        # Persistent button
        self.add_view(JokeView())

        # Sync slash commands
        await self.tree.sync()

        print("✅ Slash commands synced!")


bot = MyBot()


# =========================
# /joke
# =========================

@bot.tree.command(
    name="joke",
    description="Create the Joke Machine"
)
async def joke(interaction: discord.Interaction):

    channel_id = interaction.channel.id

    # Don't create another GUI if one already exists.
    if channel_id in gui_messages:

        try:
            await interaction.channel.fetch_message(
                gui_messages[channel_id]
            )

            await interaction.response.send_message(
                "🎭 **The Joke Machine is already here!**",
                ephemeral=True
            )

            return

        except discord.NotFound:
            # GUI was deleted, so make a new one.
            del gui_messages[channel_id]

    embed = create_gui_embed()

    message = await interaction.channel.send(
        embed=embed,
        view=JokeView()
    )

    gui_messages[channel_id] = message.id

    await interaction.response.send_message(
        "✅ **Joke Machine created!**",
        ephemeral=True
    )


# =========================
# START BOT
# =========================

print("🚀 Starting Joke Machine...")

bot.run(TOKEN)

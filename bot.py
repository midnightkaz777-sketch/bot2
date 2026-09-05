import os
import sys
import time
import logging

import discord
from discord.ext import commands
from dotenv import load_dotenv

# =========================
# CONFIG
# =========================

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise RuntimeError(
        "DISCORD_TOKEN is not set. "
        "Add it in Railway → Variables."
    )

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger("bot")

# =========================
# BOT SETUP
# =========================

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    logger.info(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")


# =========================
# COMMANDS
# =========================

@bot.command(name="ping")
async def ping(ctx: commands.Context):
    """Responds with the bot's current latency."""
    latency_ms = round(bot.latency * 1000)
    await ctx.send(f"🏓 Pong! Latency: {latency_ms}ms")


@bot.command(name="hello")
async def hello(ctx: commands.Context):
    """Greets the user who invoked the command."""
    await ctx.send(f"👋 Hello, {ctx.author.mention}!")


# =========================
# START BOT WITH AUTO-RESTART
# =========================

def run_bot():
    """Runs the bot and automatically restarts it if it crashes."""
    retry_delay = 5  # seconds

    while True:
        try:
            logger.info("🚀 Starting bot...")
            bot.run(TOKEN)
            # bot.run() returns when the bot is closed gracefully.
            logger.info("Bot stopped gracefully. Exiting.")
            break
        except Exception as exc:
            logger.exception(f"Bot crashed with an error: {exc}")
            logger.info(f"Restarting in {retry_delay} seconds...")
            time.sleep(retry_delay)
        except KeyboardInterrupt:
            logger.info("Bot stopped manually. Exiting.")
            sys.exit(0)


if __name__ == "__main__":
    run_bot()

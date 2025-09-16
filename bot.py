import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime, timezone, timedelta
import os  # ✅ Added for secure token access

# ✅ Setup intents
intents = discord.Intents.default()
intents.message_content = True

# ✅ Create bot instance
bot = commands.Bot(command_prefix="!", intents=intents)

# ✅ Owner ID
OWNER_ID = 1396835970015432727

# ✅ Bot ready event
@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} commands")
    except Exception as e:
        print(f"❌ Error syncing commands: {e}")
    print(f"🤖 Bot is online as {bot.user} (ID: {bot.user.id})")

# ✅ /executor command (owner-only)
@bot.tree.command(name="executor", description="Show executor links")
async def executor(interaction: discord.Interaction):
    if interaction.user.id != OWNER_ID:
        await interaction.response.send_message("You're not the owner bitch", ephemeral=True)
        return

    banner_embed = discord.Embed(color=discord.Color.blue())
    banner_embed.set_image(
        url="https://cdn.discordapp.com/attachments/1406249392570241136/1417352043781427241/New_Project_C94D156.png"
    )

    list_embed = discord.Embed(
        description=(
            "**``Android``**\n"
            "> **Fluxus** [**``Visit``**](https://deltaexploits.gg/)\n"
            "> **Evon** [**``Download``**](https://evon.cc/android/dl-a/Evon.apk)\n"
            "> **Codex** [**``Download``**](https://www.mediafire.com/file/kxpmihdc91o6tgz/Codex_v2.688.apk/file)\n"
            "> **Vega X** [**``Download``**](https://github.com/1f0yt/community/releases/download/Vegax/Vega.X.apk)\n"
            "> **Krnl** [**``Download``**](https://krnl.webfiles.pro/android.html)\n"
            "> **Delta** [**``Download``**](https://updowncontent.com/android.html)\n"
            "> **Ronix** [**``Download``**](https://wrdcdn.net/r/154522/1756076289297/Ronix_687.apk)\n"
            "> **Cryptic** [**``Download``**](https://www.mediafire.com/file/e5hr95v8eupsfl1/Cryptic+2.687.816+APK.apk/file)\n"
            "> **FrostWare** [**``Download``**](https://www.mediafire.com/file/o9lxcvef190r77h/Frostware+Gen-X+V3.8(fixed).apk/file)\n"
            "> **Arceus X** [**``Download``**](https://www.mediafire.com/file/zetrzozo17won9l/Roblox+-+Arceus+X+v5+1.0.8.apk/file)\n"
            "> **Trigon** [**``Download``**](https://www.mediafire.com/file/tqod645iwzrmyf4/Trigon_2.687.816.apk/file)\n"
            "> **Rift**\n"
            "\n"
            "- **``iOS``**\n"
            "> **Delta** [**``Download``**](https://gloopup.net/Delta/ios/)\n"
            "> **Krnl** [**``Download``**](https://krnl.webfiles.pro/ios.html)\n"
        ),
        color=discord.Color.blurple()
    )
    list_embed.set_image(
        url="https://cdn.discordapp.com/attachments/1405117065668591619/1417385945291821076/New_Project_11_AA602D9.png"
    )

    await interaction.response.send_message(embeds=[banner_embed, list_embed])

# ✅ /info command (owner-only)
@bot.tree.command(name="info", description="Get info about this bot")
async def info(interaction: discord.Interaction):
    if interaction.user.id != OWNER_ID:
        await interaction.response.send_message("You're not the owner bitch", ephemeral=True)
        return

    await interaction.response.send_message("I provided executor")

# ✅ /purge_all command (owner-only, instant delete)
@bot.tree.command(name="purge_all", description="Delete messages in this channel")
@app_commands.describe(amount="Number of messages to delete")
async def purge_all(interaction: discord.Interaction, amount: int):
    if interaction.user.id != OWNER_ID:
        await interaction.response.send_message("You're not the owner bitch", ephemeral=True)
        return

    if not interaction.channel.permissions_for(interaction.guild.me).manage_messages:
        await interaction.response.send_message("❌ I need 'Manage Messages' permission to purge.", ephemeral=True)
        return

    if amount > 200:
        await interaction.response.send_message("❌ Max purge limit is 200 messages.", ephemeral=True)
        return

    deleted = 0
    two_weeks_ago = datetime.now(timezone.utc) - timedelta(days=14)

    async for msg in interaction.channel.history(limit=amount):
        try:
            await msg.delete()
            deleted += 1
        except:
            continue

    await interaction.response.send_message(f"✅ Instantly purged {deleted} messages.")

# ✅ Run the bot securely
print("🔑 Starting bot...")
try:
    bot.run(os.getenv("TOKEN"))  # ✅ Secure token access for Render
except Exception as e:
    print(f"❌ Failed to start bot: {e}")
import pyperclip
import emoji

# Emoji to copy to the clipboard
emoji_to_copy = ":thumbs_up:"

# Convert emoji code to actual emoji
emoji_text = emoji.emojize(emoji_to_copy)

# Copy the emoji text to the clipboard
pyperclip.copy(emoji_text)

# Paste the copied emoji text from the clipboard
pasted_emoji = pyperclip.paste()

print(f"Pasted emoji: {pasted_emoji}")

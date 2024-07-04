from instabot import Bot

# Create an instance of Bot
bot = Bot()

# Login to Instagram
bot.login(username="your_instagram_username", password="your_instagram_password")

# Function to send messages
def send_dm(usernames, message):
    for username in usernames:
        bot.send_message(message, [username])

if __name__ == "__main__":
    import sys
    import json

    data = json.loads(sys.argv[1])
    usernames = data["usernames"]
    message = data["message"]
    send_dm(usernames, message)

# MultiPurpose-Bot

This is a MultiPurpose Discord bot that can perform Google Searches and can play games with you! It is built using Discord's and Google's Python Libraries.

# To set up:
 1) Create your own Bot at https://discord.com/developers/applications
 2) Get your Bot's token and give it "Administration" permissions
 3) In the OAuth2 section, under URL generator, give the bot the "bot" scope and choose "Administrator" Permissions. You should now see a URL for your bot on your screen
 4) In the "Bot" section, under "Privileged Gateway Intents", enable all intents
 5) Paste your Bot's Token into the Token string variable in main.py
 6) Paste the URL you generated in step 3 into your browser and add the bot to any server you are an admin in!
 7) If there isn't one already, create a "bot" channel in your discord server, this is where the bot will be able to talk!

## Usage
This bot responds to certain commands, including:

- !rps: Plays Rock Paper Scissors with you!
- !hello: Responds with a greeting message.
- !bs: Allows you to play Battleship
- !google "query" (without quotation marks): Google searches the given query and presents the top 5 results

## Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Any contributions are welcome!

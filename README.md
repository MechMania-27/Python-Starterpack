# Python-Starterpack

Thank you for coming out to the 27th edition of MechMania!

This is the starter pack for writing your own bot in Python.

Your job is to edit the strategy within **bot.py** and submit it using `mm push` for consideration in the competition. More information about how to install the MechMania command line tools are available in the [Wiki](https://github.com/MechMania-27/Wiki)

More information about the game mechanics are detailed here: [Wiki](https://github.com/MechMania-27/Wiki)

Most of the classes that you'll need to build your own bot have already been imported, and a basic bot that moves around semi-randomly has also been implemented. Your job now is to try to build bots that can get you all the achievements and build a bot that can beat all of the other bots in the competition.

You are allowed to look at any file in this repository.

Make sure to set an `Item` and `Upgrade` to use from the enum class `ItemType` and `UpgradeType` within the `Game` constructor in the `main` method.

You'll primarily need to look at the classes within the **model** package and the **model.decisions** package for information about the decisions that you are allowed to send and what those inputs are. We have also provided you with some helper functions within the **api.game_util** package and game constants within the **api.constants** package. Many of these values have been set already through the **resources/mm27.properties** file, so if you don't see an explicit value, check there.

Note: Please do not print out debug statements using `print()`. Use the provided `logger` object (`logger.info("message")` and `logger.debug("message")`).

If you have any questions, do not hesitate to contact us through Discord with any questions!

Good luck!

### Testing your bot
See the Engine JAR release here: https://github.com/MechMania-27/Wiki/releases/ for instructions on how to compile and run the engine with your bot

### Note about ML (Machine Learning)
Due to the format of the infrastructure surrounding running the bot, it is difficult/impossible to store information between games. However, you are allowed to store information between turns of a game (since all variables available to you in bot.py are available to you throughout the entire game).

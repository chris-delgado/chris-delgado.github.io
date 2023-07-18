---
layout: post
title: Arkham Horror Chaos Bag Simulator
image: "/posts/ArkhamHorror.jpeg"
tags: [JavaScript, CSS, HTML]
---
# Background
_Link to the app [here](https://chris-delgado.github.io/chaosbag/)._

A key component of the game mechanics in Arkham Horror: The Card Game is the Chaos Bag. It represents the ever-shifting forces of fate, randomness, and the unknown that the investigators must contend with during their encounters. The Chaos Bag is a collection of tokens that are specific to each scenario and difficulty level. The tokens are marked with different symbols and modifiers that represent positive or negative outcomes for the players.

The Chaos Bag adds an element of unpredictability and tension to the game, as players must consider the risks and rewards associated with each action they take. It introduces a sense of uncertainty and forces players to adapt their strategies accordingly, helping to make each playthrough unique and challenging.

# Features
I decided to implement this aspect of the game as a web app with the following features/functionality:
- Draw Token: Randomly selects a token from the chaos bag
- Reveal Another: Select another token from the chaos bag excluding those already drawn
- Draw History: Display history of token draws
- Modify Bag: Add or remove tokens from the chaos bag


Additional features available:
- Toggle draw odds
- Toggle reference text for symbol tokens
- Save/load/rename/delete profiles

# Future Enhancements
I'd like to make the following changes to this app:
- Move profile storage from the browser's localStorage to a database
- Modularize the JavaScript to pull out constants

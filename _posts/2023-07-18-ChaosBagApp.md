---
layout: post
title: Arkham Horror Chaos Bag Simulator
image: "/posts/ArkhamHorror.jpeg"
tags: [JavaScript, CSS, HTML]
---
Link to the app: https://chris-delgado.github.io/chaosbag/

# Background
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

# Code
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Arkham Horror Chaos Bag</title>
  <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
  <div id="app">
    <h1>Arkham Horror Chaos Bag</h1>
    <h4 id="subtitle"></h4>

  <div id="chaos-bag">
    <div id="instructions">
        <ul>
            <li>
              <h3>Draw Token</h3>
              <span>Randomly select a token from the chaos bag</span>
            </li>
            <li>
              <h3>Reveal Another</h3>
              <span>Select another token from the chaos bag excluding those already drawn</span>
            </li>
            <li>
              <h3>Draw History</h3>
              <span>Display history of token draws</span>
            </li>
            <li>
              <h3>Modify Bag</h3>
              <span>Add or remove tokens from the chaos bag</span>
            </li>
        </ul>
    </div>
  
    <div id="drawn-token">
      <span id="token-image"></span>
      <p id="drawn-token-value"></p>
      <p id="token-reference-text"></p>
    </div>
    <div>
      <button  class="button-style" id="draw-token-button">Draw Token</button>
      <button  class="button-style" id="reveal-another-button">Reveal Another</button>
      <button  class="button-style" id="history-button">Draw History</button>
      <button  class="button-style" id="modify-bag-button">Modify Bag</button>
    </div>
  </div>

  <div id="overlay">
    <h2>Presets</h2>

    <div id="odds-toggle">
        <label for="display-odds">Display Odds:</label>
        <input type="checkbox" id="display-odds">
    </div>

    <div id="reference-toggle">
      <label for="display-reference">Display Scenario Reference Text:</label>
      <input type="checkbox" id="display-reference" checked>
    </div>

    <div id="campaign-selector">
        <label for="campaign">Campaign:</label>
        <select id="campaign">
            <option value="The Night of the Zealot">The Night of the Zealot</option>
            <option value="The Dunwich Legacy">The Dunwich Legacy</option>
            <option value="The Path to Carcosa">The Path to Carcosa</option>
            <option value="The Forgotten Age">The Forgotten Age</option>
            <option value="The Circle Undone">The Circle Undone</option>
            <option value="The Dream-Eaters">The Dream-Eaters</option>
            <option value="The Innsmouth Conspiracy">The Innsmouth Conspiracy</option>
            <option value="Edge of the Earth">Edge of the Earth</option>
            <option value="The Scarlet Keys">The Scarlet Keys</option>
        </select>
    </div>

    <div id="scenario-selector">
      <label for="scenario">Scenario:</label>
      <select id="scenario"></select>
    </div>
    
    <div id="difficulty-selector">
      <label for="difficulty">Difficulty:</label>
      <select id="difficulty">
          <option value="easy">Easy</option>
          <option value="standard">Standard</option>
          <option value="hard">Hard</option>
          <option value="expert">Expert</option>
      </select>
    </div>

    <h2>Profiles</h2>
    <label for="profile"></label>
    <select id="profile"></select><br>
    <button class="button-style-2" id="save-button">Save</button>
    <button class="button-style-2" id="load-button">Load</button>
    <button class="button-style-2" id="rename-button">Rename</button>
    <button class="button-style-2" id="delete-button">Delete</button>

    <button id="close-overlay">X</button>
    
    <h2>Add/Remove Tokens</h2>
    <label for="token-input"></label>
    <select id="token-input" title="Choose an option">
        <option value=""></option>
        <option value="1">1</option>
        <option value="0">0</option>
        <option value="-1">-1</option>
        <option value="-2">-2</option>
        <option value="-3">-3</option>
        <option value="-4">-4</option>
        <option value="-5">-5</option>
        <option value="-6">-6</option>
        <option value="-7">-7</option>
        <option value="-8">-8</option>
        <option value="frost">Frost</option>
        <option value="skull">Skull</option>
        <option value="cultist">Cultist</option>
        <option value="tablet">Tablet</option>
        <option value="elder_thing">Elder Thing</option>
        <option value="auto_fail">Autofail</option>
        <option value="elder_sign">Elder Sign</option>
        <option value="bless">Bless</option>
        <option value="curse">Curse</option>
    </select>
    <button class="button-style-2" id="add-token-button">+</button>
    <button class="button-style-2" id="remove-token-button">-</button>

    <h2>Bag Contents (<span id="bag-total"></span>)</h2>
    <div id="bag-contents">
        <div class="row">
            <img class="token-image" src="" alt="">
        </div>
    </div>
  </div>

  <div id="history-overlay">
    <button id="close-history-overlay">X</button>
    <h2>Draw History (<span id="draw-history-total"></span>)</h2>
    <button class="button-style-2" id="clear-history-button">Clear</button>
    <div id="draw-history" class="row"></div>
  </div>
  
  <script src="main.js"></script>
</body>
</html>
```

```css
@import url('https://fonts.cdnfonts.com/css/birmingham');

:root {
  --primary-color: #ff4136;
  --text-color: #fff;
  --secondary-color: #85144b;
  --disabled-color: #999;
}

body {
  font-family: 'Birmingham', sans-serif;
  background-color: #1a1a1a;
  color: var(--text-color);
  margin: 0;
  padding: 20px;
}

#app {
  max-width: 600px;
  margin: 0 auto;
}

h1, h4 {
  text-align: center;
  color: var(--text-color);
}

h2 {
  color: grey;
}

h3 {
  color: var(--primary-color);
}

#chaos-bag {
  background-color: #333;
  padding: 0;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(255, 255, 255, 0.1);
  text-align: center;
}

#chaos-bag button {
  margin: 10px;
}

#drawn-token-value {
  display: flex;
  flex-wrap: wrap;
  max-width: 100%;
  font-size: 24px; /* font size for odds*/
  font-weight: bold;
  margin-top: 0; /* margin between token and odds*/
}

.button-style,
.button-style-2 {
  background-color: var(--primary-color);
  color: var(--text-color);
  border: none;
  padding: 10px 20px;
  margin: 10px 0;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
  font-family: 'Birmingham', sans-serif;
}

.button-style {
  width: 200px;  /* Set the width */
}

#draw-token-button:hover,
#reveal-another-button:hover,
#modify-bag-button:hover,
#add-token-button:hover,
#remove-token-button:hover,
#history-button:hover,
#save-button:hover,
#load-button:hover,
#clear-button:hover,
#rename-button:hover,
#clear-history-button:hover {
  background-color: var(--secondary-color);
}

#overlay, #history-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.9);
  display: none;
  z-index: 9999;
  overflow: auto; /* Enable scrolling */
}

.overlay-visible {
  display: block !important;
}

#close-overlay, #close-history-overlay {
  position: absolute;
  top: 20px;
  right: 20px;
  font-size: 24px;
  background: none;
  border: none;
  color: #ffffff;
  cursor: pointer;
}

#bag-contents {
  margin-top: 20px;
}

#instructions ul {
  list-style-type: none; /* Remove the bullet points */
  padding-left: 0; /* Remove the default left padding */
}

/* This is the styling for the bag contents */

.row {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  margin-bottom: 10px;
}

.row span {
  margin: 0px;
  display: flex;
  align-items: center;
  justify-content: center;
}

#draw-token-button:disabled,
#reveal-another-button:disabled {
  background-color: #999;
  cursor: not-allowed;
  position: relative;
}

#reveal-another-button:disabled:hover {
  background-color: #999;
}

#reveal-another-button:disabled::before {
  /*content: 'No tokens have been drawn';*/
  position: absolute;
  top: -30px;
  left: 50%;
  transform: translateX(-50%);
  background-color: rgba(0, 0, 0, 0.8);
  color: #fff;
  padding: 5px;
  border-radius: 3px;
  font-size: 12px;
  white-space: nowrap;
  visibility: hidden;
  opacity: 0;
  transition: visibility 0s, opacity 0.3s;
}

#reveal-another-button:disabled:hover::before {
  visibility: visible;
  opacity: 1;
}

/* icomoon images below*/
@font-face {
  font-family: 'icomoon';
  src:  url('fonts/icomoon.eot?6emcqo');
  src:  url('fonts/icomoon.eot?6emcqo#iefix') format('embedded-opentype'),
        url('fonts/icomoon.ttf?6emcqo') format('truetype'),
        url('fonts/icomoon.woff?6emcqo') format('woff'),
        url('fonts/icomoon.svg?6emcqo#icomoon') format('svg');
  font-weight: normal;
  font-style: normal;
  font-display: block;
}

[class^="icon-"],
[class*=" icon-"] {
  /* use !important to prevent issues with browser extensions that change fonts */
  font-family: 'icomoon' !important;
  font-style: normal;
  font-weight: normal;
  font-variant: normal;
  text-transform: none;
  line-height: 1;
  font-size: 96px;
  /* Better Font Rendering =========== */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.icon-token_frost_sealed:before {
  content: "\e939";
}
.icon-token_frost_highlight:before {
  content: "\e937";
}
.icon-token_frost_overlay:before {
  content: "\e938";
}
.icon-token_cultist_sealed:before {
  content: "\e900";
  color: rgb(124, 195, 124);
}
.icon-token_-2_sealed:before {
  content: "\e901";
}
.icon-token_-3_sealed:before {
  content: "\e902";
}
.icon-token_-4_sealed:before {
  content: "\e903";
}
.icon-token_-5_sealed:before {
  content: "\e904";
}
.icon-token_-6_sealed:before {
  content: "\e905";
}
.icon-token_-7_sealed:before {
  content: "\e906";
}
.icon-token_-8_sealed:before {
  content: "\e907";
}
.icon-token_tablet_sealed:before {
  content: "\e908";
}
.icon-token_1_sealed:before {
  content: "\e909";
}
.icon-token_0_sealed:before {
  content: "\e90a";
}
.icon-token_curse_sealed:before {
  content: "\e90b";
  color: rgb(106, 9, 106);
}
.icon-token_bless_sealed:before {
  content: "\e90c";
  color: rgb(255, 255, 104);
}
.icon-token_skull_sealed:before {
  content: "\e90d";
  color: rgb(222, 171, 171);
}
.icon-token_elder_thing_sealed:before {
  content: "\e90e";
}
.icon-token_elder_sign_sealed:before {
  content: "\e90f";
}
.icon-token_auto_fail_sealed:before {
  content: "\e910";
  color: red;
}
.icon-token_-1_sealed:before {
  content: "\e911";
}
.icon-token_sealed_outline:before {
  content: "\e912";
}
.icon-tap_circle:before {
  content: "\e913";
}
.icon-token_auto_fail_overlay:before {
  content: "\e914";
}
.icon-token_bless_fill:before {
  content: "\e915";
}
.icon-token_elder_thing_overlay:before {
  content: "\e916";
}
.icon-token_elder_thing_fill:before {
  content: "\e917";
}
.icon-token_tablet_fill:before {
  content: "\e918";
}
.icon-token_tablet_overlay:before {
  content: "\e919";
}
.icon-token_cultist_fill:before {
  content: "\e91a";
}
.icon-token_auto_fail_highlight:before {
  content: "\e91b";
  color: red;
}
.icon-token_elder_sign_fill:before {
  content: "\e91c";
}
.icon-token_elder_sign_overlay:before {
  content: "\e91d";
}
.icon-token_elder_sign_highlight:before {
  content: "\e91e";
  color: skyblue;
}
.icon-token_curse_fill:before {
  content: "\e91f";
}
.icon-token_curse_overlay:before {
  content: "\e920";
}
.icon-token_-2_highlight:before {
  content: "\e921";
}
.icon-token_-3_highlight:before {
  content: "\e922";
}
.icon-token_-4_highlight:before {
  content: "\e923";
}
.icon-token_-5_highlight:before {
  content: "\e924";
}
.icon-token_-6_highlight:before {
  content: "\e925";
}
.icon-token_-7_highlight:before {
  content: "\e926";
}
.icon-token_-8_highlight:before {
  content: "\e927";
}
.icon-token_0_highlight:before {
  content: "\e928";
}
.icon-token_1_highlight:before {
  content: "\e929";
}
.icon-token_-1_highlight:before {
  content: "\e92a";
}
.icon-token_number_fill:before {
  content: "\e92b";
}
.icon-token_cultist_overlay:before {
  content: "\e92c";
}
.icon-token_cultist_highlight:before {
  content: "\e92d";
  color: rgb(177, 228, 177);
}
.icon-token_elder_thing_highlight:before {
  content: "\e92e";
  color: white;
}
.icon-token_tablet_highlight:before {
  content: "\e92f";
  color: rgb(210, 230, 233);
}
.icon-token_skull_overlay:before {
  content: "\e930";
}
.icon-token_symbol_fill:before {
  content: "\e931";
}
.icon-token_skull_highlight:before {
  content: "\e932";
  color: rgb(222, 171, 171);
}
.icon-token_bless_overlay:before {
  content: "\e933";
}
.icon-token_number_overlay:before {
  content: "\e934";
}
.icon-token_plus_highlight:before {
  content: "\e935";
  color: #4f5a60;
}
.icon-token_dismiss_highlight:before {
  content: "\e936";
  color: #800000;
}
.icon-token_sealed_outline_no_border:before {
  content: "\e93a";
}

.icon-token_elder_sign_sealed:before {
  color: skyblue;
}

[class^="icon-token_"]:not(.icon-token_elder_sign_highlight):not(.icon-token_auto_fail_highlight):not(.icon-token_skull_highlight):not(.icon-token_cultist_highlight):not(.icon-token_tablet_highlight):not(.icon-token_bless_sealed):not(.icon-token_curse_sealed):not(.icon-token_elder_thing_highlight):before {
  color: white;
}
```

```javascript
const skull = 'icon-token_skull_highlight';
const cultist = 'icon-token_cultist_highlight';
const tablet = 'icon-token_tablet_highlight';
const elderThing = 'icon-token_elder_thing_highlight';
const normalizedDifficulty = difficulty === 'easy' || difficulty === 'standard' ? 'front' : 'back'

const tokenNames = [
  "icon-token_1_sealed",
  "icon-token_0_sealed",
  "icon-token_-1_sealed",
  "icon-token_-2_sealed",
  "icon-token_-3_sealed",
  "icon-token_-4_sealed",
  "icon-token_-5_sealed",
  "icon-token_-6_sealed",
  "icon-token_-7_sealed",
  "icon-token_-8_sealed",
  "icon-token_skull_highlight",
  "icon-token_cultist_highlight",
  "icon-token_tablet_highlight",
  "icon-token_elder_thing_highlight",
  "icon-token_auto_fail_highlight",
  "icon-token_elder_sign_highlight",
  "icon-token_frost_sealed",
  "icon-token_bless_sealed",
  "icon-token_curse_sealed"
];

const presets = {
  'The Night of the Zealot': {
    easy: [2, 3, 3, 2, 0, 0, 0, 0, 0, 0, 2, 1, 1, 0, 1, 1, 0, 0, 0],
    standard: [1, 2, 3, 2, 1, 1, 0, 0, 0, 0, 2, 1, 1, 0, 1, 1, 0, 0, 0],
    hard: [0, 3, 2, 2, 2, 1, 1, 0, 0, 0, 2, 1, 1, 0, 1, 1, 0, 0, 0],
    expert: [0, 1, 2, 2, 2, 2, 1, 1, 0, 1, 2, 1, 1, 0, 1, 1, 0, 0, 0]
  },
  'The Dunwich Legacy': {
    easy: [2, 3, 3, 2, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 1, 0, 0, 0],
    standard: [1, 2, 3, 2, 1, 1, 0, 0, 0, 0, 2, 1, 0, 0, 1, 1, 0, 0, 0],
    hard: [0, 3, 2, 2, 2, 1, 1, 0, 0, 0, 2, 1, 0, 0, 1, 1, 0, 0, 0],
    expert: [0, 1, 2, 2, 2, 2, 1, 1, 0, 1, 2, 1, 0, 0, 1, 1, 0, 0, 0]
  },
  'The Path to Carcosa': {
    easy: [2, 3, 3, 2, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 1, 0, 0, 0],
    standard: [1, 2, 3, 2, 1, 1, 0, 0, 0, 0, 3, 0, 0, 0, 1, 1, 0, 0, 0],
    hard: [0, 3, 2, 2, 2, 1, 1, 0, 0, 0, 3, 0, 0, 0, 1, 1, 0, 0, 0],
    expert: [0, 1, 2, 2, 2, 2, 1, 1, 0, 1, 3, 0, 0, 0, 1, 1, 0, 0, 0]
  },
  'The Forgotten Age': {
    easy: [2, 3, 2, 1, 1, 0, 0, 0, 0, 0, 2, 0, 0, 1, 1, 1, 0, 0, 0],
    standard: [1, 3, 1, 2, 1, 0, 1, 0, 0, 0, 2, 0, 0, 1, 1, 1, 0, 0, 0],
    hard: [1, 2, 1, 1, 2, 1, 0, 1, 0, 0, 2, 0, 0, 1, 1, 1, 0, 0, 0],
    expert: [0, 1, 1, 2, 2, 2, 0, 1, 0, 1, 2, 0, 0, 1, 1, 1, 0, 0, 0]
  },
  'The Circle Undone': {
    easy: [2, 3, 2, 1, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 1, 0, 0, 0],
    standard: [1, 2, 2, 2, 1, 1, 0, 0, 0, 0, 2, 0, 0, 0, 1, 1, 0, 0, 0],
    hard: [0, 2, 2, 2, 1, 1, 1, 0, 0, 0, 2, 0, 0, 0, 1, 1, 0, 0, 0],
    expert: [0, 1, 2, 2, 1, 1, 0, 1, 0, 1, 2, 0, 0, 0, 1, 1, 0, 0, 0]
  },
  'The Dream-Eaters': {
    easy: [2, 3, 2, 2, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 1, 1, 0, 0, 0],
    standard: [1, 2, 2, 2, 1, 1, 0, 0, 0, 0, 0, 1, 2, 0, 1, 1, 0, 0, 0],
    hard: [0, 2, 2, 2, 2, 1, 1, 0, 0, 0, 0, 1, 2, 0, 1, 1, 0, 0, 0],
    expert: [0, 1, 2, 2, 1, 2, 1, 1, 0, 1, 0, 1, 2, 0, 1, 1, 0, 0, 0]
  },
  'The Innsmouth Conspiracy': {
    easy: [2, 3, 3, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 1, 1, 0, 0, 0],
    standard: [1, 2, 3, 2, 1, 1, 0, 0, 0, 0, 2, 2, 2, 2, 1, 1, 0, 0, 0],
    hard: [0, 3, 2, 2, 2, 1, 1, 0, 0, 0, 2, 2, 2, 2, 1, 1, 0, 0, 0],
    expert: [0, 1, 2, 2, 2, 2, 1, 1, 0, 1, 2, 2, 2, 2, 1, 1, 0, 0, 0]
  },
  'Edge of the Earth': {
    easy: [3, 2, 3, 2, 0, 0, 0, 0, 0, 0, 2, 1, 1, 0, 1, 1, 0, 0, 0],
    standard: [1, 2, 3, 2, 1, 1, 0, 0, 0, 0, 2, 1, 1, 0, 1, 1, 1, 0, 0],
    hard: [0, 2, 2, 2, 1, 2, 1, 0, 0, 0, 2, 1, 1, 0, 1, 1, 2, 0, 0],
    expert: [0, 1, 1, 2, 1, 2, 1, 0, 1, 0, 2, 1, 1, 0, 1, 1, 3, 0, 0]
  },
  'The Scarlet Keys': {
    easy: [2, 3, 3, 2, 0, 0, 0, 0, 0, 0, 2, 0, 1, 1, 1, 1, 0, 0, 0],
    standard: [1, 2, 3, 2, 1, 1, 0, 0, 0, 0, 2, 0, 1, 1, 1, 1, 0, 0, 0],
    hard: [0, 3, 2, 2, 2, 1, 1, 0, 0, 0, 2, 0, 1, 1, 1, 1, 0, 0, 0],
    expert: [0, 1, 2, 2, 2, 2, 1, 1, 0, 1, 2, 0, 1, 1, 1, 1, 0, 0, 0]
  },
};

const scenarios = {
  'The Night of the Zealot': ['The Gathering', 'The Midnight Masks', 'The Devourer Below'],
  'The Dunwich Legacy': ['Extracurricular Activity', 'The House Always Wins', 'The Miskatonic Museum', 'The Essex County Express', 'Blood on the Altar', 'Undimensioned and Unseen', 'Where Doom Awaits', 'Lost in Time and Space'],
  'The Path to Carcosa': ['Curtain Call', 'The Last King', 'Echoes of the Past', 'The Unspeakable Oath', 'A Phantom of Truth', 'The Pallid Mask', 'Black Stars Rise', 'Dim Carcosa'],
  'The Forgotten Age': ['The Untamed Wilds', 'The Doom of Eztli', 'Threads of Fate', 'The Boundary Beyond', 'Heart of the Elders', 'The City of Archives', 'The Depths of Yoth', 'Shattered Aeons', 'Turn Back Time'],
  'The Circle Undone': ['Disappearance at the Twilight Estate', 'The Witching Hour', 'The Secret Name', 'The Wages of Sin', 'For the Greater Good', 'Union and Disillusion', 'In the Clutches of Chaos', 'Before the Black Throne'],
  'The Dream-Eaters': ['Beyond the Gates of Sleep', 'Waking Nightmare', 'The Search for Kadath', 'A Thousand Shapes of Horror', 'Dark Side of the Moon', 'Point of No Return', 'Where the Gods Dwell', 'Weaver of the Cosmos'],
  'The Innsmouth Conspiracy': ['The Pit of Despair', 'The Vanishing of Elina Harper', 'In Too Deep', 'Devil Reef', 'Horror in High Gear', 'A Light in the Fog', 'The Lair of Dagon', 'Into the Maelstrom'],
  'Edge of the Earth': ['Ice and Death', 'Fatal Mirage', 'To the Forbidden Peaks', 'City of the Elder Things', 'The Heart of Madness'],
  'The Scarlet Keys': ['Riddles and Rain', 'Dancing Mad', 'Dead Heat', 'Dealings in the Dark', 'Dogs of War', 'On Thin Ice', 'Sanguine Shadows', 'Shades of Suffering', 'Without a Trace', 'Congress of the Keys']
};

// HTML Elements
const htmlElements = {
  contentContainer: document.getElementById('drawn-token-value'),
  tokenImage: document.getElementById('token-image'),
  campaignSelector: document.getElementById('campaign'),
  scenarioSelector: document.getElementById('scenario'),
  difficultySelector: document.getElementById('difficulty'),
  drawTokenButton: document.getElementById('draw-token-button'),
  addTokenButton: document.getElementById('add-token-button'),
  removeTokenButton: document.getElementById('remove-token-button'),
  tokenInput: document.getElementById('token-input'),
  modifyBagButton: document.getElementById('modify-bag-button'),
  overlay: document.getElementById('overlay'),
  closeOverlayButton: document.getElementById('close-overlay'),
  bagContents: document.getElementById('bag-contents'),
  displayOddsCheckbox: document.getElementById('display-odds'),
  displayReferenceCheckbox: document.getElementById('display-reference'),
  revealAnotherButton: document.getElementById('reveal-another-button'),
  historyButton: document.getElementById('history-button'),
  instructionsElement: document.getElementById('instructions'),
  subtitle: document.getElementById('subtitle'),
  closeHistoryOverlayButton: document.getElementById('close-history-overlay'),
  historyOverlay: document.getElementById('history-overlay'),
  drawHistory: document.getElementById('draw-history'),
  drawHistoryTotal: document.getElementById('draw-history-total'),
  saveButton: document.getElementById('save-button'),
  loadButton: document.getElementById('load-button'),
  profile: document.getElementById('profile'),
  deleteButton: document.getElementById('delete-button'),
  renameButton: document.getElementById('rename-button'),
  clearHistoryButton: document.getElementById('clear-history-button'),
  referenceText: document.getElementById('token-reference-text')
};

const references = {
  // The Night of the Zealot
  [`${skull}_The Gathering_front`]: "-X. X is the number of Ghoul enemies at your location.",
  [`${cultist}_The Gathering_front`]: "-1. If you fail, take 1 horror.",
  [`${tablet}_The Gathering_front`]: "-2. If there is a Ghoul Enemy at your location, take 1 damage.",
  [`${skull}_The Gathering_back`]: "-2. If you fail, after this skill test, search the encounter deck and discard pile for a Ghoul enemy, and draw it. Shuffle the encounter deck.",
  [`${cultist}_The Gathering_back`]: "Reveal another token. If you fail, take 2 horror.",
  [`${tablet}_The Gathering_back`]: "-4. If there is a Ghoul Enemy at your location, take 1 damage and 1 horror.",

  [`${skull}_The Midnight Masks_front`]: "-X. X is the highest number of doom on a Cultist enemy in play.",
  [`${cultist}_The Midnight Masks_front`]: "-2. Place 1 doom on the nearest Cultist enemy.",
  [`${tablet}_The Midnight Masks_front`]: "-3. If you fail, place 1 of your clues on your location.",
  [`${skull}_The Midnight Masks_back`]: "-X. X is the total number of doom in play.",
  [`${cultist}_The Midnight Masks_back`]: "-2. Place 1 doom on each Cultist enemy in play. If there are no Cultist enemies in play, reveal another token.",
  [`${tablet}_The Midnight Masks_back`]: "-4. If you fail, place all your clues on your location.",

  [`${skull}_The Devourer Below_front`]: "-X. X is the number of Monster enemies in play.",
  [`${cultist}_The Devourer Below_front`]: "-2. Place 1 doom on the nearest enemy.",
  [`${tablet}_The Devourer Below_front`]: "-3. If there is a Monster enemy at your location, take 1 damage.",
  [`${elderThing}_The Devourer Below_front`]: "-5. If there is an Ancient One enemy in play, reveal another",
  [`${skull}_The Devourer Below_back`]: "-3. If you fail, after this skill test, search the encounter deck and discard pile for a Monster enemy, and draw it. Shuffle the encounter deck.",
  [`${cultist}_The Devourer Below_back`]: "-4. Place 2 doom on the nearest enemy.",
  [`${tablet}_The Devourer Below_back`]: "-5. If there is a Monster enemy at your location, take 1 damage and 1 horror.",
  [`${elderThing}_The Devourer Below_back`]: "-7. If there is an Ancient One enemy in play, reveal another token.",

  // The Dunwich Legacy
  [`${skull}_Extracurricular Activity_front`]: "-1. If you fail, discard the top 3 cards of your deck.",
  [`${cultist}_Extracurricular Activity_front`]: "-1 (-3 instead if there are 10 or more cards in your discard pile).",
  [`${elderThing}_Extracurricular Activity_front`]: "-X. Discard the top 2 cards of your deck. X is the total printed cost of those discarded cards.",
  [`${skull}_Extracurricular Activity_back`]: "-2. If you fail, discard the top 5 cards of your deck.",
  [`${cultist}_Extracurricular Activity_back`]: "-1 (-5 instead if there are 10 or more cards in your discard pile).",
  [`${elderThing}_Extracurricular Activity_back`]: "-X. Discard the top 3 cards of your deck. X is the total printed cost of those discarded cards.",

  [`${skull}_The House Always Wins_front`]: "-2. You may spend 2 resources to treat this token as a 0, instead.",
  [`${cultist}_The House Always Wins_front`]: "-3. If you succeed, gain 3 resources.",
  [`${tablet}_The House Always Wins_front`]: "-2. If you fail, discard 3 resources.",
  [`${skull}_The House Always Wins_back`]: "-3. You may spend 3 resources to treat this token as a 0, instead.",
  [`${cultist}_The House Always Wins_back`]: "-3. If you fail, discard 3 resources.",
  [`${tablet}_The House Always Wins_back`]: "-2. Discard 3 resources.",

  [`${skull}_The Miskatonic Museum_front`]: "-1 (-3 instead if Hunting Horror is at your location.)",
  [`${cultist}_The Miskatonic Museum_front`]: "-1. If you fail, search the encounter deck, discard pile, and the void for Hunting Horror and spawn it at your location, if able.",
  [`${tablet}_The Miskatonic Museum_front`]: "-2. Return 1 of your clues to your current location.",
  [`${elderThing}_The Miskatonic Museum_front`]: "-3. If you fail, discard an asset you control.",
  [`${skull}_The Miskatonic Museum_back`]: "-2 (-4 instead if Hunting Horror is at your location.)",
  [`${cultist}_The Miskatonic Museum_back`]: "-3. If you fail, search the encounter deck, discard pile, and the void for Hunting Horror and spawn it at your location, if able.",
  [`${tablet}_The Miskatonic Museum_back`]: "-4. If Hunting Horror is at your location, it immediately attacks you.",
  [`${elderThing}_The Miskatonic Museum_back`]: "-5. If you fail, discard an asset you control.",

  [`${skull}_The Essex County Express_front`]: "-X. X is the current Agenda #.",
  [`${cultist}_The Essex County Express_front`]: "-1. If you fail and it is your turn, lose all remaining actions and end your turn immediately.",
  [`${tablet}_The Essex County Express_front`]: "-2. Add 1 doom token to the nearest Cultist enemy.",
  [`${elderThing}_The Essex County Express_front`]: "-3. If you fail, choose and discard a card from your hand.",
  [`${skull}_The Essex County Express_back`]: "-X. X is 1 more than the current Agenda #.",
  [`${cultist}_The Essex County Express_back`]: "Reveal another token. If you fail and it is your turn, lose all remaining actions and end your turn immediately.",
  [`${tablet}_The Essex County Express_back`]: "-4. Add 1 doom token to each Cultist enemy in play.",
  [`${elderThing}_The Essex County Express_back`]: "-3. If you fail, choose and discard a card from your hand for each point you failed by.",

  [`${skull}_Blood on the Altar_front`]: "-1 for each location in play with no encounter card underneath it (max -4).",
  [`${cultist}_Blood on the Altar_front`]: "-2. If you fail, add 1 clue from the token pool to your location.",
  [`${tablet}_Blood on the Altar_front`]: "-2. If you are in the Hidden Chamber, reveal another token.",
  [`${elderThing}_Blood on the Altar_front`]: "-3. If you fail, place 1 doom on the current agenda.",
  [`${skull}_Blood on the Altar_back`]: "-1 for each location in play with no encounter card underneath it.",
  [`${cultist}_Blood on the Altar_back`]: "-4. If you fail, add 1 clue from the token pool to your location.",
  [`${tablet}_Blood on the Altar_back`]: "-3. Reveal another token.",
  [`${elderThing}_Blood on the Altar_back`]: "-3. Place 1 doom on the current agenda.",

  [`${skull}_Undimensioned and Unseen_front`]: "-1 for each Brood of Yog-Sothoth in play.",
  [`${cultist}_Undimensioned and Unseen_front`]: "Reveal another token. If you fail this test, take 1 horror.",
  [`${tablet}_Undimensioned and Unseen_front`]: "0. You must either remove all clue tokens from a Brood of Yog-Sothoth in play, or this token's modifier is -4 instead.",
  [`${elderThing}_Undimensioned and Unseen_front`]: "-3. If this token is revealed during an attack or evasion attempt against a Brood of Yog-Sothoth, it immediately attacks you.",
  [`${skull}_Undimensioned and Unseen_back`]: "-2 for each Brood of Yog-Sothoth in play.",
  [`${cultist}_Undimensioned and Unseen_back`]: "Reveal another token. If you fail this test, take 1 horror and 1 damage.",
  [`${tablet}_Undimensioned and Unseen_back`]: "0. You must either remove all clue tokens from a Brood of Yog-Sothoth in play, or this test automatically fails.",
  [`${elderThing}_Undimensioned and Unseen_back`]: "-5. If this token is revealed during an attack or evasion attempt against a Brood of Yog-Sothoth, it immediately attacks you.",

  [`${skull}_Where Doom Awaits_front`]: "-1 (-3 instead if you are at an Altered location).",
  [`${cultist}_Where Doom Awaits_front`]: "Reveal another token. Cancel the effects and icons of each skill card committed to this test.",
  [`${tablet}_Where Doom Awaits_front`]: "-2 (-4 instead if it is Agenda 2).",
  [`${elderThing}_Where Doom Awaits_front`]: "-X. Discard the top 2 cards of your deck. X is the total printed cost of those discarded cards.",
  [`${skull}_Where Doom Awaits_back`]: "-2 (-5 instead if you are at an Altered location).",
  [`${cultist}_Where Doom Awaits_back`]: "Reveal another token. Cancel the effects and icons of each skill card committed to this test.",
  [`${tablet}_Where Doom Awaits_back`]: "-3. If it is Agenda 2, you automatically fail instead.",
  [`${elderThing}_Where Doom Awaits_back`]: "-X. Discard the top 3 cards of your deck. X is the total printed cost of those discarded cards.",

  [`${skull}_Lost in Time and Space_front`]: "-1 for each Extradimensional location in play (max -5).",
  [`${cultist}_Lost in Time and Space_front`]: "Reveal another token. If you fail, after this skill test, discard cards from the top of the encounter deck until a location is discarded. Put that location into play and move there.",
  [`${tablet}_Lost in Time and Space_front`]: "-3. If Yog-Sothoth is in play, it attacks you after this skill test.",
  [`${elderThing}_Lost in Time and Space_front`]: "-X. X is the shroud value of your location. If you fail and your location is Extradimensional, discard it.",
  [`${skull}_Lost in Time and Space_back`]: "-1 for each Extradimensional location in play.",
  [`${cultist}_Lost in Time and Space_back`]: "Reveal another token. After this skill test, discard cards from the top of the encounter deck until a location is discarded. Put that location into play and move there.",
  [`${tablet}_Lost in Time and Space_back`]: "-5. If Yog-Sothoth is in play, it attacks you after this skill test.",
  [`${elderThing}_Lost in Time and Space_back`]: "-X. X is twice the shroud value of your location. If you fail and your location is Extradimensional, discard it.",

  // The Path to Carcosa
  [`${skull}_Curtain Call_front`]: "-1 (-3 instead if you have 3 or more horror on you).",
  [`${cultist}_Curtain Call_front`]: "-4. If your location has at least 1 horror on it, take 1 horror (from the token pool). If your location has no horror on it, place 1 horror on it instead.",
  [`${tablet}_Curtain Call_front`]: "-4. If your location has at least 1 horror on it, take 1 horror (from the token pool). If your location has no horror on it, place 1 horror on it instead.",
  [`${elderThing}_Curtain Call_front`]: "-4. If your location has at least 1 horror on it, take 1 horror (from the token pool). If your location has no horror on it, place 1 horror on it instead.",
  [`${skull}_Curtain Call_back`]: "-X, where X is the amount of horror on you. (If you have no horror on you, X is 1.)",
  [`${cultist}_Curtain Call_back`]: "-5. If your location has at least 1 horror on it, take 1 horror (from the token pool). If your location has no horror on it, place 1 horror on it instead.",
  [`${tablet}_Curtain Call_back`]: "-5. If your location has at least 1 horror on it, take 1 horror (from the token pool). If your location has no horror on it, place 1 horror on it instead.",
  [`${elderThing}_Curtain Call_back`]: "-5. If your location has at least 1 horror on it, take 1 horror (from the token pool). If your location has no horror on it, place 1 horror on it instead.",

  [`${skull}_The Last King_front`]: "Reveal another token. If you fail, place 1 doom on a Possessed enemy in play.",
  [`${cultist}_The Last King_front`]: "-2. If you fail, place 1 of your clues on your location.",
  [`${tablet}_The Last King_front`]: "-4. If you fail, take 1 horror.",
  [`${elderThing}_The Last King_front`]: "-X. X is the shroud value of your location.",
  [`${skull}_The Last King_back`]: "Reveal another token. If you fail, place 1 doom on the Possessed enemy in play with the most remaining health.",
  [`${cultist}_The Last King_back`]: "-3. Place 1 of your clues on your location.",
  [`${tablet}_The Last King_back`]: "-4. Take 1 horror.",
  [`${elderThing}_The Last King_back`]: "-X. X is the shroud value of your location. If you fail, take 1 damage.",

  [`${skull}_Echoes of the Past_front`]: "-X. X is the highest number of doom on an enemy in play.",
  [`${cultist}_Echoes of the Past_front`]: "-2. If you fail, place 1 doom on the nearest enemy.",
  [`${tablet}_Echoes of the Past_front`]: "-2. If you fail, discard a random card from your hand.",
  [`${elderThing}_Echoes of the Past_front`]: "-2. If you fail and there is an enemy at your location, take 1 horror.",
  [`${skull}_Echoes of the Past_back`]: "-X. X is the total number of doom on enemies in play.",
  [`${cultist}_Echoes of the Past_back`]: "-4. Place 1 doom on the nearest enemy.",
  [`${tablet}_Echoes of the Past_back`]: "-4. Discard a random card from your hand.",
  [`${elderThing}_Echoes of the Past_back`]: "-4. If there is an enemy at your location, take 1 horror.",

  [`${skull}_The Unspeakable Oath_front`]: "-1. If you fail, randomly choose an enemy from among the set-aside Monster enemies and place it beneath the act deck without looking at it.",
  [`${cultist}_The Unspeakable Oath_front`]: "-X. X is the amount of horror on you.",
  [`${tablet}_The Unspeakable Oath_front`]: "-X. X is the base shroud value of your location.",
  [`${elderThing}_The Unspeakable Oath_front`]: "0. Either randomly choose an enemy from among the set-aside Monster enemies and place it beneath the act deck without looking at it, or this test automatically fails instead.",
  [`${skull}_The Unspeakable Oath_back`]: "Reveal another token. If you fail, randomly choose an enemy from among the set-aside Monster enemies and place it beneath the act deck without looking at it. (Limit once per test.)",
  [`${cultist}_The Unspeakable Oath_back`]: "-X. X is the amount of horror on you. If you fail, take 1 horror.",
  [`${tablet}_The Unspeakable Oath_back`]: "-X. X is the base shroud value of your location. If you fail, take 1 horror.",
  [`${elderThing}_The Unspeakable Oath_back`]: "0. Either randomly choose an enemy from among the set-aside Monster enemies and place it beneath the act deck without looking at it, or this test automatically fails instead.",

  [`${skull}_A Phantom of Truth_front`]: "-X. X is the amount of doom in play (max 5).",
  [`${cultist}_A Phantom of Truth_front`]: "-2. If you fail, move each unengaged Byakhee in play once toward the nearest investigator.",
  [`${tablet}_A Phantom of Truth_front`]: "-3. Cancel the effects and icons of each skill card committed to this test.",
  [`${elderThing}_A Phantom of Truth_front`]: "-2. If you fail, lose 1 resource for each point you failed by.",
  [`${skull}_A Phantom of Truth_back`]: "-X. X is the amount of doom in play.",
  [`${cultist}_A Phantom of Truth_back`]: "-2. Move each unengaged Byakhee in play once toward the nearest investigator.",
  [`${tablet}_A Phantom of Truth_back`]: "-4. Cancel the effects and icons of each skill card committed to this test.",
  [`${elderThing}_A Phantom of Truth_back`]: "-3. If you fail, lose 1 resource for each point you failed by.",

  [`${skull}_The Pallid Mask_front`]: "-X. X is the number of locations away from the starting location you are (max 5).",
  [`${cultist}_The Pallid Mask_front`]: "-2. If this token is revealed during an attack, and this skill test is successful, this attack deals 1 less damage.",
  [`${tablet}_The Pallid Mask_front`]: "-2. If there is a ready Ghoul or Geist enemy at your location, it attacks you (if there is more than one, choose one).",
  [`${elderThing}_The Pallid Mask_front`]: "-3. If you fail, search the encounter deck and discard pile for a Ghoul or Geist enemy and draw it.",
  [`${skull}_The Pallid Mask_back`]: "-X. X is the number of locations away from the starting location you are.",
  [`${cultist}_The Pallid Mask_back`]: "-3. If this token is revealed during an attack and this skill test is successful, this attack deals no damage.",
  [`${tablet}_The Pallid Mask_back`]: "-3. If there is a Ghoul or Geist enemy at your location, it readies and attacks you (if there is more than one, choose one).",
  [`${elderThing}_The Pallid Mask_back`]: "-4. If you fail, search the encounter deck and discard pile for a Ghoul or Geist enemy and draw it.",

  [`${skull}_Black Stars Rise_front`]: "-X. X is the highest amount of doom on an agenda in play.",
  [`${cultist}_Black Stars Rise_front`]: "Reveal another token. If this token is revealed during an attack or evasion attempt against an enemy with doom on it, this skill test automatically fails instead.",
  [`${tablet}_Black Stars Rise_front`]: "Reveal another token. If you fail, place 1 doom on each agenda.",
  [`${elderThing}_Black Stars Rise_front`]: "-2. If you fail, search the encounter deck and discard pile for a Byakhee enemy and draw it.",
  [`${skull}_Black Stars Rise_back`]: "-X. X is the total amount of doom on agendas in play.",
  [`${cultist}_Black Stars Rise_back`]: "Reveal another token. If there is an enemy with 1 or more doom on it at your location, this test automatically fails instead.",
  [`${tablet}_Black Stars Rise_back`]: "Reveal another token. If you do not succeed by at least 1, place 1 doom on each agenda.",
  [`${elderThing}_Black Stars Rise_back`]: "-3. If you fail, search the encounter deck and discard pile for a Byakhee enemy and draw it.",

  [`${skull}_Dim Carcosa_front`]: "-2 (-4 instead if you have no sanity remaining).",
  [`${cultist}_Dim Carcosa_front`]: "Reveal another token. If you fail, take 1 horror.",
  [`${tablet}_Dim Carcosa_front`]: "-3. If you fail and Hastur is in play, place 1 clue on your location (from the token bank).",
  [`${elderThing}_Dim Carcosa_front`]: "-3. If this token is revealed during an attack or evasion attempt against a Monster or Ancient One enemy, lose 1 action.",
  [`${skull}_Dim Carcosa_back`]: "-X. X is the amount of horror on you.",
  [`${cultist}_Dim Carcosa_back`]: "Reveal another token. If you fail, take 2 horror.",
  [`${tablet}_Dim Carcosa_back`]: "-5. If you fail and Hastur is in play, place 1 clue on your location (from the token bank).",
  [`${elderThing}_Dim Carcosa_back`]: "-5. If this token is revealed during an attack or evasion attempt against a Monster or Ancient One enemy, lose 1 action.",

  // The Forgotten Age
  [`${skull}_The Untamed Wilds_front`]: "-X. X is the number of vengeance points in the victory display.",
  [`${cultist}_The Untamed Wilds_front`]: "-X. X is the number of locations in play (max 5).",
  [`${tablet}_The Untamed Wilds_front`]: "-X. X is the number of cards in the exploration deck (max 5).",
  [`${elderThing}_The Untamed Wilds_front`]: "-2. If you are poisoned, this test automatically fails instead.",
  [`${skull}_The Untamed Wilds_back`]: "-X. X is 1 higher than the number of vengeance points in the victory display.",
  [`${cultist}_The Untamed Wilds_back`]: "-X. X is the number of locations in play.",
  [`${tablet}_The Untamed Wilds_back`]: "-X. X is the number of cards in the exploration deck (min 3).",
  [`${elderThing}_The Untamed Wilds_back`]: "-3. If you are poisoned, this test automatically fails instead. If you are not poisoned and you fail, put a set-aside Poisoned weakness into play in your threat area.",

  [`${skull}_The Doom of Eztli_front`]: "-1 (-3 instead if there is doom on your location).",
  [`${cultist}_The Doom of Eztli_front`]: "-X. X is the number of locations with doom on them.",
  [`${tablet}_The Doom of Eztli_front`]: "-X. X is the number of locations with doom on them.",
  [`${elderThing}_The Doom of Eztli_front`]: "Reveal another chaos token. If you fail, place 1 doom on your location.",
  [`${skull}_The Doom of Eztli_back`]: "-2 (-4 instead if there is doom on your location).",
  [`${cultist}_The Doom of Eztli_back`]: "-X. X is the total amount of doom on locations in play.",
  [`${tablet}_The Doom of Eztli_back`]: "-X. X is the total amount of doom on locations in play.",
  [`${elderThing}_The Doom of Eztli_back`]: "Reveal another chaos token. Place 1 doom on your location.",

  [`${skull}_Threads of Fate_front`]: "-X. X is the highest number of doom on a cultist enemy.",
  [`${cultist}_Threads of Fate_front`]: "-2. If you do not succeed by at least 1, take 1 damage.",
  [`${tablet}_Threads of Fate_front`]: "-2. If you do not succeed by at least 1, place 1 doom on the nearest cultist enemy.",
  [`${elderThing}_Threads of Fate_front`]: "-2. If you fail, lose 1 of your clues.",
  [`${skull}_Threads of Fate_back`]: "-X. X is the total number of doom in play.",
  [`${cultist}_Threads of Fate_back`]: "-2. If you do not succeed by at least 2, take 1 direct damage.",
  [`${tablet}_Threads of Fate_back`]: "-2. If you do not succeed by at least 2, place 1 doom on each cultist enemy.",
  [`${elderThing}_Threads of Fate_back`]: "-3. If you fail, lose 1 of your clues.",

  [`${skull}_The Boundary Beyond_front`]: "-1 (-3 instead if you are at an Ancient location).",
  [`${cultist}_The Boundary Beyond_front`]: "Reveal another token. If you fail, place 1 doom on a Cultist enemy.",
  [`${tablet}_The Boundary Beyond_front`]: "Reveal another token. If you fail and there is a Serpent enemy at your location, it attacks you.",
  [`${elderThing}_The Boundary Beyond_front`]: "-4. If you fail, place 1 clue (from the token pool) on the nearest Ancient location.",
  [`${skull}_The Boundary Beyond_back`]: "-2 (-4 instead if you are at an Ancient location).",
  [`${cultist}_The Boundary Beyond_back`]: "Reveal another token. If you fail, place 1 doom on each Cultist enemy.",
  [`${tablet}_The Boundary Beyond_back`]: "Reveal another token. If you fail, each Serpent enemy at your location attacks you.",
  [`${elderThing}_The Boundary Beyond_back`]: "-4. Place 1 clue (from the token pool) on the nearest Ancient location.",

  [`${skull}_Heart of the Elders_front`]: "-1 (-3 instead if you are in a Cave location).",
  [`${cultist}_Heart of the Elders_front`]: "-2. If you fail, place 1 doom on your location.",
  [`${tablet}_Heart of the Elders_front`]: "-2. If you are poisoned, this test automatically fails instead.",
  [`${elderThing}_Heart of the Elders_front`]: "-3. If you fail, take 1 horror.",
  [`${skull}_Heart of the Elders_back`]: "-2 (-4 instead if you are in a Cave location).",
  [`${cultist}_Heart of the Elders_back`]: "-3. If you fail, place 1 doom on your location.",
  [`${tablet}_Heart of the Elders_back`]: "-3. If you are poisoned, this test automatically fails instead. If you are not poisoned and you fail, put a set-aside Poisoned weakness into play in your threat area.",
  [`${elderThing}_Heart of the Elders_back`]: "-4. If you fail, take 1 horror.",

  [`${skull}_The City of Archives_front`]: "-1 (-3 instead if you have 5 or more cards in your hand).",
  [`${cultist}_The City of Archives_front`]: "-2. If you fail, place 1 of your clues on your location.",
  [`${tablet}_The City of Archives_front`]: "-3. If you fail, discard 1 random card from your hand.",
  [`${elderThing}_The City of Archives_front`]: "-2. If you fail, place 1 of your clues on your location.",
  [`${skull}_The City of Archives_back`]: "-2 (if you have 5 or more cards in your hand, you automatically fail instead).",
  [`${cultist}_The City of Archives_back`]: "-2. Place 1 of your clues on your location.",
  [`${tablet}_The City of Archives_back`]: "-3. For each point you fail by, discard 1 random card from your hand.",
  [`${elderThing}_The City of Archives_back`]: "-2. Place 1 of your clues on your location.",

  [`${skull}_The Depths of Yoth_front`]: "-X. X is the current depth level.",
  [`${cultist}_The Depths of Yoth_front`]: "Reveal another token. If you fail, each Serpent enemy at your location or a connecting location heals 2 damage.",
  [`${tablet}_The Depths of Yoth_front`]: "Reveal another token. If you fail, place 1 clue on your location (from the token pool).",
  [`${elderThing}_The Depths of Yoth_front`]: "-2. If there are 3 or more vengeance points in the victory display, you automatically fail this test, instead.",
  [`${skull}_The Depths of Yoth_back`]: "-X. X is the current depth level. If you fail, take 1 horror.",
  [`${cultist}_The Depths of Yoth_back`]: "Reveal another token. If you fail, each Serpent enemy at your location or a connecting location heals 2 damage.",
  [`${tablet}_The Depths of Yoth_back`]: "Reveal another token. If you fail, place 1 clue on your location (from the token pool).",
  [`${elderThing}_The Depths of Yoth_back`]: "-4. If there are 3 or more vengeance points in the victory display, you automatically fail this test, instead.",

  [`${skull}_Shattered Aeons_front`]: "-2 (-4 instead if the Relic of Ages is at your location).",
  [`${cultist}_Shattered Aeons_front`]: "-2. If you do not succeed by at least 1, place 1 doom on the nearest Cultist enemy.",
  [`${tablet}_Shattered Aeons_front`]: "-2. If you are poisoned, this test automatically fails instead.",
  [`${elderThing}_Shattered Aeons_front`]: "-2. If you fail, shuffle the topmost Hex treachery in the encounter discard pile into the exploration deck.",
  [`${skull}_Shattered Aeons_back`]: "-3 (-5 instead if the Relic of Ages is at your location).",
  [`${cultist}_Shattered Aeons_back`]: "-3. If you do not succeed by at least 1, place 1 doom on each Cultist enemy.",
  [`${tablet}_Shattered Aeons_back`]: "-3. If you are poisoned, this test automatically fails instead. If you are not poisoned and you fail, put a set-aside Poisoned weakness into play in your threat area.",
  [`${elderThing}_Shattered Aeons_back`]: "-3. Shuffle the topmost Hex treachery in the encounter discard pile into the exploration deck.",

  [`${skull}_Turn Back Time_front`]: "-X . X is the number of locations with doom on them.",
  [`${elderThing}_Turn Back Time_front`]: "-4. If you fail, place 1 doom on your location.",
  [`${skull}_Turn Back Time_back`]: "-X . X is the total amount of doom on locations.",
  [`${elderThing}_Turn Back Time_back`]: "-6. Place 1 doom on your location.",

  // The Circle Undone
  [`${skull}_Disappearance at the Twilight Estate_front`]: "-3. If you fail and this is an attack or evasion attempt, resolve each haunted ability on your location.",
  [`${skull}_Disappearance at the Twilight Estate_back`]: "-5. If you fail and this is an attack or evasion attempt, resolve each haunted ability on your location.",

  [`${skull}_The Witching Hour_front`]: "-1. For each point you fail by, discard the top card of the encounter deck.",
  [`${tablet}_The Witching Hour_front`]: "-1. If you fail, after this test resolves, draw the bottommost treachery in the encounter discard pile.",
  [`${elderThing}_The Witching Hour_front`]: "-3. If you fail, choose an exhausted or damaged Witch enemy at your location or at a connecting location. Ready that enemy and heal all damage from it.",
  [`${skull}_The Witching Hour_back`]: "-2. Discard cards from the top of the encounter deck equal to this test's difficulty.",
  [`${tablet}_The Witching Hour_back`]: "-2. If you fail, after this test resolves, draw the bottommost treachery in the encounter discard pile.",
  [`${elderThing}_The Witching Hour_back`]: "-4. If you fail, ready each Witch enemy at your location and at each connecting location. Heal all damage from each of those enemies.",

  [`${skull}_The Secret Name_front`]: "-1 (-3 instead if you are at an Extradimensional location).",
  [`${cultist}_The Secret Name_front`]: "Reveal another chaos token. If you fail, discard the top 3 cards of the encounter deck.",
  [`${tablet}_The Secret Name_front`]: "-2. If you fail and Nahab is at your location, she attacks you.",
  [`${elderThing}_The Secret Name_front`]: "-3. If you fail, resolve the hunter keyword on each enemy in play.",
  [`${skull}_The Secret Name_back`]: "-2 (-4 instead if you are at an Extradimensional location).",
  [`${cultist}_The Secret Name_back`]: "Reveal another chaos token. If you fail, discard the top 5 cards of the encounter deck.",
  [`${tablet}_The Secret Name_back`]: "-3. If you fail and Nahab is in play, she attacks you (regardless of her current location).",
  [`${elderThing}_The Secret Name_back`]: "-4. Resolve the hunter keyword on each enemy in play.",

  [`${skull}_The Wages of Sin_front`]: "-X. X is 1 higher than the number of copies of Unfinished Business in the victory display.",
  [`${cultist}_The Wages of Sin_front`]: "-3. Until the end of the round, each Heretic enemy in play gets +1 fight and +1 evade.",
  [`${tablet}_The Wages of Sin_front`]: "-3. If you fail, trigger the forced ability on a copy of Unfinished Business in yout threat area as if it were the end of the round.",
  [`${elderThing}_The Wages of Sin_front`]: "-2. If you fail and this is an attack or evasion attempt, resolve each haunted ability on your location.",
  [`${skull}_The Wages of Sin_back`]: "-X. X is the number of copies of Unfinished Business in the victory display. Reveal another token.",
  [`${cultist}_The Wages of Sin_back`]: "-4. Until the end of the round, each Heretic enemy in play gets +1 fight and +1 evade.",
  [`${tablet}_The Wages of Sin_back`]: "-4. If you fail, trigger the forced ability on a copy of Unfinished Business in your threat area as if it were the end of the round.",
  [`${elderThing}_The Wages of Sin_back`]: "-2. If this is an attack or evasion attempt, resolve each haunted ability on your location.",

  [`${skull}_For the Greater Good_front`]: "-X. X is the highest number of doom on a Cultist enemy in play.",
  [`${cultist}_For the Greater Good_front`]: "-2. Reveal another token.",
  [`${tablet}_For the Greater Good_front`]: "-3. If you fail, place 1 doom on the nearest Cultist enemy.",
  [`${elderThing}_For the Greater Good_front`]: "-3. If you fail, move 1 doom from the nearest Cultist enemy to the current agenda.",
  [`${skull}_For the Greater Good_back`]: "-X. X is the total number of doom among Cultist enemies in play.",
  [`${cultist}_For the Greater Good_back`]: "-2. Reveal another token.",
  [`${tablet}_For the Greater Good_back`]: "-3. If you fail, place 1 doom on each Cultist enemy in play. If there are no Cultist enemies in play, reveal another token.",
  [`${elderThing}_For the Greater Good_back`]: "-3. If you fail, move all doom from the Cultist enemy with the most doom on it to the current agenda. If no Cultist enemies in play have doom on them, reveal another token.",

  [`${skull}_Union and Disillusion_front`]: "-2. If this is a skill test during a circle action, reveal another token.",
  [`${cultist}_Union and Disillusion_front`]: "-3. If you have no damage on you, take 1 damage. If you have no horror on you, take 1 horror.",
  [`${tablet}_Union and Disillusion_front`]: "-3. If you fail, a Spectral enemy at your location attacks you (even if it is exhausted).",
  [`${elderThing}_Union and Disillusion_front`]: "-3. If this is a skill test during a circle action and you fail, resolve each haunted ability on your location.",
  [`${skull}_Union and Disillusion_back`]: "-3. If this is a skill test during a circle action, reveal another token.",
  [`${cultist}_Union and Disillusion_back`]: "-4. If you have no damage on you, take 1 damage. If you have no horror on you, take 1 horror.",
  [`${tablet}_Union and Disillusion_back`]: "-4. If you fail, a Spectral enemy at your location attacks you (even if it is exhausted).",
  [`${elderThing}_Union and Disillusion_back`]: "-4. If this is a skill test during a circle action and you fail, resolve each haunted ability on your location.",

  [`${skull}_In the Clutches of Chaos_front`]: "-X. X is the total amount of doom and breaches on your location.",
  [`${cultist}_In the Clutches of Chaos_front`]: "Reveal another token. If there are fewer than 3 breaches on your location, place 1 breach on your location.",
  [`${tablet}_In the Clutches of Chaos_front`]: "-2. For each point you fail by, remove 1 breach from the current act.",
  [`${elderThing}_In the Clutches of Chaos_front`]: "-3. If you fail, place 1 breach on a random location.",
  [`${skull}_In the Clutches of Chaos_back`]: "-X. X is 1 higher than the total amount of doom and breaches on your location.",
  [`${cultist}_In the Clutches of Chaos_back`]: "Reveal another token. If there are fewer than 3 breaches on your location, place 1 breach on your location.",
  [`${tablet}_In the Clutches of Chaos_back`]: "-3. For each point you fail by, remove 1 breach from the current act.",
  [`${elderThing}_In the Clutches of Chaos_back`]: "-4. If you fail, place 1 breach on a random location.",

  [`${skull}_Before the Black Throne_front`]: "-X. X is half of the doom on Azathoth (rounded up), to a minimum of 2.",
  [`${cultist}_Before the Black Throne_front`]: "Reveal another token. If you fail, search the encounter deck and discard pile for a Cultist enemy and draw it. Shuffle the encounter deck.",
  [`${tablet}_Before the Black Throne_front`]: "-2. If you fail, Azathoth attacks you.",
  [`${elderThing}_Before the Black Throne_front`]: "-4. If your modified skill value for this test is 0, place 1 doom on Azathoth.",
  [`${skull}_Before the Black Throne_back`]: "-X. X is the amount of doom on Azathoth, to a minimum of 2.",
  [`${cultist}_Before the Black Throne_back`]: "Reveal another token. If you fail, search the encounter deck and discard pile for a Cultist enemy and draw it. Shuffle the encounter deck.",
  [`${tablet}_Before the Black Throne_back`]: "-3. If you fail, Azathoth attacks you.",
  [`${elderThing}_Before the Black Throne_back`]: "-6. If your modified skill value for this test is 0, place 1 doom on Azathoth.",

  [`${skull}_Beyond the Gates of Sleep_front`]: "-X. X is half the number of cards in your hand (rounded up).",
  [`${cultist}_Beyond the Gates of Sleep_front`]: "-X. X is the number of revealed Enchanted Woods locations.",
  [`${tablet}_Beyond the Gates of Sleep_front`]: "-2. If you fail and this is an attack or evasion attempt against a swarming enemy, add 1 swarm card to it.",
  [`${skull}_Beyond the Gates of Sleep_back`]: "-X. X is the number of cards in your hand.",
  [`${cultist}_Beyond the Gates of Sleep_back`]: "-X. X is the number of revealed Woods locations.",
  [`${tablet}_Beyond the Gates of Sleep_back`]: "-2. If this is an attack or evasion attempt against a swarming enemy, add 1 swarm card to it.",

  [`${skull}_Waking Nightmare_front`]: "-1 (-3 instead if you are engaged with a Staff enemy).",
  [`${cultist}_Waking Nightmare_front`]: "Reveal another chaos token. If you fail and it is agenda 2 or 3, make an infestation test.",
  [`${elderThing}_Waking Nightmare_front`]: "-X. X is the number of infested locations.",
  [`${skull}_Waking Nightmare_back`]: "-2 (-4 instead if you are engaged with a Staff enemy).",
  [`${cultist}_Waking Nightmare_back`]: "Reveal another chaos token. If it is agenda 2 or 3, make an infestation test.",
  [`${elderThing}_Waking Nightmare_back`]: "-X. X is 1 higher than the number of infested locations.",

  [`${skull}_The Search for Kadath_front`]: "-X. X is the number of Signs of the Gods the investigators have uncovered.",
  [`${cultist}_The Search for Kadath_front`]: "Reveal another token. If this token is revealed during an investigation and this skill test fails, increase that location's shroud by 1 for the remainder of the round.",
  [`${tablet}_The Search for Kadath_front`]: "-2. If you fail, either take 1 damage and 1 horror, or place 1 doom on the current agenda.",
  [`${elderThing}_The Search for Kadath_front`]: "+2. The black cat points you in the right direction. If this token is revealed during an investigation and you succeed, discover 1 additional clue.",
  [`${skull}_The Search for Kadath_back`]: "-X. X is 1 more than the number of Signs of the Gods the investigators have uncovered.",
  [`${cultist}_The Search for Kadath_back`]: "Reveal another token. If this token is revealed during an investigation and this skill test fails, increase that location's shroud by 2 for the remainder of the round.",
  [`${tablet}_The Search for Kadath_back`]: "-3. If you fail, either take 1 damage and 1 horror, or place 1 doom on the current agenda.",
  [`${elderThing}_The Search for Kadath_back`]: "+1. The black cat points you in the right direction. If this token is revealed during an investigation and you succeed, discover 1 additional clue.",

  [`${skull}_A Thousand Shapes of Horror_front`]: "-1 (-3 instead if you are at a Graveyard location).",
  [`${cultist}_A Thousand Shapes of Horror_front`]: "Reveal another token. If you fail and The Unnamable is in play, it attacks you (regardless of its current location).",
  [`${tablet}_A Thousand Shapes of Horror_front`]: "+2. The black cat causes a distraction. If this test is successful, choose and evade an enemy at any location with a fight value of X or lower, where X is the amount you succeeded by.",
  [`${elderThing}_A Thousand Shapes of Horror_front`]: "-2. If you fail, you must either place 1 of your clues on your location or take 1 damage.",
  [`${skull}_A Thousand Shapes of Horror_back`]: "-2 (-4 instead if you are at a Graveyard location).",
  [`${cultist}_A Thousand Shapes of Horror_back`]: "Reveal another token. If you fail and The Unnamable is in play, it attacks you (regardless of its current location).",
  [`${tablet}_A Thousand Shapes of Horror_back`]: "+1. The black cat causes a distraction. If this test is successful, choose and evade an enemy at any location with a fight value of X or lower, where X is the amount you succeeded by.",
  [`${elderThing}_A Thousand Shapes of Horror_back`]: "-3. If you fail, you must either place 1 of your clues on your location or take 1 damage.",
  
  [`${skull}_Dark Side of the Moon_front`]: "-X. X is half your alarm level (rounded up).",
  [`${cultist}_Dark Side of the Moon_front`]: "Reveal another token. If you fail and your alarm level is higher than your modified skill value, after this skill test ends, draw the top card of the encounter deck.",
  [`${tablet}_Dark Side of the Moon_front`]: "-1. If you fail, raise your alarm level by 1.",
  [`${elderThing}_Dark Side of the Moon_front`]: "+1. The black cat summons several other cats to help. If this token is revealed during an evasion attempt and you succeed, deal 2 damage to the evaded enemy.",
  [`${skull}_Dark Side of the Moon_back`]: "-X. X is your alarm level.",
  [`${cultist}_Dark Side of the Moon_back`]: "Reveal another token. If you fail and your alarm level is higher than your modified skill value, after this skill test ends, draw the top card of the encounter deck.",
  [`${tablet}_Dark Side of the Moon_back`]: "-2. If you fail, raise your alarm level by 1.",
  [`${elderThing}_Dark Side of the Moon_back`]: "0. The black cat summons several other cats to help. If this token is revealed during an evasion attempt and you succeed, deal 2 damage to the evaded enemy.",

  [`${skull}_Point of No Return_front`]: "-X. X is the amount of damage on this card.",
  [`${cultist}_Point of No Return_front`]: "Reveal another token. If you fail, after this skill test ends, draw the top card of the encounter deck.",
  [`${tablet}_Point of No Return_front`]: "+1. The black cat helps you navigate through the death-fire. If this token is revealed during an investigation and you succeed, draw 1 card.",
  [`${elderThing}_Point of No Return_front`]: "-3. If you fail by 2 or more, choose a ready enemy at your location or a connecting location. That enemy moves to your location, engages you, and makes an immediate attack.",
  [`${skull}_Point of No Return_back`]: "-X. X is 1 more than the amount of damage on this card.",
  [`${cultist}_Point of No Return_back`]: "Reveal another token. If you fail, after this skill test ends, draw the top card of the encounter deck.",
  [`${tablet}_Point of No Return_back`]: "0. The black cat helps you navigate through the death-fire. If this token is revealed during an investigation and you succeed, draw 1 card.",
  [`${elderThing}_Point of No Return_back`]: "-4. If you fail by 2 or more, choose a ready enemy at your location or a connecting location. That enemy moves to your location, engages you, and makes an immediate attack.",

  [`${skull}_Where the Gods Dwell_front`]: "-X. X is the number of the current act.",
  [`${cultist}_Where the Gods Dwell_front`]: "Reveal another token. If you fail, place 1 doom on the current agenda.",
  [`${tablet}_Where the Gods Dwell_front`]: "-4. If you fail, choose and reveal a copy of Nyarlathotep in your hand. It attacks you and is shuffled into the encounter deck.",
  [`${elderThing}_Where the Gods Dwell_front`]: "0. The black cat reminds you that it's all a dream.",
  [`${skull}_Where the Gods Dwell_back`]: "-X. X is the number of the current act plus the number of the current agenda.",
  [`${cultist}_Where the Gods Dwell_back`]: "Reveal another token. If you fail, place 1 doom on the current agenda. This effect may cause the current agenda to advance.",
  [`${tablet}_Where the Gods Dwell_back`]: "-6. If you fail, choose and reveal a copy of Nyarlathotep in your hand. It attacks you and is shuffled into the encounter deck.",
  [`${elderThing}_Where the Gods Dwell_back`]: "-1. The black cat reminds you that it's all a dream.",

  [`${skull}_Weaver of the Cosmos_front`]: "-X. X is the highest amount of doom on a location in play.",
  [`${cultist}_Weaver of the Cosmos_front`]: "Reveal another token. If you fail, and there is an Ancient One enemy at your location, it attacks you.",
  [`${tablet}_Weaver of the Cosmos_front`]: "0. The black cat tears at the web with its claws. If you succeed by 2 or more, remove 1 doom from your location.",
  [`${elderThing}_Weaver of the Cosmos_front`]: "-3. If this skill test fails during an attack against a Spider enemy, place 1 doom on that enemy's location.",
  [`${skull}_Weaver of the Cosmos_back`]: "-X. X is the amount of doom on locations in play.",
  [`${cultist}_Weaver of the Cosmos_back`]: "Reveal another token. If you fail, and there is an Ancient One enemy at your location, it attacks you.",
  [`${tablet}_Weaver of the Cosmos_back`]: "-1. The black cat tears at the web with its claws. If you succeed by 2 or more, remove 1 doom from your location.",
  [`${elderThing}_Weaver of the Cosmos_back`]: "-4. If this skill test fails during an attack against a Spider enemy, place 1 doom on that enemy's location.",

  [`${skull}_The Pit of Despair_front`]: "-1 (-2 instead if your location is partially flooded; -3 instead if your location is fully flooded).",
  [`${cultist}_The Pit of Despair_front`]: "-2. If you fail and your location is flooded, take 1 damage.",
  [`${tablet}_The Pit of Despair_front`]: "-2. If you fail and you control a key, take 1 horror.",
  [`${elderThing}_The Pit of Despair_front`]: "-3. If you fail and The Amalgam is in the depths, put it into play engaged with you.",
  [`${skull}_The Pit of Despair_back`]: "-2 (-3 instead if your location is partially flooded; -4 instead if your location is fully flooded).",
  [`${cultist}_The Pit of Despair_back`]: "-2. If your location is flooded, take 1 damage.",
  [`${tablet}_The Pit of Despair_back`]: "-2. If you control a key, take 1 horror.",
  [`${elderThing}_The Pit of Despair_back`]: "-3. If The Amalgam is in the depths, put it into play engaged with you.",

  [`${skull}_The Vanishing of Elina Harper_front`]: "-X. X is the current agenda number.",
  [`${cultist}_The Vanishing of Elina Harper_front`]: "-2. If you fail, place 1 doom on the nearest enemy.",
  [`${tablet}_The Vanishing of Elina Harper_front`]: "-3. If you fail, take 1 horror.",
  [`${elderThing}_The Vanishing of Elina Harper_front`]: "-4. If you fail, place 1 of your clues on your location.",
  [`${skull}_The Vanishing of Elina Harper_back`]: "-X. X is 1 more than the current agenda number.",
  [`${cultist}_The Vanishing of Elina Harper_back`]: "-2. Place 1 doom on the nearest enemy (2 doom instead if you failed).",
  [`${tablet}_The Vanishing of Elina Harper_back`]: "-3. Take 1 horror (1 horror and 1 damage instead if you failed).",
  [`${elderThing}_The Vanishing of Elina Harper_back`]: "-4. Place 1 of your clues on your location (2 clues instead if you failed).",

  [`${skull}_In Too Deep_front`]: "-1 for each location to the east of your location (on the same row).",
  [`${cultist}_In Too Deep_front`]: "-2. If you fail, move to the connecting location to the east, ignoring all barriers.",
  [`${tablet}_In Too Deep_front`]: "-3. If you fail, choose a connecting location with no barriers between it and your location. Place 1 barrier between the two locations.",
  [`${elderThing}_In Too Deep_front`]: "-X. X is the number of barriers between your location and all connecting locations.",
  [`${skull}_In Too Deep_back`]: "-2 for each location to the east of your location (on the same row).",
  [`${cultist}_In Too Deep_back`]: "-4. If you fail, move to the connecting location to the east, ignoring all barriers.",
  [`${tablet}_In Too Deep_back`]: "-5. If you fail, choose a connecting location with no barriers between it and your location. Place 1 barrier between the two locations.",
  [`${elderThing}_In Too Deep_back`]: "-X. X is twice the number of barriers between your location and all connecting locations.",

  [`${skull}_Devil Reef_front`]: "-X. X is the number of keys the investigators control.",
  [`${cultist}_Devil Reef_front`]: "-2. If you fail and this is an attack or evasion attempt against a Deep One enemy, it engages you. (If it is already engaged with you, it disengages first, then re-engages you.)",
  [`${tablet}_Devil Reef_front`]: "-3. If you fail and you are not in a vehicle, take 1 damage.",
  [`${elderThing}_Devil Reef_front`]: "-4. If you fail and your location has a key on it, take 1 horror.",
  [`${skull}_Devil Reef_back`]: "-X. X is 1 more than the number of keys the investigators control.",
  [`${cultist}_Devil Reef_back`]: "-3. If this is an attack or evasion attempt against a Deep One enemy, it engages you. (If it is already engaged with you, it disengages first, then re-engages you.)",
  [`${tablet}_Devil Reef_back`]: "-4. If you are not in a vehicle, take 1 damage.",
  [`${elderThing}_Devil Reef_back`]: "-5. If your location has a key on it, take 1 horror.",

  [`${skull}_Horror in High Gear_front`]: "-1 (-3 instead if there are 6 or fewer locations remaining in the Road deck).",
  [`${cultist}_Horror in High Gear_front`]: "-1. For each point you fail by, an investigator in your vehicle places 1 of their clues on your location.",
  [`${tablet}_Horror in High Gear_front`]: "-2. For each point you fail by, an investigator in your vehicle loses 1 resource.",
  [`${elderThing}_Horror in High Gear_front`]: "-4. If you fail, resolve the hunter keyword on each enemy in play.",
  [`${skull}_Horror in High Gear_back`]: "-2 (-4 instead if there are 6 or fewer locations remaining in the Road deck).",
  [`${cultist}_Horror in High Gear_back`]: "-2. For each point you fail by, an investigator in your vehicle places 1 of their clues on your location.",
  [`${tablet}_Horror in High Gear_back`]: "-3. For each point you fail by, an investigator in your vehicle loses 1 resource.",
  [`${elderThing}_Horror in High Gear_back`]: "-4. Resolve the hunter keyword on each enemy in play.",

  [`${skull}_A Light in the Fog_front`]: "-1. If your location is flooded, reveal an additional chaos token.",
  [`${cultist}_A Light in the Fog_front`]: "-2. If you fail, after this test ends, increase the flood level of your location.",
  [`${tablet}_A Light in the Fog_front`]: "-3. If you fail this test and your location is flooded, take 1 damage.",
  [`${elderThing}_A Light in the Fog_front`]: "-4. If you fail, move the nearest ready unengaged enemy once toward your location. It loses aloof during this movement.",
  [`${skull}_A Light in the Fog_back`]: "-2. If your location is flooded, reveal an additional chaos token.",
  [`${cultist}_A Light in the Fog_back`]: "-2. If you fail, after this test ends, increase the flood level of your location (if you cannot, take 1 horror instead).",
  [`${tablet}_A Light in the Fog_back`]: "-3. If you fail this test and your location is flooded, take 2 damage.",
  [`${elderThing}_A Light in the Fog_back`]: "-4. Move the nearest unengaged enemy once toward your location. It loses aloof during this movement.",

  [`${skull}_The Lair of Dagon_front`]: "-1 for each key on this card.",
  [`${cultist}_The Lair of Dagon_front`]: "0. Reveal an additional chaos token. If you reveal 1 or more curse tokens during this test, you automatically fail.",
  [`${tablet}_The Lair of Dagon_front`]: "-3. If you fail, place each key you control on your location.",
  [`${elderThing}_The Lair of Dagon_front`]: "-4. If you fail, add 1 curse token to the chaos bag.",
  [`${skull}_The Lair of Dagon_back`]: "-2 for each key on this card.",
  [`${cultist}_The Lair of Dagon_back`]: "-2. Reveal an additional chaos token. If you reveal 1 or more curse tokens during this test, you automatically fail.",
  [`${tablet}_The Lair of Dagon_back`]: "-3. Place each key you control on your location and take 1 damage.",
  [`${elderThing}_The Lair of Dagon_back`]: "-4. Add 2 curse tokens to the chaos bag.",

  [`${skull}_Into the Maelstrom_front`]: "-1 (-3 instead if there are 4 or more unflooded Y'ha-nthlei locations in play).",
  [`${cultist}_Into the Maelstrom_front`]: "-3. If you fail, place 1 doom on the current agenda (this may cause the current agenda to advance).",
  [`${tablet}_Into the Maelstrom_front`]: "-4. If you fail, you must either increase the flood level of your location or take 1 damage.",
  [`${elderThing}_Into the Maelstrom_front`]: "-5. If you fail and there is a key on your location, take 1 horror.",
  [`${skull}_Into the Maelstrom_back`]: "-2 (-4 instead if there are 4 or more unflooded Y'ha-nthlei locations in play).",
  [`${cultist}_Into the Maelstrom_back`]: "-4. If you fail, place 1 doom on the current agenda (this may cause the current agenda to advance).",
  [`${tablet}_Into the Maelstrom_back`]: "-5. If you fail, you must either increase the flood level of your location or take 1 damage.",
  [`${elderThing}_Into the Maelstrom_back`]: "-6. If you fail and there is a key on your location, take 1 horror.",

  [`${skull}_Ice and Death_front`]: "–X. X is half the shelter value of your location (rounded up).",
  [`${cultist}_Ice and Death_front`]: "–2. If you fail, shuffle the top card of the Tekeli-li deck into your deck without looking at it (if you cannot, take 1 horror).",
  [`${tablet}_Ice and Death_front`]: "–3. For each point you fail by, discard the top card of your deck. Draw each weakness discarded by this effect.",
  [`${skull}_Ice and Death_back`]: "–X. X is the shelter value of your location.",
  [`${cultist}_Ice and Death_back`]: "–2. For each point you fail by, shuffle the top card of the Tekeli-li deck into your deck without looking at it (for each card you cannot shuffle, take 1 horror).",
  [`${tablet}_Ice and Death_back`]: "–4. For each point you fail by, discard the top card of your deck. Draw each weakness discarded by this effect.",

  [`${skull}_Fatal Mirage_front`]: "–X. X is the number of story cards in the victory display.",
  [`${cultist}_Fatal Mirage_front`]: "–2. If you fail, place 1 of your clues on your location.",
  [`${tablet}_Fatal Mirage_front`]: "–3. If you fail, you must either move to the Prison of Memories, or shuffle the top card of the Tekeli-li deck into your deck without looking at it.",
  [`${elderThing}_Fatal Mirage_front`]: "–4. If you fail, place 1 doom on an Eidolon enemy in play.",
  [`${skull}_Fatal Mirage_back`]: "–X. X is the current agenda number plus the number of story cards in the victory display.",
  [`${cultist}_Fatal Mirage_back`]: "–2. If you do not succeed by at least 2, place 1 of your clues on your location.",
  [`${tablet}_Fatal Mirage_back`]: "–4. If you fail, you must either move to the Prison of Memories, or shuffle the top card of the Tekeli-li deck into your deck without looking at it. (If you fail by 2 or more, do both instead.)",
  [`${elderThing}_Fatal Mirage_back`]: "–5. If you fail, place 1 doom on an Eidolon enemy in play.",

  [`${skull}_To the Forbidden Peaks_front`]: "–X. X is the level of your location.",
  [`${cultist}_To the Forbidden Peaks_front`]: "–1. If you fail, move to the location directly below you.",
  [`${tablet}_To the Forbidden Peaks_front`]: "–3. If you fail, lose control of an Expedition asset and place it at your location.",
  [`${elderThing}_To the Forbidden Peaks_front`]: "–4. If you fail, the nearest Elder Thing enemy moves once toward you. If it is engaged with you, it attacks.",
  [`${skull}_To the Forbidden Peaks_back`]: "–X. X is 2 plus the level of your location.",
  [`${cultist}_To the Forbidden Peaks_back`]: "–1. Move to the location directly below you.",
  [`${tablet}_To the Forbidden Peaks_back`]: "–4. If you fail, lose control of an Expedition asset and place it at your location.",
  [`${elderThing}_To the Forbidden Peaks_back`]: "–5. If you fail, the nearest Elder Thing enemy moves once toward you. If it is engaged with you, it attacks.",

  [`${skull}_City of the Elder Things_front`]: "–X. X is the number of keys you control.",
  [`${cultist}_City of the Elder Things_front`]: "–2. If you fail, place a key you control on your location.",
  [`${tablet}_City of the Elder Things_front`]: "–3. If a frost token was revealed during this test, you automatically fail, instead.",
  [`${elderThing}_City of the Elder Things_front`]: "–4. If you fail, the nearest enemy moves once toward you. If it is engaged with you, it attacks.",
  [`${skull}_City of the Elder Things_back`]: "–X. X is 2 plus the number of keys you control.",
  [`${cultist}_City of the Elder Things_back`]: "–2. Place a key you control on your location.",
  [`${tablet}_City of the Elder Things_back`]: "–4. If a frost token was revealed during this test, take 1 damage and you automatically fail, instead.",
  [`${elderThing}_City of the Elder Things_back`]: "–5. If you fail, the nearest enemy moves once toward you. If it is engaged with you, it attacks.",

  [`${skull}_The Heart of Madness_front`]: "–1 (–3 instead if there is an Ancient One enemy at your location).",
  [`${cultist}_The Heart of Madness_front`]: "–1. If there is a seal at your location, or if your location is a Mist-Pylon, treat this token as a frost token, instead.",
  [`${tablet}_The Heart of Madness_front`]: "–3. If you fail, draw the top card of the Tekeli-li deck.",
  [`${elderThing}_The Heart of Madness_front`]: "–4. If you fail by 3 or more, place 1 doom on the current agenda. This can cause the current agenda to advance.",
  [`${skull}_The Heart of Madness_back`]: "–2 (–4 instead if there is an Ancient One enemy at your location).",
  [`${cultist}_The Heart of Madness_back`]: "–1. If there is a seal at your location, or if your location is a Mist-Pylon, treat this token as a frost token in addition to its modifier.",
  [`${tablet}_The Heart of Madness_back`]: "–3. Draw the top card of the Tekeli-li deck.",
  [`${elderThing}_The Heart of Madness_back`]: "–5. If you fail by 3 or more, place 1 doom on the current agenda. This can cause the current agenda to advance.",

  [`${skull}_Riddles and Rain_front`]: "–1 (-3 instead if you have 2 or more clues).",
  [`${tablet}_Riddles and Rain_front`]: "–1. If there is a concealed mini-card at your location, reveal another chaos token.",
  [`${elderThing}_Riddles and Rain_front`]: "-3. If you fail, you must either spend 1 clue or place 1 doom on an enemy in the shadows.",
  [`${skull}_Riddles and Rain_back`]: "–2 (-4 instead if you have 2 or more clues).",
  [`${tablet}_Riddles and Rain_back`]: "–2. If there is a concealed mini-card at your location, reveal another chaos token.",
  [`${elderThing}_Riddles and Rain_back`]: "-4. If you fail, you must either spend 1 clue or place 1 doom on an enemy in the shadows.",

  [`${skull}_Dancing Mad_front`]: "–X. X is the number of enemies in the shadows (max 3).",
  [`${cultist}_Dancing Mad_front`]: "–4. If you fail, put a decoy into play at your location, flip it over, and shuffle each concealed mini-card at your location facedown.",
  [`${tablet}_Dancing Mad_front`]: "–3. If you fail, set each non-weakness card committed to this test aside, out of play, as a hollow.",
  [`${elderThing}_Dancing Mad_front`]: "–1. If there is a concealed mini-card at your location, either take 1 damage or treat this token's modifier as –3.",
  [`${skull}_Dancing Mad_back`]: "–X. X is the number of enemies in the shadows (max 5).",
  [`${cultist}_Dancing Mad_back`]: "–6. If you fail, put a decoy into play at your location, flip it over, and shuffle each concealed mini-card at your location facedown.",
  [`${tablet}_Dancing Mad_back`]: "–3. Set each non-weakness card committed to this test aside, out of play, as a hollow.",
  [`${elderThing}_Dancing Mad_back`]: "–1. If there is a concealed mini-card at your location, either take 2 damage or treat this token's modifier as –5.",

  [`${skull}_Dead Heat_front`]: "–1 for every 1 per investigator civilians slain.",
  [`${cultist}_Dead Heat_front`]: "-4. If you fail, choose a non-Elite enemy at your location. That enemy readies and attacks you.",
  [`${tablet}_Dead Heat_front`]: "–1. You may take 1 damage. If you do not, a civilian at your location is slain.",
  [`${elderThing}_Dead Heat_front`]: "-3. If you fail, choose and discard 1 card from your hand.",
  [`${skull}_Dead Heat_back`]: "–2 for every 1 per investigator civilians slain.",
  [`${cultist}_Dead Heat_back`]: "-6. Choose a non-Elite enemy at your location. That enemy readies and attacks you.",
  [`${tablet}_Dead Heat_back`]: "–2. Take 1 damage. A civilian at your location is slain.",
  [`${elderThing}_Dead Heat_back`]: "-4. If you fail, discard 1 card from your hand at random.",

  [`${skull}_Dealings in the Dark_front`]: "–X. X is the highest number of clues on a Cultist enemy in play, to a maximum of 3. (If it is act 3, X is 3.)",
  [`${cultist}_Dealings in the Dark_front`]: "–5. You may place 1 doom on the nearest Cultist enemy to change this token's modifier to a -1.",
  [`${tablet}_Dealings in the Dark_front`]: "–3. If you fail, place 1 of your clues on your location.",
  [`${elderThing}_Dealings in the Dark_front`]: "-2. If you fail, place 1 doom on the nearest Cultist enemy.",
  [`${skull}_Dealings in the Dark_back`]: "–X. X is the total number of clues on Cultist enemies in play, to a maximum of 4. (If it is act 3, X is 4.)",
  [`${cultist}_Dealings in the Dark_back`]: "–7. You may place 1 doom on the nearest Cultist enemy to change this token's modifier to a -3.",
  [`${tablet}_Dealings in the Dark_back`]: "–4. If you fail, place 1 of your clues on your location.",
  [`${elderThing}_Dealings in the Dark_back`]: "-2. Place 1 doom on the nearest Cultist enemy.",

  [`${skull}_Dogs of War_front`]: "–1 (-3 instead if you are at a location with a Key Locus).",
  [`${cultist}_Dogs of War_front`]: "–3. If you fail, either take 1 damage and 1 horror, or place 1 doom on the nearest Key Locus or Locus Site location.",
  [`${tablet}_Dogs of War_front`]: "–2. If this is an attack against an enemy with patrol, after this attack, it disengages and resolves its patrol keyword.",
  [`${elderThing}_Dogs of War_front`]: "-2. For each point you fail by, lose 1 resource (max 3).",
  [`${skull}_Dogs of War_back`]: "–2 (-4 instead if you are at a location with a Key Locus).",
  [`${cultist}_Dogs of War_back`]: "–5. If you fail, either take 1 damage and 1 horror, or place 1 doom on the nearest Key Locus or Locus Site location.",
  [`${tablet}_Dogs of War_back`]: "–2. If this is an attack against an enemy with patrol, after this attack, it attacks you, disengages, and resolves its patrol keyword.",
  [`${elderThing}_Dogs of War_back`]: "-3. For each point you fail by, lose 1 resource.",

  [`${skull}_On Thin Ice_front`]: "–X. X is the number of Hazard treacheries in play.",
  [`${cultist}_On Thin Ice_front`]: "-4. If you fail, choose a non-weakness card in your hand and set it aside, out of play, as a hollow.",
  [`${tablet}_On Thin Ice_front`]: "–2 (-5 instead if Void Chimera is at your location).",
  [`${elderThing}_On Thin Ice_front`]: "-3. If you fail, look at the top card of your deck. If it is not a weakness, set it aside, out of play, as a hollow.",
  [`${skull}_On Thin Ice_back`]: "–X. X is 1 more than the number of Hazard treacheries in play.",
  [`${cultist}_On Thin Ice_back`]: "-5. Choose a non-weakness card in your hand and set it aside, out of play, as a hollow.",
  [`${tablet}_On Thin Ice_back`]: "–3. If Void Chimera is at your location, you automatically fail, instead.",
  [`${elderThing}_On Thin Ice_back`]: "-4. Look at the top card of your deck. If it is not a weakness, set it aside, out of play, as a hollow.",

  [`${skull}_Sanguine Shadows_front`]: "–X. X is the number of targets on this card.",
  [`${cultist}_Sanguine Shadows_front`]: "–5. If you fail by 2 or more, shuffle each concealed mini-card at your location and at each connecting location facedown, then place them at random in the positions they were in.",
  [`${tablet}_Sanguine Shadows_front`]: "–1. Cancel the effects and icons of each card committed to this skill test.",
  [`${elderThing}_Sanguine Shadows_front`]: "-2. If you fail, you must either place 1 doom on the current agenda, or the nearest Coterie enemy attacks you (even if its in the shadows).",
  [`${skull}_Sanguine Shadows_back`]: "–X. X is 1 more than the number of targets on this card.",
  [`${cultist}_Sanguine Shadows_back`]: "–7. If you fail by 2 or more, shuffle each concealed mini-card at your location and at each connecting location facedown, then place them at random in the positions they were in.",
  [`${tablet}_Sanguine Shadows_back`]: "–2. Cancel the effects and icons of each card committed to this skill test.",
  [`${elderThing}_Sanguine Shadows_back`]: "-3. If you fail, you must either place 1 doom on the current agenda, or the nearest Coterie enemy attacks you (even if its in the shadows).",

  [`${skull}_Shades of Suffering_front`]: "–X. X is half the number of charges on The Shade Reaper, rounded up (X cannot be greater than 6).",
  [`${cultist}_Shades of Suffering_front`]: "-4. If you fail by 2 or more, place 1 charge on The Shade Reaper.",
  [`${tablet}_Shades of Suffering_front`]: "–1. If you are at a location with a Geist enemy, reveal an additional chaos token.",
  [`${elderThing}_Shades of Suffering_front`]: "-4. You may place 1 charge on The Shade Reaper to treat this token's modifier as 0 instead.",
  [`${skull}_Shades of Suffering_back`]: "–X. X is the number of charges on The Shade Reaper.",
  [`${cultist}_Shades of Suffering_back`]: "-5. Place 1 charge on The Shade Reaper.",
  [`${tablet}_Shades of Suffering_back`]: "–3. If you are at a location with a Geist enemy, you automatically fail.",
  [`${elderThing}_Shades of Suffering_back`]: "-6. You may place 1 charge on The Shade Reaper to treat this token's modifier as -3 instead.",

  [`${skull}_Without a Trace_front`]: "–X. X is half the number of locations in play, rounded down.",
  [`${cultist}_Without a Trace_front`]: "–4. If you fail, the nearest Outsider enemy readies, moves once toward you, and attacks you if it is at your location.",
  [`${tablet}_Without a Trace_front`]: "–X. X is the number of set-aside hollows you own (max 5).",
  [`${elderThing}_Without a Trace_front`]: "-3. If you fail, choose a non-weakness card in your hand and set it aside, as a hollow.",
  [`${skull}_Without a Trace_back`]: "–X. X is the number of locations in play.",
  [`${cultist}_Without a Trace_back`]: "–6. If you fail, the nearest Outsider enemy readies, moves once toward you, and attacks you if it is at your location.",
  [`${tablet}_Without a Trace_back`]: "–X. X is 1 plus the number of set-aside hollows you own.",
  [`${elderThing}_Without a Trace_back`]: "-3. Choose a non-weakness card in your hand and set it aside, as a hollow.",

  [`${skull}_Congress of the Keys_front`]: "–X. X is the current act number.",
  [`${cultist}_Congress of the Keys_front`]: "–5. You may flip a Stable key you control to its Unstable side to treat this token's modifier as –2, instead.",
  [`${tablet}_Congress of the Keys_front`]: "–2. If this is an attack against a ready Outsider enemy, you automatically fail, instead.",
  [`${elderThing}_Congress of the Keys_front`]: "–3. Cancel the effects and icons of each card committed to this test and set each of them aside, out of play, as hollows.",
  [`${skull}_Congress of the Keys_back`]: "–X. X is 1 more than the current act number.",
  [`${cultist}_Congress of the Keys_back`]: "–7. You may flip a Stable key you control to its Unstable side to treat this token's modifier as –4, instead.",
  [`${tablet}_Congress of the Keys_back`]: "–2. If there is a ready Outsider enemy at your location, you automatically fail, instead.",
  [`${elderThing}_Congress of the Keys_back`]: "–4. Cancel the effects and icons of each card committed to this test and set each of them aside, out of play, as hollows.",

  /* Template
  [`${skull}__front`]: "",
  [`${cultist}__front`]: "",
  [`${tablet}__front`]: "",
  [`${elderThing}__front`]: "",
  [`${skull}__back`]: "",
  [`${cultist}__back`]: "",
  [`${tablet}__back`]: "",
  [`${elderThing}__back`]: "",
  */
};

// Variables
let profileName;
let drawHistory = [];
let drawnTokens = [];
let tokenValues = [];
let selectedCampaign = 'The Night of the Zealot';
let selectedDifficulty = 'easy';
let selectedScenario = 'The Gathering';
let chaosBag = [...presets[selectedCampaign][selectedDifficulty]];
let chaosBagCopy = [...chaosBag];

// Functions
const calculateOdds = tokenValue => {
  const [tokenCount, totalTokens] = [chaosBagCopy[tokenValue], chaosBagCopy.reduce((sum, quantity) => sum + quantity, 0)];
  const odds = Math.round((tokenCount / totalTokens) * 1000) / 10;
  return `${odds}%`;
};

const showOdds = () => {
  htmlElements.contentContainer.style.display = 'block';
};

const hideOdds = () => {
  htmlElements.contentContainer.style.display = 'none';
};

const resetChaosBag = () => {
  chaosBag = [...presets[selectedCampaign][selectedDifficulty]];
  drawnTokens = [];
};

const showContents = () => {
  htmlElements.tokenImage.className = '';
  let tokenValues = [];
  chaosBagCopy = [...chaosBag];

  chaosBag.forEach((quantity, value) => {
    tokenValues.push(...Array(quantity).fill(value));
  });

  htmlElements.contentContainer.innerHTML = '';
  htmlElements.bagContents.innerHTML = '';

  let row = document.createElement('div');
  row.className = 'row';
  htmlElements.bagContents.appendChild(row);

  tokenValues.forEach(function(value) {
    let token = document.createElement('span');
    token.className = tokenNames[value];
    row.appendChild(token);
  });

  if (htmlElements.displayOddsCheckbox.checked) {
    showOdds();
  } else {
    hideOdds();
  }
  updateBagTotal();
};

const updateSubtitle = () => {
  htmlElements.subtitle.textContent = `${selectedCampaign} | ${selectedScenario} | ${selectedDifficulty}`;
};

const updateBagTotal = () => {
  const bagTotalElement = document.getElementById('bag-total');
  const totalTokens = chaosBag.reduce((sum, quantity) => sum + quantity, 0);
  bagTotalElement.textContent = `${totalTokens}`;
};

const clearHistory = () => {
  drawHistory = [];
  htmlElements.drawHistory.innerHTML = '';
  htmlElements.drawHistoryTotal.textContent = `${drawHistory.length}`;
};

const updateScenarioDropdown = () => {
  // Get the currently selected campaign
  let selectedCampaign = htmlElements.campaignSelector.value;

  // Clear the current options
  htmlElements.scenarioSelector.innerHTML = '';

  // Get the new scenarios
  let campaignScenarios = scenarios[selectedCampaign];

  // Create and append new option elements for each scenario
  for (let scenario of campaignScenarios) {
    let option = document.createElement('option');
    option.text = scenario;
    option.value = scenario;
    htmlElements.scenarioSelector.appendChild(option);
  }

  selectedScenario = htmlElements.scenarioSelector.value;
  updateSubtitle();
};

const generateReference = (tokenValue, scenario, difficulty) => {
  let key = `${tokenValue}_${scenario}_${normalizedDifficulty}`;
  return references[key] || "";
};

// Event Listener Functions
const drawToken = () => {
  htmlElements.contentContainer.innerHTML = '';
  htmlElements.tokenImage.className = '';
  htmlElements.referenceText.innerHTML = '';
  tokenValues = [];
  chaosBagCopy = [...chaosBag];

  chaosBag.forEach((quantity, value) => {
    tokenValues.push(...Array(quantity).fill(value));
  });

  let randomIndex = Math.floor(Math.random() * tokenValues.length);
  let randomValue = tokenValues[randomIndex];
  let className = tokenNames[randomValue];
  let odds = calculateOdds(randomValue);

  // Add drawn token to history
  drawHistory.push(tokenNames[randomValue]);
  
  // Decrement the quantity of the selected token
  chaosBagCopy[randomValue]--;

  if (className === "icon-token_bless_sealed" || className === "icon-token_curse_sealed") {
    tokenValues.splice(randomIndex, 1); // Remove the value from the tokenValues array
    chaosBag[randomValue]--; // Decrement the quantity in the chaosBag array
  }

  // Disable the "Draw Token" button
  htmlElements.drawTokenButton.disabled = true;

  // Add a visual indicator
  htmlElements.drawTokenButton.innerText = "Drawing...";

  // Enable the "Reveal Another" button
  htmlElements.revealAnotherButton.disabled = false;

  // Disable the instructions
  htmlElements.instructionsElement.style.display = 'none';

  // Reset the visual indicator after a short delay
  setTimeout(() => {
    if (htmlElements.displayOddsCheckbox.checked) {
      htmlElements.contentContainer.textContent = `Odds: ${odds}`;
    } else {
      htmlElements.contentContainer.textContent = '';
    }
    htmlElements.tokenImage.className = className;
    htmlElements.drawTokenButton.disabled = false;
    htmlElements.drawTokenButton.innerText = "Draw Token";

    // Calculate the number of available tokens remaining
    let availableTokens = tokenValues.filter(value => !drawnTokens.includes(value));
    htmlElements.revealAnotherButton.innerText = `Reveal Another (${availableTokens.length - 1})`;

    // Display reference text only if the checkbox is selected
    if (htmlElements.displayReferenceCheckbox.checked) {
      let referenceText = generateReference(className, selectedScenario, selectedDifficulty);
      htmlElements.referenceText.textContent = referenceText;
    }
  }, 500);
 
};


const revealAnotherToken = () => {
  htmlElements.contentContainer.innerHTML = '';
  htmlElements.tokenImage.className = '';
  htmlElements.referenceText.innerHTML = '';

  // Calculate tokenValues
  tokenValues = [];
  chaosBagCopy.forEach((quantity, value) => {
    tokenValues.push(...Array(quantity).fill(value));
  });

  // Exclude drawn tokens from the pool
  let availableTokens = tokenValues.filter(value => !drawnTokens.includes(value));

  if (availableTokens.length === 0) {
    alert('No more tokens left!');
    return;
  }

  // Count the quantity of each available token
  let tokenCounts = {};
  availableTokens.forEach(token => {
    tokenCounts[token] = (tokenCounts[token] || 0) + 1;
  });

  // Create an array of available tokens with their quantities
  let tokensWithQuantities = Object.entries(tokenCounts);

  // Generate a random index based on the available tokens
  let randomIndex = Math.floor(Math.random() * tokensWithQuantities.length);
  let [randomValue] = tokensWithQuantities[randomIndex];
  let className = tokenNames[randomValue];
  let odds = calculateOdds(randomValue);

  // Add drawn token to history
  drawHistory.push(tokenNames[randomValue]);

  // Decrement the quantity of the selected token
  chaosBagCopy[randomValue]--;

  // Remove the token from the availableTokens if its quantity reaches zero
  if (chaosBagCopy[randomValue] === 0) {
    availableTokens = availableTokens.filter(token => token !== randomValue);
  }

  // Add the drawn token to drawnTokens
  drawnTokens.push(randomValue);

  // Disable the "Reveal Another" button
  htmlElements.revealAnotherButton.disabled = true;

  // Add a visual indicator
  htmlElements.revealAnotherButton.innerText = "Revealing...";

  // Reset the visual indicator after a short delay
  setTimeout(() => {
    let tokenImg = document.createElement('img');
    tokenImg.className = className;
    htmlElements.tokenImage.className = className;

    if (className === "icon-token_bless_sealed" || className === "icon-token_curse_sealed") {
      tokenValues.splice(randomIndex, 1); // Remove the value from the tokenValues array
      chaosBag[randomValue]--; // Decrement the quantity in the chaosBag array
    }

    if (htmlElements.displayOddsCheckbox.checked) {
      htmlElements.contentContainer.textContent = `Odds: ${odds}`;
    } else {
      htmlElements.contentContainer.textContent = '';
    }

    // Update the "Reveal Another" button text
    htmlElements.revealAnotherButton.innerText = `Reveal Another (${availableTokens.length - 1})`;

    // Enable the "Reveal Another" button
    htmlElements.revealAnotherButton.disabled = false;
    
    // Display reference text only if the checkbox is selected
    if (htmlElements.displayReferenceCheckbox.checked) {
      let referenceText = generateReference(className, selectedScenario, selectedDifficulty);
      htmlElements.referenceText.textContent = referenceText;
    }
  }, 500);
};

const modifyBag = () => {
  htmlElements.overlay.classList.toggle('overlay-visible');
  htmlElements.revealAnotherButton.disabled = true;
  htmlElements.revealAnotherButton.innerText = 'Reveal Another';
  showContents();
  htmlElements.instructionsElement.style.display = 'block';
};

const addToken = () => {
  let tokenName = "icon-token_" + htmlElements.tokenInput.value + (
    htmlElements.tokenInput.value === 'cultist' || 
    htmlElements.tokenInput.value === 'tablet' || 
    htmlElements.tokenInput.value === 'skull' ||
    htmlElements.tokenInput.value === 'elder_thing' ||
    htmlElements.tokenInput.value === 'elder_sign' ||
    htmlElements.tokenInput.value === 'auto_fail' ? '_highlight' : '_sealed');
  if (tokenNames.includes(tokenName)) {
    let tokenIndex = tokenNames.indexOf(tokenName);
    if (tokenIndex !== -1) {
      chaosBag[tokenIndex] += 1;
    } else {
      alert('Invalid token name. Please select a valid token from the dropdown.');
    }
    showContents();
  } else {
    alert('Invalid token name. Please select a valid token from the dropdown.');
  }
};

const removeToken = () => {
  let tokenName = "icon-token_" + htmlElements.tokenInput.value + (
    htmlElements.tokenInput.value === 'cultist' || 
    htmlElements.tokenInput.value === 'tablet' || 
    htmlElements.tokenInput.value === 'skull' ||
    htmlElements.tokenInput.value === 'elder_thing' ||
    htmlElements.tokenInput.value === 'elder_sign' ||
    htmlElements.tokenInput.value === 'auto_fail' ? '_highlight' : '_sealed');
  if (tokenNames.includes(tokenName)) {
    let tokenIndex = tokenNames.indexOf(tokenName);
    if (tokenIndex !== -1) {
      chaosBag[tokenIndex] = Math.max(0, chaosBag[tokenIndex] - 1);
    } else {
      alert('Invalid token name. Please select a valid token from the dropdown.');
    }
    showContents();
  } else {
    alert('Invalid token name. Please select a valid token from the dropdown.');
  }
};

const closeOverlay = () => {
  htmlElements.overlay.classList.remove('overlay-visible');
};

const toggleDisplayOdds = () => {
  if (htmlElements.displayOddsCheckbox.checked) {
    showOdds();
  } else {
    hideOdds();
  }
};

const changeCampaign = () => {
  htmlElements.contentContainer.innerHTML = '';
  htmlElements.tokenImage.className = '';
  selectedCampaign = htmlElements.campaignSelector.value;
  chaosBag = [...presets[selectedCampaign][selectedDifficulty]];
  showContents();
  updateSubtitle();
  updateScenarioDropdown();
};

const changeScenario = () => {
  htmlElements.contentContainer.innerHTML = '';
  htmlElements.tokenImage.className = '';
  selectedScenario = htmlElements.scenarioSelector.value;
  showContents();
  updateSubtitle(); // Update the subtitle when the scenario changes
};

const changeDifficulty = () => {
  htmlElements.contentContainer.innerHTML = '';
  htmlElements.tokenImage.className = '';
  selectedDifficulty = htmlElements.difficultySelector.value;
  chaosBag = [...presets[selectedCampaign][selectedDifficulty]];
  showContents();
  updateSubtitle(); // Update the subtitle when the difficulty changes
};

const displayHistory = () => {
  // clear any existing history
  htmlElements.drawHistory.innerHTML = '';

  // Add the token images to the history overlay
  drawHistory.forEach(tokenName => {
    let tokenSpan = document.createElement('span');
    tokenSpan.className = tokenName;
    htmlElements.drawHistory.appendChild(tokenSpan);
  });

  // Update the total
  htmlElements.drawHistoryTotal.textContent = `${drawHistory.length}`;

  // Show the history overlay
  htmlElements.historyOverlay.classList.add('overlay-visible');
};

const closeHistoryOverlay = () => {
  htmlElements.historyOverlay.classList.remove('overlay-visible');
};


const updateProfileSubtitle = () => {
  htmlElements.subtitle.textContent = `Profile: ${htmlElements.profile.value}`;
};

// Save profile
const saveBagContents = () => {
  let selectedProfile = htmlElements.profile.value;
  if (selectedProfile.startsWith("Empty Profile")) {
    try {
      const newName = prompt("Please enter a name for your profile:");
      if (newName === null) {
        return; // User clicked cancel, close the prompt
      }
      if (newName.trim() !== "" && newName.trim() !== "Empty Profile") {
        selectedProfile = newName;
        const selectedOption = htmlElements.profile.options[htmlElements.profile.selectedIndex];
        selectedOption.text = selectedProfile;
        selectedOption.value = selectedProfile;
        updateProfileSubtitle();
      } else {
        throw new Error('Invalid profile name.'); // Throw an error to be caught later
      }
    } catch (error) {
      alert(error.message); // Display the error message
      return;
    }
  }

  const dataToSave = {
    chaosBag: chaosBag,
    campaign: selectedCampaign,
    difficulty: selectedDifficulty
  };
  const dataJSON = JSON.stringify(dataToSave);
  localStorage.setItem("profile-" + selectedProfile, dataJSON);
  alert(`Bag contents saved to profile "${selectedProfile}"!`);
};


// Load profile
const loadBagContents = () => {
  let selectedProfile = htmlElements.profile.value;
  if (selectedProfile.startsWith("Empty Profile")) {
    alert('Please select a profile to load.');
    return;
  }

  const dataJSON = localStorage.getItem("profile-" + selectedProfile);
  if (dataJSON) {
    const dataLoaded = JSON.parse(dataJSON);
    chaosBag = dataLoaded.chaosBag;
    selectedCampaign = dataLoaded.campaign;
    selectedDifficulty = dataLoaded.difficulty;
    showContents();
    updateProfileSubtitle(); // Update the subtitle
    alert(`Bag contents loaded from profile "${selectedProfile}"!`);
  } else {
    alert(`No saved bag contents found for profile "${selectedProfile}".`);
  }
};


const updateProfileName = () => {
  profileName = htmlElements.profile.value;
};

// Delete profile
const deleteProfile = () => {
  const selectedProfile = htmlElements.profile.value;
  if (selectedProfile.startsWith("Empty Profile")) {
    alert('Please select a profile to delete.');
    return;
  }

  const confirmation = confirm(`Are you sure you want to delete profile "${selectedProfile}"?`);
  if (confirmation) {
    localStorage.removeItem("profile-" + selectedProfile);
    htmlElements.profile.options[htmlElements.profile.selectedIndex] = new Option("Empty Profile", "Empty Profile");
    // Reset the chaos bag to its initial state
    resetChaosBag();
    updateSubtitle();
    showContents();
    alert(`Profile "${selectedProfile}" deleted.`);
  }
};

const loadProfileNames = () => {
  // Get all keys from local storage
  const allKeys = Object.keys(localStorage);

  // Filter out the keys that don't start with "profile-"
  const profileKeys = allKeys.filter(key => key.startsWith("profile-"));

  // Map the profile keys to profile names
  const profileNames = profileKeys.map(key => key.replace("profile-", ""));

  // Get the select element
  const select = htmlElements.profile;

  // Remove all options
  select.innerHTML = '';

  // Add an option for each profile
  profileNames.forEach(name => {
    const option = document.createElement('option');
    option.text = name;
    option.value = name;
    select.add(option);
  });

  // Add enough empty profiles to total 5 slots
  const numberOfEmptyProfilesNeeded = 5 - profileNames.length;
  for(let i = 1; i <= numberOfEmptyProfilesNeeded; i++) {
    const option = document.createElement('option');
    option.value = `Empty Profile`;
    option.text = `Empty Profile`;
    select.add(option);
  }
};

// Call loadProfileNames function during page load to populate profile select options
window.onload = loadProfileNames;

const renameProfile = () => {
  const selectedIndex = htmlElements.profile.selectedIndex;
  const oldProfileName = htmlElements.profile.value;

  // Check if the old profile name is "Empty Profile"
  if (oldProfileName === "Empty Profile") {
    alert("Please select a valid profile.");
    return;
  }

  const newProfileName = prompt("Enter the new name for the profile:");

  // Check if the profile name already exists
  if (localStorage.getItem("profile-" + newProfileName) !== null) {
    alert(`The profile name "${newProfileName}" already exists. Please enter a different name.`);
    return;
  }

  // Validate the new profile name
  if (newProfileName.trim() === "" || newProfileName.trim() === "Empty Profile") {
    alert("Invalid profile name. Please try again.");
    return;
  }

  newProfileName = newProfileName.trim(); // Remove leading/trailing whitespace

  const dataJSON = localStorage.getItem("profile-" + oldProfileName);
  if (dataJSON) {
    // Remove the old profile
    localStorage.removeItem("profile-" + oldProfileName);

    // Save the data under the new profile name
    localStorage.setItem("profile-" + newProfileName, dataJSON);

    // Update the profile name in the select options
    htmlElements.profile[selectedIndex].text = newProfileName;
    htmlElements.profile[selectedIndex].value = newProfileName;

    // update the global profileName only after a successful rename operation
    profileName = newProfileName;

    updateProfileSubtitle(); // Update the subtitle

    alert(`Profile "${oldProfileName}" has been renamed to "${newProfileName}"`);
  } else {
    alert(`No saved profile found with the name "${oldProfileName}"`);
  }
};

// Event Listeners
htmlElements.drawTokenButton.addEventListener('click', drawToken);
htmlElements.revealAnotherButton.addEventListener('click', revealAnotherToken);
htmlElements.modifyBagButton.addEventListener('click', modifyBag);
htmlElements.addTokenButton.addEventListener('click', addToken);
htmlElements.removeTokenButton.addEventListener('click', removeToken);
htmlElements.closeOverlayButton.addEventListener('click', closeOverlay);
htmlElements.displayOddsCheckbox.addEventListener('change', toggleDisplayOdds);
htmlElements.campaignSelector.addEventListener('change', changeCampaign);
htmlElements.scenarioSelector.addEventListener('change', changeScenario);
htmlElements.difficultySelector.addEventListener('change', changeDifficulty);
htmlElements.historyButton.addEventListener('click', displayHistory);
htmlElements.closeHistoryOverlayButton.addEventListener('click', closeHistoryOverlay);
htmlElements.saveButton.addEventListener('click', saveBagContents);
htmlElements.loadButton.addEventListener('click', loadBagContents);
htmlElements.profile.addEventListener('change', updateProfileName);
htmlElements.deleteButton.addEventListener('click', deleteProfile);
htmlElements.renameButton.addEventListener('click', renameProfile);
htmlElements.clearHistoryButton.addEventListener('click', clearHistory);

// Initial setup
htmlElements.revealAnotherButton.disabled = true;
hideOdds();
updateSubtitle();
updateScenarioDropdown();
```

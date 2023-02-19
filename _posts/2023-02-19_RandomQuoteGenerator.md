---
layout: post
title: Building a Random Quote Generator with React
image: "/posts/React.png"
tags: [CSS, JavaScript, React, freeCodeCamp]
---
# Building a Random Quote Generator
<img width="478" alt="Screenshot 2023-02-19 at 3 25 12 PM" src="https://user-images.githubusercontent.com/19756136/219973377-f8559ed8-8221-400a-8b05-eb7795897b1a.png">
This is one of the freeCodeCamp Front End Development Libraries projects intended to introduce students to Frontend frameworks and libraries.

In this project I used React and a little bit of Bootstrap for button styling.

See the completed project [here](https://codepen.io/chris-delgado/pen/rNZOwVZ).

## What is React?

## What is CodePen?
CodePen is an online community for testing and showcasing user-created HTML, CSS and JavaScript code snippets. It functions as an online code editor and open-source learning environment, where developers can create code snippets, called "pens," and test them.

## Source Code
Below is the HTML, CSS, and JavaScript used to build the random quote generator. Note that Codepen only asks for HTML body and that bootstrap stylesheets were added in settings.

```html
<link rel="stylesheet"
href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"/>

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.2/font/bootstrap-icons.css">

<div id="root"></div>
```

```css
body {
  transition: all 0.5s ease-in-out;
  font-family: sans-serif;
  font-weight: 400;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

#root {
  width: 450px;
  padding: 40px 50px;
  display: table;
  background-color: #fff;
  padding: 1rem;
  border-radius: 10px;
}

#text {
  font-size: x-large;
}

.align-right {
   text-align: right;
}
```

```javascript
import React, { useState, useEffect }  from "https://cdn.skypack.dev/react@17.0.1";

import ReactDOM from "https://cdn.skypack.dev/react-dom@17.0.1";

function QuoteBox() {
  const [quote, setQuote] = useState({});
  const [color, setColor] = useState("#fff");

  async function getQuote() {
     const colors = [
    '#16a085',
    '#27ae60',
    '#2c3e50',
    '#f39c12',
    '#e74c3c',
    '#9b59b6',
    '#FB6964',
    '#342224',
    '#472E32',
    '#BDBB99',
    '#77B1A9',
    '#73A857'
  ];
    
    let randColorIndex = Math.floor(Math.random() * colors.length);
    
    
  // Update the color state with the randomly generated color
  setColor(colors[randColorIndex]);
    
  // Update the body background-color and color with the randomly generated color
  document.body.style.backgroundColor = colors[randColorIndex];
  document.body.style.color = colors[randColorIndex];
    
	const response = await fetch("https://type.fit/api/quotes");
    const quotes = await response.json();
    const randIndex = Math.floor(Math.random() * quotes.length);
    return quotes[randIndex];
  }

  useEffect(() => {
    async function loadQuote() {
      const quoteData = await getQuote();
      setQuote(quoteData);
    }

    loadQuote();
  }, []);

  function handleNewQuoteClick() {
    getQuote().then((quoteData) => setQuote(quoteData));
  }

  return (
    <div id="quote-box">
      <p id="text">{quote.text}</p>
      <div class="align-right">
        <p id="author">{quote.author}</p>
        <button type="button" id="new-quote" className="btn btn-secondary" onClick={handleNewQuoteClick}>
          New Quote
        </button>
        <a
          href={`https://twitter.com/intent/tweet?text=${quote.text} - ${quote.author}`}
          target="_top"
          id="tweet-quote"
          className="btn btn-primary"
        ><i className="bi bi-twitter"></i>
          </a>
      </div>
    </div>
  );
}

function App() {
  return (
    <div>
      <QuoteBox />
    </div>
  );
}

ReactDOM.render(<App/>, document.getElementById("root"));
```

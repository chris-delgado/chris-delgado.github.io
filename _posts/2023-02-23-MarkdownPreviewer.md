---
layout: post
title: Building a Markdown Previewer
image: "/posts/MarkdownPreviewer.png"
tags: [JavaScript, React, freeCodeCamp]
---
# Building a Markdown Previewer
<img width="515" alt="Screenshot 2023-02-23 at 5 43 12 PM" src="https://user-images.githubusercontent.com/19756136/221047438-7bcbde98-bbc5-4c78-b419-5b00d357b200.png">

This is the second of five freeCodeCamp Front End Development Libraries projects. The full list of user stories for this project can be found [here](https://www.freecodecamp.org/learn/front-end-development-libraries/front-end-development-libraries-projects/build-a-markdown-previewer).

See the completed project at Codepen [here](https://codepen.io/chris-delgado/pen/abaZjQj). Note that I could not get the optional user story completed with React-Markdown, although I did see how to do so with the Marked library.

## Helpful Tutorials
These two videos were very helpful in getting different perspectives on completing the project.

[Florin Pop](https://www.youtube.com/watch?v=CJt7uZD_iK0)


![Landon Schlangen](https://www.youtube.com/watch?v=dW0vY5vvU1U)

## Source Code
Below is the HTML, CSS, and JavaScript used to build the markdown previewer. Bootstrap stylesheets were added in the Codepen CSS settings; React, React-DOM and React-Markdown were added in the Codepen JavaScript settings.

```html
<div id='root'></div>
```

```css
body {
  background-color: #333;
  color: white;
}

textarea {
  height: 100%;
  width: 100%;
}
```

```javascript
function App() {
  const [text, setText] = React.useState(`
  # Header 1
  ## Header 2
 
  Link to [Google](https://google.com)
  
  Inline Code \`<div></div>\`
  
  Code Block
  \`\`\`
  let x = 1;
  let y = 2;
  let z = x + y;
  \`\`\`
  
  - list item 1
  - list item 2
  - list item 3
  
  > Block quote
  
  ![Cat Laughing](https://live.staticflickr.com/4105/5016931339_1db5cc145d.jpg)
  
  **Bolded Text**
  
  `);  
  return (
    <div>
      <h1 className="text-center">Markdown Previewer</h1>
      <div className="row">
        <span className="col-6">
        <textarea 
          id="editor"
          value={text}
          onChange={(e) => setText(e.target.value)}
        ></textarea>
        </span>

        <span className="col-6">
        <Preview markdown={text}/>
        </span>
      </div>
    </div>
  );
}

function Preview( {markdown} ) {
  return (
    <div id="preview"><ReactMarkdown>
      {markdown}
    </ReactMarkdown></div>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));
```

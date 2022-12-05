---
layout: post
title: Notetaking With Obsidian
image: "/posts/obsidian.png"
tags: [JavaScript, Notetaking, Obsidian]
---
# Notetaking With Obsidian
This post is intended to give a quick overview of notetaking principles and the notes app Obsidian. I have included an example vault as well which can be viewed through Obsidian.

## Notetaking Principles
Using a smart note taking system is a good strategy to compensate for our brain's limitations. By transferring thoughts and ideas to an external source (like a notebook or laptop), we facilitate an ongoing dialogue with them, helping to better reinforce these concepts within ourselves.

The evolution of personal notetaking methods has roughly progressed as listed in the following table (1 being the oldest):

| Number | Method       | Benefits                                                        | Drawbacks                                        |
| ------ | ------------ | --------------------------------------------------------------- | ------------------------------------------------ |
| 1      | Paper     | Lets you offload ideas from your head                           | No organization or relationships between notes   |
| 2      | Notebooks | Allows you to keep a related collection of notes together       | Rigid structure that is difficult to rearrange   |
| 3      | Folders   | Allows you to move contents in and out                          | Real-world ideas rarely fit into neat categories |
| 4      | Tags      | Notes no longer have to belong to mutually exclusive categories | Difficult to understand how notes are connected  |
| 5       | Links     | Explicitly connects ideas together                              | Difficult to implement in the physical world     |

Using links to navigate between topics and ideas is commonplace on the Internet (e.g. search results, wikipedia). With the advent of more sophisticated digital notetaking applications, that same method can now easily be used in personal knowledge management. Apps like Obsidian make links "first class citizens" and are designed around getting the most utility out of them.

One of the biggest temptations when organizing notes is to get too perfectionistic, treating the process of organizing as an end in itself. A natural way to manage information with minimal effort is by organizing notes by active projects. Consider new information in terms of utility - how is this going to help me move forward one of my current projects?

Some useful principles to keep in mind when making notes:
1. Make notes as concise and independently comprehensible as possible
2. Keep every note linked to at least one other
3. Use notes dedicated for connecting ideas (e.g. an index)
4. Use note sequences (e.g. for constructing sequential arguments or stories)
5. Don't worry about organizational structure (take a bottom-up approach instead)

## Obsidian

<img width="163" alt="Screenshot 2022-12-01 at 5 35 44 PM" src="https://user-images.githubusercontent.com/19756136/205523275-f69f7ffe-b649-4807-bc07-80f6dadaa1aa.png">

Obsidian is an extensible knowledge base that works on top of your local folder of plain text files. It can be downloaded [here](https://obsidian.md).

Its main features are:
1. Your notes are composed of plaintext files which can be saved locally
2. An emphasis on internal links for connecting your notes
3. The usage of panes to allow you to view and work on multiple notes at once
4. Extensibility with Core and Community Plugins

## YAML
Depending on whom you ask, YAML stands for yet another markup language or YAML ain’t markup language (a recursive acronym). It is a superset of JSON, so JSON files are valid in YAML, but YAML tends to have better readability and user-friendliness.

In the context of Obsidian note-taking, YAML frontmatter is an optional section of valid YAML that is placed at the top of a page and is used for maintaining metadata for the page and its contents. You can then query this metadata using community plugins like Dataview and Obsidian Charts.

Here's an example of YAML I have at the top of one of my daily notes:

```YAML Example
---
Highlight: "Having chicken and waffles at the diner with Amy."
Reflections:
- {Number: 1, Subject: Health, Note: "Shoulder is killing me this morning. Arm circles from yesterday were a bad idea maybe? Although the pants pulls were also surprisingly tough. Less weight today."}
- {Number: 2, Subject: Health, Note: "Four supraspinatus exercises seemed OK. Thinking I'll alternate between these and three infraspinatus exercises. Definitely no arm circles lol."}
- {Number: 3, Subject: Music, Note: "Finished Regrets. It should be published on the 6th."}
- {Number: 4, Subject: Misc, Note: "I should have a daily highlight to capture in my notes."}
- {Number: 5, Subject: Health, Note: "Terrible allergies today."}

Exercise:
- {Name: 90/90 External Rotation, Weight: 2.5, Unit: lb, Sets: 2, Reps: 20}
- {Name: Full Can, Weight: 2.5, Unit: lb, Sets: 2, Reps: 20}
- {Name: Prone Y, Weight: 2.5, Unit: lb, Sets: 2, Reps: 20}
- {Name: Side Lying External Rotation, Weight: 2.5, Unit: lb, Sets: 2, Reps: 20}
- {Name: Stationary Bike, Resistance: 12, Unit: level, Duration: 1h 10m, Avg_HR: 128}

Calories: 3040
Protein: 177
Saturated_Fat: 30
SleepStart: 2022-11-14T21:30
SleepEnd: 2022-11-15T06:30
Weight: 145.2
BookTime: 49m
ExerciseTime: 100m
PianoTime: 76m
ProjectTime: 362m
TaskTime: 67m
---
```

## Obsidian Community Plugins
Below are five of the Obsidian community plugins that I've found the most helpful and interesting.

#### Advanced Tables
![basic functionality](https://raw.githubusercontent.com/tgrosinger/advanced-tables-obsidian/main/resources/screenshots/basic-functionality.gif)
Tables in markdown are a pain, but this plugin mitigates some of that by adding improved navigation, formatting, and manipulation in Obsidian. Auto formatting is the feature I like the most about it.

#### Dataview
Lets you use Obsidian as a database from which you can query. Queries are similar in syntax to SQL, and for more complex use cases, it has JavaScript integration as well.

**Example**: Show all files in the `books` folder that you read in 2021, grouped by genre and sorted by rating:

<img width="857" alt="Screenshot 2022-12-04 at 7 00 20 PM" src="https://user-images.githubusercontent.com/19756136/205523871-8aa68f4c-e654-4dea-bf3d-89a0ea9ffe08.png">

![Books By Genre](https://raw.githubusercontent.com/blacksmithgu/obsidian-dataview/HEAD/docs/docs/assets/books-by-genre.png)

#### Obsidian Charts
Obsidian Charts let's you create interactive Charts inside Obsidian.

<img width="417" alt="Screenshot 2022-12-03 at 2 44 24 PM" src="https://user-images.githubusercontent.com/19756136/205523297-c810c435-3c8f-46b9-9c18-b2037ca52755.png">

#### Tracker
Helps you collect data from notes and represent it visually.

![Pasted image 20221203144546](https://user-images.githubusercontent.com/19756136/205523307-a2d8b5c6-ab48-4129-a4e9-e6ffa14af032.png)

#### Templater
Templater is a template language that lets you insert **variables** and **functions** results into your notes. It will also let you execute JavaScript code manipulating those variables and functions.

The following template file uses Templater syntax:

<img width="745" alt="Screenshot 2022-12-04 at 6 59 05 PM" src="https://user-images.githubusercontent.com/19756136/205523792-c48c2005-4fc4-498f-83e6-de6b91653d2a.png">

The above file will produce the following result when inserted:

<img width="704" alt="Screenshot 2022-12-04 at 6 59 45 PM" src="https://user-images.githubusercontent.com/19756136/205523828-f8cf21c4-665f-4d1b-90ef-9eb6d6ced542.png">


## Example Vault
I've uploaded an example Obsidian vault on GitHub [here](https://github.com/chris-delgado/chris-delgado.github.io/blob/main/obsidian/Example_Vault.zip) with some of the notes I've created that leverage YAML and the above plugins. The table below describes key notes in that vault. You will need to install and enable the community plugins I listed above for some of these notes to render and function correctly. Not all of the links from my personal vault were transferred to the example vault, so there will be many that will be grayed out.

| Note                               | Description                                                                           |
| ---------------------------------- | ------------------------------------------------------------------------------------- |
| [[2022 New Orleans]]               | Index note for planning a trip to New Orleans (images have been removed)              |
| [[Book Note Template]]             | Template note for the books I read                                                    |
| [[Books]]                          | Index note for books I've read/am reading                                             |
| [[Daily Note Template]]            | My current daily note template                                                        |
| [[Index]]                          | Top level index note containing the PARA links to which all my other notes are linked |
| [[Meal Prep Cheatsheet]]           | Note that contains a dataview table which I refer to when preparing food              |
| [[Monthly Review - November 2022]] | Monthly review note which pulls metadata from 30 daily notes from November 2022       |
| [[Monthly Review Template]]        | Template note for reviewing the past month                                            |
| [[Project Note Template]]          | Template note for the projects I work on                                              |
| [[Projects]]                       | Index note for all my projects                                                        |
| [[Templates]]                      | Index note for templates I've created                                                 |

## Further Reading
[Building a Second Brain: An Overview](https://fortelabs.com/blog/basboverview/)

[What is YAML?](https://www.redhat.com/en/topics/automation/what-is-yaml)

[Zettelkasten — How One German Scholar Was So Freakishly Productive](https://writingcooperative.com/zettelkasten-how-one-german-scholar-was-so-freakishly-productive-997e4e0ca125)

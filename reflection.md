# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
      Before I started playing it, the game that the AI has built looked clean, has a nice user interface, and it contained all the fields and settings needed to play the game. However, the first time, I played the game, I noticed that it was giving the wrong hints. For example, when the secret is 6 and I guessed 5, the game displayed "Go Lower" rather than "Go higher". 

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
    1. The first bug I noticed was that When I click the New game button, the history doesn't get reset 
    2. The 2nd bug I noticed was that the history doesn't get updated immediately when I enter a guess. 
       when I make a 2nd guess, it logs the first guess value into the history. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

|        Input                  | Expected Behavior | Actual Behavior        | Console Output / Error |
|-------------------------------|-------------------|------------------------|------------------------|
|Guess 7 with secret 73         | Go Higher!        | Go Lower!              | None                   |
|Score inaccurate when game won | Score: postive num| Score: negative num    | None                   |
|Start Over button doesn't work |Starts over game   |History list stays same | None                   |



## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
      I used Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

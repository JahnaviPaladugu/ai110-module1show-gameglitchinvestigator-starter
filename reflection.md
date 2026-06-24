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

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
      I used Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
    An example of an AI suggestion was to swap the hint messages in the check_guess function so that if the secret is 20 and guess is 30, the game will give accurate hints such as "Go Lower!". The AI implemented this code change correctly and I was able to test this by running the pytest cases and also manually played the game to ensure that the hints shown are accurate when making a guess. 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
    I have given the instruction to AI to generate pytests for both of the bugs that it fixed (Show correct hints and show correct score). 
    Claude has created the test cases in test_game_logic.py and I verfied that the test cases code sytanx and logic looks accurate. 
    However, when Claude tried to run the pytest, I don't have the pytest package installed so rather than letting me know its not installed/failed to run the tests file, it told me that all the tests have passed.
    I found out pytest was not installed when I tried to manually run the pytest.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
    I read through the explanation that AI gave after it fixed the bug to make sure it understood my intention. I then looked into the code that it modified and ensure the code fix looked correct. Finally, for testing, I ran the pytests and manually tested the game by playing it with different scenarios. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
    One of the bugs I wanted to fix was the incorrect score shown when the game is won. Initially, the score was showing negative numbers even though I guessed the secret in the first try. Once AI fixed the bug, I tested again manually and the score was more accurate and the score was higher if the guess is correct in fewer attempts. I understood more about the score system when I checked the code and how AI fixed this bug.
- Did AI help you design or understand any tests? How?
   Yes, when I asked AI to generate pytests, I only thought of a few test cases but the AI generated a lot of test cases and edge cases that I did not initially think of. I am also not familar with pytests and the syntax and looking at AI code helped me learn some of the sytax for pytests.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
   Streamlit is a tool (python opensource framework) that allows us to build web applications like this game. Streamlit "reruns" means that the web application doesn't save your previous state and what you've done so every time the application runs, its a new clean application that runs from the top again. A session state is data that we can write to when running the strealit so that the data is saved and can be called in the next run. When the streamlit "reruns", it checks the data is session state and rathers the previous states info and uses it if needed.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
     When I used to work with AI before and I needed bugs to be fixed in the code, I used to tell the UI to find the bug and fix it and used that code with minimal testing and no proofreading. From this project, I learned that its important to point the Agent to the exact bugs that you want to be fixed, read the code that it modified, and do thorough testing before using the code. I learned that Prompty engineering is more than "fix this" and we need to be the guide to the agent rather than blidly following it.
- What is one thing you would do differently next time you work with AI on a coding task?
    next time I work with AI, I would ask follow up questions before approving to let it implement the bug fixes. I would also ask it to ask me questions to understand the problem statment better so that it can create accurate code.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
    I used to be intimidated by AI because it can offscript and generate code that it not needed or code that I didn't understand. But this project showed me that its a very useful tool if we learn to stay in control with the type of prompts that we give the AI.

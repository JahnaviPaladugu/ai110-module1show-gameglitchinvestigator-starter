# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
       The purpose of the game is to guess the secret number within the given number of attempts. User can choose the difficulty level and whether hints should be shown.
- [ ] Detail which bugs you found.
      The first bug I fixed is that the score was always showing negative even if User guesses the secret so using the Agent, I updated the logic to show an accurate score. The 2nd bug I found is that the hints are shown incorrectly when the guess is made.
- [ ] Explain what fixes you applied.
       Using the Agnt,I fixed the bugs so that the score is more accurate when user wins the game and the hints are shown correctly when user makes a guess.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

Secret: 55
1. User enters 25 as a guess
2. Game displays "Go Higher!"
3. User guesses 80
4. Game dispalys "Go Lower!"
5. Score gets updated correctly for every guess made
6. User enters 55, game won, balloons shown in UI

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->



## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```
================================ test session starts =================================
platform win32 -- Python 3.13.0, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\jahna\OneDrive\Desktop\Codepath\AI110\Week2\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 15 items                                                                    

tests\test_game_logic.py ...............                                        [100%]

================================= 15 passed in 0.08s =================================


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]

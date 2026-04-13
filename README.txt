# Workout Generator Web App

A simple Flask-based web application that generates workout routines based on the user's previous workout and tracks weekly weight progress.

## Features

- Push/Pull/Legs workout rotation
- Randomized exercise selection from a JSON dataset
- Tracks last workout using file storage
- Weight tracking system with saved history
- Simple web interface using HTML/CSS

## How It Works

- The user selects their previous workout (Push, Pull, or Legs)
- The app generates the next workout using a rotation system:
  - Push → Pull
  - Pull → Legs
  - Legs → Push
- Exercises are randomly selected from predefined categories
- User weight entries are saved and can be retrieved later

## Technologies Used

- Python
- Flask
- HTML/CSS
- JSON (data storage)

## How to Run

1. Clone the repository  

2. Install Flask:
   pip install flask  

3. Run the app:
   app.py 
 
4. Open in browser: http://127.0.0.1:5000/

OR

Use Render Link: https://workout-app-1-h1r9.onrender.com/

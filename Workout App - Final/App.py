# This is a script that generates workouts based on what muscles the user trained yesterday.

from flask import Flask, request, render_template
import random
import json
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)  # allows the .txt or .json file to be seen on every computer

exercises_path = os.path.join(
    BASE_DIR, "exercises_list.json"
)  # allows the exercises_list.json file to be seen on every computer

with open(exercises_path, "r") as file:
    exercises = json.load(file)

last_workout_path = os.path.join(BASE_DIR, "last_workout.txt")
weight_tracker = os.path.join(BASE_DIR, "weight_tracker.txt")

push_exercises = exercises["push"]
pull_exercises = exercises["pull"]
leg_exercises = exercises["legs"]


def load_last_workout():  # this is the function that reads the file of what the user selected last for their workout
    try:
        with open(last_workout_path, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return None


def load_weight_tracker():
    try:
        with open(weight_tracker, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return None


def generate_workout(
    user_input,
):  # this function generates a list of exercises that belong to each group withtin the json file
    user_input = user_input.lower()
    with open(last_workout_path, "w") as file:
        file.write(user_input)

    if user_input == "push":
        back = random.sample(pull_exercises["back"], 3)
        biceps = random.sample(pull_exercises["biceps"], 2)

        today = back + biceps
        title = "Pull"

    elif user_input == "pull":
        quads = random.sample(leg_exercises["quads"], 2)
        hamstrings = random.sample(leg_exercises["hamstrings"], 2)
        calves = random.sample(leg_exercises["calves"], 1)
        glutes = random.sample(leg_exercises["glutes"], 1)

        today = quads + hamstrings + calves + glutes
        title = "Legs"

    elif user_input == "legs":
        chest = random.sample(push_exercises["chest"], 2)
        shoulders = random.sample(push_exercises["shoulders"], 2)
        triceps = random.sample(push_exercises["triceps"], 2)

        today = chest + shoulders + triceps
        title = "Push"

    else:
        return None

    return title, today


@app.route("/", methods=["GET", "POST"])
def home():
    workout_text = None
    last_display = None
    selected_workout = None

    if request.method == "POST":

        action = request.form.get("action")
        user_input = request.form.get("workout")

        if action == "generate":
            selected_workout = user_input
            result = generate_workout(user_input)
            if result:
                title, today = result
                workout_text = title + "\n\n" + "\n".join(today)

        elif action == "last":
            last_display = load_last_workout()
            selected_workout = last_display

    return render_template(  # passes the information to the html file
        "index.html",
        workout=workout_text,
        last_display=last_display,
        selected_workout=selected_workout,
    )


@app.route("/weight", methods=["GET", "POST"])
def weight():
    weight_text = None
    last_weight = None

    if request.method == "POST":

        action = request.form.get("action")
        user_input = request.form.get("weight_value")

        if action == "save":
            if user_input:
                with open(weight_tracker, "a") as file:
                    file.write(user_input + "\n")

                weight_text = user_input

        elif action == "last":
            data = load_weight_tracker()

            if data:
                lines = data.strip().split("\n")
                last_weight = lines[-1]

    return render_template(
        "weight.html", 
        weight=weight_text, 
        last_weight=last_weight
    )


if __name__ == "__main__":
    app.run()

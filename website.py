from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Initialize the random number
ran = random.randint(1, 100)

@app.route('/')
def guess():
    return render_template('guess.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get the user's guess from the form
    gs = request.form.get("guess")
    
    # Convert the guess to an integer
    try:
        guess = int(gs)
    except ValueError:
        return "Please enter a valid number."

    # Check if the guess is correct
    if guess == ran:
        result = "Congratulations! You guessed correctly."
    elif guess < ran:
        result = "Too low! Try again."
    else:
        result = "Too high! Try again."

    # Render the template with the result
    return render_template('guess.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

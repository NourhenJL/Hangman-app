from flask import Flask, render_template, request
import random

app = Flask(__name__)

words = ["apple", "banana", "cherry", "orange", "pear"]
chosen_word = ""

@app.route('/')
def index():
    global chosen_word
    chosen_word = random.choice(words)
    return render_template('index.html', word_length=len(chosen_word))

@app.route('/play', methods=['POST'])
def play():
    guess = request.form['guess']
    result = check_guess(guess)
    return render_template('result.html', result=result)

def check_guess(guess):
    global chosen_word
    if guess == chosen_word:
        return "Congratulations! You guessed the word correctly!"
    else:
        return "Sorry, that's not the correct word. Try again!"

if __name__ == '__main__':
    app.run(debug=True)

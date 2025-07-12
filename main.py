from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    password = ""
    if request.method == 'POST':
        n_letters = int(request.form['letters'])
        n_symbols = int(request.form['symbols'])
        n_numbers = int(request.form['numbers'])

        letters = list(string.ascii_letters)
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        password_list = random.choices(letters, k=n_letters) + \
                        random.choices(symbols, k=n_symbols) + \
                        random.choices(numbers, k=n_numbers)

        random.shuffle(password_list)
        password = ''.join(password_list)

    return render_template("index.html", password=password)

if __name__ == '__main__':
    app.run(debug=True)

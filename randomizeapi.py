from flask import Flask, jsonify
from faker import Faker
import random

app = Flask(__name__)

fake = Faker()

countries = ["USA", "Canada", "UK", "Germany", "France", "Italy", "Spain", "Japan", "China", "Australia", "Brazil", "Argentina", "Mexico", "Russia", "India", "South Africa", "Nigeria", "Egypt", "Kenya", "Ethiopia"]

@app.route('/random_person', methods=['GET'])
def get_random_person():
    country = random.choice(countries)
    name = fake.first_name()
    surname = fake.last_name()
    age = random.randint(18, 99)

    person = {
        'country': country,
        'name': name,
        'surname': surname,
        'age': age
    }

    return jsonify(person)

if __name__ == '__main__':
    app.run(debug=True)

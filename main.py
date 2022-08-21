import json
import sqlite3
from flask import Flask, jsonify

from dao.utils import get_value_by_title, get_value_in_range, get_sort_by_rating, get_sort_by_genre, step_5, step_6

app = Flask(__name__)

"""
Шаг 1: Реализуйте поиск по названию.
"""

@app.route('/movie/<title>')
def view_by_title(title):
    result = get_value_by_title(title)
    return jsonify(result)
    # return app.response_class(response=json.dumps(result, ensure_ascii=False, indent=4),
    # status=200,
    # mimetype="application/json")


"""
Шаг 2: Сделайте поиск по диапазону лет выпуска.
"""

@app.route('/movie/<int:year1>/to/<int:year2>')
def view_in_range(year1, year2):
    result = get_value_in_range(year1, year2)
    return jsonify(result)

"""
Шаг 3: Реализуйте поиск по рейтингу
"""

@app.route('/rating/family')
def view_by_children():
    rating = ('G', 'PG', 'PG-13')
    result = get_sort_by_rating(rating)
    return jsonify(result)


@app.route('/rating/children')
def view_by_family():
    rating = ('G', '')
    result = get_sort_by_rating(rating)
    return jsonify(result)


@app.route('/rating/adult')
def view_by_adult():
    rating = ('NC-17', 'R')
    result = get_sort_by_rating(rating)
    return jsonify(result)

"""
Шаг 4: Напишите функцию,на входе название жанра 
возвращает 10 самых свежих фильмов в формате json.
"""

@app.route('/genre/<genre>')
def view_by_genre(genre):
    result = get_sort_by_genre(genre)
    return jsonify(result)


if __name__ == '__main__':
    #app.run(debug=True)

    print(step_5())
    #print(step_6('TV Show', '2019', 'Dramas'))

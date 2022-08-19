import json
import sqlite3


def connection_to_db(sql):
    with sqlite3.connect('netflix.db') as connection:
        connection.row_factory = sqlite3.Row
        result = connection.execute(sql).fetchall()
        return result


def get_value_by_title(title):
    """
    Шаг 1:
    :param title:
    :return:
    """
    sql = f"""select title, country, release_year, listed_in as genre, description  from netflix
              where title = '{title}'
              order by release_year desc
    """
    result = connection_to_db(sql)
    for item in result:
        return dict(item)


def get_value_in_range(year_1, year_2):
    """
    Шаг 2:
    :param title:
    :return:
    """
    sql = f"""select title, description from netflix
              where release_year between {year_1} and {year_2}
              limit 100
    """
    result = connection_to_db(sql)
    list_result = []
    for item in result:
        list_result.append(dict(item))
    return list_result


def get_sort_by_rating(r):
    """
    Шаг 3:
    :param title:
    :return:
    """
    sql = f"""select title, rating, description from netflix
              where rating in {r}
              
    """
    result = connection_to_db(sql)
    list_result = []
    for item in result:
        list_result.append(dict(item))
    return list_result


def get_sort_by_genre(genre):
    """
    Шаг 4:
    :param genre: str
    :param column:
    :return:
    """

    sql = f"""SELECT title, description, listed_in 
              FROM netflix 
              where listed_in like '%{genre}%'
              order by release_year desc
              limit 10
"""

    result = connection_to_db(sql)
    list_result = []
    for item in result:
        list_result.append(dict(item))
    return list_result


def step_5(name1='Jack Black', name2='Dustin Hoffman'):
    """
    Шаг 5:
    :param name1:
    :param name2:
    :return:
    """
    sql = f"""select "cast"
              from netflix
              where "cast" like '%Rose McIver%'
              and "cast" like '%Ben Lamb%'
    """
    result = connection_to_db(sql)
    together = []
    dict_count = {}
    for actors in result:
        names = set(dict(actors).get('cast').split(', ')) - set([name1, name2])

        for name in names:
            dict_count[name] = dict_count.get(name, 0) + 1

    for k, v in dict_count.items():
        if v > 2:
            together.append(k)
    return together

def step_6(typ, year, genre):
    sql = f"""select *
          from netflix
          where type like '%{typ}%'
          and release_year = '{year}'
          and listed_in like '%{genre}%'
    """

    result = connection_to_db(sql)
    list_result = []
    for item in result:
        list_result.append(dict(item))
    return json.dumps(list_result)

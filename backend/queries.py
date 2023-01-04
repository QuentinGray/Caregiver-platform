"""
Simple queries file for manual SQL queries.
You can use an ORM once your project gets more complex.
"""

import sqlite3


def post_calendar(date, event_name, event_description, location):
    with sqlite3.connect("caregiver.db") as conn:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO calendar (date, event_name, event_description, location) VALUES ('{date}', ');")
        results = cursor.fetchall()
        print(results)
        return results









def get_actors():
    with sqlite3.connect("sakila.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM actor;")
        results = cursor.fetchall()
        print(results)
        return results

# TODO: Add more functions below.


if __name__ == "__main__":
    get_actors()
    #post_calendar()
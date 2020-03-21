import sqlite3
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def _add_recipe(roast,
                coffeename,
                waterweight,
                coffeeweight,
                watertemp,
                grind,
                brewtime):
  try:
    with sqlite3.connect('coffee.db') as connection:
      cursor = connection.cursor()
      cursor.execute("""
        INSERT INTO coffee (roast, 
                            coffeename, 
                            waterweight,
                            coffeeweight,
                            watertemp, 
                            grind, 
                            brewtime) values(?,?,?,?,?,?,?);
      """, (roast, coffeename, waterweight, coffeeweight, watertemp, grind, brewtime))
      result = {'status': 1, 'message': 'Recipe Added'}
  except:
    result = {'status': 0, 'message': 'Error'}
  return result


def _get_all_recipes():
  with sqlite3.connect('coffee.db') as connection:
    connection.row_factory = dict_factory
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM coffee ORDER BY id desc")
    all_recipes = cursor.fetchall()
    return all_recipes

@app.route('/api/recipes', methods=['GET','POST'])
def collection():
  if request.method == 'GET':
    result = _get_all_recipes()
    return json.dumps(result)
  elif request.method == 'POST':
    data = request.form
    result = _add_recipe(data['roast'],
                         data['coffeename'],
                         data['waterweight'],
                         data['coffeeweight'],
                         data['watertemp'],
                         data['grind'],
                         data['brewtime'])
    return jsonify(result)

if __name__ == '__main__':
  app.debug = True
  app.run()
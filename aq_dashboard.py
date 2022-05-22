'''OpenAQ Air Quality Dashboard with Flask.'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import openaq

FLASK_ENV = 'development'
FLASK_DEBUG = 1

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB = SQLAlchemy(app)
DB.init_app(app)

api = openaq.OpenAQ()


class Record(DB.Model):

    id = DB.Column(DB.Integer, primary_key=True)

    datetime = DB.Column(DB.String)

    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return f'''Datetime: {self.datetime},
                   Value: {self.value}'''


def get_results():
    status, body = api.measurements(city='Los Angeles',
                                    parameter='pm25')
    data = body['results']
    mylist = [i['date'] for i in data if 'date' in i]
    list1 = [i['utc'] for i in mylist if 'utc' in i]
    list2 = [i['value'] for i in data if 'value' in i]
    mergedlist = [(list1[i], list2[i]) for i in range(0, len(list1))]
    return mergedlist


@app.route('/')
def root():
    '''Filtered results'''
    for i in get_results():
        if i[1] >= 18:
            Record(datetime=i[0], value=i[1])
            return str(Record.query.all())


@app.route('/refresh')
def refresh():
    """Pull fresh data from Open AQ and replace existing data."""
    DB.drop_all()
    DB.create_all()
    for i in get_results():
        DB.session.add(Record(datetime=i[0], value=i[1]))
    DB.session.commit()
    return 'Data refreshed!'

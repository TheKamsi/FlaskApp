from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLAlCHEMY_DATABASE_URI'] = 'jdbc:mysql://root:1234@localhost:3306/arinze'


db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return '<Task %r>' %self.id

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')

@app.route('/store', methods=['POST'])
def store_data():
    print(app.config.get('SQLAlCHEMY_DATABASE_URI'))
    print(request.form)
    print(Todo.query.all())
    new_data = Todo(content=request.form.get('content'))
    db.session.add(new_data)
    db.session.commit()
    print(Todo.query.all())
    return render_template('index.html')



if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    app.run(debug=True)



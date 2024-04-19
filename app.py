from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///frogger.db'
db = SQLAlchemy(app)
app.app_context()


class Create(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Article %r>' % self.id

@app.route('/')
def hello_world():  # put application's code here
    articles = Create.query.all()
    return render_template("index.html", articles=articles)
@app.route('/create', methods=["GET", "POST"])
def create_post():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form[('desc')]

        article = Create(name=name, description=description)


        try:
            db.session.add(article)
            db.session.commit()
            redirect('/')
        except:
            return "An error occurred"

    else:
        return render_template("create.html")

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
from data import db_session
from data.jobs import Jobs

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template("jobs.html", title="Журнал работ", jobs=jobs)


def main():
    db_session.global_init("db/mars_explorer.sqlite")
    app.run()


if __name__ == "__main__":
    main()

from flask import redirect, render_template, request, url_for

from application import app, db
from application.series.models import Series
from application.series.forms import SeriesForm

@app.route("/series", methods=["GET"])
def series_index():
    return render_template("series/list.html", series = Series.query.all())

@app.route("/series/new/")
def series_form():
    return render_template("series/new.html", form = SeriesForm())

@app.route("/series/<series_id>/", methods=["POST"])
def series_set_episodes_total(series_id):
    s = Series.query.get(series_id)
    s.episodes_total += 1
    db.session().commit()

    return redirect(url_for("series_index"))

@app.route("/series/", methods=["POST"])
def series_create():
    form = SeriesForm(request.form)

    if not form.validate():
        return render_template("series/new.html", form = form)

    s = Series(form.name.data)
    s.episodes_total = form.episodes_total.data

    db.session().add(s)
    db.session().commit()
  
    return redirect(url_for("series_index"))

from flask import flash, redirect, render_template, request, url_for

from app import app, db
from app.forms import ConsultationForm
from app.models import Answer, City, Question, Registration


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ConsultationForm()
    if form.validate_on_submit():
        answers = []
        for i in range(1, Question.query.count() + 1):
            qid = 'question-%d' % i
            if qid not in request.form or request.form[qid] not in {'yes', 'no'}:
                flash('Kitöltetlen kérdések.')
                break
            answers.append(request.form[qid])
        else:
            r = Registration(
                    lastname=form.lastname.data, firstname=form.firstname.data, age=form.age.data,
                    email=form.email.data, postcode=form.postcode.data, city_id=City.query.filter_by(name=form.city.data).first().id,
                    address=form.address.data, phone=form.phone.data, ssn=form.ssn.data
                )
            db.session.add(r)
            for i in range(1, Question.query.count() + 1):
                qid = 'question-%d' % i
                db.session.add(Answer(rid=r.id, qid=i, value=request.form[qid] == 'yes'))
            db.session.commit()
            flash('Válaszát rögzítettük.')
            return redirect(url_for('index'))
    questions = Question.query.all()
    return render_template('index.html', form=form, questions=questions)

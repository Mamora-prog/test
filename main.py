from flask import Flask, render_template, request
import mail

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        try:
            name = request.form.get('name')
            surname = request.form.get('surname')
            surname2 = request.form.get('surname2')
            birthday = request.form.get('birthday')
            work1 = request.form.get('work1')
            work2 = request.form.get('work2')
            work3 = request.form.get('work3')
            phone = request.form.get('phone')
            mail.send_email(name,surname,surname2,birthday,work1,work2,work3,phone)
            return render_template("yes.html")
        except:
            return render_template("no.html")
    else:
        return render_template("index.html")

@app.route('/regulations')
def regulations():
    return render_template('regulations.html')

if __name__ == "__main__":
    app.run(debug=True)
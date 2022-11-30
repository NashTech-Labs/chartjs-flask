# Flask Setup
from flask import Flask, request, render_template

app = Flask(__name__, template_folder='./templates')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', title="Home Page")


@app.route('/index', methods=['GET', 'POST'])
def costdata():
    if request.method == 'POST':
        User = request.form['User']
        RAM = float(request.form['RAM'])
        vCPUs = int(request.form['vCPUs'])
        Number_of_Nodes = int(request.form['No of Nodes'])

        labels = ['RAM','vCPUs','Nodes']
        values = [RAM, vCPUs, Number_of_Nodes]

        return render_template('index.html', heading='Graph generated As per {} inputs'.format(User), title="Dashboard", labels=labels, values=values)

    elif request.method == 'GET':
        return render_template('index.html', title="Dashboard")


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=9999)

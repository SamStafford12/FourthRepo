from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    #return '<h1>Hello World!</h1>'

    returnvalue = """
        <iframe
          width="1355"
          height="645"
          frameborder="0" style="border:0"
          src="https://www.google.com/maps/embed/v1/place?key=AIzaSyApbBpuE7fUU3NiNEeMIkS6RnTqa21Sq3M
            &q=Concord+NH&zoom=19" allowfullscreen>
        </iframe>
    """

    return returnvalue


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

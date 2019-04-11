from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/" method="POST">
            <P>
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot" value="0" />
                <textarea rows="4" cols="50" name="text">{0}</textarea>
                <input type="submit" />
            </p>
        </form>
    </body>
</html>
"""

@app.route("/", methods=["POST"])
def incrypt():
    rotate_val = int(request.form["rot"])
    text_val = str(request.form["text"])
    result = rotate_string(text_val, rotate_val)
    return form.format(result)
    

@app.route("/")
def index():
    return form.format("")

app.run()
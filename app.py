from flask import Flask, request, render_template
from load_model import load_model
from load_model import predict_color

app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def page():
    return render_template('index.html')

@app.route('/get_color', methods = ['POST'])
def get_color():
    if (request.method == 'POST'):
        name = request.form.get('color')
        print(name)
        r, g, b = predict_color(model, name)
        background_color = f"rgb({r}, {g}, {b})"
        return render_template("index.html", background_color=background_color)


model = load_model()

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)
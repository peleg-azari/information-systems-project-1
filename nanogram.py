from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    # Render the home_page.html template for the homepage
    return render_template('home_page.html')

@app.route('/show_picture')
def show_picture():
    # Get the 'size' and 'pixs' parameters from the request's query string
    size = request.args.get('size')
    pixs = request.args.get('pixs')

    # Define color codes for pixel values
    color_codes = ['#FFFFFF', '#000000', '#FF0000', '#00FF00', '#0000FF', '#800080']

    # Convert the 'pixs' string to a list of integers
    pixs_list = [int(num) for num in pixs.split(',')]

    # Map pixel values to their corresponding color codes
    pixs_list_colors = [color_codes[i] for i in pixs_list]

    # Check if 'size' is not None
    if size:
        # Split the size string into rows and columns
        rows, col = map(int, size.split(','))
    else:
        # Default values if 'size' is not provided
        rows, col = 0, 0

    # Render the show_picture.html template with the provided parameters
    return render_template("show_picture.html", pixs=pixs_list_colors, rows=rows, col=col)

#running the script
if __name__ == "__main__":

    # Run the Flask application in debug mode
    app.run(debug=True)


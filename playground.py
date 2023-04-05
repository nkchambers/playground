from flask import Flask, render_template

app = Flask(__name__)

# Level 1 - when user visits /play have it render three blue boxes
@app.route('/play')
def playground_level_one():
    return render_template('playground_index.html', num=3, color='rgb(30, 220, 245)')


# Level 2 - when user visits /play/(x) have it render blue boxes x number of times (/play/7) should render 7 blue boxes
@app.route('/play/<int:num>')
def playground_level_two(num):
    return render_template('playground_index.html', num=num, color='rgb(30, 220, 245)')


# Level 3 - when user visits /play/(x)/color have it render boxes x number of times in color selected 
# (/play_color/10/green) should render 10 green boxes
@app.route('/play/<int:num>/<string:color>')
def playground_level_three(num, color):
    return render_template('playground_index.html', num=num, color=color)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True) 
from flask import Flask, request#Flask as for starting a server
from datetime import datetime


app = Flask("My First Application")


@app.route('/')#route where server will get information where function will serve the actual content



def index():
    return """
    <h1>Roger website</h1>
    <p>My name is Roger</p>
    """
#static as it display same info all the time



@app.route('/nyandikira')

def contact_page():
    return "Contact me at rogerbyakunda@gmail.com or 0788xxxxxxxxxxx"


#dynamic
@app.route('/date')

def date_page():
    date = str(datetime.now())
    return f"Today is {date}"

@app.route('/birthyear', methods=['POST','GET'])

def calc_birthyear():
    if request.method == "POST": #user is posting or submitting his/her information
        return f"""
        <form action="/birthyear" method='POST'>
        <input type="number" name="birthyear" placeholder="Birthyear e.g 2020">
        <button type="submit">submit</button>
        </form>
        From yor submission your age is {2022 - int(request.form.get('birthyear'))}
        """
    elif request.method == "GET":#USER IS ASKING FOR THIS PAGE
        return """
        <form action="/birthyear" method='POST'>
        <input type="number" name="birthyear" placeholder="Birthyear e.g 2020">
        <button type="submit" value="Submit">submit</button>
        </form>
        """

if __name__ == '__main__':#if not run as main it will not be displayed
    app.run()



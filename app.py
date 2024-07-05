from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API_KEY = '76099b11651d41689adcd3c7bb570481'

def get_weather_data(city, country=None):
    if country:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={API_KEY}&units=metric'
    else:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        city = request.form['city']
        country = request.form.get('country', '')
        weather = get_weather_data(city, country)
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run()

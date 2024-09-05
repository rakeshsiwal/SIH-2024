from flask import Flask , render_template,request,jsonify
import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    selected_date = data['date']
    selected_time = data['time']

    datetime_input = datetime.datetime.strptime(f"{selected_date} {selected_time}", '%Y-%m-%d %H:%M')

    # Here you can pass the `datetime_input` to your machine learning model
    # result = your_ml_model.predict(datetime_input)
    # For the example, let's assume it returns a dummy result:
    result = "Predicted Output"
    
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(debug=True)
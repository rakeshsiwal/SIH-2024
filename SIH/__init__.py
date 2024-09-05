from flask import Flask , render_template,request,jsonify
import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_data():
    data = request.get_json()
    date = data['date']
    time = data['time']
    
    # Combine date and time into a single datetime object (if needed)
    datetime_input = f"{date} {time}"

    # Process the input through your ML model
    model_output = datetime_input # Assuming you have a predict function

    return jsonify({'result': model_output})

if __name__ == "__main__":
    app.run(debug=True)
# Flask REST API to receive data from ESP32

from flask import Flask, request, jsonify
import csv
import datetime
import os

app = Flask(__name__)
DATA_FILE = 'data.csv'

# Create CSV file with headers if not exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp', 'temperature', 'humidity'])

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()

    if not data or 'temperature' not in data or 'humidity' not in data:
        return jsonify({'status': 'error', 'message': 'Invalid data'}), 400

    temp = data['temperature']
    hum = data['humidity']
    timestamp = datetime.datetime.now().isoformat()

    with open(DATA_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, temp, hum])

    print(f"[{timestamp}] Received -> Temp: {temp}°C, Humidity: {hum}%")

    return jsonify({'status': 'success', 'timestamp': timestamp})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

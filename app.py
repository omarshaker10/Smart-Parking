from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# الخزنة المؤقتة للبيانات الحقيقية القادمة من الراسبري باي
sensor_data = {
    "slot_is_busy": False,
    "distance_cm": 0.0,
    "temperature": 0.0,
    "humidity": 0.0,
    "gas_percentage": 0.0,
    "ldr_is_night": False,
    "motion_detected": False,
    "flame_detected": False,
    "vibration_detected": False
}

@app.route('/')
def home():
    return render_template('index.html')

# 1. مسار الاستقبال من الراسبري باي (POST)
@app.route('/api/update', methods=['POST'])
def update_data():
    global sensor_data
    data = request.get_json()
    if data:
        sensor_data.update(data)
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "error", "message": "No data"}), 400

# 2. مسار الإرسال للموقع (GET) - بديل الـ mock_data
@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify(sensor_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

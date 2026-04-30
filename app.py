from flask import Flask, render_template, jsonify
import random
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # لازم نبعت قاموس (Dictionary) فاضي أو فيه قيم مبدئية 
    # عشان الـ HTML ميزعلش أول ما يفتح
    initial_data = {
        'slots': "جاري التحميل...",
        'solar': "0%",
        'status': "برجاء الانتظار",
        'plate_number': "---",
        'type': "---",
        'entry_time': "---"
    }
    return render_template('index.html', data=initial_data)

@app.route('/get_latest_car')
def get_latest_car():
    plates = ["أ ب ج 123", "س ص ع 456", "ط ي ك 789"]
    types = ["Owner", "Visitor"]
    mock_data = {
        'plate_number': random.choice(plates),
        'type': random.choice(types),
        'entry_time': datetime.now().strftime("%I:%M:%S %p")
    }
    return jsonify(mock_data)

if __name__ == '__main__':
    # إضافة host='0.0.0.0' بتخلي السيرفر متاح لأي جهاز معاك على الشبكة
    app.run(host='0.0.0.0', port=5000, debug=True)
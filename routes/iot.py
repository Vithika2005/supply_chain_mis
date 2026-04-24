from flask import Blueprint, jsonify
from services.simulation import generate_sensor_data
from services.rule_engine import check_alerts
from database.db import db
from database.models import SensorData, Alert

iot_bp = Blueprint("iot", __name__)

@iot_bp.route("/sensor", methods=["GET"])
def sensor():
    data = generate_sensor_data()

    sensor_entry = SensorData(**data)
    db.session.add(sensor_entry)

    alerts = check_alerts(data)

    for a in alerts:
        db.session.add(Alert(message=a))

    db.session.commit()

    return jsonify({
        "data": data,
        "alerts": alerts
    })

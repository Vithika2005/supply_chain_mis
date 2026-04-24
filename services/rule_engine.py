def check_alerts(sensor):
    alerts = []

    if sensor["temperature"] > 35:
        alerts.append("High Temperature Alert")

    if sensor["stock_level"] < 50:
        alerts.append("Low Stock Alert")

    return alerts

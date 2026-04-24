from flask import Blueprint, jsonify
from database.models import Inventory

inventory_bp = Blueprint("inventory", __name__)

@inventory_bp.route("/inventory", methods=["GET"])
def get_inventory():
    items = Inventory.query.all()

    return jsonify([
        {
            "product": i.product_name,
            "quantity": i.quantity
        } for i in items
    ])

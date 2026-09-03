from flask import Blueprint, jsonify

ventas_bp = Blueprint("ventas", __name__, url_prefix="/api/ventas")

@ventas_bp.route("/", methods=["GET"])
def get_ventas():
    return jsonify([])

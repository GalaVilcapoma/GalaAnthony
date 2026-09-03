from flask import Blueprint, jsonify

productos_bp = Blueprint("productos", __name__, url_prefix="/api/productos")

@productos_bp.route("/", methods=["GET"])
def get_productos():
    return jsonify([])

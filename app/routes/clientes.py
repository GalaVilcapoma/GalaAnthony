from flask import Blueprint, jsonify

clientes_bp = Blueprint("clientes", __name__, url_prefix="/api/clientes")

@clientes_bp.route("/", methods=["GET"])
def get_clientes():
    return jsonify([])

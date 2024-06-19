from flask import Blueprint, jsonify
from .models import Empleado

views_bp = Blueprint('views', __name__)

@views_bp.route('/empleados')
def get_empleados():
    empleados = Empleado.query.all()
    return jsonify([empleado.to_dict() for empleado in empleados])

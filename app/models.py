from . import db

class Empleado(db.Model):
    __tablename__ = 'empleado'
    id_empleado = db.Column(db.Integer, primary_key=True)
    rut_empleado = db.Column(db.String(255))
    id_encargado = db.Column(db.Integer, db.ForeignKey('encargado.id_encargado'))

    def to_dict(self):
        return {
            'id_empleado': self.id_empleado,
            'rut_empleado': self.rut_empleado,
            'id_encargado': self.id_encargado,
        }

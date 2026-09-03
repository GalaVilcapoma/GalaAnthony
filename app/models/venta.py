# Modelo Venta
class Venta:
    def __init__(self, id_venta, cliente_id, producto_id, cantidad, total, fecha):
        self.id_venta = id_venta
        self.cliente_id = cliente_id
        self.producto_id = producto_id
        self.cantidad = cantidad
        self.total = total
        self.fecha = fecha

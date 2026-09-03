# Schema para validación y formato de Indicadores Analíticos
class IndicadorSchema:
    def serialize(self, nombre, valor, unidad=""):
        return {
            "nombre": nombre,
            "valor": valor,
            "unidad": unidad
        }

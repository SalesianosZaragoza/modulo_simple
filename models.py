from odoo import api, models, fields

class Cliente(models.Model):
    _name = 'salesianos.cliente'
    name = fields.Char(required=True)
    email = fields.Char()
    phone = fields.Char()
    vendedor = fields.Many2one(comodel_name='salesianos.vendedor', string='vendedor')
    edad = fields.Integer()

    @api.constrains('edad', 'name')
    def _check_edad(self):
        # solo se ejecuta una vez
        for record in self:
            if record.edad < 18:
                raise models.ValidationError("El cliente "+record.name+" debe ser mayor de edad")
            elif record.edad > 100:
                raise models.ValidationError("El cliente "+record.name+"  no puede ser tan viejo")
            else:
                pass

class Vendedor(models.Model):
    _name = 'salesianos.vendedor'
    name = fields.Char(required=True)
    company = fields.Char()
    fecha_incorporacion = fields.Date()
    fecha_despido = fields.Date()
    cliente = fields.One2many(comodel_name='salesianos.cliente', inverse_name='vendedor')
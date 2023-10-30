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
    
    altura = fields.Float()
    peso = fields.Float()
    imc = fields.Float(compute='_compute_imc', store=True)


    @api.depends('altura', 'peso')
    def _compute_imc(self):
        for record in self:
            if record.altura > 0:
                record.imc = record.peso / (record.altura * record.altura)
            else:
                record.imc = 0
    proveedor = fields.Many2many(comodel_name='salesianos.proveedor', string='proveedor')

class proveedor(models.Model):
    _name = 'salesianos.proveedor'
    cif = fields.Char(required=True)
    titular = fields.Char()
    #cliente = fields.Many2many(comodel_name='salesianos.cliente', string='cliente')
    
class Vendedor(models.Model):
    _name = 'salesianos.vendedor'
    name = fields.Char(required=True)
    company = fields.Char()
    fecha_incorporacion = fields.Date()
    fecha_despido = fields.Date(index=True)
    cliente = fields.One2many(comodel_name='salesianos.cliente', inverse_name='vendedor')
from odoo import api, models, fields, api

class Cliente(models.Model):
    _name = 'salesianos.cliente'
    name = fields.Char(required=True)
    email = fields.Char()
    phone = fields.Char()
    vendedor = fields.Many2one(comodel_name='salesianos.vendedor', string='vendedor')

class Vendedor(models.Model):
    _name = 'salesianos.vendedor'
    name = fields.Char(required=True)
    company = fields.Char()
    fecha_incorporacion = fields.Date()
    fecha_despido = fields.Date()
    cliente = fields.One2many(comodel_name='salesianos.cliente', inverse_name='vendedor')
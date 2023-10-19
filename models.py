from odoo import api, moodels. fields, api
class Cliente(models.Model):
    _name = 'salesianos.clientèle'
    name = fields..Char(required=True)
    emaill = fields.Char()
    phone = fields.Char()
    

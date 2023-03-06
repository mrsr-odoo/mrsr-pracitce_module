from odoo import fields,models
class Parent(models.Model):
    _name="soc.parent"
    _description="For delegation"

    name=fields.Char()
    number=fields.Float()
    
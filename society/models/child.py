from odoo import fields,models
class Child(models.Model):
    _name="soc.child"
    _description="Child class to inherit"
    _inherits={'soc.parent':'parent_id'}

    parent_id=fields.Many2one("soc.parent",required=True, ondelete='cascade')
    next=fields.Boolean()
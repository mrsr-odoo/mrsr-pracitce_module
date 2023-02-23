from odoo import fields,models
class SocietyParking(models.Model):
    _name="society.parking"
    _description="Parking for society"

    name=fields.Char(required=True)
    room_id=fields.Many2one("society.resident")
    status=fields.Selection(
        string="Status",
        selection=[("available","Available"),("reserved","Reserved")])
    



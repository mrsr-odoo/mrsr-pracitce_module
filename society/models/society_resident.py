from odoo import models,fields 
class SocietyResident(models.Model):
    _name="society.resident"
    _description="Residential Society"
    _rec_name="room_no"

    room_no=fields.Char(required=True)
    owner_id=fields.Many2one('res.users')
    block_no=fields.Selection(
        string='Block no',
       selection=[('a','A'),('b','B'),('c','C'),('d','D'),('e','E')],
        help="Select Block no"
                                )
    house_type=fields.Selection(
        string='House Type',
       selection=[('1bhk','1BHK'),('2bhk','2BHK'),('3bhk','3BHK')],
        help="Select house type"
                                )
    
    society_id=fields.Many2one('society.detail')
    members=fields.Char()
    contact_no=fields.Char()
from odoo import models,fields 
class SocietyResident(models.Model):
    _name="society.resident"
    _description="Residential Society"
    _rec_name="room_no"

    room_no=fields.Char(required=True)
    owner=fields.Char(required=True)
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
    state=fields.Selection(string="house status",
                           selection=[('new','New'),('register','Registered'),('abandoned','Abandoned')],
                           default="new")
    society_id=fields.Many2one('society.detail')
    members=fields.Char()
    contact_no=fields.Char()


    def register_action(self):
        for record in self:
            record.state="register"
        return True
    def ab_action(self):
        for record in self:
            record.state="abandoned"
            record.owner="NONE"
            record.members="0"
            record.contact_no=""

        return True
    def re_register_action(self):
        for record in self:
            record.state="new"
            record.owner=""
            record.members=""
            record.contact_no=""

from odoo import api, models,fields 
class SocietyResident(models.Model):
    _name="society.resident"
    _description="Residential Society"
    _rec_name="room_no"
    _sql_constraints=[
        ("unique_rooms",'unique(rb)',"Room no. must be unique")]

    room_no=fields.Char(required=True,default="")
    owner=fields.Char(required=True)
    block_no=fields.Selection(
        string='Block no',
       selection=[('a','A'),('b','B'),('c','C'),('d','D'),('e','E')],
        help="Select Block no")
    house_type=fields.Selection(
        string='House Type',
       selection=[('1bhk','1BHK'),('2bhk','2BHK'),('3bhk','3BHK')],
        help="Select house type"
                                )
    state=fields.Selection(string="house status",
                           selection=[('new','New'),('register','Registered')],
                           default="new")
    society_id=fields.Many2one('society.detail')
    members=fields.Char()
    contact_no=fields.Char()
    rb=fields.Char(default="",compute="_compute_rb",store=True)

    @api.depends("room_no","block_no")
    def _compute_rb(self):
        for record in self:
            record.rb=record.room_no+record.block_no


    # @api.constrains("room_no")
    # def _check_room(self):
    #     for record in self:
    #         breakpoint()
    #         print(record.room_no)
    #         # if record.room_no==self.room_no:
    #             # raise ValueError("EROOOR")
        


    def register_action(self):
        for record in self:
            record.state="register"
        return True
    
    def re_register_action(self):
        for record in self:
            record.state="new"
            record.owner=""
            record.members=""
            record.contact_no=""

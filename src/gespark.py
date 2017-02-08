# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from openerp import models, fields
class GesPark(models.Model):
    _name = "gestorparking"
    user_id = fields.Many2one('res.users','Empleado')
    matricula = fields.Text('Matricula')
    num_plaza = fields.Integer(help="numero de plaza")
    

    


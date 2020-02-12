from odoo import models, fields, api

class Employee1(models.Model):   
    _inherit = "hr.employee"
    _description = "Costumize Employee View"
     
    no_karyawan = fields.Char("No. Induk Karyawan")
    no_NPWP = fields.Integer("No. NPWP", required=True)
    no_KTP = fields.Integer("NIK", required=True)
    no_BPJS_Kes = fields.Integer("No. BPJS Kesehatan", required=True)
    no_BPJS_TK = fields.Integer("No. BPJS Ketenagakerjaan", required=True)
    tgl_masuk = fields.Date("Tanggal Masuk", required=True)

    @api.model
    def create(self, values):
        seq = self.env['ir.sequence'].next_by_code('employee.no')
        values['no_karyawan'] = seq
        return super(Employee1, self).create(values)
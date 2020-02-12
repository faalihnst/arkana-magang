from odoo import models, fields, api

class Employee1(models.Model):   
    _inherit = "hr.employee"
    _description = "Costumize Employee View"
     
    no_karyawan = fields.Integer("No. Induk Karyawan", required=True)
    no_NPWP = fields.Integer("No. NPWP", required=True)
    no_KTP = fields.Integer("NIK", required=True)
    no_BPJS_Kes = fields.Integer("No. BPJS Kesehatan", required=True)
    no_BPJS_TK = fields.Integer("No. BPJS Ketenagakerjaan", required=True)
    tgl_masuk = fields.Date("Tanggal Masuk", required=True)
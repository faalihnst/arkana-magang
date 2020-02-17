from odoo import models, fields, api
from datetime import date

class Employee1(models.Model):   
    _inherit = "hr.employee"
    _description = "Costumize Employee View"
     
    no_karyawan = fields.Char("No. Induk Karyawan")
    no_NPWP = fields.Integer("No. NPWP", required=True)
    no_KTP = fields.Integer("NIK", required=True)
    no_BPJS_Kes = fields.Integer("No. BPJS Kesehatan", required=True)
    no_BPJS_TK = fields.Integer("No. BPJS Ketenagakerjaan", required=True)
    tgl_masuk = fields.Date("Tanggal Masuk", required=True)
    keluarga_id = fields.One2many('hr.employee.family', 'employee_id', string='Data Keluarga')
    sertif_ids = fields.Many2many('hr.employee.sertif', string='Sertifikasi')

    @api.model
    def create(self, values):
        seq = self.env['ir.sequence'].next_by_code('employee.no')
        values['no_karyawan'] = seq
        return super(Employee1, self).create(values)


class Employee1Family(models.Model):
    _name = "hr.employee.family"
    _description = "Data Keluarga"

    employee_id = fields.Many2one('hr.employee', 'Employee', ondelete='cascade')
    status = fields.Selection([
        ('pasangan','Pasangan'),
        ('orangtua','Orangtua'),
        ('saudara','Saudara'),
        ('anak','Anak'),
        ('pasangan','Pasangan')
    ], string='Status Keluarga')
    nama = fields.Char('Nama')
    tgl_lahir = fields.Date('Tanggal Lahir')
    umur = fields.Integer('Umur', compute='compute_umur', store=True)

    @api.depends('tgl_lahir')
    def compute_umur(self):
        for record in self:
            today = date.today()
            if record.tgl_lahir:
                record.umur = today.year - record.tgl_lahir.year - ((today.month, today.day) < (record.tgl_lahir.month, record.tgl_lahir.day))


class EmployeeSertif(models.Model):
    _name = "hr.employee.sertif"
    _description = "Data Sertifikasi Karyawan"

    employee_ids = fields.Many2many('hr.employee', string='Employees')
    name = fields.Char("Nama Sertifikasi", required=True)
    tahun = fields.Integer("Tahun", required=False)
    masa_berlaku = fields.Integer("Masa Berlaku (Dalam tahun)", required=False)
    kesulitan = fields.Selection([('beginner','Beginner'),('intermediate','Intermediate'),('advanced','Advanced')], string="Tingkat Kesulitan")




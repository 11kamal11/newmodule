from odoo import fields, models

class Project(models.Model):
    _name = 'project.project'
    _description = 'Project'

    name = fields.Char(string='Project Name', required=True)
    description = fields.Text(string='Description')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    status = fields.Selection([
        ('planning', 'Planning'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='planning')
    manager_id = fields.Many2one('res.users', string='Project Manager')
    task_ids = fields.One2many('project.task', 'project_id', string='Tasks')
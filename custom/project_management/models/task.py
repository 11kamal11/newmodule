from odoo import fields, models

class Task(models.Model):
    _name = 'project.task'
    _description = 'Task'

    name = fields.Char(string='Task Name', required=True)
    description = fields.Text(string='Description')
    due_date = fields.Date(string='Due Date')
    status = fields.Selection([
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')
    ], string='Status', default='todo')
    project_id = fields.Many2one('project.project', string='Project')
    assigned_to_id = fields.Many2one('res.users', string='Assigned To')
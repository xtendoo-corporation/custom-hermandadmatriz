# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    date_report = fields.Date(
        string="Fecha Informe",
        default=fields.Date.today(),
    )
    date_created = fields.Date(
        string="Fecha Creación",
        default=fields.Date.today(),
    )
    metal_id = fields.Many2one(
        "metals",
        string="Metal",
    )


class Metals(models.Model):
    _name = "metals"
    _description = "Metales"

    name = fields.Char(
        string="Nombre",
    )





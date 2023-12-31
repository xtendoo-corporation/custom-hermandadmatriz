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
    technique_name = fields.Char(
        string="Técnica",
        placeholder="Técnica",
    )
    metal_color_id = fields.Many2one(
        comodel_name="metal.colors",
        string="Color Metal",
    )
    metal_law_id = fields.Many2one(
        comodel_name="metal.laws",
        string="Ley Metal",
        placeholder="Ley Metal",
    )
    awl = fields.Char(
        string="Punzones",
        placeholder="Punzones",
    )
    weight_product = fields.Float(
        string='Peso en grs',
        digits=(16,2),
    )
    length_product = fields.Float(
        string='Longitud en cm',
        digits=(6,2),
    )
    width_product = fields.Float(
        string='Ancho en cm',
        digits=(6,2),
    )
    rhodium = fields.Char(
        string="Rodio",
        placeholder="Rodio",
    )
    manufacturing = fields.Char(
        string="Hechura",
        placeholder="Hechura",
    )

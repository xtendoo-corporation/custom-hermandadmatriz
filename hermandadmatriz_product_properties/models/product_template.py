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
    technique_name = fields.Char(
        string="Nombre Técnica",
        placeholder="Nombre Técnica",
    )
    metal_color = fields.Char(
        string="Color Metal",
        placeholder="Color Metal",
    )
    metal_law = fields.Many2one(
        "metal_laws",
        string="Ley Metal",
        placeholder="Ley Metal",
    )


class Metals(models.Model):
    _name = "metals"
    _description = "Metales"

    name = fields.Char(
        string="Nombre",
    )


class MetalLaws(models.Model):
    _name = "metal_laws"
    _description = "Leyes Metales"

    name = fields.Char(
        string="Nombre",
    )




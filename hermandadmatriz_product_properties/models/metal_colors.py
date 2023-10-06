# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import fields, models


class MetalColors(models.Model):
    _name = "metal.colors"
    _description = "Color Metales"

    name = fields.Char(
        string="Nombre",
    )


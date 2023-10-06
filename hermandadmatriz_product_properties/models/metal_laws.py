# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import fields, models


class MetalLaws(models.Model):
    _name = "metal.laws"
    _description = "Leyes Metales"

    name = fields.Char(
        string="Nombre",
    )

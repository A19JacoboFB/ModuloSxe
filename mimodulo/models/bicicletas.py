
from odoo import models, fields, api

class Bicicletas(models.Model):
     _name = "bicicletas"

     modelo = fields.One2many("modelo", "id", string="Modelos")
     precio = fields.Float("Precio",required=True)
     descripcion = fields.Text("Descripción")

class Modelo(models.Model):
    _name = "modelo"

    nombre = fields.Char("Nombre",required=True)
    foto = fields.Binary("Imagen")
    color = fields.Char("Color")

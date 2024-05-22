# controllers/material_controller.py
from odoo import http
from odoo.http import request, Response

class MaterialController(http.Controller):

    @http.route('/api/materials', type='json', auth='user', methods=['GET'])
    def get_materials(self):
        materials = request.env['material.registration'].search([])
        data = [{'material_code': material.material_code,
                 'material_name': material.material_name,
                 'material_type': material.material_type,
                 'material_buy_price': material.material_buy_price,
                 'supplier_id': material.supplier_id.name} for material in materials]
        return data

    @http.route('/api/materials', type='json', auth='user', methods=['POST'])
    def create_material(self, **kwargs):
        material = request.env['material.registration'].create(kwargs)
        return {'id': material.id, 'message': 'Material created successfully'}

    @http.route('/api/materials/<int:material_id>', type='json', auth='user', methods=['PUT'])
    def update_material(self, material_id, **kwargs):
        material = request.env['material.registration'].browse(material_id)
        if material:
            material.write(kwargs)
            return {'message': 'Material updated successfully'}
        else:
            return Response(status=404, response='Material not found')

    @http.route('/api/materials/<int:material_id>', type='json', auth='user', methods=['DELETE'])
    def delete_material(self, material_id):
        material = request.env['material.registration'].browse(material_id)
        if material:
            material.unlink()
            return {'message': 'Material deleted successfully'}
        else:
            return Response(status=404, response='Material not found')

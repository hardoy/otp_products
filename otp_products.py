from trytond.model import ModelView, ModelSQL, fields

# list of all classes in the file
__all__ = ['Product']


class Product(ModelSQL, ModelView):
    # description (mandatory on first declaration)
    'Product'

    __name__ = 'otp_products.product'

    name = fields.Char('Product Name', required=True)
    description = fields.Text('Description')
    price = fields.Float('Price')
    price_level = fields.Function(fields.Char('Level'), 'get_price_leve')
    
        
    def get_price_leve(self, name):
        if self.price<10: return "Low"
        if self.price<100: return "Medium"
        return "High"



from trytond.pool import Pool
from .otp_products import Product

def register():
    Pool.register(
        Product,
        module='otp_products', type_='model'
    )

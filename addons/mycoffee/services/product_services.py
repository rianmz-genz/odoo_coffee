from ..models.models import Models

class ProductService:
    def get_all(request):
        products = Models.Product(request.env).search([
            ('detailed_type', '=', 'product')
        ])
        if(len(products) == 0): raise Exception("Product notfound")
        res = []
        for product in products:
            res.append({
                'id': product.id,
                'name': product.name,
                'price': product.list_price,
                'canBeSold': product.sale_ok,
                'canBePurchased': product.purchase_ok,
                'type': product.detailed_type,
                'hpp': product.standard_price
            })
        return res

    def get_by_id(request, id):
        try:
            product = Models.Product(request.env).search([
                ('id', '=', int(id))
            ],limit=1)
        except Exception as e:
            raise e
        
        if not product: raise Exception("Product notfound")
        return {
                'id': product.id,
                'name': product.name,
                'price': product.list_price,
                'canBeSold': product.sale_ok,
                'canBePurchased': product.purchase_ok,
                'type': product.detailed_type,
                'hpp': product.standard_price
            }
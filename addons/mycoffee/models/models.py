
class Models:
    @staticmethod
    def Product(env):
        return env['product.template'].sudo()
    
    @staticmethod
    def User(env):
        return env['res.users'].sudo()
    
    @staticmethod
    def Partner(env):
        return env['res.partner'].sudo()
    
    @staticmethod
    def SaleOrder(env):
        return env['sale.order'].sudo()
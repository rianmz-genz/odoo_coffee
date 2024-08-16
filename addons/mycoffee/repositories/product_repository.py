from abc import ABC, abstractmethod
from ..models.models import Models

class IProductRepository(ABC):
    @abstractmethod
    def search(self, domain, limit=None):
        pass
    
class ProductRepository(IProductRepository):
    def __init__(self, env):
        self.env = env
    
    def search(self, domain, limit=None):
        return Models.Product(self.env).search(domain, limit=limit)
from abc import ABC, abstractmethod
from ..models.models import Models

class ISaleRepository(ABC):
    @abstractmethod
    def search(self, domain, limit=None):
        pass
    
class SaleRepository(ISaleRepository):
    def __init__(self, env):
        self.env = env
    
    def search(self, domain, limit=None):
        return Models.SaleOrder(self.env).search(domain, limit=limit)
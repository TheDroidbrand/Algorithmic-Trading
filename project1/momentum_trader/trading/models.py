# pyright: reportMissingModuleSource=false
from django.db import models

# Create your models here.
class Stock(models.Model):
    ticker = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    sector = models.CharField(max_length=50)
    market_cap = models.DecimalField(max_digits=20, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PriceData(models.Model):
    pass

class MomentumScore(models.Model):
    pass

class TradingSignal(models.Model):
    pass

class RebalanceEvent(models.Model):
    pass
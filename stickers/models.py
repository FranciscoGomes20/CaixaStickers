from django.db import models

# Create your models here.
class CaixaStickers(models.Model):
    data_venda = models.DateField(auto_now_add=False)
    quantidade_vendidos = models.IntegerField()
    valor_unidade = models.FloatField(default=0)
    valor_total = models.FloatField(default=0)
    
    def __str__(self):
        return "Stickers vendidos {}".format(self.data_venda)
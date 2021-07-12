from django.db import models

# Create your models here.
class CaixaSticker(models.Model):
    data_venda = models.DateField(auto_now_add=False)
    quantidade_vendidos = models.IntegerField()
    valor_unidade = models.DecimalField(max_digits=10 ,default=0, decimal_places=2)
    valor_total = models.DecimalField(max_digits=10 ,default=0, decimal_places=2)

    def __str__(self):
        return "{}".format(self.data_venda)

class TotalSticker(models.Model):
    stickers_total = models.IntegerField(default=0)

    def __str__(self):
        return "{}".format(self.stickers_total)

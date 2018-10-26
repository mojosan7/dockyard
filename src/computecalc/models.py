from django.db import models

# Create your models here.
class Computecalc(models.Model):
    aws_sku = models.CharField(max_length=255)
    aws_vCPU = models.PositiveIntegerField()
    aws_ram = models.PositiveIntegerField()
    aws_cost_per_hour = models.DecimalField(max_digits = 8, decimal_places = 4)
    do_sku_equivalent = models.CharField(max_length=255)
    do_cost_per_month= models.DecimalField(max_digits = 7, decimal_places = 2)


    @property
    def aws_cost_per_month(self):
        return round(self.aws_cost_per_hour * 744)

    def __string__(self):
        return self.aws_sku

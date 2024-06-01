from django.db import models
from photogallery import models as pgmodels


class Expense(models.Model):
    trip = models.ForeignKey(pgmodels.Trip, on_delete=models.SET_NULL, null=True)
    budget = models.IntegerField('Planned budget, EUR', null=True, blank=True)
    EXPENSE = (
        ('f', 'Flights'),
        ('t', 'Transport'),
        ('a', 'Apartment'),
        ('d', 'Food & Drinks'),
        ('e', 'Entertainments'),
        ('x', 'Extra - not planned')
    )
    expense_category=models.CharField('Expenses category', max_length=1, default='f', choices=EXPENSE)
    expense_amount=models.IntegerField('Expenses, EUR')

    def __str__(self):
        return 'Trip expenses'

    class Meta:
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'

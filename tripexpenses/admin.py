from django.contrib import admin
from tripexpenses.models import Expense


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('trip', 'budget', 'expense_category', 'expense_amount')
    list_editable = ('expense_category', 'expense_amount')
    list_filter = ('expense_category',)
    search_fields = ('trip__city', 'trip__country')

    fieldsets = (
        ('Budget', {
            'fields': ('trip', 'budget')
        }),
        ('Expenses', {
            'fields': ('expense_category', 'expense_amount')         
        })
    )

admin.site.register(Expense, ExpenseAdmin)
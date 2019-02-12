from django.contrib import admin

from .models import (
    BillingRecord, CommisionRecord, LoanRecord,
    ProfitRecord,
)

@admin.register(BillingRecord)
class BillingRecordAdmin(admin.ModelAdmin):
    list_per_page = 20
    search_fields = [
        'instansale_trx__code'
    ]
    list_display = [
        'display_sale', 'display_product',
        'user',
        'debit', 'credit', 'balance',
        'display_status',
        'timestamp'
    ]

    def get_sale(self, instance):
        if instance.instansale_trx:
            return instance.instansale_trx
        return None

    def display_sale(self, instance):
        if self.get_sale(instance):
            return self.get_sale(instance).code
        return None

    def display_product(self, instance):
        if self.get_sale(instance):
            return self.get_sale(instance).product.product_name
        return None

    def display_status(self, instance):
        if self.get_sale(instance):
            return self.get_sale(instance).get_status()
        return None

@admin.register(CommisionRecord)
class CommisionRecordAdmin(admin.ModelAdmin):
    list_display = [
        'agen',
        'debit', 'credit', 'balance'
    ]

@admin.register(LoanRecord)
class LoanRecordAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'agen',
        'debit', 'credit', 'balance',
        'record_type',
        'is_delete', 'is_paid'
    ]

@admin.register(ProfitRecord)
class ProfitRecordAdmin(admin.ModelAdmin):
    pass
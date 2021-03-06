from django.db import models
from django.contrib.auth.models import User
from django.db.models import F, Q, Sum, Value as V
from django.db.models.functions import Coalesce

from core.models import CommonBase
from transaction.models import (
    InstanSale, PpobSale
)
from payment.models import (
    Payment, LoanPayment,
    Transfer,
)
from witdraw.models import (
    Witdraw
)

class BillingRecord(CommonBase):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    debit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    prev_billing = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    sequence = models.PositiveSmallIntegerField(default=1)
    instansale_trx = models.ForeignKey(InstanSale, on_delete=models.CASCADE, blank=True, null=True, related_name='bill_instan_trx')
    ppobsale_trx = models.ForeignKey(PpobSale, on_delete=models.CASCADE, blank=True, null=True, related_name='bill_ppob_trx')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, blank=True, null=True, related_name='billing_apyment')
    transfer = models.ForeignKey(Transfer, on_delete=models.CASCADE, blank=True, null=True, related_name='billing_transfer')

    class Meta:
        verbose_name = "Billing"
        ordering = [
            '-timestamp'
        ]
    
    def get_active_balance(self):
        if self.user.profile.user_type == 2:
            return self.balance
            
        return BillingRecord.objects.filter(
            id__lte=self.id, user=self.user, is_delete=False
        ).aggregate(
            bal = Sum(F('debit') - F('credit'))
        )['bal']


    def get_trx(self):
        if self.instansale_trx:
            return self.instansale_trx
        if self.ppobsale_trx:
            return self.ppobsale_trx
        return None

    def get_api_trx(self):
        trx = dict()
        if self.get_trx():
            trx['trx_code'] = self.get_trx().code
            trx['customer'] = self.get_trx().customer
            trx['product'] = self.get_trx().product.product_name
            trx['commision'] = self.get_trx().commision
            trx['sn'] = self.get_trx().get_sn()
        return trx

    def get_api_status(self):
        if self.get_trx():
            return self.get_trx().get_status().get_status_display()
        return None

class CommisionRecord(CommonBase):
    agen = models.ForeignKey(User, on_delete=models.CASCADE)
    debit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    prev_com = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    sequence = models.PositiveSmallIntegerField(default=1)

    verified = models.BooleanField(default=False)
    instansale_trx = models.ForeignKey(InstanSale, on_delete=models.CASCADE, blank=True, null=True, related_name='commision_instan_trx')
    ppobsale_trx = models.ForeignKey(PpobSale, on_delete=models.CASCADE, blank=True, null=True, related_name='commision_ppob_trx')
    
    is_withdraw = models.BooleanField(default=False)
    withdraw = models.OneToOneField(Witdraw, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Komisi'
        ordering = [
            '-timestamp'
        ]

    def get_trx(self):
        if self.instansale_trx:
            return self.instansale_trx
        elif self.ppobsale_trx:
            return self.ppobsale_trx
        else:
            return None
            

class LoanRecord(CommonBase):
    LOAN = 'LO'
    PAYMENT = 'PA'
    LIST_TYPE = (
        (LOAN, 'LOAN'),
        (PAYMENT, 'PAYMENT')
    )
    agen = models.ForeignKey(User, on_delete=models.CASCADE, related_name='loan_record_agen')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='loan_record_user')
    debit = models.DecimalField(max_digits=12, decimal_places=2, default=0) # tambah utang
    credit = models.DecimalField(max_digits=12, decimal_places=2, default=0) # pengurangan utang
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0) # loan user balance
    is_paid = models.BooleanField(default=False)
    record_type = models.CharField(max_length=2, choices=LIST_TYPE, default=LOAN)
    payform = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True) # form payment
    loan_payment = models.ForeignKey(LoanPayment, on_delete=models.CASCADE, blank=True, null=True, related_name='loan_payment')
    bill_record = models.ForeignKey(BillingRecord, on_delete=models.CASCADE, blank=True, null=True, related_name='loan_bill')
    closed = models.BooleanField(default=False)

    instansale_trx = models.ForeignKey(InstanSale, on_delete=models.CASCADE, blank=True, null=True, related_name='loan_instan_trx')
    ppobsale_trx = models.ForeignKey(PpobSale, on_delete=models.CASCADE, blank=True, null=True, related_name='loan_ppob_trx')

    class Meta:
        verbose_name = 'Pinjaman'
        ordering = [
            '-timestamp'
        ]

    def get_loan_residu(self):
        loan_unpaid = self.bill_record.loan_bill.aggregate(
            unpaid = Sum(F('debit') - F('credit'))
        )
        return loan_unpaid['unpaid']



class ProfitRecord(CommonBase):
    instansale_trx = models.ForeignKey(InstanSale, on_delete=models.CASCADE, blank=True, null=True, related_name='profit_instan_trx')
    ppobsale_trx = models.ForeignKey(PpobSale, on_delete=models.CASCADE, blank=True, null=True, related_name='profit_ppob_trx')
    debit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Keuntungan'
        ordering = ['-timestamp']
from django.contrib import admin
from loan.models import Register
from loan.models import Loan
# Register your models here.

admin.site.register(Register)
admin.site.register(Loan)
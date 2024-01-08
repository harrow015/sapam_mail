from django.contrib import admin
from .models import country_table,  register_table, state_table

admin.site.register(country_table)
admin.site.register(register_table)
admin.site.register(state_table)

# Register your models here.

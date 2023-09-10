from django.contrib import admin
from .models import *


admin.site.register(Item)
admin.site.site_header='Gova Warehouse'
admin.site.site_title='Gova Warehouse'
admin.site.register(Request)
admin.site.register(Support)

# admin.site.register(Return_items)
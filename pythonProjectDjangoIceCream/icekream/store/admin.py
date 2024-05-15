from django.contrib import admin

from store.models import People, Children, Ice, StoreIcecream

# Register your models here.
admin.site.register(People)
admin.site.register(Children)
admin.site.register(Ice)
admin.site.register(StoreIcecream)


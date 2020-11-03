from django.contrib import admin

# Register your models here.

from .models import Pricelist, Masters, Brands, Workshops, Masterlist, Brandlist, Cars, Works, Documents, Workslist

admin.site.register(Pricelist)
admin.site.register(Masters)
admin.site.register(Brands)
admin.site.register(Workshops)
admin.site.register(Masterlist)
admin.site.register(Brandlist)
admin.site.register(Cars)
admin.site.register(Works)
admin.site.register(Documents)
admin.site.register(Workslist)
from django.contrib import admin

from .models import Product, User, Cart,Anime,Category, current_user
# Register your models here.
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Cart)
admin.site.register(Anime)
admin.site.register(Category)
admin.site.register(current_user)

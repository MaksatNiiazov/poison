from django.contrib import admin

# Register your models here.

from shop_api.models import *

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Color)
admin.site.register(ProductColor)
admin.site.register(ProductPhoto)
admin.site.register(Comment)
admin.site.register(Like)

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'username', "email", "telegram", 'registration_date')
#     list_display_links = ('id', 'username', 'email')
#     search_fields = ('username', "email", 'telegram')
#
#
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('category_name',)
#     list_display_links = ('category_name',)
#
#
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'product_name', "category", 'url')
#     list_display_links = ('id', 'product_name', 'url')
#     search_fields = ("product_name", 'url')
#
#
# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('user', 'created_date', 'total_price')
#     list_display_links = ('user', 'created_date')
#     search_fields = ('user', 'created_date')
#

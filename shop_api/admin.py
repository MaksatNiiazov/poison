from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from shop_api.models import *

admin.site.register(Brand)
admin.site.register(Category)
# admin.site.register(Product)
admin.site.register(Color)
admin.site.register(ProductColor)
# admin.site.register(ProductPhoto)
admin.site.register(Comment)
admin.site.register(Like)


class ImgInLine(admin.StackedInline):
    model = ProductPhoto
    list_display = ('product', 'photo', )
    readonly_fields = ('photo',)
    extra = 1

    def photo(self, obj):
        return mark_safe(f'<img src = {obj.photos.image.url} with = "100" height = "100"')


@admin.register(Product)
class Product(admin.ModelAdmin):
    model = Product
    list_display = ("name", 'description', 'category', "brand", "vendor_code", 'sex', 'new', 'is_product_in_stock',)
    inlines = [ImgInLine, ]

    def get_image(self, obj):
        return mark_safe(f'<img src = {obj.photos.image.url} with = "50" height = "60"')




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

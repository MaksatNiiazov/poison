from django.db import models
from users.models import User


# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50,)


class Brand(models.Model):
    brand = models.CharField(max_length=50,)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_products')
    vendor_code = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand_products')
    SEX_CHOICE = (
        ('unisex', 'Unisex'),
        ('men', 'Men'),
        ('women', 'Women'),
        )
    sex = models.CharField(max_length=20, choices=SEX_CHOICE)
    new = models.BooleanField(default=False)
    is_product_in_stock = models.BooleanField(default=True)


class Color(models.Model):
    color = models.CharField(max_length=8)


class ProductColor(models.Model):  # Промежуточная таблица связывающая цвет с продуктом
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)


class ProductPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/list/')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_comments')
    created_time = models.DateTimeField(auto_now=True)
    message = models.TextField()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_likes')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_likes')


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='orders')
    created_date = models.DateTimeField(auto_now=True)
    items = models.PositiveIntegerField(default=0)
    discount = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    grand_total = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    finished = models.BooleanField(default=False)

    class Meta:
        ordering = ('finished', 'created_date')

    def __str__(self):
        return f'{self.user}, {self.created_date}'


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='products_in_order')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='orders')
    count = models.PositiveIntegerField(default=1)
    total_price = models.PositiveIntegerField(default=0)




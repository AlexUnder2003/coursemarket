from django.db import models

class Order(models.Model):
    # Добавляем связь с пользователем (если вы используете систему аутентификации Django)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)

    # Поля для информации о продукте
    product_id = models.IntegerField()
    quantity = models.IntegerField(default=1)  # Количество товаров в заказе
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    # Поля для информации о пользователе и адресе
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}: Product ID {self.product_id}, Total Price {self.total_price} USD"
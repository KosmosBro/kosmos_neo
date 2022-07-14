# from django.db import models
# from django.core import validators
#
#
# class UserProfile(models.Model):
#     username = models.CharField(db_index=True, max_length=255, unique=True)
#
#     email = models.EmailField(
#         validators=[validators.validate_email],
#         unique=True,
#         blank=False
#     )
#
#     USERNAME_FIELD = 'email'
#
#     REQUIRED_FIELDS = ('username',)
#
#     def __str__(self):
#         return self.username
#
#
# class Product(models.Model):
#     title = models.CharField(max_length=50, verbose_name='Название продукта')
#     description = models.CharField(max_length=150, verbose_name='Описание продукта')
#     creation_date = models.DateTimeField(null=True, verbose_name='Дата создания продукта')
#     picture = models.ImageField(upload_to='images/', blank=True, verbose_name="Картинка продукта",
#                                 max_length=900)
#     price = models.IntegerField(verbose_name="Цена продукта")
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         unique_together = ['id', 'title']

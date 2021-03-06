from django.db import models
from django.contrib.auth.models import User

# Language =(
#     ("Tamil", "Tamil"),
#     ("English", "English"),
#     ("Sinhala", "Sinhala"),
# )


class Category(models.Model):
    title = models.CharField(max_length=65,unique=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Category"

class Books (models.Model):
    isbn = models.CharField(max_length=20,unique=True)
    book = models.CharField(max_length=65,unique=True)
    language = models.CharField(max_length=10)
    category = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    publisher = models.CharField(max_length=50)
    pub_date = models.DateField()
    pages = models.CharField(max_length=50)
    note = models.CharField(max_length=65)
    edition = models.CharField(max_length=50)
    image = models.ImageField(upload_to='book_cover')
    create_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Books"

class Expenses (models.Model):
    book = models.CharField(max_length=65)
    transport = models.CharField(max_length=65)
    transport_cost = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    purchase_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    exchange_rates = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    total_book_cost = models.IntegerField(default=0)
    quantity = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    date = models.DateField(auto_now=False, auto_now_add=False, max_length=65) # it is for manual date
    create_date = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        self.total_book_cost = self.purchase_price * self.quantity
        super(Expenses, self).save(*args, **kwargs)
        pass

    class Meta:
        verbose_name_plural = "Expenses"

class Sales (models.Model):
    book = models.CharField(max_length=65)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    quantity = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total = self.sale_price * self.quantity
        super(Sales, self).save(*args, **kwargs)
        pass


    class Meta:
        verbose_name_plural = "Sales"


class Carousel(models.Model):
    headline = models.CharField(max_length=65)
    banner = models.ImageField(upload_to='web_banner')
    create_date = models.DateTimeField(auto_now_add=True)

    #class Meta:
        #verbose_name_plural = "Carousel"

    #def __str__(self):
        #return self.headline

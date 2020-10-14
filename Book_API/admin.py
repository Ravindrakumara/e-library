from django.contrib import admin
from.models import Books, Category, Expenses, Sales, Carousel

# Register your models here.
admin.site.site_header = "Bookshop"
admin.site.site_title = "Bk Sl Bookshop Admin Portal"
admin.site.index_title = "Welcome to Bk Sl Bookshop"

class BookAdmin(admin.ModelAdmin):
    list_display = ['isbn', 'book', 'language',
                    'description', 'publisher', 'pub_date', 'pages', 'note', 'edition', 'create_date']


class CateAdmin(admin.ModelAdmin):
    list_display = ['title']


class CarouselAdmin(admin.ModelAdmin):
    list_display = ['headline', 'banner', 'create_date']


class ExpensesAdmin(admin.ModelAdmin):
    list_display = ['book', 'transport', 'transport_cost', 'purchase_price', 'exchange_rates', 'sale_price', 'total_book_cost', 'quantity', 'date', 'create_date']

admin.site.register(Books,BookAdmin)
admin.site.register(Category,CateAdmin)
admin.site.register(Expenses, ExpensesAdmin)

admin.site.register(Sales)
admin.site.register(Carousel, CarouselAdmin)
#

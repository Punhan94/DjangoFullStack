from django.contrib import admin
from django.utils.html import format_html
from mptt.admin import DraggableMPTTAdmin, MPTTModelAdmin
from .models import Product, Category, Images, ShoppingComment

# Register your models here.
class ProductImagesInline(admin.TabularInline):
    model = Images
    extra = 3
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    class Meta: model = Product
    list_display = ['title', 'amount', 'price', 'status']
    list_editable = ['status', 'price', 'amount']
    inlines = [ProductImagesInline]

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    class Meta: model = Images
    list_display=['product','title']


@admin.register(ShoppingComment)
class ShoppingCommmentAdmin(admin.ModelAdmin):
    class Meta: model = ShoppingComment

@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count',
                    'status')
    list_editable = ['status']
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug':('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'
from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Product, ProductImage, ProductDimension, ProductPattern


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ('image', 'alt_text', 'order')


class ProductDimensionInline(admin.TabularInline):
    model = ProductDimension
    extra = 1
    fields = ('length', 'width', 'height', 'order')


class ProductPatternInline(admin.TabularInline):
    model = ProductPattern
    extra = 1
    fields = ('image', 'order')


@admin.register(ProductDimension)
class ProductDimensionAdmin(admin.ModelAdmin):
    list_display = ('product', 'length', 'width', 'height', 'order')
    list_filter = ('product',)
    search_fields = ('product__title',)


@admin.register(ProductPattern)
class ProductPatternAdmin(admin.ModelAdmin):
    list_display = ('product', 'image', 'order')
    list_filter = ('product',)
    search_fields = ('product__title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'sku', 'current_price', 'stock_status', 'is_active', 'created_at')
    list_filter = ('stock_type', 'is_active', 'created_at')
    search_fields = ('title', 'sku', 'short_description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductImageInline, ProductDimensionInline, ProductPatternInline]
    fieldsets = (
        (_('Osnovne informacije'), {
            'fields': ('title', 'slug', 'sku')
        }),
        (_('SEO'), {
            'fields': ('meta_title', 'meta_description')
        }),
        (_('Slika'), {
            'fields': ('thumbnail',)
        }),
        (_('Opis'), {
            'fields': ('short_description', 'full_description')
        }),
        (_('Cena'), {
            'fields': ('price', 'sale_price')
        }),
        (_('Zalihe'), {
            'fields': ('stock_type', 'stock_quantity', 'is_active')
        }),
    )

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name in ('short_description', 'full_description'):
            kwargs['widget'] = CKEditorUploadingWidget(config_name='default')
        return super().formfield_for_dbfield(db_field, request, **kwargs)

    def stock_status(self, obj):
        if obj.stock_type == 'always':
            return _('Uvek na stanju')
        if obj.stock_quantity and obj.stock_quantity > 0:
            return f"{obj.stock_quantity} komada"
        return _('Nema na stanju')
    stock_status.short_description = _('Status zaliha')

    def current_price(self, obj):
        if obj.sale_price:
            return format_html('<span style="text-decoration: line-through;">{}</span> {}', obj.price, obj.sale_price)
        return obj.price
    current_price.short_description = _('Cena')

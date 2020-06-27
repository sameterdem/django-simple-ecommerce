from django.contrib import admin

from .models import Category, Product, Images

class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'status']
    list_editable = ['status']
    list_filter = ['status']

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'status', 'category']
    list_editable = ['status']
    list_filter = ['status', 'category']
    inlines = [ProductImageInline]

class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images, ImageAdmin)

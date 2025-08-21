from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from netmodel.models import NetworkModel, Products


class ProductsInline(admin.TabularInline):
    model = Products
    fk_name = "network_model"


class NetworkModelAdmin(admin.ModelAdmin):
    inlines = [ProductsInline, ]
    list_display = ("name", "hierarchy_level", "contact_city", "arrears", "creation_time",
                    "supplier",
                    # "link_to_supplier",
                    )
    list_filter = ("contact_city",)
    # search_fields = ("hierarchy_level",) # Поиск
    list_display_links = ("name",)

    # def link_to_supplier(self, obj):
    #     link = reverse("admin:netmodel_supplier_change", args=[obj.supplier.id])
    #     return format_html('<a href="{}">{}</a>', link, obj.supplier)
    #
    # link_to_supplier.short_description = "supplier"

admin.site.register(NetworkModel, NetworkModelAdmin)


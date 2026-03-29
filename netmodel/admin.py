from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from netmodel.models import NetworkModel, Products


@admin.action(description="Очищает задолженность перед поставщиком у выбранных объектов")
def clear_debt(model_admin, request, queryset):
    queryset.update(arrears=0)


class ProductsInline(admin.TabularInline):
    model = Products
    fk_name = "network_model"


@admin.register(NetworkModel)
class NetworkModelAdmin(admin.ModelAdmin):
    inlines = [ProductsInline, ]
    list_display = ("id", "name", "hierarchy_level", "contact_city", "arrears", "creation_time",
                    # "supplier",
                    "link_to_supplier",
                    )
    list_filter = ("contact_city",)
    readonly_fields = ("creation_time",)
    # search_fields = ("hierarchy_level",) # Поиск
    list_display_links = ("id",)
    actions = (clear_debt,)

    def link_to_supplier(self, obj):
        try:
            link = reverse("admin:netmodel_networkmodel_change", args=[obj.supplier.id])
        except AttributeError:
            return None
        else:
            return format_html(
                "<a href='{}'>{}</a>",
                link,
                obj.supplier,
            )

    link_to_supplier.short_description = "supplier_"

# admin.site.register(NetworkModel, NetworkModelAdmin)


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("network_model", "product_name", "product_model", "product_date")
    # list_filter = ("name", "release_year")

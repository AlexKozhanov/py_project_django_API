from django.db import models
from config.settings import AUTH_USER_MODEL

NULLABLE = {"blank": True, "null": True}


class NetworkModel(models.Model):
    """
    Класс Модель сети по продаже электроники.
    Поля класса: Название. email, страна, город, улица, номер дома. продукт, Поставщик. Задолженность. Время создания.
    """
    factory = "завод"
    retail_network = "розничная сеть"
    individual_entrepreneur = "индивидуальный предприниматель"
    NETWORK_LINK = [(factory, "завод"), (retail_network, "розничная сеть"),
                    (individual_entrepreneur, "индивидуальный предприниматель"), ]

    type = models.CharField(max_length=50, choices=NETWORK_LINK, default=factory,
                            verbose_name="Тип модели сети (по умолчанию Завод)")
    name = models.CharField(max_length=100, **NULLABLE, verbose_name='Название модели сети',
                            help_text='Введите название модели сети')

    hierarchy_level = models.PositiveIntegerField(default=0,
                                                  verbose_name="Иерархический уровень (определяется программой)", )
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, max_length=100,
                                 related_name="suppliers", verbose_name='Поставщик')

    contact_email = models.EmailField(**NULLABLE, verbose_name="email", help_text="Укажите email")
    contact_country = models.CharField(max_length=100, **NULLABLE, verbose_name='Страна',
                                       help_text='Введите название страны')
    contact_city = models.CharField(max_length=100, **NULLABLE, verbose_name='Город',
                                    help_text='Введите название города')
    contact_street = models.CharField(max_length=100, **NULLABLE, verbose_name='Улица',
                                      help_text='Введите название улицы')
    contact_house_number = models.CharField(max_length=100, **NULLABLE, verbose_name='Номер дома',
                                            help_text='Введите номер дома')

    arrears = models.DecimalField(max_digits=12, decimal_places=2, **NULLABLE, verbose_name='Задолженность',
                                  help_text='Введите Задолженность')
    creation_time = models.DateField(auto_now=False, auto_now_add=True, verbose_name='Дата создания')
    related_person = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="netmodel",
                                       verbose_name="связанное с организацией лицо",
                                       help_text="Автоматически заполняется данными текущего пользователя", **NULLABLE)

    def save(self, *args, **kwargs):
        if self.type == "завод":
            self.hierarchy_level = 0
        elif self.supplier:
            self.hierarchy = self.supplier.hierarchy + 1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

    def __str__(self):
        return self.name


class Products(models.Model):
    """
    Класс Продукты.
    Поля класса: Название. email, страна, город, улица, номер дома. название продукта, модель,
    """
    network_model = models.ForeignKey(NetworkModel, on_delete=models.SET_NULL, **NULLABLE, max_length=100,
                                      verbose_name='Модель сети')
    product_name = models.CharField(max_length=100, **NULLABLE, verbose_name='Название продукта',
                                    help_text='Введите название продукта')
    product_model = models.CharField(max_length=100, **NULLABLE, verbose_name='Модель продукта',
                                     help_text='Введите модель продукта')
    product_date = models.DateField(auto_now=False, auto_now_add=False, **NULLABLE,
                                    verbose_name='Дата выхода продукта на рынок')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.product_name

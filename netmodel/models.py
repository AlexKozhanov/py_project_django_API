from django.conf import settings
from django.db import models

NULLABLE = {"blank": True, "null": True}


class Product(models.Model):
    """
    Класс Завод.
    Поля класса: Название. email, страна, город, улица, номер дома. название продукта, модель,
    """
    product_name = models.CharField(max_length=100, **NULLABLE, verbose_name='Описание курса',
                                    help_text='Введите описание')
    product_model = models.TextField(max_length=100, **NULLABLE, verbose_name='Описание курса',
                                     help_text='Введите описание')
    product_date = models.TextField(max_length=100, **NULLABLE, verbose_name='Описание курса',
                                    help_text='Введите описание')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'price', 'created_at', 'updated_at']

    def __str__(self):
        return self.name


class NetworkModel(models.Model):
    """
    Класс Завод.
    Поля класса: Название. email, страна, город, улица, номер дома. продукт, Поставщик. Задолженность. Время создания.
    """
    factory = "завод"
    retail_network = "розничная сеть"
    individual_entrepreneur = "индивидуальный предприниматель"
    NETWORK_LINK = [
        (factory, "завод"),
        (retail_network, "розничная сеть"),
        (individual_entrepreneur, "индивидуальный предприниматель"),
    ]
    level_model = models.CharField(
        max_length=50,
        choices=NETWORK_LINK,
        default=factory,
        **NULLABLE,
        verbose_name="Вид",
    )
    name = models.CharField(max_length=100, verbose_name='Название завода', help_text='Введите название завода')
    email = models.CharField(max_length=100, verbose_name='email', help_text='Введите email')
    country = models.CharField(max_length=100, **NULLABLE, verbose_name='Страна', help_text='Введите название страны')
    city = models.CharField(max_length=100, **NULLABLE, verbose_name='Город', help_text='Введите описание')
    street = models.CharField(max_length=100, **NULLABLE, verbose_name='Описание курса', help_text='Введите описание')
    house_number = models.CharField(max_length=100, **NULLABLE, verbose_name='Описание курса', help_text='Введите описание')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True, max_length=100,
        verbose_name='Курс', help_text='Прикрепите урок к курсу')
    supplier = models.TextField(blank=True, null=True, max_length=100, verbose_name='Описание курса',
                                    help_text='Введите описание')
    Arrears = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Задолженность',
                                    help_text='Введите Задолженность')
    Creation_time = models.DateField(auto_now=False, auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['name', 'description', 'png', 'owner', ]

    def __str__(self):
        return self.name


class Lesson(models.Model):
    """
    Класс Урок.
    Поля класса: название, описание, превью (картинка), ссылка на видео.
    """
    name = models.CharField(
        max_length=100,
        verbose_name='Название урока',
        help_text='Введите название')
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        max_length=100,
        verbose_name='Курс',
        help_text='Прикрепите урок к курсу')
    description = models.TextField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name='Описание урока',
        help_text='Введите описание')
    png = models.ImageField(
        upload_to='Ims/png',
        blank=True,
        null=True,
        verbose_name='Превью урока',
        help_text='Добавьте картинку')
    link = models.TextField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name='Ссылка на видео',
        help_text='Введите ссылку')
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Автор урока",
        help_text="Укажите автора урока", )

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['name', 'course', 'description', 'png', 'link', 'owner', ]

    def __str__(self):
        return self.name




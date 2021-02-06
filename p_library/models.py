from django.db import models
from django.db.models.deletion import SET_NULL
from django.utils.translation import gettext as _

class Author(models.Model):
    full_name = models.TextField(verbose_name=_("Имя автора"))
    birth_year = models.SmallIntegerField(verbose_name=_("Год рожения"))
    country = models.CharField(max_length=2, verbose_name=_("Страна"))

    def __str__(self):
        return self.full_name

class Book(models.Model):
    ISBN = models.CharField(max_length=13,
                            verbose_name=_("Международный стандартный "
                                           "книжный номер"))
    title = models.TextField(verbose_name=_("Название"))
    description = models.TextField(verbose_name=_("Аннотация"))
    year_release = models.SmallIntegerField(verbose_name=_("Год издания"))
    copy_count = models.SmallIntegerField(verbose_name=_("Число копий"))
    price = models.DecimalField(max_digits=12, decimal_places=2,
                                verbose_name=_("Цена"))
    author = models.ForeignKey("p_library.Author", on_delete=models.CASCADE,
                               verbose_name=_("Автор"),
                               related_name="book_author")
    friends = models.ForeignKey("p_library.Friend", on_delete=SET_NULL, null=True, verbose_name=_("Должник"))
    def __str__(self):
        return self.title

class Friend(models.Model):
    full_name = models.TextField(verbose_name=_("Имя друга"))
    address = models.TextField(verbose_name=_("Адрес"))
    phone = models.TextField(verbose_name=_("Телефон"))
    def __str__(self):
            return self.full_name

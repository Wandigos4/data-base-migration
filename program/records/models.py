from django.db import models
from django.conf import settings


class Department(models.Model):
    name = models.CharField("Назва підрозділу", max_length=100)
    address = models.CharField("Адреса", max_length=200)
    phone = models.CharField("Телефон", max_length=20, blank=True)

    class Meta:
        verbose_name = "Підрозділ"
        verbose_name_plural = "Підрозділи"

    def __str__(self):
        return self.name


class Applicant(models.Model):
    surname = models.CharField("Прізвище", max_length=50)
    name = models.CharField("Ім'я", max_length=50)
    patronymic = models.CharField("По батькові", max_length=50, blank=True)
    birth_date = models.DateField("Дата народження")
    document_number = models.CharField("Номер документа", max_length=30)
    phone = models.CharField("Телефон", max_length=20, blank=True)
    address = models.CharField("Адреса проживання", max_length=200)

    class Meta:
        verbose_name = "Заявник"
        verbose_name_plural = "Заявники"

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"


class Service(models.Model):
    name = models.CharField("Назва послуги", max_length=100)
    description = models.TextField("Опис послуги", blank=True)
    processing_days = models.PositiveIntegerField("Термін виконання, днів")
    price = models.DecimalField("Вартість", max_digits=8, decimal_places=2, default=0)

    class Meta:
        verbose_name = "Послуга"
        verbose_name_plural = "Послуги"

    def __str__(self):
        return self.name


class Application(models.Model):
    STATUS_CHOICES = [
        ("new", "Нова"),
        ("processing", "В обробці"),
        ("waiting", "Очікує документи"),
        ("completed", "Виконана"),
        ("rejected", "Відхилена"),
    ]

    applicant = models.ForeignKey(
        Applicant,
        on_delete=models.CASCADE,
        verbose_name="Заявник"
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.PROTECT,
        verbose_name="Послуга"
    )
    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Працівник"
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Підрозділ"
    )
    created_date = models.DateField("Дата подання")
    status = models.CharField(
        "Статус заяви",
        max_length=20,
        choices=STATUS_CHOICES,
        default="new"
    )
    note = models.TextField("Примітка", blank=True)

    class Meta:
        verbose_name = "Заява"
        verbose_name_plural = "Заяви"

    def __str__(self):
        return f"Заява №{self.id} - {self.applicant}"
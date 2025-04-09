from django.core.validators import RegexValidator
from django.db import models


class Card(models.Model):

    MALE = "мужской"
    FEMALE = "женский"
    SEX_CHOICES = ((MALE, "мужской"), (FEMALE, "женский"))

    # Поля, заполняющиеся автоматически
    number = models.PositiveIntegerField(
        unique=True, blank=True, null=True, verbose_name="Номер бонусной карты"
    )
    balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Баланс бонусной карты",
    )
    bonus = models.PositiveSmallIntegerField(
        default=5, verbose_name="Бонус", blank=True, null=True
    )

    # Поля, заполняющиеся пользователем, обязательные к заполнению
    phone_number = models.CharField(
        unique=True,
        max_length=10,
        validators=[
            RegexValidator(
                regex=r"\d{10}$",
                message="Номер телефона должен быть в формате 9999999999 (10 цифр)",
            )
        ],
    )
    owner = models.CharField(
        max_length=100,
        verbose_name="Владелец бонусной карты",
        help_text="Введите фамилию",
    )
    birth_date = models.DateField(
        verbose_name="Дата рождения", help_text="Введите дату своего рождения"
    )
    sex = models.CharField(
        choices=SEX_CHOICES, verbose_name="Пол", help_text="Выберите пол"
    )

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "Бонусная карта"
        verbose_name_plural = "Бонусные карты"
        ordering = ["number"]

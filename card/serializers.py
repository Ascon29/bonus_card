from rest_framework import serializers

from card.models import Card


class CardCreateSerializer(serializers.ModelSerializer):
    """ Сериализатор для создания бонусной карты """

    class Meta:
        model = Card
        fields = ["owner", "birth_date", "sex", "phone_number"]
        read_only_fields = ["number", "balance", "bonus"]


class CardSerializer(serializers.ModelSerializer):
    """ Сериализатор для просмотра бонусной(ных) карт """

    class Meta:
        model = Card
        fields = "__all__"


class CardUpdateSerializer(serializers.ModelSerializer):
    """ Сериализатор для изменения бонусной карты """

    class Meta:
        model = Card
        fields = ["number", "owner", "balance", "birth_date"]

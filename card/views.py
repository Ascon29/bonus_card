import json

from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from card.permissions import IsSuperUser
from card.services import check_birthday

from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView, \
    get_object_or_404

from card.models import Card
from card.serializers import CardCreateSerializer, CardSerializer, CardUpdateSerializer


class CardCreateAPIView(CreateAPIView):
    """ Контроллер создания бонусной карты. Создается первая карта: присваивается номер 1000.
    Последующим картам присваивается номер последней + 1.
    Присваивает бонус 10%, если у пользователя ДР (+/- 3 дня от даты). """
    serializer_class = CardCreateSerializer
    queryset = Card.objects.all()

    def perform_create(self, serializer):
        if self.queryset.count() == 0:
            serializer.save(number=1000)
        else:
            serializer.save(number=self.queryset.last().number + 1)
        serializer.save(balance=100)
        # сервисная функция на проверку актуальности дня рождения (services.py)
        if check_birthday(self.queryset.last().birth_date):
            serializer.save(bonus=10)


class CardRetrieveAPIView(RetrieveAPIView):
    """ Контроллер просмотра информации о бонусной карте. """
    serializer_class = CardSerializer
    queryset = Card.objects.all()


class CardUpdateAPIView(UpdateAPIView):
    """ Контроллер изменения бонусной карты (только суперпользователь). """
    serializer_class = CardUpdateSerializer
    queryset = Card.objects.all()
    # permission_classes = [IsSuperUser,]


class CardDestroyAPIView(DestroyAPIView):
    """ Контроллер удаления бонусной карты (только суперпользователь). """
    queryset = Card.objects.all()
    permission_classes = [IsSuperUser, ]


class CardListAPIView(ListAPIView):
    """ Контроллер просмотра списка бонусных карт (только суперпользователь). """
    serializer_class = CardSerializer
    queryset = Card.objects.all()
    # permission_classes = [IsSuperUser,]


class CardActivate(APIView):
    """ Контроллер активации бонусной карты. Проверяет актуальность ДР, устанавливая соответствующий бонус """
    def post(self, *args, **kwargs):
        card = get_object_or_404(Card, pk=self.kwargs['pk'])
        if check_birthday(card.birth_date):
            card.bonus = 10
        else:
            card.bonus = 5
        card.save()
        result = {
            'Номер карты': card.number,
            'Владелец': card.owner,
            'Пол': card.sex,
            'Баланс': card.balance,
            'Бонус': card.bonus,
            'Дата рождения': card.birth_date,
        }
        return HttpResponse(json.dumps(result, indent=4, ensure_ascii=False, default=str))

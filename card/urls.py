from django.urls import path

from card.apps import CardConfig
from card.views import CardCreateAPIView, CardListAPIView, CardDestroyAPIView, CardRetrieveAPIView, CardUpdateAPIView, \
    CardActivate

app_name = CardConfig.name

urlpatterns = [
    path("card_create/", CardCreateAPIView.as_view(), name="card_create"),
    path("card_list/", CardListAPIView.as_view(), name="card_list"),
    path("card_delete/<int:pk>/", CardDestroyAPIView.as_view(), name="card_delete"),
    path("card_detail/<int:pk>/", CardRetrieveAPIView.as_view(), name="card_detail"),
    path("card_update/<int:pk>/", CardUpdateAPIView.as_view(), name="card_update"),
    path("card_activate/<int:pk>/", CardActivate.as_view(), name="card_activate"),
]

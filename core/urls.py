from django.urls import path
from .views import ContactPage, NosotrosPage, HomePage

urlpatterns = [
    path('', HomePage.as_view()),
    path('home/', HomePage.as_view(), name="home"),
    path('contacto/', ContactPage.as_view(), name="contacto"),
    path('nosotros/', NosotrosPage.as_view(), name="nosotros"),


]

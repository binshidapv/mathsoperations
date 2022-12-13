from django.urls import path
from calculator import views
urlpatterns=[
    path("add",views.AddView.as_view(),name="addition"),
    path("sub", views.SubView.as_view(),name="substraction"),
    path("factorial",views.FactView.as_view(),name="factorial"),
    path("prime",views.PrimeView.as_view(),name="prime"),
    path("Home",views.IndexView.as_view(),name="Home")

]
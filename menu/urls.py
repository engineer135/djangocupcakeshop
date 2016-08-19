from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.cupcake_list,name="cupcake_list"),
    url(r'^cupcake/high/$',views.cupcake_high_list,name="cupcake_high_list"),
    url(r'^cupcake/low/$',views.cupcake_low_list,name="cupcake_low_list"),
    url(r'^cupcake/(?P<pk>\d+)/$',views.cupcake_detail,name="cupcake_detail"),
    url(r'^cupcake/new/$', views.cupcake_new, name='cupcake_new'),
]

from django.urls import path,include
from . import views
urlpatterns = [
path('',views.pm1,name='pm1'),
path('login1',views.login1,name='login1'),
path('logout1',views.logout1,name='logout1'),
path('req_holy',views.req_holy,name='req_holy'),
path('show_req',views.show_req,name='show_req'),
path('<str:pro_name>/sho',views.show_msg,name='show_msg'),
path('don_prim',views.don_prim,name='don_prim'),
path('acceptes',views.acceptes,name='acceptes'),
path('jes',views.jes,name='jes'),
path('<str:pro_id>/fil',views.show_fil,name='show_fil'),
path('<str:pro_del>/del',views.dele,name='dele'),



]

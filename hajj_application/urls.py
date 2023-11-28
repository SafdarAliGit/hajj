from django.urls import path

from hajj_application.views import CreateHajjApplication, ListHajjApplication, UpdateHajjApplication, \
    DeleteHajjApplication, DetailHajjApplication

app_name = 'hajj_application'
urlpatterns = [
    path('add', CreateHajjApplication.as_view(), name='add'),
    path('list', ListHajjApplication.as_view(), name='list'),
    path('update/<int:pk>', UpdateHajjApplication.as_view(), name='update'),
    path('delete/<int:pk>', DeleteHajjApplication.as_view(), name='delete'),
    path('detail/<int:pk>', DetailHajjApplication.as_view(), name='detail'),
]

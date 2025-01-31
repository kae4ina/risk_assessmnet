from django.urls import path


from measure.views import measure_create, get_risk, measure_saved

urlpatterns=[
    path('measure_create/', measure_create, name='measure_create'),
    path('get_risk/', get_risk, name='get_risk'),
    path('measure_saved/', measure_saved, name='measure_saved'),
]
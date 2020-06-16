from api.views import ManufacturerViewSet, ShoeTypeViewSet, ShoeColorViewSet, ShoesViewSet

from rest_framework.routers import DefaultRouter

from django.conf.urls import include, url

router = DefaultRouter()

router.register(r'Manufacturer', ManufacturerViewSet,basename='M')
router.register(r'ShoeType', ShoeTypeViewSet,basename='ST')
router.register(r'ShoeColor', ShoeColorViewSet,basename='SC')
router.register(r'Shoes', ShoesViewSet,basename='S')

urlpatterns = [
    url(r'^api/',include(router.urls))
]
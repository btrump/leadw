from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from montyhall.models import MontyHallResult


class MontyHallResultResource(ModelResource):
    class Meta:
        queryset = MontyHallResult.objects.all()
        resource_name = 'monty_hall_result'
        authorization = Authorization()
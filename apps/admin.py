from django.contrib import admin
from .models import City,State,Hospital,Facility, Availability   #Service

from django.db.models.signals import post_save
from django.dispatch import receiver

# Register your models here.
@receiver(post_save , sender =  Hospital)
def afterHospitalSave(signal , instance,**kwargs):
    facilities = Facility.objects.all()
    for facility in facilities:
        availability = Availability(hospital = instance,facility= facility)
        availability.save()

    # service = Facility(hospital = instance)
    # service.save()

def afterFacilitySave(signal , instance,**kwargs):
    hospitals = Hospital.objects.all()
    for hospital in hospitals:
        availability = Availability(hospital = hospital,facility= instance)
        availability.save()

class FacilityAdmin(admin.ModelAdmin):
    model = Facility
    list_display = [
        'title'

        # 'hospital',
        # 'oxygen_beds',
        # 'oxygen_cylinder',
        # 'ventilator'
    ]

    # def oxygen_beds(self , object):
    #     return f'{object.oxygen_beds_available}/{object.oxygen_beds_total}'
    #
    # def oxygen_cylinder(self , object):
    #     return f'{object.oxygen_cylinder_available}/{object.oxygen_cylinder_total}'
    #
    # def ventilator(self , object):
    #     return f'{object.ventilator_available}/{object.ventilator_total}'

class HospitalAdmin(admin.ModelAdmin):
    model = Hospital
    list_display = ['name','phone','address','city']

class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = ['name','state']

class StateAdmin(admin.ModelAdmin):
    model = State
    list_display = ['name']

class AvailabilityAdmin(admin.ModelAdmin):
    model = Availability
    list_display = ['hospital','facility','total','available','updated_at']
    list_editable = ['total','available']

admin.site.register(City , CityAdmin)
admin.site.register(State , StateAdmin)
admin.site.register(Hospital , HospitalAdmin)
admin.site.register(Facility , FacilityAdmin)
admin.site.register(Availability , AvailabilityAdmin)


from django import template

from apps.models import Availability

register = template.Library()

@register.simple_tag
def get_table_class(value):
    if value:
        return 'bg-success'
    return 'bg-danger'

    # if value == 0:
    #     return 'bg-danger'
    # elif 1 <= value < 5:
    #     return 'bg-warning'
    # return 'bg-success'
@register.simple_tag
def get_total_class(value):

        return 'bg-warning'


@register.simple_tag
def get_availabilities(hospital):
    return Availability.objects.filter(hospital = hospital).order_by('facility_id')

@register.simple_tag
def is_option_selected(selected_option,pk):
    if selected_option == str(pk):
        return 'selected'
    return ""

# @register.simple_tag
# def is_state_selected(seslcted_state_id,pk):
#     if seslcted_state_id == str(pk):
#         return 'selected'
#     return ""

#
# @register.simple_tag
# def is_city_selected(seslcted_city_id,pk):
#     if seslcted_city_id == str(pk):
#         return 'selected'
#     return ""
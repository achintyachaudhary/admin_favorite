from django.http import JsonResponse


# Create your views here.
def get_district(request):
    """
    give a state id, returns district mapped to that state
    :param request: state_id
    :return:
    """

    return JsonResponse({"dist_data": {"keyd": "valude"}})

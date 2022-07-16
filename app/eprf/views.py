import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.utils import timezone

from eprf.models import ZipCode, DataSet, VedTranscript


def main_page(request, *args, **kwargs):
    if request.method == 'GET':
        category_filters = []
        # subcategory_filters = Category.objects.distinct('sub_code', 'sub_text').filter(removed=False)
        return render(request, 'index.html', {'category_filters': category_filters})

def check_producer(request, *args, **kwargs):
    countries = DataSet.objects.distinct('producer_country').all()
    ved_groups = VedTranscript.objects.distinct('GRUPPA').all()
    labs = DataSet.objects.distinct('lab_name').all()
    # producers = DataSet.objects.distinct('producer_name').all()

    return render(request, 'check_producer.html', {'filterCountries': countries,
                                                   'filterVedGroups': ved_groups,
                                                   'filterLabs': labs})

def load_csv_codes(file):
    ZipCode


def get_detail_sets(request, *args, **kwargs):
    data = json.loads(request.body)
    if data.get('name') == 'filterVedGroups':
        filterVedGroups = VedTranscript.objects.distinct('GRUPPA').filter(GRUPPA=data.get('val')).only('GRUPPA', 'GRUPPA_text').all()
        return JsonResponse({'status': 'ok', 'result': list(filterVedGroups.values())})
    return JsonResponse({'status': 'false', 'message': 'Словарь не найден!'}, status=500)


def get_count_by_zips(request, *args, **kwargs):
    data = json.loads(request.body)
    if data.get('zips'):
        pass
    else:
        pass
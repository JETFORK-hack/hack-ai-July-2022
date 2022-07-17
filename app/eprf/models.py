from django.db import models

class ZipCode(models.Model):
    """ Зип коды """
    country_code = models.CharField(max_length=4, null=True, blank=True)
    zipcode = models.TextField(null=True, blank=True)
    place = models.TextField(null=True, blank=True)
    state = models.TextField(null=True, blank=True)
    state_code = models.TextField(null=True, blank=True)
    province = models.TextField(null=True, blank=True)
    province_code = models.TextField(null=True, blank=True)
    community = models.TextField(null=True, blank=True)
    community_code = models.TextField(null=True, blank=True)
    latitude = models.TextField(null=True, blank=True)
    longitude = models.TextField(null=True, blank=True)

class DataSet(models.Model):
    """ Юридические лица и их адреса"""
    id = models.AutoField(primary_key=True, blank=True)
    id_without_explode = models.IntegerField(blank=True)
    product_number = models.TextField(null=True, blank=True)
    ved_code_id = models.TextField(null=True, blank=True)
    technical_regulations = models.TextField(null=True, blank=True)
    product_group = models.TextField(null=True, blank=True)
    product_name = models.TextField(null=True, blank=True)
    lab_name = models.TextField(null=True, blank=True)
    requester_name = models.TextField(null=True, blank=True)
    requester_address = models.TextField(null=True, blank=True)
    requester_zipcode = models.CharField(max_length=10, null=True, blank=True)
    producer_name = models.TextField(null=True, blank=True)
    producer_country = models.TextField(null=True, blank=True)
    producer_address = models.TextField(null=True, blank=True)

    producer_zipcode = models.CharField(max_length=10, null=True, blank=True)
    producer_country_code = models.TextField(null=True, blank=True)
    requester_country_code = models.TextField(null=True, blank=True)
    requester_latitude = models.TextField(null=True, blank=True)
    requester_longitude = models.TextField(null=True, blank=True)
    producer_latitude = models.TextField(null=True, blank=True)
    producer_longitude = models.TextField(null=True, blank=True)
    GRUPPA = models.TextField(null=True, blank=True)
    GRUPPA_text = models.TextField(null=True, blank=True) # NAIM2
    TOV_POZ =models.TextField(null=True, blank=True)
    TOV_POZ_text = models.TextField(null=True, blank=True) # NAIM3
    SUB_POZ = models.TextField(null=True, blank=True)
    SUB_POZ_text = models.TextField(null=True, blank=True) # NAIM4
    outlier = models.IntegerField(default=None, null=True, blank=True)


class VedTranscript(models.Model):
    """ расшифровка ВЭД
    00 00 000000
    ГР ПЗ СУБПОЗ = ВЭД
    Гр - группа
    ПЗ - товарная позиция
    СУБПОЗ - суб позиция
    """
    GRUPPA = models.CharField(max_length=2)
    GRUPPA_text = models.TextField(null=True, blank=True)
    TOV_POZ = models.CharField(max_length=2, null=True, blank=True)
    TOV_POZ_text = models.TextField(null=True, blank=True)
    SUB_POZ = models.CharField(max_length=6, null=True, blank=True)
    SUB_POZ_text = models.TextField(null=True, blank=True)
    VED = models.CharField(max_length=10, null=True, blank=True)


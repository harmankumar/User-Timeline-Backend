# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Clientlog(models.Model):
    rt = models.CharField(max_length=32L, db_column='RT') # Field name made lowercase.
    type = models.CharField(max_length=128L, db_column='TYPE') # Field name made lowercase.
    subtype = models.CharField(max_length=128L)
    authkey = models.CharField(max_length=128L)
    userid = models.CharField(max_length=32L, blank=True)
    usertype = models.CharField(max_length=32L, blank=True)
    time = models.DateTimeField()
    session_id = models.CharField(max_length=36L, blank=True)
    keyword_search = models.CharField(max_length=128L, blank=True)
    query_len = models.IntegerField(null=True, blank=True)
    querytime = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = 'CLIENTLOG'

class Clientlog1(models.Model):
    rt = models.CharField(max_length=32L, db_column='RT') # Field name made lowercase.
    type = models.CharField(max_length=128L, db_column='TYPE') # Field name made lowercase.
    subtype = models.CharField(max_length=128L)
    authkey = models.CharField(max_length=128L)
    userid = models.CharField(max_length=32L, blank=True)
    usertype = models.CharField(max_length=32L, blank=True)
    time = models.DateTimeField()
    session_id = models.CharField(max_length=36L, blank=True)
    query_len = models.IntegerField(null=True, blank=True)
    querytime = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = 'CLIENTLOG1'

class Copresense(models.Model):
    user1 = models.CharField(max_length=32L)
    type1 = models.CharField(max_length=10L, blank=True)
    user2 = models.CharField(max_length=128L)
    type2 = models.CharField(max_length=10L, blank=True)
    time = models.BigIntegerField()
    cop_score = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    edge_weight = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'COPRESENSE'

class Messagelog(models.Model):
    id = models.CharField(max_length=5L, primary_key=True)
    userid = models.CharField(max_length=32L)
    usertype = models.CharField(max_length=32L, blank=True)
    source = models.CharField(max_length=128L)
    subgroup = models.CharField(max_length=128L)
    time = models.DateTimeField()
    salerent = models.CharField(max_length=32L, db_column='SaleRent', blank=True) # Field name made lowercase.
    availreq = models.CharField(max_length=32L, db_column='AvailReq', blank=True) # Field name made lowercase.
    listings = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'MESSAGELOG'

class Wifilog(models.Model):
    userid = models.CharField(max_length=32L)
    usertype = models.CharField(max_length=16L)
    time = models.BigIntegerField()
    wifissid = models.CharField(max_length=64L, blank=True)
    wifibssid = models.CharField(max_length=64L)
    session_id = models.CharField(max_length=36L, blank=True)
    lng = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    lat = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    distance = models.IntegerField(null=True, blank=True)
    strength = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'WIFILOG'

class Wifilog1(models.Model):
    userid = models.CharField(max_length=32L)
    usertype = models.CharField(max_length=16L)
    time = models.BigIntegerField()
    wifi = models.CharField(max_length=64L)
    lng = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    lat = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    distance = models.IntegerField(null=True, blank=True)
    strength = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'WIFILOG1'

class Messages(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    msg_text = models.CharField(max_length=300L, blank=True)
    msg_time = models.DateTimeField()
    class Meta:
        db_table = 'messages'

class Operators(models.Model):
    name = models.CharField(max_length=50L, blank=True)
    password = models.CharField(max_length=1000L, blank=True)
    class Meta:
        db_table = 'operators'


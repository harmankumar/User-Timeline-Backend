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

class Alarmlog(models.Model):
    phone = models.CharField(max_length=32L, unique=True)
    req = models.CharField(max_length=128L)
    status = models.CharField(max_length=128L)
    description = models.CharField(max_length=128L, blank=True)
    time = models.DateTimeField()
    class Meta:
        db_table = 'ALARMLOG'

class Alarms(models.Model):
    field_id = models.IntegerField(primary_key=True, db_column='_id') # Field renamed because it started with '_'.
    err = models.CharField(max_length=32L)
    phone = models.CharField(max_length=32L)
    description = models.CharField(max_length=128L)
    params = models.CharField(max_length=256L, db_column='Params') # Field name made lowercase.
    ccid = models.ForeignKey('CustomerCare', db_column='CCid') # Field name made lowercase.
    comment = models.CharField(max_length=128L, db_column='Comment') # Field name made lowercase.
    action = models.CharField(max_length=128L, db_column='Action', blank=True) # Field name made lowercase.
    time = models.DateTimeField()
    class Meta:
        db_table = 'ALARMS'

class Clientkeys(models.Model):
    imei = models.CharField(max_length=128L, unique=True)
    publickey = models.CharField(max_length=1024L, blank=True)
    aeskey = models.CharField(max_length=128L, blank=True)
    class Meta:
        db_table = 'CLIENTKEYS'

class Copresense(models.Model):
    user1 = models.CharField(max_length=32L)
    user2 = models.CharField(max_length=128L)
    time1 = models.DateTimeField()
    time2 = models.DateTimeField()
    cop_score = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    edge_weight = models.IntegerField(null=True, blank=True)
    distance = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    class Meta:
        db_table = 'COPRESENSE'

class CustomerCare(models.Model):
    field_id = models.IntegerField(primary_key=True, db_column='_id') # Field renamed because it started with '_'.
    name = models.CharField(max_length=128L)
    class Meta:
        db_table = 'CUSTOMER_CARE'

class Engagement(models.Model):
    field_id = models.IntegerField(primary_key=True, db_column='_id') # Field renamed because it started with '_'.
    user_id = models.IntegerField()
    message = models.CharField(max_length=512L)
    operator = models.CharField(max_length=128L)
    medium = models.CharField(max_length=128L, blank=True)
    shout_id = models.IntegerField(null=True, blank=True)
    comments = models.CharField(max_length=512L, blank=True)
    time = models.DateTimeField()
    class Meta:
        db_table = 'ENGAGEMENT'

class EngagementTable(models.Model):
    uid = models.CharField(max_length=128L)
    comments = models.TextField()
    ccr = models.CharField(max_length=128L)
    deltag = models.IntegerField(null=True, blank=True)
    time = models.DateTimeField()
    class Meta:
        db_table = 'ENGAGEMENT_TABLE'

class Locations(models.Model):
    field_id = models.IntegerField(primary_key=True, db_column='_id') # Field renamed because it started with '_'.
    title = models.CharField(max_length=128L, unique=True)
    location = models.CharField(max_length=128L)
    internal = models.IntegerField(null=True, blank=True)
    count = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'LOCATIONS'

class Mininglog(models.Model):
    field_id = models.IntegerField(primary_key=True, db_column='_id') # Field renamed because it started with '_'.
    k = models.CharField(max_length=128L)
    dup_k = models.CharField(max_length=128L)
    class Meta:
        db_table = 'MININGLOG'

class Regrequests(models.Model):
    phone = models.CharField(max_length=32L, unique=True)
    time = models.DateTimeField()
    utm_campaign = models.CharField(max_length=32L, blank=True)
    utm_source = models.CharField(max_length=32L, blank=True)
    utm_medium = models.CharField(max_length=32L, blank=True)
    utm_term = models.CharField(max_length=32L, blank=True)
    utm_content = models.CharField(max_length=32L, blank=True)
    class Meta:
        db_table = 'REGREQUESTS'

class TemporalTable(models.Model):
    k = models.CharField(max_length=128L, unique=True)
    v = models.CharField(max_length=128L)
    expirytime = models.DateTimeField()
    class Meta:
        db_table = 'TEMPORAL_TABLE'

class Users(models.Model):
    field_id = models.IntegerField(primary_key=True, db_column='_id') # Field renamed because it started with '_'.
    phone = models.CharField(max_length=32L, unique=True)
    imei = models.CharField(max_length=128L)
    ostype = models.CharField(max_length=32L, blank=True)
    osversion = models.CharField(max_length=32L, blank=True)
    appversion = models.CharField(max_length=32L, blank=True)
    phonemodel = models.CharField(max_length=32L, blank=True)
    registrationid = models.CharField(max_length=256L, blank=True)
    time = models.DateTimeField()
    dev = models.IntegerField(null=True, blank=True)
    invites = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'USERS'

class UserBookmarks(models.Model):
    uid = models.IntegerField()
    messageid = models.CharField(max_length=128L)
    time = models.DateTimeField()
    class Meta:
        db_table = 'USER_BOOKMARKS'

class UserContacts(models.Model):
    uid = models.IntegerField()
    phone = models.CharField(max_length=32L)
    time = models.DateTimeField()
    class Meta:
        db_table = 'USER_CONTACTS'

class UserFollowing(models.Model):
    uid = models.IntegerField()
    followid = models.IntegerField()
    time = models.DateTimeField()
    class Meta:
        db_table = 'USER_FOLLOWING'

class UserProfile(models.Model):
    uid = models.IntegerField()
    k = models.CharField(max_length=128L)
    v = models.TextField()
    forall = models.IntegerField(null=True, blank=True)
    time = models.DateTimeField()
    class Meta:
        db_table = 'USER_PROFILE'

class Validlist(models.Model):
    phone = models.CharField(max_length=32L, unique=True)
    source = models.CharField(max_length=32L, db_column='SOURCE', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=32L, blank=True)
    smscode = models.CharField(max_length=8L, blank=True)
    smstime = models.DateTimeField()
    type = models.CharField(max_length=64L, blank=True)
    utm_campaign = models.CharField(max_length=32L, blank=True)
    utm_source = models.CharField(max_length=32L, blank=True)
    utm_medium = models.CharField(max_length=32L, blank=True)
    utm_term = models.CharField(max_length=32L, blank=True)
    utm_content = models.CharField(max_length=32L, blank=True)
    id = models.IntegerField(primary_key=True)
    enabled = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'VALIDLIST'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80L, unique=True)
    class Meta:
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255L, blank=True)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100L)
    class Meta:
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128L)
    last_login = models.DateTimeField(null=True, blank=True)
    is_superuser = models.IntegerField()
    username = models.CharField(max_length=30L, unique=True)
    first_name = models.CharField(max_length=30L)
    last_name = models.CharField(max_length=30L)
    email = models.CharField(max_length=254L, blank=True)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = 'auth_user_user_permissions'

class ContactUs(models.Model):
    cs_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50L)
    email = models.CharField(max_length=50L)
    phone = models.CharField(max_length=15L)
    msg = models.TextField()
    dt = models.DateTimeField()
    class Meta:
        db_table = 'contact_us'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200L)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', null=True, blank=True)
    user = models.ForeignKey(AuthUser)
    class Meta:
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    app_label = models.CharField(max_length=100L)
    model = models.CharField(max_length=100L)
    class Meta:
        db_table = 'django_content_type'

class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)
    app = models.CharField(max_length=255L)
    name = models.CharField(max_length=255L)
    applied = models.DateTimeField()
    class Meta:
        db_table = 'django_migrations'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40L, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = 'django_session'

class PhoneRequests(models.Model):
    p_id = models.IntegerField(primary_key=True)
    phone = models.CharField(max_length=15L)
    dt = models.DateTimeField()
    class Meta:
        db_table = 'phone_requests'


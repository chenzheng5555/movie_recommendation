# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actor(models.Model):
    a_id = models.AutoField(primary_key=True)
    a_name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'actor'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Country(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'country'


class Director(models.Model):
    d_id = models.AutoField(primary_key=True)
    d_name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'director'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Genre(models.Model):
    g_id = models.AutoField(primary_key=True)
    g_name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'genre'


class Movie(models.Model):
    m_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    pictureurl = models.CharField(db_column='pictureURL', max_length=100)  # Field name made lowercase.
    filming_time = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'movie'


class MovieActor(models.Model):
    m = models.ForeignKey(Movie, models.DO_NOTHING)
    a = models.ForeignKey(Actor, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'movie_actor'


class MovieCountry(models.Model):
    m = models.ForeignKey(Movie, models.DO_NOTHING)
    c = models.ForeignKey(Country, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'movie_country'


class MovieDirector(models.Model):
    m = models.ForeignKey(Movie, models.DO_NOTHING)
    d = models.ForeignKey(Director, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'movie_director'


class MovieGenre(models.Model):
    m = models.ForeignKey(Movie, models.DO_NOTHING)
    g = models.ForeignKey(Genre, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'movie_genre'


class RecommendMovie(models.Model):
    u = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    m = models.ForeignKey(Movie, models.DO_NOTHING, blank=True, null=True)
    ranking = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'recommend_movie'


class Tag(models.Model):
    t_id = models.AutoField(primary_key=True)
    t_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tag'


class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    u_name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'user'


class UserCode(models.Model):
    id = models.AutoField(primary_key=True)
    u_name = models.CharField(max_length=40)
    code = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'user_code'


class UserMovieHistory(models.Model):
    u = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    m = models.ForeignKey(Movie, models.DO_NOTHING, blank=True, null=True)
    attr_id = models.IntegerField()
    attr_score = models.FloatField()

    class Meta:
        managed = False
        db_table = 'user_movie_history'


class UserMovieTag(models.Model):
    u = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    m = models.ForeignKey(Movie, models.DO_NOTHING, blank=True, null=True)
    t = models.ForeignKey(Tag, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_movie_tag'


class UserTagHistory(models.Model):
    u = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    t = models.ForeignKey(Tag, models.DO_NOTHING, blank=True, null=True)
    attr_id = models.IntegerField()
    attr_score = models.FloatField()

    class Meta:
        managed = False
        db_table = 'user_tag_history'

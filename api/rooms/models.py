from enum import Enum

from django.db import models

class Location(models.Model):
    state     = models.CharField(max_length=45)
    city      = models.CharField(max_length=45)
    dong      = models.CharField(max_length=45)
    detail    = models.CharField(max_length=100)
    dong_code = models.CharField(max_length=45)
    latitude  = models.DecimalField(max_digits=17, decimal_places=14)
    longitude = models.DecimalField(max_digits=17, decimal_places=14)
    utmk_x    = models.DecimalField(max_digits=18, decimal_places=10)
    utmk_y    = models.DecimalField(max_digits=18, decimal_places=10)

    class Meta:
        db_table = 'locations'

class RoomType(models.Model):
    class Enum(Enum):
        ONE_ROOM   = 1
        MULTI_ROOM = 2
        OFFICETEL  = 3

    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'room_types'

class TradeType(models.Model):
    class Enum(Enum):
        MONTHLY_RENT = 1
        DEPOSIT      = 2
        SALE         = 3

    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'trade_types'

class Room(models.Model):
    title          = models.CharField(max_length=100)
    content        = models.TextField()
    location       = models.ForeignKey(Location, on_delete=models.CASCADE)
    room_type      = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    trade_type     = models.ForeignKey(TradeType, on_delete=models.CASCADE)
    monthly_rent   = models.IntegerField(null=True)
    deposit        = models.IntegerField(null=True)
    sale           = models.IntegerField(null=True)
    agent          = models.CharField(max_length=45)
    floor          = models.IntegerField()
    room_area      = models.FloatField()
    room_count     = models.IntegerField()
    bathroom_count = models.IntegerField()
    heating_type   = models.CharField(max_length=45)
    elevator       = models.CharField(max_length=45)
    created_at     = models.DateTimeField(auto_now_add=True)
    option         = models.ManyToManyField('Option', through='RoomOption')

    class Meta:
        db_table = 'rooms'

class OptionType(models.Model):
    class Enum(Enum):
        NORMAL   = 1
        SECURITY = 2

    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'option_types'

class Option(models.Model):
    name        = models.CharField(max_length=45)
    image_url   = models.URLField()
    option_type = models.ForeignKey(OptionType, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'options'

class RoomOption(models.Model):
    room   = models.ForeignKey(Room, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'room_options'

class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    url  = models.URLField()
    
    class Meta:
        db_table = 'room_images'
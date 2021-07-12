
from rest_framework   import serializers
from api.rooms.models import Location, Option, Room, RoomImage

class RoomImageSerializer(serializers.ModelSerializer):
    class Meta: 
        model  = RoomImage
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer): 
    class Meta:
        model  = Location
        # fields = '__all__'
        fields = ["state", "city","dong","detail","dong_code","latitude","longitude","utmk_x","utmk_y"]
        # fields = ("state",)
class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Option
        fields = ['image_url', 'name']
    
class RoomSerializer(serializers.ModelSerializer):
    # location = serializers.SerializerMethodField()
    roomimage_set = RoomImageSerializer(many=True, read_only=True)
    location      = LocationSerializer(many=False)
    option        = OptionSerializer(many=True, read_only=True)

    class Meta: 
        model  = Room
        # fields = ["id", "title","content","monthly_rent","deposit", "sale","agent","floor","room_area","room_count","bathroom_count","heating_type", "elevator","room_type","trade_type","location","roomimage_set","option"]
        fields = '__all__'
    # def create(self, validated_data):
    #     locations = validated_data.pop("location")
    #     rooms = Room.objects.create(**validated_data)
    #     for location_data in locations:
    #             Location.objects.create(
    #                rooms=rooms, **location_data)
    #             return rooms    
    
    def create(self, validated_data):
        location = validated_data.pop('location')
        location_instance, created = Location.objects.get_or_create(state=location)
        room_instance = Room.objects.create(**validated_data, location=location_instance)
        return room_instance

    
    # for track_data in tracks_data:
    #         Track.objects.create(album=album, **track_data)
    #     return album
    # def create(self, validated_data):
    #     tracks_data = validated_data.pop('tracks')
    #     album = Album.objects.create(**validated_data)
    #     for track_data in tracks_data:
    #         Track.objects.create(album=album, **track_data)
    #     return album

        
        
        
        
    # class SessionSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model  = Session
    #     fields = ('title', 'description')
    # class SessionTypeSerializer(serializers.ModelSerializer):
    # sessions = SessionSerializer(source='session_set', many=True)
    # class Meta:
    #     model = SessionType
    #     fields = ('id', 'name', 'sessions')
    # def create(self, validated_data):
    #     sessions     = validated_data.pop("session_set")
    #     session_type = SessionType.objects.create(**validated_data)
    #     Session.objects.bulk_create([
    #         Session(
    #             title = session["title"],
    #             description = session["description"],
    #             session_type_id = session_type.id
    #         ) for session in sessions]
    #     )
    #     return session_type
    
    
    
    
    
   
    # def get_location(self, obj):
    #     return obj.location.state
      
    # def create(self, validated_data):
    #     location = validated_data.pop('location')
    #     rooms = Room.objects.create(**validated_data)
    #     for location_data in location:
    #         Location.objects.create(location=location_data, **validated_data)
    #         return rooms
            
  
      
  
  
     





    # class TradePostCreateSerializer(serializers.ModelSerializer):
    # basePost = PostCreateSerializer()
    # baseProductItem = ProductItemCreateSerializer()

    # class Meta:
    #     model = TradePost
    #     fields = ('basePost', 'baseProductItem',)

    # def create(self, validated_data):
    #     # pop out the dict to create post and item, depend on whether you want to create post or not
    #     post = validated_data.get('basePost')
    #     product = validated_data.get('baseProductItem')
    #     # create post first
    #     trade_post = None
    #     post_obj = Post.objects.create(**post)
    #     if post_obj:
    #         # create product item
    #         prod_item = ProductItem.objects.create(basePost=post_obj, **product)
    #         trade_post = TradePost.objects.create(baseProduct=prod_item, **validated_data)
    #     return trade_post    
        
        
    # def create(self, validated_data):
    #     locations_data = validated_data.pop('location')
    #     location = Location.objects.create(**validated_data)
    #     for location_data in locations_data:
    #         Location.objects.create(location=location, **validated_data)
    #         return location
        
        
        
        # fields = ('id', 'content', 'title')
        # exclude = ('location',)
        
    
from django.db.models.query import Prefetch
from django.http            import JsonResponse
from django.views           import View

from ..models import Room, Option

class RoomView(View):
    def get(self, request, room_id):

        try:
            room = Room.objects\
                .select_related('location','room_type','trade_type')\
                .prefetch_related(
                    'roomimage_set',
                    Prefetch(
                        'option', 
                        queryset = Option.objects.select_related('option_type').filter(option_type__id = 1),
                        to_attr='normal_options'
                    ),
                    Prefetch(
                        'option', 
                        queryset = Option.objects.select_related('option_type').filter(option_type__id = 2),
                        to_attr='security_options'
                    )
                )\
                .get(id=room_id)

            result = {
                'id'             : room.id,    
                'title'          : room.title,
                'content'        : room.content,
                'location'       : {
                    'id'       : room.location.id,
                    'state'    : room.location.state,
                    'city'     : room.location.city,
                    'dong'     : room.location.dong,
                    'detail'   : room.location.detail,
                    'latitude' : room.location.latitude,
                    'longitude': room.location.longitude,
                },
                'room_type'      : room.room_type.name,
                'trade_type'     : room.trade_type.name,
                'monthly_rent'   : room.monthly_rent,
                'deposit'        : room.deposit,
                'sale'           : room.sale,
                'agent'          : room.agent,
                'floor'          : room.floor,
                'room_area'      : room.room_area,
                'room_count'     : room.room_count,
                'bathroom_count' : room.bathroom_count,
                'heating_type'   : room.heating_type,
                'elevator'       : room.elevator,
                'created_at'     : room.created_at,
                'image'          : [image.url for image in room.roomimage_set.all()],
                'normal_option'  : [{
                    'name'       : option.name,
                    'image_url'  : option.image_url,
                    'option_type': option.option_type.name
                }for option in room.normal_options],
                'security_option': [{
                    'name'       : option.name,
                    'image_url'  : option.image_url,
                    'option_type': option.option_type.name
                }for option in room.security_options]
            }
            return JsonResponse({'message':result}, status =200)

        except Room.DoesNotExist:
            return JsonResponse({'message':'NOT FOUND'}, status =404)

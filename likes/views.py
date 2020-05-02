from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from .models import Like

User = get_user_model()

def add_like(obj, user):
    #Лайкает `obj`.
    obj_type = ContentType.objects.get_for_model(obj)
    like = Like.objects.get_or_create(
        content_type=obj_type, object_id=obj.id, user=user)
    return like

def dislike(obj, user):
    #Удаляет лайк с `obj`.
    obj_type = ContentType.objects.get_for_model(obj)
    Like.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user
    ).delete()

def get_liked(obj):
    #Получает всех пользователей, которые лайкнули `obj`.
    obj_type = ContentType.objects.get_for_model(obj)
    liked = User.objects.filter(
        likes__content_type=obj_type, likes__object_id=obj.id)
    return liked
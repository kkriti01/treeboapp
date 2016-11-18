import json
from django.http import HttpResponse, JsonResponse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


from .models import UserSubscription, Product


def subscribe(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id', None)
        print user_id
        product_id = request.POST.get('product_id', None)
        print product_id
        notification_interval = request.POST.get('when', None)
        print notification_interval
        if user_id and product_id and notification_interval:
            user = User.objects.get(id=user_id)
            product = Product.objects.get(id=product_id)
            usersubs_obj,created = UserSubscription.objects.get_or_create(product=product)
            usersubs_obj.notification_interval=notification_interval
            usersubs_obj.subscribe=True
            usersubs_obj.product.add(product)
            usersubs_obj.user.add(user)
            return HttpResponse("successfully subscribed")
        else:
            return HttpResponse("error in subscription")


def unsubscribe(request):
    if request.method == 'POST':
        user_id  = request.POST.get('user_id', None)
        product_id = request.POST.get('product_id', None)
        if user_id and product_id:
            user = User.objects.get(id=user_id)
            product = Product.objects.get(id=product_id)
            usersubs_obj = UserSubscription.objects.get(product=product)
            usersubs_obj.subscribe=False
            usersubs_obj.save()
            usersubs_obj.user.add(user)
            return HttpResponse("successfully unsubscribed")
    else:
            return HttpResponse("error in unsubscription")
    return HttpResponse("Post with required data")


def priceDataPoint(request):
    id = request.POST.get('product_id', None)
    new_price = request.POST.get('price')
    print "new_price %s" %new_price
    url = request.POST.get('url')
    if new_price and url:
        product = Product.objects.get(id=id)
        product.old_price = product.price
        product.price = new_price
        product.url = url
        product.save()
        return HttpResponse("succesfull updated  price")
    else:
        return HttpResponse("error in update")


@receiver(post_save, sender=Product)
def notify(sender,instance, created,**kwargs):
    if created == 'False':
        print "in notification"
        print instance
        subscription = UserSubscription.objects.get(product=instance)
        if instance.old_price > instance.new_price and subscription.notification_interval == 'ALWAYS':
            data ={
                'id': id,
                'price': instance.new_price,
                'url': instance.url,
                'when': 'ALWAYS'
            }

        elif ((instance.old_price-int(instance.new_price))/instance.old_price)*100.0 > 10/100 and subscription.notification_interval == 'MORE_THAN_10':
            data ={
                'id': id,
                'price': instance.new_price,
                'url': instance.url,
                'when': 'MORE_THAN_10'
            }
        else:
            data ={
                'id': id,
                'price': instance.new_price,
                'url': instance.url,
                'when': 'ALL_TIME_LOW'
            }
        print data
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        return HttpResponse("saved successfully")

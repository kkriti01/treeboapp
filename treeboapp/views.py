from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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
            print user
            product = Product.objects.get(id=product_id)
            print product
            usersubs_obj = UserSubscription.objects.create(notification_interval=notification_interval,subscribe = 'subscribe')

            usersubs_obj.product.add(product)

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
            usersubs_obj, created = UserSubscription.objects.get_or_create(
                                                                           subscribe='False',
                                                                           )

            usersubs_obj.save()
            usersubs_obj.product.add(product)
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
        product.price = new_price
        product.url = url
        subscription = UserSubscription.objects.filter(product=product)
        print product.price
        for data in subscription:
            if product.price < new_price and subscription.notification_interval == 'ALWAYS':
                data ={
                    'id': id,
                    'price': new_price,
                    'url': product.url,
                    'when': 'ALWAYS'
                }
            elif ((new_price-product.price)/product.price)*100.0 > 0.01 and subscription.notification_interval == 'MORE_THAN_10':
                data ={
                    'id': id,
                    'price': new_price,
                    'url': product.url,
                    'when': 'MORE_THAN_10'
                }
            else:
                data ={
                    'id': id,
                    'price': new_price,
                    'url': product.url,
                    'when': 'ALL_TIME_LOW'
                }
            return JsonResponse(data)

    else:
        return HttpResponse("error in update")



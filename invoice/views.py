from django.http import HttpRequest, JsonResponse
from invoice.models import *


def add_product_to_order(request: HttpRequest):
    product_id = int(request.GET.get('product_id'))
    count = int(request.GET.get('count'))
    if count < 1:
        return JsonResponse({
            'status': 'invalid_count'
        })
    if request.user.is_authenticated:
        product = Product.objects.filter(pk=product_id).first()
        if product is not None:
            current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
            current_order_detail = current_order.orderdetail_set.filter(product_id=product_id).first()

            if current_order_detail is not None:
                current_order_detail.count += int(count)
                current_order_detail.save()
            else:
                new_detail = OrderDetail(order_id=current_order.id, product_id=product_id,
                                         final_price=product.price * count, count=count)
                new_detail.save()
            return JsonResponse({
                'status': 'success'
            })

        else:
            return JsonResponse({
                'status': 'not_found'
            })
    else:
        return JsonResponse({
            'status': 'not_authenticated'
        })


def remove_from_cart(request: HttpRequest):
    product_id = int(request.GET.get('product_id'))

    cart_item = OrderDetail.objects.filter(product_id=product_id).first()
    print(cart_item)
    if cart_item.count > 1:
        cart_item.count -= 1
        cart_item.save()
    else:
        cart_item.delete()

    total_price = cart_item.final_price * int(cart_item.count)
    return JsonResponse({
        'final_price': total_price
    })


def add_from_cart(request: HttpRequest):
    product_id = int(request.GET.get('product_id'))
    cart_item = OrderDetail.objects.filter(product_id=product_id).first()
    print(cart_item)
    if cart_item.count >= 1:
        cart_item.count += 1
        cart_item.save()

    total_price = cart_item.final_price * int(cart_item.count)
    return JsonResponse({
        'final_price': total_price
    })
from django.contrib import messages
from django.shortcuts import redirect
from comment.models import ProductComment, Comment
from comment.forms import CommentForm, CommentProductForm


def product_comment(request, product_id):
    form = CommentProductForm(request.POST)
    if form.is_valid():
        ProductComment.objects.create(product_id=product_id, user=request.user, comment=form.cleaned_data['comment'],
                                      is_active=False)
        messages.success(request, 'نظر شما با موفقیت درمورد این محصول ثبت شد ')
        return redirect('main:index')
    else:
        messages.error(request, 'اطلاعات معتبر نمی باشد')
    return redirect('main:index')


def comment(request):
    form = CommentForm(request.POST)
    if form.is_valid():
        Comment.objects.create(comment=form.cleaned_data['comment'], user=request.user, is_active=False)
        messages.success(request, 'نظر شما با موفقیت درمورد  سایت ثبت شد ')
        return redirect('main:index')
    else:
        messages.error(request, 'اطلاعات معتبر نمی باشد')
        return redirect('main:index')

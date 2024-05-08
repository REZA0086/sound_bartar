from django.contrib import admin
from comment.models import ProductComment,Comment


def active_comment(modeladmin, request, queryset):
    res = queryset.update(is_active=True)
    message = f'تعداد {res} نظر فعال شد'
    modeladmin.message_user(request, message)


def de_active_comment(modeladmin, request, queryset):
    res = queryset.update(is_active=True)
    message = f'تعداد {res} نظر غیرفعال شد'
    modeladmin.message_user(request, message)


@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'comment', 'register_date', 'is_active')
    actions = [active_comment, de_active_comment]
    active_comment.short_description = 'فعال کردن نظرات انتخابی'
    de_active_comment.short_description = 'غیرفعال کردن نظرات انتخابی'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','comment')

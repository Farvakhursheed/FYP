from django.contrib import admin
from restaurant.models import Customer,Client,User,Restaurant, RestBranch, Category, RestCategory, RestCommentBox, RestTimetable,Item,ItemInDeal,ItemCommentBox,ItemSize,ItemCategory,ItemDiscount,PlatformDisCommentBox,Platform,Deal,DealCommentBox,DealDiscount, Discount, MCDiscount, MCDiscountCommentBox
from django.contrib.auth.models import Group

# Register your models here.
class MyAdminSite(admin.AdminSite):
    site_header = "Meal Catcher"
    site_title = "Meal Catcher"
    index_title = "Meal Catcher"

admin_site = MyAdminSite()
admin_site.register([User, Group])
admin_site.register([Restaurant, RestBranch,RestCategory,RestCommentBox,RestTimetable,Item,ItemInDeal,ItemCommentBox,ItemSize,ItemCategory,ItemDiscount,PlatformDisCommentBox,Platform,Deal,DealCommentBox,DealDiscount,Category,Discount,MCDiscount, MCDiscountCommentBox])
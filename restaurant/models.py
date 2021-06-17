from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_premium = models.BooleanField(null=True)
    phone = models.CharField(max_length=12)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=models.Manager()

class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=models.Manager()

    def __str__(self):
        return self.title

    class Meta:	
       verbose_name_plural = 'Categories'

class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)   
    #user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=models.Manager()

class Restaurant(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    logo = models.FileField(upload_to="restaurants/",null=True)	
    total_comments = models.IntegerField(default=0)
    good_comments = models.IntegerField(default=0)
    total_rating = models.FloatField(max_length=4, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=models.Manager()

    def __str__(self):
        return self.title

    def show_logo(self):
        return format_html('<img src="/static/%s" width="100" />' %
        self.logo)
    
    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Restaurants'

class RestCommentBox(models.Model):
    rest_id = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    item_Comment = models.TextField(max_length=2555)
    is_good = models.BooleanField(null=True)
    cust_id = models.ForeignKey(User,related_name="restcomment", on_delete=models.CASCADE)
    rating = models.TextField(max_length=100, null=True)
    objects=models.Manager()

    def __str__(self):
        return self.rest_id

    class Meta:
        verbose_name_plural = 'RestCommentBoxes'

class RestCategory(models.Model):
    rest_id = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    cat_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=models.Manager()

    def __str__(self):
        return self.rest_id

    class Meta:
        verbose_name_plural = 'RestCategories'

class RestBranch(models.Model):
    name = models.CharField(max_length=255)
    rid = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    location = models.CharField(max_length=255,default='')
    is_dine_in = models.BooleanField(null=True)
    is_take_away = models.BooleanField(null=True)
    is_delivery = models.BooleanField(null=True)
    number = models.CharField(max_length=20,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'RestBranches'

class Item(models.Model):
    item_name = models.CharField(max_length=255)
    branch_id = models.ForeignKey(RestBranch, on_delete=models.CASCADE)
    price = models.IntegerField(default='')
    disc_percent = models.CharField(max_length=5)
    total_comments = models.IntegerField(default=0)
    good_comments = models.IntegerField(default=0)
    total_rating = models.FloatField(max_length=4, default=0.0)
    logo = models.FileField(upload_to="items/",null=True)	
    is_any_discount = models.BooleanField(null=True)
    is_size = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=models.Manager()

    def __str__(self):
        return self.item_name

    def show_logo(self):
        return format_html('<img src="/static/%s" width="100" />' %
        self.logo)

    class Meta:
        verbose_name_plural = 'Items'

class ItemCommentBox(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_comment = models.TextField(max_length=2555)
    is_good = models.BooleanField(null=True)
    cust_id = models.ForeignKey(User,related_name="itemcomment", on_delete=models.CASCADE)
    rating = models.TextField(max_length=100, null=True)
    objects=models.Manager()

    def __str__(self):
        return self.item_id

    class Meta:
        verbose_name_plural = 'ItemCommentBoxes'


class ItemSize(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_size = models.CharField(max_length=15,default='') 
    price = models.IntegerField(default='')   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=models.Manager()

    def __str__(self):
        return self.item_id

    class Meta:
        verbose_name_plural = 'ItemSizes'

class ItemCategory(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=models.Manager()

    def __str__(self):
        return self.item_id

    class Meta:
        verbose_name_plural = 'ItemCategories'

class RestTimetable(models.Model):
    branch_id = models.ForeignKey(RestBranch, on_delete=models.CASCADE)
    day = models.CharField(max_length=255,default='')
    start_time = models.TimeField(default='')
    end_time = models.TimeField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=models.Manager()

    def __str__(self):
        return self.branch_id

    class Meta:
        verbose_name_plural = 'RestTimetables'

class Deal(models.Model):
    deal_name = models.CharField(max_length=255,default='')
    branch_id = models.ForeignKey(RestBranch, on_delete=models.CASCADE)
    price = models.IntegerField(default='')
    total_comments = models.IntegerField(default=0)
    good_comments = models.IntegerField( default=0)
    total_rating = models.FloatField(max_length=5.0, default=0.0)
    discount_price = models.IntegerField(default='')
    logo = models.FileField(upload_to="deals/",null=True)	
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=models.Manager()

    def __str__(self):
        return self.deal_name

    def show_logo(self):
        return format_html('<img src="/static/%s" width="100" />' %
        self.logo)

    class Meta:
        verbose_name_plural = 'Deals'

class DealCommentBox(models.Model):
    deal_id = models.ForeignKey(Deal, on_delete=models.CASCADE)
    item_comment = models.TextField(max_length=2555)
    is_good = models.BooleanField(null=True)
    cust_id = models.ForeignKey(User,related_name="dealcomment", on_delete=models.CASCADE)
    rating = models.TextField(max_length=100, null=True)
    objects=models.Manager()

    def __str__(self):
        return self.deal_id

    class Meta:
        verbose_name_plural = 'DealCommentBoxes'


class ItemInDeal(models.Model):
    deal_id = models.ForeignKey(Deal, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=models.Manager()

    def __str__(self):
        return self.deal_id

    class Meta:
        verbose_name_plural = 'ItemInDeals'

class Platform(models.Model):
    platform_name = models.CharField(max_length=255)
    logo = models.FileField(upload_to="platforms/",null=True)	
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=models.Manager()

    def __str__(self):
        return self.platform_name

    class Meta:
        verbose_name_plural = 'Platforms'

class PlatformDisCommentBox(models.Model):
    deal_id = models.ForeignKey(Deal, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    disc_comment = models.TextField(max_length=2555)
    is_good = models.BooleanField(null=True)
    cust_id = models.ForeignKey(User,related_name="platformcomment", on_delete=models.CASCADE)
    objects=models.Manager()

    def __str__(self):
        return self.deal_id

    class Meta:
        verbose_name_plural = 'PlatformDisCommentBoxes'

class Discount(models.Model):
    deal_id = models.ForeignKey(Deal, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    discription = models.TextField(max_length=255)
    dis_percent = models.CharField(max_length=255)
    platform_id = models.ForeignKey(Platform, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=models.Manager()

    def __str__(self):
        return self.deal_id

    class Meta:
        verbose_name_plural = 'Discounts'


class ItemDiscount(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    is_other_discount = models.BooleanField(null=True)
    is_mc_discount = models.BooleanField(null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=models.Manager()

    def __str__(self):
        return self.item_id

    class Meta:
        verbose_name_plural = 'ItemDiscounts'

class DealDiscount(models.Model):
    deal_id = models.ForeignKey(Deal, on_delete=models.CASCADE)
    is_other_discount = models.BooleanField(null=True)
    is_mc_discount = models.BooleanField(null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=models.Manager()
    
    def __str__(self):
        return self.item_id

    class Meta:
        verbose_name_plural = 'DealDiscounts'

class MCDiscount(models.Model):
    deal_id = models.ForeignKey(Deal, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    discription = models.TextField(max_length=255)
    dis_percent = models.CharField(max_length=255)
    is_available = models.BooleanField(null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=models.Manager()

    def __str__(self):
        return self.deal_id

    class Meta:
        verbose_name_plural = 'MealCatcherDiscounts'

class MCDiscountCommentBox(models.Model):
    deal_id = models.ForeignKey(Deal, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    disc_comment = models.TextField(max_length=2555)
    is_good = models.BooleanField(null=True)
    cust_id = models.ForeignKey(User,related_name="mcdiscom", on_delete=models.CASCADE)
    objects=models.Manager()

    def __str__(self):
        return self.item_id

    class Meta:
        verbose_name_plural = 'MealCatcherDiscountCommentBoxes'
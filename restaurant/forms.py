from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from restaurant.models import Client, User,Customer,Restaurant,Category,RestCategory,RestBranch,RestTimetable,Item,ItemCategory,ItemSize,ItemDiscount,Deal,DealDiscount,ItemInDeal,MCDiscount,Discount,Platform,MCDiscountCommentBox,RestCommentBox,ItemCommentBox,PlatformDisCommentBox,DealCommentBox

class ClientSignUpForm(UserCreationForm):
    email = forms.EmailField(
        widget = forms.EmailInput,
        required = True
    )
    phone = forms.CharField(
        widget = forms.TextInput,
        required = True
    )
    class Meta(UserCreationForm.Meta):
        model = User


    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_client = True
        if commit:
            user.save()
        return user

class CustomerSignUpForm(UserCreationForm):
    email = forms.EmailField(
        widget = forms.EmailInput,
        required = True
    )
    phone = forms.CharField(
        widget = forms.TextInput,
        required = True
    )
    is_premium = forms.BooleanField(
        widget = forms.CheckboxInput,
        required = True
    )
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        return user

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['title', 'logo','owner']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Restaurant Name"}),
            'logo': forms.FileInput(attrs={'class':'form-control'}),
            'owner': forms.Select(attrs={'class':'form-control'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Category Name"}),
        }

class RestCategoryForm(forms.ModelForm):
    class Meta:
        model = RestCategory
        fields = ['rest_id','cat_id']
        widgets = {
            'rest_id': forms.Select(attrs={'class':'form-control'}),
            'cat_id': forms.Select(attrs={'class':'form-control'}),
        }

class RestBranchForm(forms.ModelForm):
    class Meta:
        model = RestBranch
        fields = ['name', 'rid','location','is_dine_in', 'is_take_away','is_delivery','number']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Restaurant Branch Name"}),
            'rid': forms.Select(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Restaurant Location"}),
            'is_dine_in': forms.CheckboxInput(attrs={'class':'form-control'}),
            'is_take_away': forms.CheckboxInput(attrs={'class':'form-control'}),
            'is_delivery': forms.CheckboxInput(attrs={'class':'form-control'}),
            'number': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Number"})
        }

class RestTimetableForm(forms.ModelForm):
    class Meta:
        model = RestTimetable
        fields = ['branch_id','day','start_time','end_time']
        widgets = {
            'branch_id': forms.Select(attrs={'class':'form-control'}),
            'day': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Day"}),
            'start_time': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Time"}),
            'end_time': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Time"}),
        }

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'branch_id','price','disc_percent', 'logo','is_any_discount','is_size']
        widgets = {
            'item_name': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Item Name"}),
            'branch_id': forms.Select(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control','placeholder':"Enter item price"}),
            'logo': forms.FileInput(attrs={'class':'form-control'}),
            'disc_percent': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter discount in percentage "}),
            'is_any_discount': forms.CheckboxInput(attrs={'class':'form-control'}),
            'is_size': forms.CheckboxInput(attrs={'class':'form-control'}),
        }

class ItemCategoryForm(forms.ModelForm):
    class Meta:
        model = ItemCategory
        fields = ['item_id','cat_id']
        widgets = {
            'item_id': forms.Select(attrs={'class':'form-control'}),
            'cat_id': forms.Select(attrs={'class':'form-control'}),
        }

class ItemSizeForm(forms.ModelForm):
    class Meta:
        model = ItemSize
        fields = ['item_id','item_size','price']
        widgets = {
            'item_id': forms.Select(attrs={'class':'form-control'}),
            'item_size': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Item Size"}),
            'price': forms.NumberInput(attrs={'class':'form-control','placeholder':"Enter item price"}),
        }
        
class ItemDiscountForm(forms.ModelForm):
    class Meta:
        model = ItemDiscount
        fields = ['item_id','is_other_discount','is_mc_discount']
        widgets = {
            'item_id': forms.Select(attrs={'class':'form-control'}),
            'is_other_discount': forms.CheckboxInput(attrs={'class':'form-control'}),
            'is_mc_discount': forms.CheckboxInput(attrs={'class':'form-control'}),
        }

class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ['deal_name','branch_id','price','discount_price','logo']
        widgets = {
            'deal_name': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Deal Name"}),
            'branch_id': forms.Select(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control','placeholder':"Enter deal price"}),
            'discount_price': forms.NumberInput(attrs={'class':'form-control','placeholder':"Enter deal discounted price"}),
            'logo': forms.FileInput(attrs={'class':'form-control'}),
        }

class ItemInDealForm(forms.ModelForm):
    class Meta:
        model = ItemInDeal
        fields = ['deal_id','item_id']
        widgets = {
            'deal_id': forms.Select(attrs={'class':'form-control'}),
            'item_id': forms.Select(attrs={'class':'form-control'}),
        }

class DealDiscountForm(forms.ModelForm):
    class Meta:
        model = DealDiscount
        fields = ['deal_id','is_other_discount','is_mc_discount']
        widgets = {
            'deal_id': forms.Select(attrs={'class':'form-control'}),
            'is_other_discount': forms.CheckboxInput(attrs={'class':'form-control'}),
            'is_mc_discount': forms.CheckboxInput(attrs={'class':'form-control'}),
        }

class MCDiscountForm(forms.ModelForm):
    class Meta:
        model = MCDiscount
        fields = ['deal_id','item_id','discription','dis_percent','is_available']
        widgets = {
            'deal_id': forms.Select(attrs={'class':'form-control'}),
            'item_id': forms.Select(attrs={'class':'form-control'}),
            'discription': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Description"}),
            'dis_percent': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter '%' discount"}),
            'is_available': forms.CheckboxInput(attrs={'class':'form-control'}),
        }

class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = ['deal_id','item_id','discription','dis_percent','platform_id']
        widgets = {
            'deal_id': forms.Select(attrs={'class':'form-control'}),
            'item_id': forms.Select(attrs={'class':'form-control'}),
            'discription': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Description"}),
            'dis_percent': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter '%' discount"}),
            'platform_id': forms.Select(attrs={'class':'form-control'}),
        }

class PlatformForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = ['platform_name','logo']
        widgets = {
            'platform_name': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Platform Name"}),
            'logo': forms.FileInput(attrs={'class':'form-control'}),
        }

class RestCommentBoxForm(forms.ModelForm):
    class Meta:
        model = RestCommentBox
        fields = ['rest_id','item_Comment','is_good','cust_id']
        widgets = {
            'rest_id': forms.Select(attrs={'class':'form-control'}),
            'item_Comment': forms.Textarea(attrs={'class':'form-control'}),
            'is_good': forms.CheckboxInput(attrs={'class':'form-control',}),
            'cust_id': forms.Select(attrs={'class':'form-control'}),
        }

class ItemCommentBoxForm(forms.ModelForm):
    class Meta:
        model = ItemCommentBox
        fields = ['item_id','item_comment','is_good','cust_id']
        widgets = {
            'item_id': forms.Select(attrs={'class':'form-control'}),
            'item_comment': forms.Textarea(attrs={'class':'form-control'}),
            'is_good': forms.CheckboxInput(attrs={'class':'form-control',}),
            'cust_id': forms.Select(attrs={'class':'form-control'}),
        }

class DealCommentBoxForm(forms.ModelForm):
    class Meta:
        model = DealCommentBox
        fields = ['deal_id','item_comment','is_good','cust_id']
        widgets = {
            'deal_id': forms.Select(attrs={'class':'form-control'}),
            'item_comment': forms.Textarea(attrs={'class':'form-control'}),
            'is_good': forms.CheckboxInput(attrs={'class':'form-control',}),
            'cust_id': forms.Select(attrs={'class':'form-control'}),
        }

class PlatformDisCommentBoxForm(forms.ModelForm):
    class Meta:
        model = PlatformDisCommentBox
        fields = ['deal_id','item_id','disc_comment','is_good','cust_id']
        widgets = {
            'deal_id': forms.Select(attrs={'class':'form-control'}),
            'item_id': forms.Select(attrs={'class':'form-control'}),
            'disc_comment': forms.Textarea(attrs={'class':'form-control'}),
            'is_good': forms.CheckboxInput(attrs={'class':'form-control',}),
            'cust_id': forms.Select(attrs={'class':'form-control'}),
        }

class MCDiscountCommentBoxForm(forms.ModelForm):
    class Meta:
        model = MCDiscountCommentBox
        fields = ['deal_id','item_id','disc_comment','is_good','cust_id']
        widgets = {
            'deal_id': forms.Select(attrs={'class':'form-control'}),
            'item_id': forms.Select(attrs={'class':'form-control'}),
            'disc_comment': forms.Textarea(attrs={'class':'form-control'}),
            'is_good': forms.CheckboxInput(attrs={'class':'form-control',}),
            'cust_id': forms.Select(attrs={'class':'form-control'}),
        }
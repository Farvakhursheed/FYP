from django.shortcuts import render,redirect
from django.views.generic import CreateView,TemplateView, UpdateView, DeleteView
from restaurant.forms import CustomerSignUpForm,RestCommentBoxForm,ItemCommentBoxForm,DealCommentBoxForm,PlatformDisCommentBoxForm,MCDiscountCommentBoxForm,DealDiscountForm
from django.contrib.auth import login
from restaurant.models import User, Customer,RestCommentBox,Restaurant,Item,RestBranch,RestTimetable,ItemCommentBox,DealCommentBox,PlatformDisCommentBox,MCDiscountCommentBox,Deal,Platform,Discount, MCDiscount,DealDiscount
from django.contrib import messages
from django.utils.decorators import method_decorator
from ..decorators import customer_required
from django.contrib.auth.decorators import login_required
from ..ml import sentimental

class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('customers:home_content')

@method_decorator([login_required, customer_required], name='dispatch')
class DemoView(TemplateView):
    template_name = "restaurant/customers/home_content.html"

def restaurant(request):
    branch = RestBranch.objects.all()
    time = RestTimetable.objects.all()
    return render(request,"restaurant/customers/restaurant.html",{"branchmodel":branch,"timemodel":time})

#Restaurant Comment Box
def sentimental_analysis(request):
    if request.method == 'POST':
        form = RestCommentBoxForm(request.POST)
        analyse = sentimental()


@method_decorator([login_required, customer_required], name='dispatch')
class ShowRestCommentBox(TemplateView):
    template_name="restaurant/rest_comment_box_form.html"
    model = RestCommentBox
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list1"] = self.model.objects.all()
        return context


@method_decorator([login_required, customer_required], name='dispatch')
class AddRestCommentBox(CreateView):
    form_class = RestCommentBoxForm
    template_name = 'restaurant/customers/rest_comment_box.html'
    success_url = "/"

#item

def item(request):
    rest = Restaurant.objects.all()
    item = Item.objects.all()
    return render(request,"restaurant/customers/item.html",{"itemmodel":item,"restmodel":rest})


class ShowItemCommentBox(TemplateView):
    template_name = "restaurant/item_comment_box_form.html"
    model = ItemCommentBox
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = self.model.objects.all()
        return context

@method_decorator([login_required, customer_required], name='dispatch')
class AddItemCommentBox(CreateView):
    form_class = ItemCommentBoxForm
    template_name = 'restaurant/customers/item_comment_box.html'
    success_url = "/"

#deals

def deal(request):
    #rest = Restaurant.objects.all()
    deal = Deal.objects.all()
    return render(request,"restaurant/customers/deal.html",{"dealmodel":deal})


class ShowDealCommentBox(TemplateView):
    template_name = "restaurant/deal_comment_box_form.html"
    model = DealCommentBox
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = self.model.objects.all()
        return context

@method_decorator([login_required, customer_required], name='dispatch')
class AddDealCommentBox(CreateView):
    form_class = DealCommentBoxForm
    template_name = 'restaurant/customers/deal_comment_box.html'
    success_url = "/"

#platform

def platform(request):
    dis = Discount.objects.all()
    return render(request,"restaurant/customers/platform.html",{"dismodel":dis})


class ShowPlatformCommentBox(TemplateView):
    template_name = "restaurant/platform_comment_box_form.html"
    model = PlatformDisCommentBox
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = self.model.objects.all()
        return context


@method_decorator([login_required, customer_required], name='dispatch')
class AddPlatformCommentBox(CreateView):
    form_class = PlatformDisCommentBoxForm
    template_name = 'restaurant/customers/platform_comment_box.html'
    success_url = "/"

#MC

def mc(request):
    #rest = Restaurant.objects.all()
    mc = MCDiscount.objects.all()
    return render(request,"restaurant/customers/mc.html",{"mcmodel":mc})


class ShowMCDiscountCommentBox(TemplateView):
    template_name = "restaurant/mc_comment_box_form.html"
    model = MCDiscountCommentBox
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = self.model.objects.all()
        return context

@method_decorator([login_required, customer_required], name='dispatch')
class AddMCDiscountCommentBox(CreateView):
    form_class = MCDiscountCommentBoxForm
    template_name = 'restaurant/customers/mc_comment_box.html'
    success_url = "/"
from django.shortcuts import render,redirect
from django.views.generic import CreateView,TemplateView,CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from restaurant.forms import ClientSignUpForm,RestaurantForm,CategoryForm,RestCategoryForm,RestBranchForm,RestTimetableForm,ItemForm,ItemCategoryForm,ItemSizeForm,ItemDiscountForm,DealForm,ItemInDealForm,DealDiscountForm,MCDiscountForm,DiscountForm,PlatformForm
from django.utils.decorators import method_decorator
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy
from restaurant.models import Client, User,Restaurant,Category,RestCategory,RestBranch,RestTimetable,Item,ItemCategory,ItemSize,ItemDiscount,Deal,ItemInDeal,DealDiscount,MCDiscount,Discount,Platform
from ..decorators import client_required
from rest_framework import permissions


class ClientSignUpView(CreateView):
    model = User
    form_class = ClientSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'client'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('clients:home_content')

@method_decorator([login_required, client_required], name='dispatch')
class DemoView(TemplateView):
    template_name = "restaurant/clients/home_content.html"

@method_decorator([login_required, client_required], name='dispatch')
class CalendarView(TemplateView):
    template_name = "restaurant/clients/calendar.html"

#Restaurant

@method_decorator([login_required, client_required], name='dispatch')
class ShowRestaurant(TemplateView):
    template_name="restaurant/clients/restaurant.html"
    model = Restaurant
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = self.model.objects.all()
        return context

@method_decorator([login_required, client_required], name='dispatch')
class AddRestaurant(CreateView):
    form_class = RestaurantForm
    template_name = 'restaurant/restaurant_form.html'
    success_url = "/"

    def form_valid(self, form):
        files = self.request.FILES.getlist('logo')
        restaurant = form.save(commit=False)
        form.save()
       
        return super().form_valid(form)

@method_decorator([login_required, client_required], name='dispatch')
class EditRestaurant(UpdateView):
    form_class = RestaurantForm
    success_url = "/"

    def get_queryset(self):
        id = self.kwargs['pk']
        return Restaurant.objects.filter(pk=id)
    
    def form_valid(self, form):  
        files = self.request.FILES.getlist('logo')
        restaurant = form.save(commit=False)
        form.save()
        
        return super().form_valid(form)

@method_decorator([login_required, client_required], name='dispatch')
class DeleteRestaurant(DeleteView):
    model = Restaurant
    success_url = "/clients/restaurant"

#Restaurant Category

@method_decorator([login_required, client_required], name='dispatch')
class ShowCategory(TemplateView):
    template_name="restaurant/clients/category.html"
    model = Category
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = self.model.objects.all()
        return context

@method_decorator([login_required, client_required], name='dispatch')
class AddCategory(CreateView):
    form_class = CategoryForm
    template_name = 'restaurant/category_form.html'
    success_url = "/"

@method_decorator([login_required, client_required], name='dispatch')
class EditCategory(UpdateView):
    form_class = CategoryForm
    success_url = "/"

    def get_queryset(self):
        id = self.kwargs['pk']
        return Category.objects.filter(pk=id)

@method_decorator([login_required, client_required], name='dispatch')
class DeleteCategory(DeleteView):
    model = Category
    success_url = "/clients/category"

#restaurant_category

@method_decorator([login_required, client_required], name='dispatch')
class ShowRestCategory(TemplateView):
    template_name="restaurant/clients/restcategory.html"
    model = RestCategory
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = self.model.objects.all()
        return context

@method_decorator([login_required, client_required], name='dispatch')
class AddRestCategory(CreateView):
    form_class = RestCategoryForm
    template_name = 'restaurant/restcategory_form.html'
    success_url = "/"

@method_decorator([login_required, client_required], name='dispatch')
class EditRestCategory(UpdateView):
    form_class = RestCategoryForm
    success_url = "/"

    def get_queryset(self):
        id = self.kwargs['pk']
        return RestCategory.objects.filter(pk=id)

@method_decorator([login_required, client_required], name='dispatch')
class DeleteRestCategory(DeleteView):
    model = RestCategory
    success_url = "/clients/restcategory"

#restaurant_branch

@method_decorator([login_required, client_required], name='dispatch')
class ShowRestBranch(TemplateView):
    template_name="restaurant/clients/restbranch.html"
    model = RestBranch
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = self.model.objects.all()
        return context

@method_decorator([login_required, client_required], name='dispatch')
class AddRestBranch(CreateView):
    form_class = RestBranchForm
    template_name = 'restaurant/restbranch_form.html'
    success_url = "/"

@method_decorator([login_required, client_required], name='dispatch')
class EditRestBranch(UpdateView):
    form_class = RestBranchForm
    success_url = "/"

    def get_queryset(self):
        id = self.kwargs['pk']
        return RestBranch.objects.filter(pk=id)

@method_decorator([login_required, client_required], name='dispatch')
class DeleteRestBranch(DeleteView):
    model = RestBranch
    success_url = "/clients/restbranch"

#timetable

@method_decorator([login_required, client_required], name='dispatch')
class ShowTimetable(TemplateView):
    template_name="restaurant/clients/timetable.html"
    model = RestTimetable
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = self.model.objects.all()
        return context

@method_decorator([login_required, client_required], name='dispatch')
class AddTimetable(CreateView):
    form_class = RestTimetableForm
    template_name = 'restaurant/resttimetable_form.html'
    success_url = "/"

@method_decorator([login_required, client_required], name='dispatch')
class EditTimetable(UpdateView):
    form_class = RestTimetableForm
    success_url = "/"

    def get_queryset(self):
        id = self.kwargs['pk']
        return RestTimetable.objects.filter(pk=id)

@method_decorator([login_required, client_required], name='dispatch')
class DeleteTimetable(DeleteView):
    model = RestTimetable
    success_url = "/clients/timetable"

#item

@method_decorator([login_required, client_required], name='dispatch')
class ShowItem(TemplateView):
    template_name="restaurant/clients/item.html"
    model = Item
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = self.model.objects.all()
        return context

@method_decorator([login_required, client_required], name='dispatch')
class AddItem(CreateView):
    form_class = ItemForm
    template_name = 'restaurant/item_form.html'
    success_url = "/"

    def form_valid(self, form):
        files = self.request.FILES.getlist('logo')
        item = form.save(commit=False)
        form.save()
       
        return super().form_valid(form)

@method_decorator([login_required, client_required], name='dispatch')
class EditItem(UpdateView):
    form_class = ItemForm
    success_url = "/"

    def get_queryset(self):
        id = self.kwargs['pk']
        return Item.objects.filter(pk=id)

    def form_valid(self, form):  
        files = self.request.FILES.getlist('logo')
        item = form.save(commit=False)
        form.save()
        
        return super().form_valid(form)

@method_decorator([login_required, client_required], name='dispatch')
class DeleteItem(DeleteView):
    model = Item
    success_url = "/clients/item"

#item Category

@method_decorator([login_required, client_required], name='dispatch')
class ShowItemCategory(TemplateView):
    template_name="restaurant/clients/itemcategory.html"
    model = ItemCategory
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = self.model.objects.all()
        return context

@method_decorator([login_required, client_required], name='dispatch')
class AddItemCategory(CreateView):
    form_class = ItemCategoryForm
    template_name = 'restaurant/itemcategory_form.html'
    success_url = "/"

@method_decorator([login_required, client_required], name='dispatch')
class EditItemCategory(UpdateView):
    form_class = ItemCategoryForm
    success_url = "/"

    def get_queryset(self):
        id = self.kwargs['pk']
        return ItemCategory.objects.filter(pk=id)

@method_decorator([login_required, client_required], name='dispatch')
class DeleteItemCategory(DeleteView):
    model = ItemCategory
    success_url = "/clients/itemcategory"

#item Size

@method_decorator([login_required, client_required], name='dispatch')
class ShowItemSize(TemplateView):
    template_name="restaurant/clients/itemsize.html"
    model = ItemSize
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = self.model.objects.all()
        return context

@method_decorator([login_required, client_required], name='dispatch')
class AddItemSize(CreateView):
    form_class = ItemSizeForm
    template_name = 'restaurant/itemsize_form.html'
    success_url = "/"

@method_decorator([login_required, client_required], name='dispatch')
class EditItemSize(UpdateView):
    form_class = ItemSizeForm
    success_url = "/"

    def get_queryset(self):
        id = self.kwargs['pk']
        return ItemSize.objects.filter(pk=id)

@method_decorator([login_required, client_required], name='dispatch')
class DeleteItemSize(DeleteView):
    model = ItemSize
    success_url = "/clients/itemsize"

#item Discount

@method_decorator([login_required, client_required], name='dispatch')
class ShowItemDiscount(TemplateView):
    template_name="restaurant/clients/itemdiscount.html"
    model = ItemDiscount
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = self.model.objects.all()
        return context

@method_decorator([login_required, client_required], name='dispatch')
class AddItemDiscount(CreateView):
    form_class = ItemDiscountForm
    template_name = 'restaurant/itemdiscount_form.html'
    success_url = "/"

@method_decorator([login_required, client_required], name='dispatch')
class EditItemDiscount(UpdateView):
    form_class = ItemDiscountForm
    success_url = "/"

    def get_queryset(self):
        id = self.kwargs['pk']
        return ItemDiscount.objects.filter(pk=id)

@method_decorator([login_required, client_required], name='dispatch')
class DeleteItemDiscount(DeleteView):
    model = ItemDiscount
    success_url = "/clients/itemdiscount"

#Deal

@method_decorator([login_required, client_required], name='dispatch')
class ShowDeal(TemplateView):
    template_name="restaurant/clients/deal.html"
    model = Deal
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = self.model.objects.all()
        return context

@method_decorator([login_required, client_required], name='dispatch')
class AddDeal(CreateView):
    form_class = DealForm
    template_name = 'restaurant/deal_form.html'
    success_url = "/"

    def form_valid(self, form):
        files = self.request.FILES.getlist('logo')
        deal = form.save(commit=False)
        form.save()
       
        return super().form_valid(form)

@method_decorator([login_required, client_required], name='dispatch')
class EditDeal(UpdateView):
    form_class = DealForm
    success_url = "/"

    def get_queryset(self):
        id = self.kwargs['pk']
        return Deal.objects.filter(pk=id)

    def form_valid(self, form):  
        files = self.request.FILES.getlist('logo')
        deal = form.save(commit=False)
        form.save()
        
        return super().form_valid(form)

@method_decorator([login_required, client_required], name='dispatch')
class DeleteDeal(DeleteView):
    model = Deal
    success_url = "/clients/deal"

#Discount

@method_decorator([login_required, client_required], name='dispatch')
class ShowDiscount(TemplateView):
    template_name="restaurant/clients/discount.html"
    model = Discount
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = self.model.objects.all()
        return context

@method_decorator([login_required, client_required], name='dispatch')
class AddDiscount(CreateView):
    form_class = DiscountForm
    template_name = 'restaurant/discount_form.html'
    success_url = "/"


@method_decorator([login_required, client_required], name='dispatch')
class EditDiscount(UpdateView):
    form_class = DiscountForm
    success_url = "/"

    def get_queryset(self):
        id = self.kwargs['pk']
        return Discount.objects.filter(pk=id)


@method_decorator([login_required, client_required], name='dispatch')
class DeleteDiscount(DeleteView):
    model = Discount
    success_url = "/clients/discount"

#Deal Discount

@method_decorator([login_required, client_required], name='dispatch')
class ShowDealDiscount(TemplateView):
    template_name="restaurant/clients/dealdiscount.html"
    model = DealDiscount
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = self.model.objects.all()
        return context

@method_decorator([login_required, client_required], name='dispatch')
class AddDealDiscount(CreateView):
    form_class = DealDiscountForm
    template_name = 'restaurant/dealdiscount_form.html'
    success_url = "/"


@method_decorator([login_required, client_required], name='dispatch')
class EditDealDiscount(UpdateView):
    form_class = DealDiscountForm
    success_url = "/"

    def get_queryset(self):
        id = self.kwargs['pk']
        return DealDiscount.objects.filter(pk=id)


@method_decorator([login_required, client_required], name='dispatch')
class DeleteDealDiscount(DeleteView):
    model = DealDiscount
    success_url = "/clients/dealdiscount"

#Item In Deal

@method_decorator([login_required, client_required], name='dispatch')
class ShowItemInDeal(TemplateView):
    template_name="restaurant/clients/itemindeal.html"
    model = ItemInDeal
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = self.model.objects.all()
        return context

@method_decorator([login_required, client_required], name='dispatch')
class AddItemInDeal(CreateView):
    form_class = ItemInDealForm
    template_name = 'restaurant/itemindeal_form.html'
    success_url = "/"


@method_decorator([login_required, client_required], name='dispatch')
class EditItemInDeal(UpdateView):
    form_class = ItemInDealForm
    success_url = "/"

    def get_queryset(self):
        id = self.kwargs['pk']
        return ItemInDeal.objects.filter(pk=id)


@method_decorator([login_required, client_required], name='dispatch')
class DeleteItemInDeal(DeleteView):
    model = ItemInDeal
    success_url = "/clients/itemindeal"

#MC Discount

@method_decorator([login_required, client_required], name='dispatch')
class ShowMCDiscount(TemplateView):
    template_name="restaurant/clients/mcdiscount.html"
    model = MCDiscount
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = self.model.objects.all()
        return context

@method_decorator([login_required, client_required], name='dispatch')
class AddMCDiscount(CreateView):
    form_class = MCDiscountForm
    template_name = 'restaurant/mcdiscount_form.html'
    success_url = "/"


@method_decorator([login_required, client_required], name='dispatch')
class EditMCDiscount(UpdateView):
    form_class = MCDiscountForm
    success_url = "/"

    def get_queryset(self):
        id = self.kwargs['pk']
        return MCDiscount.objects.filter(pk=id)


@method_decorator([login_required, client_required], name='dispatch')
class DeleteMCDiscount(DeleteView):
    model = MCDiscount
    success_url = "/clients/mcdiscount"

#Platform

@method_decorator([login_required, client_required], name='dispatch')
class ShowPlatform(TemplateView):
    template_name="restaurant/clients/platform.html"
    model = Platform
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = self.model.objects.all()
        return context

@method_decorator([login_required, client_required], name='dispatch')
class AddPlatform(CreateView):
    form_class = PlatformForm
    template_name = 'restaurant/platform_form.html'
    success_url = "/"

    def form_valid(self, form):
        files = self.request.FILES.getlist('logo')
        platform = form.save(commit=False)
        form.save()
       
        return super().form_valid(form)

@method_decorator([login_required, client_required], name='dispatch')
class EditPlatform(UpdateView):
    form_class = PlatformForm
    success_url = "/"

    def get_queryset(self):
        id = self.kwargs['pk']
        return Platform.objects.filter(pk=id)

    def form_valid(self, form):  
        files = self.request.FILES.getlist('logo')
        platform = form.save(commit=False)
        form.save()
        
        return super().form_valid(form)

@method_decorator([login_required, client_required], name='dispatch')
class DeletePlatform(DeleteView):
    model = Platform
    success_url = "/clients/platform"

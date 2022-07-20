from django.shortcuts import render,redirect
from django.views.generic import CreateView,TemplateView, UpdateView, DeleteView
from restaurant.forms import CustomerSignUpForm,RestCommentBoxForm,ItemCommentBoxForm,DealCommentBoxForm,PlatformDisCommentBoxForm,MCDiscountCommentBoxForm,DealDiscountForm
from django.contrib.auth import login
from restaurant.models import User, Customer,RestCommentBox,Restaurant,Item,RestBranch,RestTimetable,ItemCommentBox,DealCommentBox,PlatformDisCommentBox,MCDiscountCommentBox,Deal,Platform,Discount, MCDiscount,DealDiscount
from django.contrib import messages
from django.utils.decorators import method_decorator
from ..decorators import customer_required
from django.contrib.auth.decorators import login_required


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
    rest = Restaurant.objects.all()
    comments = RestCommentBox.objects.all()
    return render(request,"restaurant/customers/restaurant.html",{"restmodel":rest, "comments": comments, 'total_comments':0})

def search(request):
    if(request.method == 'POST'):
        getData = Restaurant.objects.filter(title = request.POST.get('search'))
        return render(request,'restaurant/customers/restaurant.html',{'restmodel': getData})
      
    getData = Restaurant.objects.all()
    return render(request,'restaurant/customers/restaurant.html',{'restmodel': getData})
=======
#Restaurant Comment Box
#def sentimental_analysis(request):
#    if request.method == 'POST':
#        form = RestCommentBoxForm(request.POST)
#        analyse = sentimental()



@method_decorator([login_required, customer_required], name='dispatch')
class ShowRestCommentBox(TemplateView):
    template_name="restaurant/rest_comment_box_form.html"
    model = RestCommentBox
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list1"] = self.model.objects.all()
        return context



#item

def item(request):
    rest = Restaurant.objects.all()
    item = Item.objects.all()
    return render(request,"restaurant/customers/item.html",{"itemmodel":item,"restmodel":rest})


# class ShowItemCommentBox(TemplateView):
#     template_name = "restaurant/item_comment_box_form.html"
#     model = ItemCommentBox
    
#     def get_context_data(self,*args, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["object_list"] = self.model.objects.all()
#         return context

# @method_decorator([login_required, customer_required], name='dispatch')
# class AddItemCommentBox(CreateView):
#     form_class = ItemCommentBoxForm
#     template_name = 'restaurant/customers/item_comment_box.html'
#     success_url = "/"


#deals

def deal(request):
    deal = Deal.objects.all()
    return render(request,"restaurant/customers/deal.html",{"dealmodel":deal})


# class ShowDealCommentBox(TemplateView):
#     template_name = "restaurant/deal_comment_box_form.html"
#     model = DealCommentBox
    
#     def get_context_data(self,*args, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["object_list"] = self.model.objects.all()
#         return context

# @method_decorator([login_required, customer_required], name='dispatch')
# class AddDealCommentBox(CreateView):
#     form_class = DealCommentBoxForm
#     template_name = 'restaurant/customers/deal_comment_box.html'
#     success_url = "/"

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


def view_branches(request):
    rec = RestBranch.objects.filter(rid_id=request.GET.get('id'))
    return render(request,'restaurant/customers/view_branches.html',{'rec':rec, 'id': request.GET.get('id')})

def view_branche_details(request):
    item_rec = Item.objects.filter(branch_id_id=request.GET.get('id'))
    deal_rec = Deal.objects.filter(branch_id_id=request.GET.get('id'))
    time_rec = RestTimetable.objects.filter(branch_id_id=request.GET.get('id'))
    return render(request,'restaurant/customers/view_details.html',{'item_rec':item_rec, 'deal_rec': deal_rec, 'time_rec':time_rec})

def view_comments(request):
    if( request.GET.get('method')=='item_comments' and request.GET.get('id') ):
        item_comment = ItemCommentBox.objects.filter(item_id_id=request.GET.get('id'))
        return render(request,'restaurant/customers/view_comments_items.html',{'comment':item_comment,'id':request.GET.get('id')})

    if( request.GET.get('method')=='restaurant_comments' and request.GET.get('id') ):
        restaurant_comment = RestCommentBox.objects.filter(rest_id_id=request.GET.get('id'))
        return render(request,'restaurant/customers/view_comments.html',{'comment':restaurant_comment, 'id':request.GET.get('id')})

    deal_comment = DealCommentBox.objects.filter(deal_id_id=request.GET.get('id'))
    return render(request,'restaurant/customers/view_comments_deals.html',{'comment': deal_comment, 'id':request.GET.get('id')})

def AddRestCommentBox(request):
    if(request.method == 'POST'):
        
        rest = Restaurant.objects.get(id= request.POST['id'])
        temp = request.POST['item_Comment']

        d = str(temp)
        d = d.lower()
        dt = d.split()
        dt = [item.replace(".", "").replace("/", " ").replace("!", " ").replace("(", " ").replace(")", " ").replace('?', ' ').replace('"', ' ').replace('name', ' ').replace('dtype', ' ').replace('\\n', ' ').replace('float64', ' ').replace('!', ' ').replace('[', ' ').replace(']', ' ').replace(',', ' ').replace(':', ' ').replace('series', ' ')for item in dt]
        d = " "
        d = d.join(dt)
        dt = d.split()
        score = {'very':1,'fantastic': 1, 'great': 1, 'enjoy': 1, 'thank': 1, 'superb':1, 'wonderful':1, 'comfortable':1, 'best':1, 'beautiful':1, 'surprising':1, 'relaxing': 1, 'impressed': 1, 'extraordinary': 1, 'excellent':1, 'tasty':1, 'mazay':1, 'appetising':1, 'delicious': 1, 'behtreen':1, 'nice':1, 'acha':1, 'bad':-1, 'unpleasant':-1, 'worst':-1, 'good':1, 'bura':-1, 'gnda':-1, 'dislike': -1, 'dont':-1, 'not':-1, 'bakwas':-1, 'ghatiya':-1, 'fazool':-1, 'farig':-1, 'wahiyaat':-1, 'tasteless':-1, 'guzara':-1}
        points = 0
        t_comments = 0
        g_comments = 0
        for d in dt:
            for key in list(score.keys()):
                if d.startswith(key):
                    points = score[key] + points
        if(points<0):
            is_good = False
            t_comments = rest.total_comments + 1
            g_comments = rest.good_comments
        else:
            is_good = True
            g_comments = rest.good_comments + 1
            t_comments = rest.total_comments + 1
        
        
        rest.total_comments = t_comments 
        rest.good_comments = g_comments
        rest.total_rating = (float(g_comments)/float(t_comments))*5.0
        rest.save()

        data = RestCommentBox(
            item_Comment = request.POST['item_Comment'],
            is_good = is_good,
            rest_id = Restaurant.objects.get(id= request.POST['id']),
            cust_id = User.objects.get(id=request.user.id),
            rating = points
        )
        data.save()
        restaurant_comment = RestCommentBox.objects.filter(rest_id_id=request.POST['id'])
        return render(request,'restaurant/customers/view_comments.html',{'comment':restaurant_comment,'id': request.POST['id']})
    return render(request,'restaurant/customers/rest_comment_box.html')

def pass_id(request):
    return render(request,'restaurant/customers/rest_comment_box.html',{'id': request.GET.get('id')})

def pass_id_deal_items(request):
    if(request.GET.get('method')=='add_deal_comments'):
        return render(request,'restaurant/customers/add_comments_deal.html',{'id': request.GET.get('id')})
    return render(request,'restaurant/customers/add_comments_items.html',{'id': request.GET.get('id')})

def AddItemCommentBox(request):
    if(request.method == 'POST'):
        
        temp = request.POST['item_Comment']
        temp2 = Item.objects.get(id= request.POST['id'])
        d = str(temp)
        d = d.lower()
        dt = d.split()
        dt = [item.replace(".", "").replace("/", " ").replace("!", " ").replace("(", " ").replace(")", " ").replace('?', ' ').replace('"', ' ').replace('name', ' ').replace('dtype', ' ').replace('\\n', ' ').replace('float64', ' ').replace('!', ' ').replace('[', ' ').replace(']', ' ').replace(',', ' ').replace(':', ' ').replace('series', ' ')for item in dt]
        d = " "
        d = d.join(dt)
        dt = d.split()
        score = {'very':1,'fantastic': 1, 'great': 1, 'enjoy': 1, 'thank': 1, 'superb':1, 'wonderful':1, 'comfortable':1, 'best':1, 'beautiful':1, 'surprising':1, 'relaxing': 1, 'impressed': 1, 'extraordinary': 1, 'excellent':1, 'tasty':1, 'mazay':1, 'appetising':1, 'delicious': 1, 'behtreen':1, 'nice':1, 'acha':1, 'bad':-1, 'unpleasant':-1, 'worst':-1, 'good':1, 'bura':-1, 'gnda':-1, 'dislike': -1, 'dont':-1, 'not':-1, 'bakwas':-1, 'ghatiya':-1, 'fazool':-1, 'farig':-1, 'wahiyaat':-1, 'tasteless':-1, 'guzara':-1}
        points = 0
        t_comments = 0
        g_comments = 0
        for d in dt:
            for key in list(score.keys()):
                if d.startswith(key):
                    points = score[key] + points
        if(points<0):
            is_good = False
            t_comments = temp2.total_comments + 1
            g_comments = temp2.good_comments
        else:
            is_good = True
            g_comments = temp2.good_comments + 1
            t_comments = temp2.total_comments + 1
        
        
        temp2.total_comments = t_comments 
        temp2.good_comments = g_comments
        temp2.total_rating = (float(g_comments)/float(t_comments))*5.0
        temp2.save()
        
        data = ItemCommentBox(
            item_comment = request.POST['item_Comment'],
            is_good = is_good,
            item_id_id = request.POST['id'],
            cust_id = User.objects.get(id=request.user.id),
            rating = points,
        )
        data.save()
        restaurant_comment = ItemCommentBox.objects.filter(item_id_id=request.POST['id'])
        return render(request,'restaurant/customers/view_comments_items.html',{'comment':restaurant_comment,'id': request.POST['id']})
    return render(request,'restaurant/customers/view_comments_items.html')


def AddDealCommentBox(request):
    if(request.method == 'POST'):
        
        temp = request.POST['item_Comment']
        temp2 = Deal.objects.get(id= request.POST['id'])
        d = str(temp)
        d = d.lower()
        dt = d.split()
        dt = [item.replace(".", "").replace("/", " ").replace("!", " ").replace("(", " ").replace(")", " ").replace('?', ' ').replace('"', ' ').replace('name', ' ').replace('dtype', ' ').replace('\\n', ' ').replace('float64', ' ').replace('!', ' ').replace('[', ' ').replace(']', ' ').replace(',', ' ').replace(':', ' ').replace('series', ' ')for item in dt]
        d = " "
        d = d.join(dt)
        dt = d.split()
        score = {'very':1,'fantastic': 1, 'great': 1, 'enjoy': 1, 'thank': 1, 'superb':1, 'wonderful':1, 'comfortable':1, 'best':1, 'beautiful':1, 'surprising':1, 'relaxing': 1, 'impressed': 1, 'extraordinary': 1, 'excellent':1, 'tasty':1, 'mazay':1, 'appetising':1, 'delicious': 1, 'behtreen':1, 'nice':1, 'acha':1, 'bad':-1, 'unpleasant':-1, 'worst':-1, 'good':1, 'bura':-1, 'gnda':-1, 'dislike': -1, 'dont':-1, 'not':-1, 'bakwas':-1, 'ghatiya':-1, 'fazool':-1, 'farig':-1, 'wahiyaat':-1, 'tasteless':-1, 'guzara':-1}
        points = 0
        t_comments = 0
        g_comments = 0
        for d in dt:
            for key in list(score.keys()):
                if d.startswith(key):
                    points = score[key] + points
        if(points<0):
            is_good = False
            t_comments = temp2.total_comments + 1
            g_comments = temp2.good_comments
        else:
            is_good = True
            g_comments = temp2.good_comments + 1
            t_comments = temp2.total_comments + 1
        
        
        temp2.total_comments = t_comments 
        temp2.good_comments = g_comments
        temp2.total_rating = (float(g_comments)/float(t_comments))*5.0
        temp2.save()

        data = DealCommentBox(
            item_comment = request.POST['item_Comment'],
            is_good = is_good, 
            deal_id_id = request.POST['id'],
            cust_id_id = request.user.id,
            rating = points,
        )
        data.save()
        restaurant_comment = DealCommentBox.objects.filter(deal_id_id=request.POST['id'])
        return render(request,'restaurant/customers/view_comments_items.html',{'comment':restaurant_comment,'id': request.POST['id']})
    return render(request,'restaurant/customers/view_comments_items.html')

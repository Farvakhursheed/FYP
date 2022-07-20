from django.urls import include, path
from restaurant.views import restaurant,clients,customers

urlpatterns = [
    path('', restaurant.home, name='home'),
    #path('restaurant/', customers.RestaurantView.as_view(), name='restaurant'),

    path('customers/restaurant/pass_id/', customers.pass_id),

    path('customers/restaurant/comments/', customers.view_comments),

    path('customers/restaurant/comments/add_comments/' ,customers.pass_id),

    path('customers/restaurant/comments/add_comments_item/' ,customers.pass_id_deal_items),

    path('customers/restaurant/comments/add_comments_deal/' ,customers.pass_id_deal_items),

    path('clients/', include(([
        path('', clients.DemoView.as_view(), name='home_content'),
        path('calendar/', clients.CalendarView.as_view(), name='calender'),


        path('restaurant/', clients.ShowRestaurant.as_view(), name='restaurant'),
        path('restaurant/add/', clients.AddRestaurant.as_view(), name='restaurant.add'),
        path('restaurant/edit/<int:pk>/', clients.EditRestaurant.as_view(), name='restaurant.edit'),
        path('restaurant/delete/<int:pk>/',clients.DeleteRestaurant.as_view(),name="restaurant.delete"),
        
        path('category/', clients.ShowCategory.as_view(), name='category'),
        path('category/add/', clients.AddCategory.as_view(), name='category.add'),
        path('category/edit/<int:pk>/', clients.EditCategory.as_view(), name='category.edit'),
        path('category/delete/<int:pk>/',clients.DeleteCategory.as_view(),name="category.delete"),
        
        path('restaurant_category/', clients.ShowRestCategory.as_view(), name='restaurant_category'),
        path('restaurant_category/add/', clients.AddRestCategory.as_view(), name='restaurant_category.add'),
        path('restaurant_category/edit/<int:pk>/', clients.EditRestCategory.as_view(), name='restaurant_category.edit'),
        path('restaurant_category/delete/<int:pk>/',clients.DeleteRestCategory.as_view(),name="restaurant_category.delete"),
        
        path('restaurant_branch/', clients.ShowRestBranch.as_view(), name='restaurant_branch'),
        path('restaurant_branch/add/', clients.AddRestBranch.as_view(), name='restaurant_branch.add'),
        path('restaurant_branch/edit/<int:pk>/', clients.EditRestBranch.as_view(), name='restaurant_branch.edit'),
        path('restaurant_branch/delete/<int:pk>/',clients.DeleteRestBranch.as_view(),name="restaurant_branch.delete"),
        
        path('timetable/', clients.ShowTimetable.as_view(), name='timetable'),
        path('timetable/add/', clients.AddTimetable.as_view(), name='timetable.add'),
        path('timetable/edit/<int:pk>/', clients.EditTimetable.as_view(), name='timetable.edit'),
        path('timetable/delete/<int:pk>/',clients.DeleteTimetable.as_view(),name="timetable.delete"),
        
        path('item/', clients.ShowItem.as_view(), name='item'),
        path('item/add/', clients.AddItem.as_view(), name='item.add'),
        path('item/edit/<int:pk>/', clients.EditItem.as_view(), name='item.edit'),
        path('item/delete/<int:pk>/',clients.DeleteItem.as_view(),name="item.delete"),
        
        path('item_category/', clients.ShowItemCategory.as_view(), name='item_category'),
        path('item_category/add/', clients.AddItemCategory.as_view(), name='item_category.add'),
        path('item_category/edit/<int:pk>/', clients.EditItemCategory.as_view(), name='item_category.edit'),
        path('item_category/delete/<int:pk>/',clients.DeleteItemCategory.as_view(),name="item_category.delete"),
        
        path('item_size/', clients.ShowItemSize.as_view(), name='item_size'),
        path('item_size/add/', clients.AddItemSize.as_view(), name='item_size.add'),
        path('item_size/edit/<int:pk>/', clients.EditItemSize.as_view(), name='item_size.edit'),
        path('item_size/delete/<int:pk>/',clients.DeleteItemSize.as_view(),name="item_size.delete"),
        
        path('item_discount/', clients.ShowItemDiscount.as_view(), name='item_discount'),
        path('item_discount/add/', clients.AddItemDiscount.as_view(), name='item_discount.add'),
        path('item_discount/edit/<int:pk>/', clients.EditItemDiscount.as_view(), name='item_discount.edit'),
        path('item_discount/delete/<int:pk>/',clients.DeleteItemDiscount.as_view(),name="item_discount.delete"),
        
        path('mc_discount/', clients.ShowMCDiscount.as_view(), name='mc_discount'),
        path('mc_discount/add/', clients.AddMCDiscount.as_view(), name='mc_discount.add'),
        path('mc_discount/edit/<int:pk>/', clients.EditMCDiscount.as_view(), name='mc_discount.edit'),
        path('mc_discount/delete/<int:pk>/',clients.DeleteMCDiscount.as_view(),name="mc_discount.delete"),
        
        path('dealdiscount/', clients.ShowDealDiscount.as_view(), name='deal_discount'),
        path('dealdiscount/add/', clients.AddDealDiscount.as_view(), name='deal_discount.add'),
        path('dealdiscount/edit/<int:pk>/', clients.EditDealDiscount.as_view(), name='deal_discount.edit'),
        path('dealdiscount/delete/<int:pk>/',clients.DeleteDealDiscount.as_view(),name="deal_discount.delete"),
        
        path('deal/', clients.ShowDeal.as_view(), name='deal'),
        path('deal/add/', clients.AddDeal.as_view(), name='deal.add'),
        path('deal/edit/<int:pk>/', clients.EditDeal.as_view(), name='deal.edit'),
        path('deal/delete/<int:pk>/',clients.DeleteDeal.as_view(),name="deal.delete"),
        
        path('item_in_deal/', clients.ShowItemInDeal.as_view(), name='item_in_deal'),
        path('item_in_deal/add/', clients.AddItemInDeal.as_view(), name='item_in_deal.add'),
        path('item_in_deal/edit/<int:pk>/', clients.EditItemInDeal.as_view(), name='item_in_deal.edit'),
        path('item_in_deal/delete/<int:pk>/',clients.DeleteItemInDeal.as_view(),name="item_in_deal.delete"),
        
        path('discount/', clients.ShowDiscount.as_view(), name='discount'),
        path('discount/add/', clients.AddDiscount.as_view(), name='discount.add'),
        path('discount/edit/<int:pk>/', clients.EditDiscount.as_view(), name='discount.edit'),
        path('discount/delete/<int:pk>/',clients.DeleteDiscount.as_view(),name="discount.delete"),
        
        path('platform/', clients.ShowPlatform.as_view(), name='platform'),
        path('platform/add/', clients.AddPlatform.as_view(), name='platform.add'),
        path('platform/edit/<int:pk>/', clients.EditPlatform.as_view(), name='platform.edit'),
        path('platform/delete/<int:pk>/',clients.DeletePlatform.as_view(),name="platform.delete"),
        
    ], 'restaurant'), namespace='clients')),

    path('customers/', include(([
        path('', customers.DemoView.as_view(), name='home_content'),
        path('restaurant/',customers.restaurant, name="restaurant"),
        path('item/',customers.item, name="item"),
        path('deal/',customers.deal, name="deal"),
        path('platform/',customers.platform, name="platform"),
        path('mc/',customers.mc,name="meal_catcher"),
        path('restaurant/search/',customers.search,name="search"),
        #path('restaurant/view/',customers.view, name="view"),
        path('restaurant/view', customers.view_branches),
        path('restaurant/details', customers.view_branche_details),


        path('restaurant/restaurant_comment/', customers.ShowRestCommentBox.as_view(), name='rest_comment_box'),
        path('restaurant/restaurant_comment/add/', customers.AddRestCommentBox ),

        path('restaurant/restaurant_comment/add_item_comment/', customers.AddItemCommentBox ),

        path('restaurant/restaurant_comment/add_deal_comment/', customers.AddDealCommentBox ),


        # path('item/item_comment/', customers.ShowItemCommentBox.as_view(), name='item_comment_box'),
        # path('item/item_comment/add/', customers.AddItemCommentBox.as_view(), name='item_comment_box.add'),
        
        # path('deal/deal_comment/', customers.ShowDealCommentBox.as_view(), name='deal_comment_box'),
        # path('deal/deal_comment/add/', customers.AddDealCommentBox.as_view(), name='deal_comment_box.add'),
        
        path('platform/platform_comment/', customers.ShowPlatformCommentBox.as_view(), name='platform_discount_box'),
        path('platform/platform_comment/add/', customers.AddPlatformCommentBox.as_view(), name='platform_discount_box.add'),

        path('mc/mc_comment/', customers.ShowMCDiscountCommentBox.as_view(), name='mc_comment_box'),
        path('mc/mc_comment/add/', customers.AddMCDiscountCommentBox.as_view(), name='mc_comment_box.add'),

    ], 'restaurant'), namespace='customers')),
]
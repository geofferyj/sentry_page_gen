from django.urls import path
from site_pages.views import AddPageView, ListPageView, UpdatePageView, PageContentView

urlpatterns = [
    path('',ListPageView.as_view() ),
    path('add-page/',AddPageView.as_view() ),
    path('set-page-markdown/<int:pk>/',UpdatePageView.as_view() ),   
    path('get-page-html/<int:pk>/',PageContentView.as_view() ),  

] 
from django.urls import path
from site_pages.views import AddPageView, ListPageView, UpdatePageView, PageContentView

urlpatterns = [
    path('list_pages/',ListPageView.as_view() ),
    path('add_page/',AddPageView.as_view() ),
    path('set_page_markdown/<str:slug>/',UpdatePageView.as_view() ),   
    path('retrieve_page_html/<str:slug>/',PageContentView.as_view() ),  

] 
from site_pages.models import Page, MetaTag
from site_pages.serializers import PageSerializer, PageUpdateSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from  markdown import Markdown
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render

#index page
def index(request):

    return render(request, 'index.html')

class AddPageView(CreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    # def post(self, request, format=None):
    #     data = request.data
    #     if isinstance(data, list): 
    #         serializer = self.get_serializer(data=request.data, many=True)
            
    #     else:
    #         serializer = self.get_serializer(data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListPageView(ListAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer 

class UpdatePageView(RetrieveUpdateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageUpdateSerializer  

    

class PageContentView(RetrieveAPIView):
    queryset = Page.objects.all()
    serializer = PageSerializer


    def get_meta(self, pk):
        page = Page.objects.get(pk=pk)
        t = []
        meta = page.meta_tags.all()
        if meta:
            for entry in meta:
                t.append("<meta name='{}' content='{}'>".format(entry.name, entry.content))
            print('inside get_meta down ', t)

            return "".join([i for i in t]) 
        return ""
    
    # def get_script(self, pk):
    #     page = Page.objects.get(pk=pk)
    #     t = []
    #     script_tags = page.scripts.all()
    #     if script_tags:
    #         for entry in script_tags:
    #             t.append("<script src='{}'>{}</script>".format(entry.scr_link, entry.content))
    #         return "".join([i for i in t])
    #     return ""

    def get_css(self, pk):
        page = Page.objects.get(pk=pk)
        t = []
        css = page.css.all()
        if t:
            for entry in css:
                t.append("<link rel='{}' href='{}'>".format(entry.rel, entry.href))
            return "".join([i for i in t])
        return ""

    def get(self, request, pk):
        try:
            page = Page.objects.get(pk=pk)
        except Page.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        md = Markdown()
        content = md.convert(page.content)
        template = f"<!doctype html><html lang='en'><head><title>{page.title}</title>{self.get_meta(pk)}\
                    {self.get_css(pk)}</head><body>{content}</body></html>"
       
        data = {
            'id':page.id, 
            'title':page.title, 
            'date_created':page.date_created, 
            'category':page.category, 
            'tags':page.tags,
            'html': template}
        return Response(data=data, status=status.HTTP_200_OK,)


# Create your views here.

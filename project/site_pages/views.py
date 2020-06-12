from site_pages.models import Page, MetaTag
from site_pages.serializers import PageSerializer, PageUpdateSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from  markdown import Markdown
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response
from rest_framework import status

class AddPageView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Page.objects.all()
    serializer_class = PageSerializer

# -------------- Uncomment to add support for adding multiple pages at once ------------------ 
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
    lookup_field = 'slug'

class UpdatePageView(RetrieveUpdateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageUpdateSerializer  
    lookup_field = 'slug'
    

class PageContentView(RetrieveAPIView):
    queryset = Page.objects.all()
    serializer = PageSerializer
    lookup_field = 'slug'


    def get_meta(self, slug):
        page = Page.objects.get(slug=slug)
        t = []
        meta = page.meta_tags.all()
        if meta:
            for entry in meta:
                t.append("<meta name='{}' content='{}'>".format(entry.name, entry.content))

            return "".join([i for i in t]) 
        return ""
    
    def get_script(self, slug):
        page = Page.objects.get(slug=slug)
        t = []
        scripts = page.scripts.all()
        if scripts:
            for entry in scripts:
                if entry.src:
                    t.append("<script src='{}'></script>".format(entry.src))
                else:
                    t.append("<script>{}</script>".format(entry.body))
            return "".join([i for i in t])
        return ""

    def get_css(self, slug):
        page = Page.objects.get(slug=slug)
        t = []
        css = page.css.all()
        if css:
            for entry in css:
                t.append("<link rel='{}' href='{}'>".format(entry.rel, entry.href))
            return "".join([i for i in t])
        return ""
        
    def get(self, request, slug):
        try:
            page = Page.objects.get(slug=slug)
        except Page.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        md = Markdown()
        content = md.convert(page.content)
        template = f"<!doctype html><html lang='en'><head><title>{page.title}</title>{self.get_meta(slug)}{self.get_css(slug)}</head><body>{content}{self.get_script(slug)}</body></html>"
        slug_id = page.slug[-5:]
        page_name = page.slug[:len(page.slug) - 5][:19] + "-"+slug_id + ".html"
        location = "pages/"
        with open(location + page_name, 'w+') as file:
            file.write(template)



        data = {
            'id':page.id, 
            'slug':page.slug,
            'title':page.title, 
            'url': location + page_name,
            'date_created':page.date_created, 
            'author':page.author,
            'category':page.category, 
            'tags':page.tags,
            'content':page.content,
            'html': template}
        return Response(data=data, status=status.HTTP_200_OK,)


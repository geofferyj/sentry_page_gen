from rest_framework import serializers
from site_pages.models import Page, MetaTag, CSS, ScriptTag
from django.contrib.auth.models import User



class MetaTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaTag
        exclude = ['page']

class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScriptTag
        exclude = ['page']
 
class CSSSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSS
        exclude = ['page']


class PageSerializer(serializers.ModelSerializer):
    meta_tags = MetaTagSerializer(many=True, required=False)
    scripts = ScriptSerializer(many=True, required=False)
    css = CSSSerializer(many=True, required=False)
    lookup_field = 'slug'
    class Meta:
        model = Page
        fields = '__all__'
        read_only_fields = ['slug']


    def create(self, validated_data):
        if validated_data.get('meta_tags'):
            meta_tag_data = validated_data.pop('meta_tags')
        else:
            meta_tag_data=[]
        if validated_data.get('scripts'):
            script_data = validated_data.pop('scripts')
        else:
            script_data = []
        if validated_data.get('css'):
            css_data = validated_data.pop('css')
        else:
            css_data = []
        page = Page.objects.create(**validated_data)

        for data in meta_tag_data:
            MetaTag.objects.create(page=page, **data)
        
        for data in script_data:
            print(data)
            ScriptTag.objects.create(page=page, **data)
        
        for data in css_data:
            CSS.objects.create(page=page, **data)
            
        return page


class PageUpdateSerializer(serializers.ModelSerializer):
    lookup_field = 'slug'
    class Meta:
        model = Page
        fields = ['content']


class RegisterSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    # def create(self, validated_data):
    #     user = User.objects.create(**validated_data)
    #     return user

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
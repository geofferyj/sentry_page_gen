from rest_framework import serializers
from site_pages.models import Page, MetaTag, CSS



class MetaTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaTag
        exclude = ['page']

# class ScriptSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ScriptTag
#         exclude = ['page']

class CSSSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSS
        exclude = ['page']


class PageSerializer(serializers.ModelSerializer):
    meta_tags = MetaTagSerializer(many=True)
    # script_tags = ScriptSerializer(many=True)
    css = CSSSerializer(many=True)
    class Meta:
        model = Page
        fields = '__all__'


    def create(self, validated_data):
        meta_tag_data = validated_data.pop('meta_tags')
        # script_data = validated_data.pop('script_tags')
        css_data = validated_data.pop('css')
        page = Page.objects.create(**validated_data)

        for data in meta_tag_data:
            MetaTag.objects.create(page=page, **data)
        
        # for data in script_data:
        #     print(data)
        #     ScriptTag.objects.create(page=page, **data)
        
        for data in css_data:
            CSS.objects.create(page=page, **data)
            
        return page


class PageUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['content']





# class UserSerializer(serializers.ModelSerializer):
#     profile = ProfileSerializer()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'profile']

#     def create(self, validated_data):
#         profile_data = validated_data.pop('profile')
#         user = User.objects.create(**validated_data)
#         Profile.objects.create(user=user, **profile_data)
#         return user
from rest_framework import serializers
from items.models import Item, FavoriteItem
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['first_name', 'last_name']



class ItemListSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
		view_name = "api-item-detail",
		lookup_field = "id",
		lookup_url_kwarg = "item_id"
		)
	added_by = UserSerializer()
	favorites = serializers.SerializerMethodField()
	class Meta:
		model = Item
		fields = ['id', 'image', 'name', 'description', 'detail', 'added_by', 'favorites']
	def get_favorites(self, obj):
		return obj.favoriteitem_set.all().count()

class ItemDetailSerializer(serializers.ModelSerializer):
	favorites_by = serializers.SerializerMethodField()
	class Meta:
		model = Item
		fields = ['id', 'image', 'name', 'description', 'favorites_by']
	def get_favorites_by(self, obj):
		favorites = obj.favoriteitem_set.all()
		users = []
		for fave in favorites:
			users.append(fave.user)
		return UserSerializer(users, many=True).data





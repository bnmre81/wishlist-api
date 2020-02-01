from django.shortcuts import render
from items.models import Item
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ItemListSerializer, ItemDetailSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsStaffOrOwner

class ItemListView(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemListSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'
	permission_classes = [AllowAny]

class ItemDetailView(RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'
	permission_classes = [IsAuthenticated, IsStaffOrOwner]

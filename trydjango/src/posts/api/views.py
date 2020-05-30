from django.db.models import Q
from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	ListAPIView, 
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	UpdateAPIView,
	)

from rest_framework.filters import (
		SearchFilter,
		OrderingFilter,
	)
from rest_framework.permissions import (
		AllowAny,
		IsAuthenticated,
		IsAdminUser,
		IsAuthenticatedOrReadOnly,
	)
from .pagination import PostLimitOffsetPagination,PostPageNumberPagination
from posts.models import Post
from .serializers import (
	PostCreateUpdateSerializer,
	PostDetailSerializer,
	PostListSerializer,
	)
from .permissions import IsOwnerOrReadOnly

class PostCreateAPIView(CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCreateUpdateSerializer
	# permission_classes = [IsAdminUser]
	def perform_update(self, serializer):
		serializer.save(user=self.request.user)

class PostDetailAPIView(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	permission_classes = [AllowAny]
	lookup_field='slug'
	# lookup_url_kwarg='abc'
	
class PostUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCreateUpdateSerializer
	lookup_field='slug'
	permission_classes = [IsOwnerOrReadOnly]
	# lookup_url_kwarg='abc'
	def perform_update(self, serializer):
		serializer.save(user=self.request.user)

class PostDeleteAPIView(DestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	permission_classes = [IsOwnerOrReadOnly]
	lookup_field = 'slug'
	# lookup_url_kwarg='abc'

class PostListAPIView(ListAPIView):
	serializer_class = PostListSerializer
	permission_classes = [AllowAny]
	filter_backends = [SearchFilter,OrderingFilter]
	pagination_class = PostPageNumberPagination
	search_fields = ['title','content']
	# queryset_list = Post.objects.all()
	def get_queryset(self, *args, **kwargs):
		queryset = Post.objects.all()
		queryset_list = queryset
		query = self.request.GET.get("q")
		if query:
			queryset_list = queryset_list.filter(
					Q(title__icontains=query)|
					Q(content__icontains=query)|
					Q(user__first_name__icontains=query) |
					Q(user__last_name__icontains=query)
					).distinct()
		return queryset_list
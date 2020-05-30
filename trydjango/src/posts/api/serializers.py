from rest_framework.serializers import (
	HyperlinkedIdentityField,
	ModelSerializer,
	SerializerMethodField
	)

from posts.models import Post
from comments.models import Comment
from accounts.api.serializers import UserDetailSerializer
from comments.api.serializers import CommentSerializer

class PostCreateUpdateSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields =[
			# 'id',
			'title',
			# 'slug',
			'content',
			'publish',
		]

post_detail_url = HyperlinkedIdentityField(
		view_name='posts-api:detail',
		lookup_field='slug'
		)
class PostDetailSerializer(ModelSerializer):
	url = post_detail_url
	# user = SerializerMethodField()
	user = UserDetailSerializer()
	image = SerializerMethodField()
	html = SerializerMethodField()
	comments = SerializerMethodField()
	class Meta:
		model = Post
		fields =[
			'url',
			'id',
			'title',
			'user',
			'slug',
			'content',
			'html',
			'publish',
			'image',
			'comments',
		]
	# def get_user(self,obj):
	# 	return str(obj.user.username)
	def get_image(self,obj):
		# print(self)
		# print("******")
		# print(obj)
		try:
			image = obj.image.url
		except:
			image = None
		return image
	def get_html(self,obj):
		return obj.get_markdown()
	def get_comments(self,obj):
		content = obj.get_content_type
		print(content)
		object_id = obj.id
		c_qs = Comment.objects.filter_by_instance(obj)
		print(c_qs)
		return CommentSerializer(c_qs, many=True).data

class PostListSerializer(ModelSerializer):
	# url= HyperlinkedIdentityField(
	# 	view_name='posts-api:detail',
	# 	lookup_field='slug'
	# 	)
	url = post_detail_url
	user = SerializerMethodField()
	class Meta:
		model = Post
		fields =[
			'url',
			'user',
			'title',
			# 'slug',
			'content',
		]
	def get_user(self,obj):
		return str(obj.user.username)	

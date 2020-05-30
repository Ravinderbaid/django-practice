from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from rest_framework.serializers import (
	HyperlinkedIdentityField,
	ModelSerializer,
	SerializerMethodField,
	ValidationError,
	HyperlinkedRelatedField,
	EmailField,
	CharField,
	)
from django.contrib.auth import (
    get_user_model,
    # login,
    # logout,
    )


User = get_user_model()



class UserCreateSerializer(ModelSerializer):
	email = EmailField(label= 'Email Address')
	email2 = EmailField(label= 'Confirm Email')
	class Meta:
		model = User
		fields =[
			'username',
			'email',
			'email2',
			'password',
		]
		extra_kwargs = {"password": {
									"write_only":True
								}
						}
	# def validate(self,data):
	# 	email = data['email']
	# 	user_qs = User.objects.filter(email=email)
	# 	if user_qs.exists():
	# 		raise ValidationError("User already Exists")
	# 	return data
	def validate_email(self, value):
		data = self.get_initial()
		email1 = data.get("email2")
		email2 = value
		if email1 != email2:
			raise ValidationError("Emails must match")
		user_qs = User.objects.filter(email=value)
		if user_qs.exists():
			raise ValidationError("User already Exists")
		return value
	def validate_email2(self, value):
		data = self.get_initial()
		email1 = data.get("email2")
		email2 = value
		if email1 != email2:
			raise ValidationError("Emails must match")
		return value
	def create(self,validated_data):
		# print(validated_data)
		username = validated_data['username']
		password = validated_data['password']
		email = validated_data['email']
		user_obj = User(
					username = username,
					email =email
			)
		user_obj.set_password(password)
		user_obj.save()
		return validated_data

class UserDetailSerializer(ModelSerializer):
	class Meta:
		model = User
		fields =[
			'email',
			'username',
			'password',
		]


class UserLoginSerializer(ModelSerializer):
	token = CharField(allow_blank=True, read_only=True)
	username = CharField(required=False, allow_blank=True)
	email = EmailField(label= 'Email Address', required=False, allow_blank=True)
	class Meta:
		model = User
		fields =[
			'username',
			'email',
			'password',
			'token',
		]
		extra_kwargs = {"password": {
									"write_only":True
								}
						}
	def validate(self,data):
		user_obj = None
		email = data.get('email', None)
		username = data.get('username', None)
		password = data['password']
		if not email and not username:
			raise ValidationError("A username or email must be present")
		user = User.objects.filter(
			Q(email=email) |
			Q(username=username)
			).distinct()
		user = user.exclude(email__isnull=True).exclude(email__iexact='')
		if user.exists() and user.count() ==1:
			user_obj = user.first()
		else:
			raise ValidationError("User doesnot exists")
		if user_obj:
			if user_obj.check_password(password):
				raise ValidationError("Invlaid Password")
		data["token"] =  "Some random data"
	# 	user_qs = User.objects.filter(email=email)
	# 	if user_qs.exists():
	# 		raise ValidationError("User already Exists")
		return data
from rest_framework.permissions import BasePermission
class IsOwnerOrReadOnly(BasePermission):
	message = "You are not the owner of the blog"
	# my_safe_mehtods = ['PUT','GET']
	# def has_permission(self, request, view):
	# 	if request.method in self.my_safe_mehtods:
			# return True
	def has_object_permission(self, request, view, obj):
		return obj.user == request.user
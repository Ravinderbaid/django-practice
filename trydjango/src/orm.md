 Post.objects.all()
 query = Post()
 query.title = "Ra"
 query.content = "Hello"
 query.save()
 Post.objects.all()
 Post.objects.filter(title = "Ra")
 Post.objects.filter(title__icontains = "aBc")
 Post.objects.create(title="Query",content="Test")
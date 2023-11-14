from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class News(models.Model):
    title=models.CharField(max_length=100)
    img=models.ImageField(upload_to="newsimgs")
    published_time=models.DateTimeField(auto_now_add=True)
    description=models.TextField()
    def __str__(self):
        return self.title

class Post(models.Model):
    img = models.ImageField(upload_to="postimg",null=True,blank=True)
    text1=models.TextField()
    text=models.TextField(null=True,blank=True)
    published_time=models.DateTimeField(auto_now_add=True,null=True)
    author2=models.ForeignKey(User,related_name='userposts',on_delete=models.CASCADE)
    votup=models.ManyToManyField(User,related_name='postup')
    votdown=models.ManyToManyField(User,related_name='postdown')
    def total_likes(self):
        return self.likes.count()
    def total_unlikes(self):
        return self.likes.count()
    def __str__(self):
        return self.author2.username+ "post"+str(self.pk)
class Profile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio=models.TextField(max_length=150,null=True,blank=True)
    profile_pic=models.ImageField(upload_to="profile_pics",null=True,blank=True)
    def __str__(self):
        return str(self.user)
    
    
class Comment(models.Model):
    author=models.ForeignKey(User,related_name='usercomments',on_delete=models.CASCADE)
    post_id=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    text=models.TextField()
    published_time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.post_id.text + " " + self.author.username
from django.db import models
class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)
    def __str__(self) :
        return self.username

class BooksDetails(models.Model):
    Title=models.CharField(max_length=50)
    author=models.CharField(max_length=20)
    Quantity=models.PositiveBigIntegerField()
    image=models.ImageField(upload_to='All images')
    def __str__(self) :
        return self.Title
class LibraryMember(models.Model):
    Name=models.ForeignKey(User, on_delete=models.CASCADE)
    Book_title=models.ForeignKey(BooksDetails,on_delete=models.CASCADE)
    Date=models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"self.Book_title ,self.Name"

class image(models.Model):
    Name=models.CharField(max_length=20)
    Date=models.DateTimeField(auto_now=True)
    photo=models.ImageField(upload_to="All images")


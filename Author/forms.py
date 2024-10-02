# from django import forms
# from .models import Author
# from.models import  Book
#
#
# class AuthorForm(forms.ModelForm):
#     class Meta:
#         model = Author
#         fields = ['name', 'username', 'email']
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author Name'}),
#             'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
#         }
#
#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         if Author.objects.filter(username=username).exists():
#             raise forms.ValidationError("This username is already taken.")
#         return username
#
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if Author.objects.filter(email=email).exists():
#             raise forms.ValidationError("This email address is already in use.")
#         return email
#
#
#
# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = ['book_name', 'author_name']
#         widgets = {
#             'book_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Book Name'}),
#             'author_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author Name'}),
#         }
#
#
#     def clean_book_name(self):
#         book_name = self.cleaned_data.get('book_name')
#         if Book.objects.filter(book_name=book_name).exists():
#             raise forms.ValidationError("This book is already taken.")
#         return book_name
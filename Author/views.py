# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Author
# from .forms import AuthorForm
# from django.contrib.auth.decorators import login_required
#
# # View to add a new author
# @login_required
# def add_author.css(request):
#     if request.method == 'POST':
#         form = AuthorForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('author_list')  # Redirect to the author list view
#     else:
#         form = AuthorForm()
#
#     return render(request, 'Author/add_author.css.html', {'form': form})
#
# @login_required
# def author_list(request):
#     # Fetch all authors from the database
#     authors = Author.objects.all()
#
#
#     query = request.GET.get('q', '')
#     if query:
#         authors = authors.filter(name__icontains=query)  # Filter authors by name
#
#     return render(request, 'Author/author_list.html', {'authors': authors, 'query': query})
#
#
# @login_required
# def edit_author(request, author_id):
#     author = get_object_or_404(Author, id=author_id)
#     if request.method == 'POST':
#         form = AuthorForm(request.POST, instance=author)
#         if form.is_valid():
#             form.save()
#             return redirect('author_list')  # Redirect to the author list after editing
#     else:
#         form = AuthorForm(instance=author)
#
#     return render(request, 'Author/edit_author.html', {'form': form, 'author': author})
#
# def author_details(request, author_id):
#     author = get_object_or_404(Author, id=author_id)
#     return render(request, 'Author/author_details.html', {'author': author})


# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from .models import Author
# from .forms import AuthorForm
# from .models import Book
# from django.contrib import messages
# from .forms import BookForm
#
# # View to add a new author
# @login_required
# def add_author.css(request):
#     if request.method == 'POST':
#         form = AuthorForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the new author
#             return redirect('author_list')  # Redirect to the author list view
#     else:
#         form = AuthorForm()
#
#     return render(request, 'Author/add_author.css.html', {'form': form})
#
# # View to list all authors
# @login_required
# def author_list(request):
#     authors = Author.objects.all()  # Get all authors from the database
#
#     query = request.GET.get('q', '')  # Search query from request
#     if query:
#         authors = authors.filter(name__icontains=query)  # Filter authors by name
#
#     # Calculate total counts for the info box
#     total_books = Book.objects.count()  # Assuming you have a Book model
#     total_authors = authors.count()  # Count of filtered authors
#
#     # Render the template with authors and total counts
#     return render(request, 'Author/author_list.html', {
#         'authors': authors,
#         'query': query,
#         'total_books': total_books,
#         'total_authors': total_authors,
#     })
#
# # View to edit an existing author
# @login_required
# def edit_author(request, author_id):
#     author = get_object_or_404(Author, id=author_id)  # Fetch the author by ID
#     if request.method == 'POST':
#         form = AuthorForm(request.POST, instance=author)
#         if form.is_valid():
#             form.save()  # Save the updated author details
#             return redirect('author_list')  # Redirect to the author list view
#     else:
#         form = AuthorForm(instance=author)
#
#     return render(request, 'Author/edit_author.html', {'form': form, 'author': author})
#
# # View to display author details
# @login_required
# def author_details(request, author_id):
#     author = get_object_or_404(Author, id=author_id)  # Get the author by ID
#     return render(request, 'Author/author_details.html', {'author': author})
#
#
#
#
# @login_required
# def book_list.css(request):
#     # Fetch all books from the database
#     books = Book.objects.all()
#
#     # Calculate total books and distinct authors
#     total_books = books.count()
#     total_authors = Book.objects.values('author_name').distinct().count()
#
#     # Handle search query if applicable
#     query = request.GET.get('q', '')
#     if query:
#         books = books.filter(book_name__icontains=query)
#
#     # Handle adding a new book
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Book added successfully!')  # Success message
#             return redirect('book_list.css')  # Redirect to the book list after adding a book
#     else:
#         form = BookForm()
#
#     return render(request, 'Book/book_list.css.html', {
#         'books': books,
#         'total_books': total_books,
#         'total_authors': total_authors,
#         'form': form,
#         'query': query,
#     })
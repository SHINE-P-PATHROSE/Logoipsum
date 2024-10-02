from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Author
from .forms import BookForm, RegisterForm, LoginForm, AuthorForm
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json



@login_required
def author_list(request):
    """Fetches and displays a list of authors."""
    authors = Author.objects.all()
    total_authors = authors.count()
    total_books = Book.objects.count()

    # Handle search query if applicable
    query = request.GET.get('q', '')
    if query:
        authors = authors.filter(name__icontains=query)

    # Handle author form submission
    form = handle_author_form(request)

    return render(request, 'Book/author_list.html', {
        'authors': authors,
        'total_books': total_books,
        'total_authors': total_authors,
        'form': form,
        'query': query,
    })

def handle_author_form(request):
    """Handles the logic for adding or editing an author."""
    form = AuthorForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        try:
            form.save()
            messages.success(request, 'Author added successfully!')
            return redirect('author_list')
        except IntegrityError:
            messages.error(request, 'An error occurred while adding the author. Please try again.')
    return form

@login_required
def book_list(request):
    """Displays the list of books along with total counts."""
    books = Book.objects.all()
    total_books = books.count()
    total_authors = Author.objects.count()  # Count authors directly

    # Distinct authors from the books
    authors = Book.objects.values_list('author_name', flat=True).distinct()

    # Handle search query if applicable
    query = request.GET.get('q', '')
    if query:
        books = books.filter(book_name__icontains=query)

    # Handle adding a new book
    form = handle_book_form(request)

    return render(request, 'Book/book_list.html', {
        'books': books,
        'total_books': total_books,
        'total_authors': total_authors,
        'form': form,
        'query': query,
        'authors': authors,
    })

def handle_book_form(request):
    """Handles the logic for adding or editing a book."""
    form = BookForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()  # Save the book
        messages.success(request, 'Book added successfully!')
        return redirect('book_list.html')

    return form

@login_required
def add_book(request):
    """Renders the page to add a new book."""
    form = handle_book_form(request)
    return render(request, 'Book/add_book.html', {'form': form})

@login_required
def edit_book(request, book_id):
    """Handles the editing of a specific book."""
    book = get_object_or_404(Book, id=book_id)
    form = BookForm(request.POST or None, instance=book)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Book updated successfully!')
        return redirect('book_list.html')

    return render(request, 'Book/edit_book.html', {'form': form, 'book': book})

def user_login(request):
    """Handles user login."""
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('author_list')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'Book/home_login.html', {'form': form})

def register(request):
    """Handles user registration."""
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, 'Registration successful!')
        return redirect('login')

    return render(request, 'Book/home_register.html', {'form': form})

def logout(request):
    """Logs out the user."""
    auth_logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')

@login_required
def add_author(request):
    """Renders the page to add a new author."""
    form = handle_author_form(request)
    return render(request, 'Book/add_author.html', {'form': form})


@login_required
def edit_author(request, author_id):
    """Handles the editing of a specific author."""
    author = get_object_or_404(Author, id=author_id)
    form = AuthorForm(request.POST or None, instance=author)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Author updated successfully!')
            return redirect('author_list')
        else:
            messages.error(request, 'Please correct the errors below.')

    return render(request, 'Book/edit_author.html', {'form': form, 'author': author})

@login_required
def author_details(request, author_id):
    """Displays the details of a specific author along with their books."""
    author = get_object_or_404(Author, id=author_id)
    books = Book.objects.filter(author_name=author.name)  # Assuming author_name is a field in the Book model
    return render(request, 'Book/author_details.html', {'author': author, 'books': books})




@csrf_exempt  # You can also use csrf_token for security
def update_book_status(request, book_id):
    if request.method == 'POST':
        try:
            book = Book.objects.get(id=book_id)
            data = json.loads(request.body)
            book.status = data['status']  # Update the status based on the request
            book.save()

            return JsonResponse({'success': True})
        except Book.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Book not found'}, status=404)
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)


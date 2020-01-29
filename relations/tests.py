#from django.test import TestCase

# Create your tests here.
from django.test import TestCase


from ddf import G

def test_search_person_by_name():
    p1 = G(Person)
    p2 = G(Person)
    gp = G(PeopleGroup, person=[p1])


class SearchingPerson(TestCase):
    def test_search_book_by_author(self):
        author1 = G(Author)
        author2 = G(Author)
        book1 = G(Book, authors=[author1])
        book2 = G(Book, authors=[author2])
        books = Book.objects.search_by_author(author1.name)

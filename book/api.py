# main/api.py

from rest_framework.views import APIView
from rest_framework.response import Response
import json

class BookListView(APIView):
    def get(self, request):
        try:
            with open('book/fixtures/book.json', 'r') as file:
                book_data = json.load(file)
            return Response(book_data)
        except Exception as e:
            return Response({'error': str(e)})

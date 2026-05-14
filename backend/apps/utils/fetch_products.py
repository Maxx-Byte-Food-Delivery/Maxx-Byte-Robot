import mysql.connector
from dotenv import load_dotenv
from rest_framework.views import APIView
from rest_framework.response import Response
import os

load_dotenv()

class FetchProductsView(APIView):

    def get(self, request):

        conn = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )

        products = []
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM menu_items")
        results = cursor.fetchall()

        for row in results:
            products.append(dict(id=row[0], name=row[1], description=row[2], price=row[3]))

        conn.close()

        return Response(products)
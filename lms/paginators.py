from rest_framework.pagination import PageNumberPagination


class LMSPaginator(PageNumberPagination):
    """
    Пагинатор для вывода ограниченного колества данных на странице.
    """
    page_size = 3

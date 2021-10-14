from rest_framework.pagination import PageNumberPagination


class LogPagination(PageNumberPagination):
    page_size = 10
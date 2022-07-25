from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination


class OwnLimitOffsetPagination(LimitOffsetPagination):
    max_limit = 10
    default_limit = 2


class OwnPageNumberPagination(PageNumberPagination):
    page_size = 2
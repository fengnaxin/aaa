
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2  # 默认每显示2个 最小
    page_size_query_param = 'page_size'  # 默认不写为None 指定分页前端参数字段
    # page_query_param = 'page'
    max_page_size = 20  # 每页显示最大数量


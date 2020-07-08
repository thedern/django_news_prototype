from django.urls import path
from .views import ArticleListView, ArticleUpdateView, ArticleDetailView, ArticleDeleteView, ArticleCreateView, RunList

# urlpatterns = [
#     path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
#     path('<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
#     path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
#     path('new/', ArticleCreateView.as_view(), name='article_new'),
#     path('<int:pk>/run/', RunList.as_view(), name='run_list'),
#     path('', ArticleListView.as_view(), name='article_list')
# ]

# note:  urls are now a hash, not an integer thus, <int:pk> --> <pk>
urlpatterns = [
    path('<pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('<pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('<pk>/run/', RunList.as_view(), name='run_list'),
    path('', ArticleListView.as_view(), name='article_list')
]

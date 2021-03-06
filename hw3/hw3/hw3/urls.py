from django.conf.urls import url
from django.contrib import admin
from kvstore import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^kv-store/get_node_details', views.get_node_details),
    url(r'^kv-store/get_all_replicas', views.get_all_replicas),
    url(r'^kv-store/update-view$', views.update_view),
    url(r'^kv-store/check_nodes', views.check_nodes),
    url(r'^kv-store/(?P<key>[a-zA-Z0-9_]{1,200})$', views.kvs_response),
    url(r'^kv-store/(?P<key>[a-zA-Z0-9_]{201,})$', views.failure),
]



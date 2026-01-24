from django.urls import path
from . import views as view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', view.home,name="Homepage"),
    path('blogs/', view.blog,name="Blogs"),
    path('members/', view.members,name="Members"),
    path('addmember/', view.addmembers,name="New Member"),
    path('deletemember/<int:member_id>/', view.deletemember, name='DeleteMember'),
    path('editmember/<int:member_id>/', view.editmember, name='Editmember'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
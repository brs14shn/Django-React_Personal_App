from django.urls import include, path

from .views import DepartmentView,DepartmentPersonalView,PersonalListCreate,PersonalGetUpdateDelete

urlpatterns = [
   
    path("",DepartmentView.as_view(),name="department"),
    path("department/<str:department>/",DepartmentPersonalView.as_view()),
    path("personal/",PersonalListCreate.as_view()),
    path("personal/<int:pk>/",PersonalGetUpdateDelete.as_view())
   
]

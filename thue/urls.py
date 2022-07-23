from django.urls import path
from . import order_views 
from . import user_views
from . import product_views

urlpatterns = [
    
    path('api/orders/', order_views.getOrders, name='orders'),
    path('api/orders/add/', order_views.addOrderItems, name='orders-add'),
    path('api/orders/myorders/', order_views.getMyOrders, name='myorders'),
    path('api/orders/<str:pk>/deliver/', order_views.updateOrderToDelivered, name='order-delivered'),
    path('api/orders/<str:pk>/', order_views.getOrderById, name='user-order'),
    path('api/orders/<str:pk>/pay/', order_views.updateOrderToPaid, name='pay'),
    
    path("api/products/", product_views.getProducts, name="products"),
    path("api/products/create/", product_views.createProduct, name="product-create"),
    path("api/products/upload/", product_views.uploadImage, name="image-upload"),
    path("api/products/<str:pk>/re", product_views.createProductReview, name="create-review"),
    path("api/products/top/", product_views.getTopProducts, name="top-products"),
    path("api/products/<str:pk>/", product_views.getProduct, name="product"),
    path('api/products/<str:pk>/reviews/', product_views.createProductReview, name="create-review"),
    path("api/products/update/<str:pk>/", product_views.updateProduct, name="product-update"),
    path("api/products/delete/<str:pk>/", product_views.deleteProduct, name="product-delete"),
    
    path("api/users/login/", user_views.MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/users/register/", user_views.registerUser, name="register"),
    path("api/users/profile/", user_views.getUserProfile, name="users-profile"),
    path("api/users/profile/update/", user_views.updateUserProfile, name="user-profile-update"),
    path("api/users/", user_views.getUsers, name="users"),
    path("api/users/<str:pk>/", user_views.getUserById, name="user"),
    path("api/users/update/<str:pk>/", user_views.updateUser, name="user-update"),
    path("api/users/delete/<str:pk>/", user_views.deleteUser, name="user-delete"),

]
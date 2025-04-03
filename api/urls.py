from django.urls import path
from . import views

urlpatterns = [
  path('healthcheck/', views.health_check),
  #API Category urls
  path('categories/', views.InventoryCategoryPost.as_view(), name='category-lc'),
  path('categories/<int:pk>/', views.InventoryCategoryCrud.as_view() , name='category-rud'),
  #API Supplier urls
  path('suppliers/', views.InventorySupplierPost.as_view(), name='supplier-lc'),
  path('suppliers/<int:pk>/', views.InventorySupplierCrud.as_view(), name='supplier-rud'),
  #API Customer urls
  path('customers/', views.InventoryCustomerPost.as_view(), name='customer-lc'),
  path('customers/<int:pk>/', views.InventoryCustomerCrud.as_view(), name='customer-rud'),
  #API Product urls
  path('products/', views.InventoryProductPost.as_view(), name='product-lc'),
  path('products/all/', views.InventoryProductGet.as_view(), name='product-all'),
  path('products/<int:pk>/', views.InventoryProductCrud.as_view(), name='product-rud'),
  path('products/low-stock/', views.LowStockProductsGet.as_view(), name='low-stock-products'),
  #API Sale urls
  path('sales/', views.InventorySalePost.as_view(), name='sale-lc'),
  path('sales/<int:pk>/', views.InventorySaleCrud.as_view(), name='sale-rud'),
  path('sales/items/', views.InventorySaleItemPost.as_view(), name='sale-item-lc'),
  path('sales/items/<int:pk>/', views.InventorySaleItemCrud.as_view(), name='sale-item-rud'),
  #API Purchase urls
  path('purchases/', views.InventoryPurchasePost.as_view(), name='purchase-lc'),
  path('purchases/<int:pk>/', views.InventoryPurchaseCrud.as_view(), name='purchase-rud'),
  path('purchases/items/', views.InventoryPurchaseItemPost.as_view(), name='purchase-item-lc'),
  path('purchases/items/<int:pk>/', views.PurchaseItemCrud.as_view(), name='purchase-item-rud'),
]
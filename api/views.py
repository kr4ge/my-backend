from .serializers import UserSerializer, InventoryCategorySerializer, InventorySupplierSerializer, InventoryProductSerializer, InventoryCustomerSerializer, InventorySaleSerializer, InventorySaleItemSerializer, InventoryPurchaseSerializer, InventoryPurchaseItemSerializer
from .models import Purchase, PurchaseItem, Customer, Product, Category, Supplier, Sale, SaleItem
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import generics, status
from django.http import JsonResponse

def health_check(request):
    return JsonResponse({"status": "healthy"})
# !User views
#Creating a user
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
#User login
class LoginView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    
    def get(self, request):
        user = request.user
        return Response({'username': user.username,'email': user.email})

#Category CRUD views
class InventoryCategoryPost(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = InventoryCategorySerializer
    permission_classes = [IsAuthenticated]
    
class InventoryCategoryCrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = InventoryCategorySerializer
    permission_classes = [IsAuthenticated]

#Supplier CRUD views
class InventorySupplierPost(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = InventorySupplierSerializer
    permission_classes = [IsAuthenticated]
    
class InventorySupplierCrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = InventorySupplierSerializer
    permission_classes = [IsAuthenticated]
    
#Customer CRUD views
class InventoryCustomerPost(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = InventoryCustomerSerializer
    permission_classes = [IsAuthenticated]
    
class InventoryCustomerCrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = InventoryCustomerSerializer
    permission_classes = [IsAuthenticated]      
    
#Product CRUD views
class InventoryProductPost(generics.ListCreateAPIView):
    serializer_class = InventoryProductSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(author=user, is_active=True)
    
    def perform_create(self, serializer):
        if serializer.is_valid():   
            serializer.save(author=self.request.user)
        else :
            print(serializer.errors)
            
class InventoryProductCrud(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InventoryProductSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(author=user)
    
class InventoryProductGet(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = InventoryProductSerializer
    permission_classes = [IsAuthenticated]

#low stock products view
class LowStockProductsGet(generics.ListAPIView):
    serializer_class = InventoryProductSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(
            author=user,
            stockQuantity__lte=3
        ).order_by('stockQuantity')    

#Sale CRUD views
class InventorySalePost(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = InventorySaleSerializer
    permission_classes = [IsAuthenticated]
    
class InventorySaleCrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = InventorySaleSerializer
    permission_classes = [IsAuthenticated]
    
#Sale Item CRUD views
class InventorySaleItemPost(generics.ListCreateAPIView):
    queryset = SaleItem.objects.all()
    serializer_class = InventorySaleItemSerializer
    permission_classes = [IsAuthenticated]

class InventorySaleItemCrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = SaleItem.objects.all()
    serializer_class = InventorySaleItemSerializer
    permission_classes = [IsAuthenticated]
    
#Purchase CRUD views
class InventoryPurchasePost(generics.ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = InventoryPurchaseSerializer
    permission_classes = [IsAuthenticated]
    
class InventoryPurchaseCrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = InventoryPurchaseSerializer
    permission_classes = [IsAuthenticated]
    
#Purchase Item CRUD views
class InventoryPurchaseItemPost(generics.ListCreateAPIView):
    queryset = PurchaseItem.objects.all()
    serializer_class = InventoryPurchaseItemSerializer
    permission_classes = [IsAuthenticated]
    
class PurchaseItemCrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseItem.objects.all()
    serializer_class = InventoryPurchaseItemSerializer
    permission_classes = [IsAuthenticated]    
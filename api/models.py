from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    """Represents a product category."""
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name.capitalize()
    
class Supplier(models.Model):
    """Represents a supplier providing products to the store."""
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, blank=True, null=True, unique=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name.capitalize()
    
class Customer(models.Model):
    """Represents a customer who purchases products."""
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, blank=True, null=True, unique=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name.capitalize()
    
class Product(models.Model):
    """Represents a product available for sales."""
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    sellingPrice = models.DecimalField(max_digits=10, decimal_places=2)
    costPrice = models.DecimalField(max_digits=10, decimal_places=2)
    stockQuantity = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    productCategory = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='productCategory')

    def __str__(self):
        return self.name.capitalize()
    
class Sale(models.Model):
    """Represents a sale transaction made by a customer."""
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sale {self.id} - {self.sale_date}"
    
class SaleItem(models.Model):
    """Represents a product item in a sale transaction."""
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='sale')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='saleItems')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name} - {self.sale.id}"
    
    def save(self, *args, **kwargs):
        "Automatically set the price based on the product's selling price if not provided and update stock quantity and sale total"
        if not self.price:
            self.price = self.product.sellingPrice
        super().save(*args, **kwargs)
        self.product.stockQuantity -= self.quantity
        self.product.save()
        self.sale.total += self.quantity * self.price
        self.sale.save()
        
class Purchase(models.Model):
    """Represents a purchase transaction from a supplier."""
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="supplier")
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Purchase {self.id} - {self.purchase_date}"

class PurchaseItem(models.Model):
    """Represents a product item in a purchase transaction."""
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='purchase')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='purchaseItems')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} - {self.purchase.id}"
    
    def save(self, *args, **kwargs):
        "Automatically set the price based on the product's selling price if not provided and update stock quantity and purchase total"
        if not self.price:
            self.price = self.product.costPrice
        super().save(*args, **kwargs)
        self.product.stockQuantity += self.quantity
        self.product.save()
        self.purchase.total += self.quantity * self.price
        self.purchase.save()
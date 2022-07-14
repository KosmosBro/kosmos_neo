from rest_framework import serializers

from django.contrib.auth.models import User

from main.models import UserProfile, Supplier, Discount, Category, Product


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        if not username.isalnum():
            raise serializers.ValidationError(
                'The user name should only contain alphanumeric characters')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name']


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['id', 'discount']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'description']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    discount = DiscountSerializer(many=True)
    supplier = SupplierSerializer(many=True)

    class Meta:
        model = Product
        fields = ['title', 'description', 'creation_date', 'picture', 'price', 'category', 'discount', 'supplier']

    def create(self, validated_data):
        create_category = validated_data.pop('category')
        create_discount = validated_data.pop('discount')
        create_supplier = validated_data.pop('supplier')
        product = Product.objects.create(**validated_data)

        for category in create_category:
            Category.objects.create(product=product, **category)

        for discount in create_discount:
            Discount.objects.create(product=product, **discount)

        for supplier in create_supplier:
            Supplier.objects.create(product=product, **supplier)
        return product

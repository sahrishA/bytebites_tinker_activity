import pytest
from models import Customer, FoodItem, FoodCategory, Transaction


class TestCustomer:
    """Test cases for the Customer class."""

    def test_customer_initialization(self):
        """Test that a customer is initialized correctly."""
        customer = Customer("John Doe")
        assert customer.name == "John Doe"
        assert customer.purchase_history == []

    def test_add_transaction(self):
        """Test adding a transaction to customer's purchase history."""
        customer = Customer("Jane Smith")
        drinks = FoodCategory("Drinks")
        soda = FoodItem("Large Soda", 2.50, drinks, 4.5)
        transaction = Transaction(customer)
        transaction.add_item(soda)

        customer.add_transaction(transaction)
        assert len(customer.purchase_history) == 1
        assert customer.purchase_history[0] == transaction


class TestFoodCategory:
    """Test cases for the FoodCategory class."""

    def test_food_category_initialization(self):
        """Test that a food category is initialized correctly."""
        category = FoodCategory("Desserts")
        assert category.name == "Desserts"
        assert category.items == []

    def test_add_item(self):
        """Test adding items to a category."""
        category = FoodCategory("Burgers")
        burger = FoodItem("Spicy Burger", 8.99, category, 4.2)

        category.add_item(burger)
        assert len(category.items) == 1
        assert category.items[0] == burger

    def test_get_items_by_category(self):
        """Test getting all items in a category."""
        category = FoodCategory("Drinks")
        soda = FoodItem("Large Soda", 2.50, category, 4.5)
        juice = FoodItem("Orange Juice", 3.00, category, 3.8)

        category.add_item(soda)
        category.add_item(juice)

        items = category.get_items_by_category()
        assert len(items) == 2
        assert soda in items
        assert juice in items


class TestFoodItem:
    """Test cases for the FoodItem class."""

    def test_food_item_initialization(self):
        """Test that a food item is initialized correctly."""
        category = FoodCategory("Desserts")
        item = FoodItem("Chocolate Cake", 5.99, category, 4.7)

        assert item.name == "Chocolate Cake"
        assert item.price == 5.99
        assert item.category == category
        assert item.popularity_rating == 4.7

    def test_food_item_default_popularity(self):
        """Test that popularity rating defaults to 0.0."""
        category = FoodCategory("Appetizers")
        item = FoodItem("Nachos", 7.50, category)

        assert item.popularity_rating == 0.0


class TestTransaction:
    """Test cases for the Transaction class."""

    def test_transaction_initialization(self):
        """Test that a transaction is initialized correctly."""
        customer = Customer("Alice")
        transaction = Transaction(customer)

        assert transaction.customer == customer
        assert transaction.items == []
        assert transaction.total_cost == 0.0

    def test_add_item(self):
        """Test adding items to a transaction."""
        customer = Customer("Bob")
        transaction = Transaction(customer)
        drinks = FoodCategory("Drinks")
        burger_category = FoodCategory("Burgers")

        soda = FoodItem("Large Soda", 2.50, drinks, 4.5)
        burger = FoodItem("Cheese Burger", 9.99, burger_category, 4.8)

        transaction.add_item(soda)
        assert len(transaction.items) == 1
        assert transaction.items[0] == soda
        assert transaction.total_cost == 2.50

        transaction.add_item(burger)
        assert len(transaction.items) == 2
        assert transaction.total_cost == 12.49

    def test_compute_total(self):
        """Test computing total cost of items."""
        customer = Customer("Charlie")
        transaction = Transaction(customer)
        category = FoodCategory("Desserts")

        cake = FoodItem("Cake", 5.00, category)
        ice_cream = FoodItem("Ice Cream", 3.50, category)

        transaction.add_item(cake)
        transaction.add_item(ice_cream)

        total = transaction.compute_total()
        assert total == 8.50
        assert transaction.total_cost == 8.50

    def test_empty_transaction_total(self):
        """Test that empty transaction has zero total."""
        customer = Customer("Dave")
        transaction = Transaction(customer)

        assert transaction.compute_total() == 0.0
        assert transaction.total_cost == 0.0


class TestIntegration:
    """Integration tests for class relationships."""

    def test_complete_purchase_flow(self):
        """Test a complete customer purchase flow."""
        # Create customer
        customer = Customer("Emma")

        # Create categories and items
        drinks = FoodCategory("Drinks")
        burgers = FoodCategory("Burgers")

        soda = FoodItem("Large Soda", 2.50, drinks, 4.5)
        burger = FoodItem("Spicy Burger", 8.99, burgers, 4.2)

        # Add items to categories
        drinks.add_item(soda)
        burgers.add_item(burger)

        # Create transaction and add items
        transaction = Transaction(customer)
        transaction.add_item(soda)
        transaction.add_item(burger)

        # Add transaction to customer
        customer.add_transaction(transaction)

        # Verify everything is connected correctly
        assert customer.name == "Emma"
        assert len(customer.purchase_history) == 1
        assert customer.purchase_history[0] == transaction

        assert transaction.customer == customer
        assert len(transaction.items) == 2
        assert soda in transaction.items
        assert burger in transaction.items
        assert transaction.total_cost == 11.49

        assert soda.category == drinks
        assert burger.category == burgers
        assert soda in drinks.items
        assert burger in burgers.items


if __name__ == "__main__":
    pytest.main([__file__])
    
ByteBites UML Design
Classes and Relationships
1. Customer
Attributes:
name: str
purchase_history: List[Order]
Methods:
add_to_history(order: Order) -> None
2. Item
Attributes:
name: str
price: float
category: str
popularity_rating: int
Methods:
update_popularity(new_rating: int) -> None
3. Menu
Attributes:
items: List[Item]
Methods:
filter_by_category(category: str) -> List[Item]
add_item(item: Item) -> None
remove_item(item_name: str) -> None
4. Order
Attributes:
selected_items: List[Item]
total_cost: float
Methods:
compute_total() -> float
add_item(item: Item) -> None
remove_item(item_name: str) -> None
Relationships
Customer has a one-to-many relationship with Order.
Order has a many-to-many relationship with Item.
Menu aggregates Item objects.

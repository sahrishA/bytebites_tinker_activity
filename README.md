# Client Feature Request
We need to build the backend logic for the ByteBites app. The system needs to manage our customers, tracking their names and their past purchase history so the system can verify they are real users.

These customers need to browse specific food items (like a "Spicy Burger" or "Large Soda"), so we must track the name, price, category, and popularity rating for every item we sell.

We also need a way to manage the full collection of items — a digital list that holds all items and lets us filter by category such as "Drinks" or "Desserts".

Finally, when a user picks items, we need to group them into a single transaction. This transaction object should store the selected items and compute the total cost.


# Reflection
The main thing that students need to understand how to model a real-world system using object-oriented four classes : Customer, Item, Menu, and Order. Each has distinct tasks and respond with method calls.  Order.compute_total() logic can be complicated when they try to understnad it and knowing when to use it, since add_item and remove_item both need to keep total_cost in sync, which requires thinking about state carefully.

AI can be helpful when it come to udnerstand the class structure and docstrings quickly and suggesting edge cases in tests. However full rely on the AI can lead to misleading or wrong answer because it doesn't give/ suggest right answer all the time. You need to use your own logic to manipulate it. I can help student by asking them to trace through what happens to total_cost step by step when remove_item is called after that I wili explain what happend without giving answer

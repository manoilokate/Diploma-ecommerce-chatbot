import json
import random
from datetime import datetime, timedelta
from typing import List, Dict, Any

PRODUCTS = {
    "dresses": [
        {"name": "Luna",   "colors": ["Black", "White", "Red", "Blue"],         "sizes": ["XS", "S", "M", "L", "XL"],        "price": 49.99},
        {"name": "Stella", "colors": ["Navy", "Burgundy", "Green"],             "sizes": ["S", "M", "L", "XL"],              "price": 59.99},
        {"name": "Aurora", "colors": ["Pink", "Lavender", "Mint"],              "sizes": ["XS", "S", "M", "L"],              "price": 54.99},
        {"name": "Nicol",  "colors": ["Black", "Charcoal", "Beige"],            "sizes": ["S", "M", "L", "XL", "XXL"],       "price": 64.99},
        {"name": "Summer", "colors": ["Yellow", "Coral", "Turquoise"],          "sizes": ["XS", "S", "M", "L"],              "price": 44.99},
        {"name": "Verona", "colors": ["Black", "White", "Olive"],               "sizes": ["XS", "S", "M", "L", "XL"],        "price": 52.99},
        {"name": "Sofia",  "colors": ["Rose", "Sage", "Ivory"],                 "sizes": ["S", "M", "L"],                    "price": 57.99},
    ],
    "tops": [
        {"name": "Vega",   "colors": ["White", "Blue", "Black", "Grey"],        "sizes": ["XS", "S", "M", "L", "XL"],        "price": 29.99},
        {"name": "Cloud",  "colors": ["Cream", "Pink", "Lilac"],                "sizes": ["S", "M", "L"],                    "price": 34.99},
        {"name": "Silk",   "colors": ["Champagne", "Pearl", "Ivory"],           "sizes": ["XS", "S", "M", "L"],              "price": 39.99},
        {"name": "Cotton", "colors": ["White", "Black", "Navy", "Olive"],       "sizes": ["S", "M", "L", "XL"],              "price": 24.99},
        {"name": "Breeze", "colors": ["Sky Blue", "Mint", "Peach"],             "sizes": ["XS", "S", "M", "L"],              "price": 27.99},
        {"name": "Urban",  "colors": ["Black", "White", "Grey", "Red"],         "sizes": ["S", "M", "L", "XL", "XXL"],       "price": 32.99},
    ],
    "jeans": [
        {"name": "Classic",  "colors": ["Blue", "Black", "Grey"],               "sizes": ["26", "28", "30", "32", "34"],      "price": 69.99},
        {"name": "Slim",     "colors": ["Dark Blue", "Black"],                  "sizes": ["26", "28", "30", "32"],            "price": 74.99},
        {"name": "Straight", "colors": ["Blue", "Light Blue", "Black"],         "sizes": ["28", "30", "32", "34", "36"],      "price": 64.99},
        {"name": "Relaxed",  "colors": ["Blue", "Black", "Sand"],               "sizes": ["28", "30", "32", "34", "36"],      "price": 67.99},
    ],
    "skirts": [
        {"name": "Star",  "colors": ["Black", "Red", "Navy"],                   "sizes": ["XS", "S", "M", "L"],              "price": 39.99},
        {"name": "Midi",  "colors": ["Beige", "Brown", "Black"],                "sizes": ["S", "M", "L", "XL"],              "price": 44.99},
        {"name": "Pleat", "colors": ["Navy", "Burgundy", "Forest"],             "sizes": ["XS", "S", "M", "L"],              "price": 49.99},
        {"name": "Wrap",  "colors": ["Floral", "Stripe", "Solid Black"],        "sizes": ["XS", "S", "M", "L", "XL"],        "price": 42.99},
    ],
    "shoes": [
        {"name": "Comfort", "colors": ["Black", "White", "Beige"],              "sizes": ["36", "37", "38", "39", "40"],      "price": 89.99},
        {"name": "Sport",   "colors": ["White", "Black", "Grey", "Blue"],       "sizes": ["36", "37", "38", "39", "40", "41"], "price": 79.99},
        {"name": "Elegant", "colors": ["Black", "Nude", "Silver"],              "sizes": ["36", "37", "38", "39", "40"],      "price": 99.99},
        {"name": "Casual",  "colors": ["White", "Beige", "Brown"],              "sizes": ["36", "37", "38", "39", "40", "41"], "price": 69.99},
    ]
}

CUSTOMER_NAMES = [
    "Anna", "Maria", "Olena", "Kateryna", "Yulia", "Natalia", "Iryna", "Oksana",
    "Victoria", "Sophia", "Diana", "Elena", "Alina", "Daryna", "Anastasia",
    "Halyna", "Tetiana", "Svitlana", "Maryna", "Liudmyla",
    "Andrii", "Mykola", "Ivan", "Oleksandr", "Dmytro", "Serhii", "Vasyl", "Taras"
]

UKRAINIAN_CITIES = [
    "Kyiv", "Lviv", "Odesa", "Dnipro", "Kharkiv", "Zaporizhzhia", "Vinnytsia",
    "Poltava", "Chernihiv", "Cherkasy", "Zhytomyr", "Rivne", "Ternopil", "Kherson",
    "Ivano-Frankivsk", "Khmelnytskyi", "Sumy", "Mykolaiv", "Uzhhorod", "Lutsk",
    "Kremenchuk", "Bila Tserkva", "Kryvyi Rih", "Brovary", "Boryspil"
]

PAYMENT_METHODS = ["card", "cash"]

# ============================================================================
# PHRASES
# ============================================================================

USER_GREETINGS = [
    "Hi", "Hello", "Hey", "Good day", "Hi there", "Hello there",
    "Good morning", "Good afternoon", "Good evening", "Hey there",
    "Greetings", "Hi, I need help", "Hello, I want to order something", "",
]

ORDER_PHRASES = [
    "I want to order {product} in {color} size {size}",
    "I'd like to buy {product} {color} {size}",
    "Can I get {product} in {color}, size {size}?",
    "I need {product} {color} size {size}",
    "I want {product} size {size} color {color}",
    "I'm looking for {product} in {color} size {size}",
    "I'd like to purchase {product} in {color}, size {size}",
    "Please add {product} in {color} size {size} to my order",
    "I want to buy {product}, color {color}, size {size}",
    "Can you help me order {product} in {color} size {size}?",
    "I'll take {product} in {color}, size {size}",
    "Order {product} {color} size {size} for me please",
    "I'm interested in {product} in {color}, size {size}",
    "Could I order {product} in {color} size {size}?",
    "I'd love to get {product} in {color}, size {size}",
    "Can I place an order for {product} in {color} size {size}?",
    "I want to get {product} — {color}, size {size}",
    "Please help me order {product} in {color} size {size}",
    "I'd like {product} in {color} color, size {size}",
    "Can you order {product} in {color} size {size} for me?",
]

MULTI_ITEM_CONNECTORS = [
    ", and also ", ", also ", ", and ", ", plus ", ", and I need ",
    " as well as ", " together with ", ", additionally ",
]

PAYMENT_PHRASES = {
    "card": [
        "I'll pay by card", "Card payment", "Credit card", "Paying with card",
        "I want to pay by card", "Card please", "By card", "Debit card",
        "I'll use my card", "Card payment please", "Visa card",
        "I'll pay with my credit card", "Card is fine",
    ],
    "cash": [
        "Cash on delivery", "I'll pay cash", "COD please", "Cash payment",
        "I want to pay cash", "Cash", "Pay on delivery",
        "I'll pay when I receive it", "Cash on pickup",
        "Cash on arrival", "I prefer cash", "Pay cash upon delivery",
    ],
}

SIZE_CHANGE_PHRASES = [
    "Change size to {size}",
    "I want size {size} instead",
    "Can you change the size to {size}?",
    "Actually, make it size {size}",
    "Switch to size {size}",
    "I need size {size}, not {old_size}",
    "Please update the size to {size}",
    "Wrong size, I need {size}",
    "Can I change to size {size}?",
    "Swap the size to {size}",
    "I made a mistake, I need size {size}",
    "Could you change my size to {size}?",
    "I'd like to change the size from {old_size} to {size}",
]

COLOR_CHANGE_PHRASES = [
    "Change the color to {color}",
    "I want {color} instead",
    "Can you change color to {color}?",
    "Actually, I prefer {color}",
    "Switch to {color} color",
    "I need {color}, not {old_color}",
    "Please update the color to {color}",
    "Wrong color, I need {color}",
    "Can I get it in {color} instead?",
    "I'd prefer {color} color",
    "I made a mistake, I want {color}",
    "Could you change the color to {color}?",
    "I'd like to change the color from {old_color} to {color}",
]

CANCEL_PHRASES = [
    "Cancel my order",
    "I want to cancel",
    "Cancel the order please",
    "Please cancel my order",
    "I changed my mind, cancel it",
    "I don't want it anymore",
    "Cancel everything",
    "Can you cancel my order?",
    "I'd like to cancel my order",
    "Please remove my order",
    "Cancel it please",
    "I need to cancel my order",
    "I've changed my mind, I don't want it",
    "Please cancel the purchase",
    "I want to cancel the purchase",
]

TRACK_ORDER_PHRASES = [
    "Where is my order?",
    "What's the status of my order?",
    "Can you track my order?",
    "When will my order arrive?",
    "Track my delivery please",
    "What's happening with my order?",
    "Has my order been shipped?",
    "How long until my order arrives?",
    "I want to check my order status",
    "Any updates on my delivery?",
    "Check my order status please",
    "What's the delivery status?",
    "Is my order on its way?",
    "Can I get an update on my order?",
]

RETURN_PHRASES = [
    "I want to return my order",
    "How do I return an item?",
    "I'd like to make a return",
    "Can I return this?",
    "I want to send it back",
    "I'm not happy with my purchase",
    "The item doesn't fit, I want to return it",
    "I need to return something",
    "The item is not what I expected",
    "I want a refund",
    "I'd like to initiate a return",
    "Can I get my money back?",
]

SEARCH_PHRASES = [
    "What {category} do you have?",
    "Show me your {category}",
    "What's available in {category}?",
    "I'm looking for {category}",
    "Do you have any {category}?",
    "Show me {category} in {color}",
    "What {category} do you have in {color}?",
    "Browse your {category} collection",
    "What styles of {category} are available?",
    "Can you show me all {category}?",
    "What {category} options do you have?",
]

CONFIRMATION_PHRASES = [
    "Yes", "Yes please", "Sure", "Proceed", "Ok",
    "Sounds good", "Let's go", "Perfect", "Go ahead",
    "That works", "Confirmed", "Yep", "Absolutely",
    "Alright", "Let's do it", "Yes, proceed please",
]

ORDER_HISTORY_PHRASES = [
    "Show me my orders",
    "What are my previous orders?",
    "Order history please",
    "Can I see my order history?",
    "Show my past orders",
    "What have I ordered before?",
    "List my orders",
    "My purchase history",
    "Can you pull up my orders?",
]

AVAILABILITY_OK_RESPONSES = [
    "{product} in {color} size {size} is available! Price: ${price}. Ready to proceed?",
    "Great news! {product} ({color}, size {size}) is in stock. Price: ${price}. Shall we continue?",
    "{product} in {color}, size {size} — available at ${price}. Want to order?",
    "Yes, we have {product} in {color} size {size}. Price: ${price}. Proceed with order?",
    "In stock: {product} {color} size {size} for ${price}. Ready to place the order?",
    "Good news — {product} in {color} size {size} is available for ${price}. Shall we go ahead?",
]

PAYMENT_PROMPT_RESPONSES = [
    "Order created! How would you like to pay? (card/cash)",
    "Great! Your order is ready. Payment method — card or cash?",
    "Almost done! How will you pay — card or cash?",
    "Your order is set! Choose payment: card or cash?",
    "Order placed! Now, how would you like to pay?",
    "Perfect! One last step — card or cash payment?",
]

DELIVERY_PROMPT_RESPONSES = [
    "Payment confirmed! Now I need delivery details: name, phone, city, and post office number.",
    "Payment done! Please provide: your name, phone number, city, and Nova Poshta branch number.",
    "Great, payment confirmed! For delivery I need: name, phone, city, post office #.",
    "Paid! Please share your delivery info: name, phone, city, and post office number.",
    "Payment received! To complete your order, please give me your delivery details: name, phone, city, post office.",
]

ORDER_CONFIRMED_RESPONSES = [
    "Your order is confirmed! You'll receive the {product} in 2-3 business days. Thank you!",
    "All done! Your {product} will be delivered in 2-3 days. Thanks for shopping with us!",
    "Order confirmed! Expect your {product} within 2-3 business days. Thank you!",
    "Great! Your order for {product} is confirmed. Delivery in 2-3 days. Thank you!",
    "Everything is set! Your {product} will arrive in 2-3 business days. Enjoy!",
]

def get_random_product(category=None):
    if category:
        products = PRODUCTS[category]
    else:
        category = random.choice(list(PRODUCTS.keys()))
        products = PRODUCTS[category]
    product = random.choice(products)
    return {
        "category": category,
        "name": product["name"],
        "color": random.choice(product["colors"]),
        "size": random.choice(product["sizes"]),
        "price": product["price"],
        "all_colors": product["colors"],
        "all_sizes": product["sizes"],
        "full_name": f"{product['name']} {category[:-1]}"
    }

def generate_phone():
    return f"+380{random.randint(100000000, 999999999)}"

def generate_order_id():
    return random.randint(1000, 9999)

def format_delivery_address():
    return {
        "name": random.choice(CUSTOMER_NAMES),
        "phone": generate_phone(),
        "city": random.choice(UKRAINIAN_CITIES),
        "post_office": str(random.randint(1, 50))
    }

def make_user_message(greeting, order_phrase):
    return f"{greeting} {order_phrase}".strip() if greeting else order_phrase

def system_prompt():
    return "You are an AI shopping assistant for a Ukrainian clothing store. Help customers find and order clothes. Always check product availability before creating orders."


def generate_simple_order():
    product = get_random_product()
    order_id = generate_order_id()
    delivery = format_delivery_address()
    payment_method = random.choice(PAYMENT_METHODS)

    greeting = random.choice(USER_GREETINGS)
    order_phrase = random.choice(ORDER_PHRASES).format(
        product=product["full_name"], color=product["color"], size=product["size"]
    )
    user_message = make_user_message(greeting, order_phrase)

    return {
        "conversation_id": f"conv_{random.randint(10000, 99999)}",
        "scenario": "simple_order",
        "messages": [
            {"role": "system", "content": system_prompt()},
            {"role": "user", "content": user_message},
            {"role": "assistant", "tool_calls": [{"name": "check_product_availability", "arguments": {"product_name": product["name"], "color": product["color"], "size": product["size"]}}]},
            {"role": "tool", "name": "check_product_availability", "content": {"available": True, "stock_quantity": random.randint(3, 20), "price": product["price"]}},
            {"role": "assistant", "content": random.choice(AVAILABILITY_OK_RESPONSES).format(product=product["full_name"], color=product["color"], size=product["size"], price=product["price"])},
            {"role": "user", "content": random.choice(CONFIRMATION_PHRASES)},
            {"role": "assistant", "tool_calls": [{"name": "create_order", "arguments": {"product_name": product["name"], "color": product["color"], "size": product["size"], "quantity": 1}}]},
            {"role": "tool", "name": "create_order", "content": {"order_id": order_id, "status": "draft", "product": product["full_name"], "size": product["size"], "color": product["color"]}},
            {"role": "assistant", "content": random.choice(PAYMENT_PROMPT_RESPONSES)},
            {"role": "user", "content": random.choice(PAYMENT_PHRASES[payment_method])},
            {"role": "assistant", "tool_calls": [{"name": "confirm_payment", "arguments": {"payment_method": payment_method}}]},
            {"role": "tool", "name": "confirm_payment", "content": {"status": "paid", "transaction_id": f"TXN_{random.randint(1000, 9999)}"}},
            {"role": "assistant", "content": random.choice(DELIVERY_PROMPT_RESPONSES)},
            {"role": "user", "content": f"Name: {delivery['name']}, Phone: {delivery['phone']}, City: {delivery['city']}, Post office: {delivery['post_office']}"},
            {"role": "assistant", "tool_calls": [{"name": "add_delivery_details", "arguments": delivery}]},
            {"role": "tool", "name": "add_delivery_details", "content": {"delivery_id": f"DEL_{random.randint(100, 999)}"}},
            {"role": "assistant", "tool_calls": [{"name": "confirm_order", "arguments": {}}]},
            {"role": "tool", "name": "confirm_order", "content": {"confirmed_orders": [{"order_id": order_id, "status": "confirmed"}]}},
            {"role": "assistant", "content": random.choice(ORDER_CONFIRMED_RESPONSES).format(product=product["full_name"])},
        ]
    }


def generate_multi_item_order():
    num_items = random.randint(2, 3)
    products = [get_random_product() for _ in range(num_items)]
    order_ids = [generate_order_id() for _ in range(num_items)]
    delivery = format_delivery_address()
    payment_method = random.choice(PAYMENT_METHODS)

    greeting = random.choice(USER_GREETINGS)
    items_text = []
    for i, p in enumerate(products):
        phrase = random.choice(ORDER_PHRASES).format(
            product=p["full_name"], color=p["color"], size=p["size"]
        )
        items_text.append(phrase if i == 0 else random.choice(MULTI_ITEM_CONNECTORS) + phrase)

    user_message = make_user_message(greeting, "".join(items_text))

    conversation = {
        "conversation_id": f"conv_{random.randint(10000, 99999)}",
        "scenario": "multi_item_order",
        "messages": [
            {"role": "system", "content": system_prompt()},
            {"role": "user", "content": user_message},
        ]
    }

    for p in products:
        conversation["messages"].extend([
            {"role": "assistant", "tool_calls": [{"name": "check_product_availability", "arguments": {"product_name": p["name"], "color": p["color"], "size": p["size"]}}]},
            {"role": "tool", "name": "check_product_availability", "content": {"available": True, "stock_quantity": random.randint(3, 15), "price": p["price"]}},
        ])

    total_price = sum(p["price"] for p in products)
    conversation["messages"].append({"role": "assistant", "content": f"All {num_items} items are available! Total: ${total_price:.2f}. Ready to proceed with payment?"})
    conversation["messages"].append({"role": "user", "content": random.choice(CONFIRMATION_PHRASES)})

    for i, p in enumerate(products):
        conversation["messages"].extend([
            {"role": "assistant", "tool_calls": [{"name": "create_order", "arguments": {"product_name": p["name"], "color": p["color"], "size": p["size"], "quantity": 1}}]},
            {"role": "tool", "name": "create_order", "content": {"order_id": order_ids[i], "status": "draft", "product": p["full_name"], "size": p["size"], "color": p["color"]}},
        ])

    conversation["messages"].extend([
        {"role": "assistant", "content": random.choice(PAYMENT_PROMPT_RESPONSES)},
        {"role": "user", "content": random.choice(PAYMENT_PHRASES[payment_method])},
        {"role": "assistant", "tool_calls": [{"name": "confirm_payment", "arguments": {"payment_method": payment_method}}]},
        {"role": "tool", "name": "confirm_payment", "content": {"status": "paid", "transaction_id": f"TXN_{random.randint(1000, 9999)}"}},
        {"role": "assistant", "content": random.choice(DELIVERY_PROMPT_RESPONSES)},
        {"role": "user", "content": f"{delivery['name']}, {delivery['phone']}, {delivery['city']}, Post {delivery['post_office']}"},
        {"role": "assistant", "tool_calls": [{"name": "add_delivery_details", "arguments": delivery}]},
        {"role": "tool", "name": "add_delivery_details", "content": {"delivery_id": f"DEL_{random.randint(100, 999)}"}},
        {"role": "assistant", "tool_calls": [{"name": "confirm_order", "arguments": {}}]},
        {"role": "tool", "name": "confirm_order", "content": {"confirmed_orders": [{"order_id": oid, "status": "confirmed"} for oid in order_ids]}},
        {"role": "assistant", "content": f"All {num_items} orders confirmed! You'll receive your items in 2-3 business days. Thank you!"},
    ])

    return conversation


def generate_size_change_conversation():
    product = get_random_product()
    order_id = generate_order_id()

    old_size = product["size"]
    available_sizes = [s for s in product["all_sizes"] if s != old_size]
    new_size = random.choice(available_sizes) if available_sizes else old_size

    conversation = generate_simple_order()
    conversation["scenario"] = "order_with_size_change"

    change_phrase = random.choice(SIZE_CHANGE_PHRASES).format(size=new_size, old_size=old_size)

    conversation["messages"].extend([
        {"role": "user", "content": change_phrase},
        {"role": "assistant", "tool_calls": [{"name": "get_current_order_context", "arguments": {}}]},
        {"role": "tool", "name": "get_current_order_context", "content": {"active_orders": [{"order_id": order_id, "product": product["full_name"], "size": old_size, "color": product["color"], "status": "confirmed"}]}},
        {"role": "assistant", "content": f"Found your order for {product['full_name']}. Let me check if I can still update the size."},
        {"role": "assistant", "tool_calls": [{"name": "update_order_item", "arguments": {"order_id": order_id, "field": "size", "new_value": new_size}}]},
    ])

    if random.choice([True, False]):
        conversation["messages"].extend([
            {"role": "tool", "name": "update_order_item", "content": {"order_id": order_id, "updated": True, "new_status": "confirmed", "message": f"Size updated to {new_size}"}},
            {"role": "assistant", "content": f"Done! Size successfully changed from {old_size} to {new_size}."},
        ])
    else:
        conversation["messages"].extend([
            {"role": "tool", "name": "update_order_item", "content": {"updated": False, "message": "Order already in processing. Cannot update."}},
            {"role": "assistant", "content": f"Sorry, your order is already being processed and can't be modified. Would you like to cancel and reorder in size {new_size}?"},
            {"role": "user", "content": random.choice(["Yes please", "Cancel and reorder", "Sure", "Let's do that"])},
            {"role": "assistant", "tool_calls": [{"name": "cancel_order", "arguments": {"order_id": order_id}}]},
            {"role": "tool", "name": "cancel_order", "content": {"cancelled": True, "refund_amount": product["price"], "message": "Order cancelled successfully"}},
            {"role": "assistant", "content": f"Order cancelled. Refund of ${product['price']} will be processed. Shall I place a new order in size {new_size}?"},
        ])

    return conversation


def generate_color_change_conversation():
    product = get_random_product()
    order_id = generate_order_id()

    old_color = product["color"]
    available_colors = [c for c in product["all_colors"] if c != old_color]
    new_color = random.choice(available_colors) if available_colors else old_color

    conversation = generate_simple_order()
    conversation["scenario"] = "order_with_color_change"

    change_phrase = random.choice(COLOR_CHANGE_PHRASES).format(color=new_color, old_color=old_color)

    conversation["messages"].extend([
        {"role": "user", "content": change_phrase},
        {"role": "assistant", "tool_calls": [{"name": "get_current_order_context", "arguments": {}}]},
        {"role": "tool", "name": "get_current_order_context", "content": {"active_orders": [{"order_id": order_id, "product": product["full_name"], "size": product["size"], "color": old_color, "status": "confirmed"}]}},
        {"role": "assistant", "content": f"Found your order for {product['full_name']}. Let me try to update the color."},
        {"role": "assistant", "tool_calls": [{"name": "update_order_item", "arguments": {"order_id": order_id, "field": "color", "new_value": new_color}}]},
    ])

    if random.choice([True, False]):
        conversation["messages"].extend([
            {"role": "tool", "name": "update_order_item", "content": {"order_id": order_id, "updated": True, "new_status": "confirmed", "message": f"Color updated to {new_color}"}},
            {"role": "assistant", "content": f"Done! Color successfully changed from {old_color} to {new_color}."},
        ])
    else:
        conversation["messages"].extend([
            {"role": "tool", "name": "update_order_item", "content": {"updated": False, "message": "Order already in processing. Cannot update."}},
            {"role": "assistant", "content": f"Unfortunately the order is already being processed. Would you like to cancel and reorder in {new_color}?"},
            {"role": "user", "content": random.choice(["Yes please", "Sure", "Yes, do that", "Let's do it"])},
            {"role": "assistant", "tool_calls": [{"name": "cancel_order", "arguments": {"order_id": order_id}}]},
            {"role": "tool", "name": "cancel_order", "content": {"cancelled": True, "refund_amount": product["price"]}},
            {"role": "assistant", "content": f"Order cancelled. Refund of ${product['price']} will be processed. Shall I place a new order in {new_color}?"},
        ])

    return conversation


def generate_cancellation_conversation():
    product = get_random_product()
    order_id = generate_order_id()

    return {
        "conversation_id": f"conv_{random.randint(10000, 99999)}",
        "scenario": "order_cancellation",
        "messages": [
            {"role": "system", "content": system_prompt()},
            {"role": "user", "content": random.choice(CANCEL_PHRASES)},
            {"role": "assistant", "tool_calls": [{"name": "get_current_order_context", "arguments": {}}]},
            {"role": "tool", "name": "get_current_order_context", "content": {"active_orders": [{"order_id": order_id, "product": product["full_name"], "size": product["size"], "color": product["color"], "status": random.choice(["draft", "paid", "confirmed"])}]}},
            {"role": "assistant", "content": f"Found your order for {product['full_name']} ({product['color']}, size {product['size']}). Cancelling now..."},
            {"role": "assistant", "tool_calls": [{"name": "cancel_order", "arguments": {"order_id": order_id}}]},
            {"role": "tool", "name": "cancel_order", "content": {"cancelled": True, "refund_amount": product["price"], "message": "Order cancelled successfully"}},
            {"role": "assistant", "content": f"Your order has been cancelled. Refund of ${product['price']} will be processed within 3-5 business days."},
        ]
    }


def generate_out_of_stock_conversation():
    product = get_random_product()

    return {
        "conversation_id": f"conv_{random.randint(10000, 99999)}",
        "scenario": "out_of_stock",
        "messages": [
            {"role": "system", "content": system_prompt()},
            {"role": "user", "content": random.choice(ORDER_PHRASES).format(product=product["full_name"], color=product["color"], size=product["size"])},
            {"role": "assistant", "tool_calls": [{"name": "check_product_availability", "arguments": {"product_name": product["name"], "color": product["color"], "size": product["size"]}}]},
            {"role": "tool", "name": "check_product_availability", "content": {"available": False, "stock_quantity": 0, "price": product["price"]}},
            {"role": "assistant", "content": f"I'm sorry, {product['full_name']} in {product['color']} size {product['size']} is currently out of stock. Would you like to:\n1. Choose a different size or color\n2. Get notified when it's back in stock"},
        ]
    }


def generate_order_history_conversation():
    past_orders = []
    for _ in range(random.randint(2, 5)):
        p = get_random_product()
        past_orders.append({
            "order_id": generate_order_id(),
            "product": p["full_name"],
            "color": p["color"],
            "size": p["size"],
            "status": random.choice(["delivered", "shipped", "confirmed"]),
            "date": (datetime.now() - timedelta(days=random.randint(1, 90))).strftime("%Y-%m-%d")
        })

    return {
        "conversation_id": f"conv_{random.randint(10000, 99999)}",
        "scenario": "order_history",
        "messages": [
            {"role": "system", "content": system_prompt()},
            {"role": "user", "content": random.choice(ORDER_HISTORY_PHRASES)},
            {"role": "assistant", "tool_calls": [{"name": "get_order_history", "arguments": {"limit": 10}}]},
            {"role": "tool", "name": "get_order_history", "content": {"orders": past_orders}},
            {"role": "assistant", "content": "Here are your recent orders:\n\n" + "\n".join([
                f"• {o['product']} ({o['color']}, size {o['size']}) — {o['status']} — {o['date']}"
                for o in past_orders
            ])},
        ]
    }


def generate_track_order_conversation():
    product = get_random_product()
    order_id = generate_order_id()
    status = random.choice(["processing", "shipped", "out_for_delivery", "delivered"])

    status_messages = {
        "processing":       "Your order is being processed and will be shipped soon.",
        "shipped":          f"Your order has been shipped! Tracking number: UA{random.randint(10000000, 99999999)}. Expected delivery: 1-2 days.",
        "out_for_delivery": "Great news! Your order is out for delivery today.",
        "delivered":        "Your order has been delivered. We hope you enjoy your purchase!",
    }

    return {
        "conversation_id": f"conv_{random.randint(10000, 99999)}",
        "scenario": "track_order",
        "messages": [
            {"role": "system", "content": system_prompt()},
            {"role": "user", "content": random.choice(TRACK_ORDER_PHRASES)},
            {"role": "assistant", "tool_calls": [{"name": "get_current_order_context", "arguments": {}}]},
            {"role": "tool", "name": "get_current_order_context", "content": {"active_orders": [{"order_id": order_id, "product": product["full_name"], "size": product["size"], "color": product["color"], "status": status}]}},
            {"role": "assistant", "tool_calls": [{"name": "track_order", "arguments": {"order_id": order_id}}]},
            {"role": "tool", "name": "track_order", "content": {"order_id": order_id, "status": status, "product": product["full_name"], "estimated_delivery": (datetime.now() + timedelta(days=random.randint(1, 3))).strftime("%Y-%m-%d")}},
            {"role": "assistant", "content": f"Order #{order_id} ({product['full_name']}): {status_messages[status]}"},
        ]
    }


def generate_return_request_conversation():
    product = get_random_product()
    order_id = generate_order_id()
    return_id = f"RET_{random.randint(1000, 9999)}"

    reasons = [
        "doesn't fit", "wrong color received", "not as described",
        "changed my mind", "received wrong item", "quality issue",
        "item is damaged", "wrong size delivered",
    ]

    return {
        "conversation_id": f"conv_{random.randint(10000, 99999)}",
        "scenario": "return_request",
        "messages": [
            {"role": "system", "content": system_prompt()},
            {"role": "user", "content": random.choice(RETURN_PHRASES)},
            {"role": "assistant", "tool_calls": [{"name": "get_order_history", "arguments": {"limit": 5}}]},
            {"role": "tool", "name": "get_order_history", "content": {"orders": [{"order_id": order_id, "product": product["full_name"], "color": product["color"], "size": product["size"], "status": "delivered", "date": (datetime.now() - timedelta(days=random.randint(1, 14))).strftime("%Y-%m-%d")}]}},
            {"role": "assistant", "content": f"I found your recent order: {product['full_name']} ({product['color']}, size {product['size']}). What is the reason for the return?"},
            {"role": "user", "content": random.choice(reasons)},
            {"role": "assistant", "tool_calls": [{"name": "create_return_request", "arguments": {"order_id": order_id, "reason": random.choice(reasons)}}]},
            {"role": "tool", "name": "create_return_request", "content": {"return_id": return_id, "status": "approved", "refund_amount": product["price"], "instructions": "Drop off at any Nova Poshta branch within 14 days."}},
            {"role": "assistant", "content": f"Return #{return_id} approved! Refund of ${product['price']} will be processed after we receive the item. Please drop it off at any Nova Poshta branch within 14 days."},
        ]
    }


def generate_search_products_conversation():
    category = random.choice(list(PRODUCTS.keys()))
    color = random.choice(["Black", "White", "Blue", "Red", "Beige", "Pink"])

    available = PRODUCTS[category]
    results = [{"name": p["name"], "colors": p["colors"], "price": p["price"], "sizes": p["sizes"]} for p in available]

    use_color = random.choice([True, False])

    if use_color:
        phrase = random.choice(SEARCH_PHRASES).format(category=category, color=color)
        filtered = [p for p in results if color in p["colors"]]
        tool_args = {"category": category, "color": color}
    else:
        phrase = random.choice(SEARCH_PHRASES).format(category=category, color="any").replace(" in any", "").replace(" any", "")
        filtered = results
        tool_args = {"category": category}

    filtered = filtered if filtered else results
    greeting = random.choice(USER_GREETINGS)
    user_message = make_user_message(greeting, phrase)

    return {
        "conversation_id": f"conv_{random.randint(10000, 99999)}",
        "scenario": "search_products",
        "messages": [
            {"role": "system", "content": system_prompt()},
            {"role": "user", "content": user_message},
            {"role": "assistant", "tool_calls": [{"name": "search_products", "arguments": tool_args}]},
            {"role": "tool", "name": "search_products", "content": {"category": category, "results": filtered, "total": len(filtered)}},
            {"role": "assistant", "content": f"Here's what we have in {category}:\n\n" + "\n".join([
                f"• {p['name']} — ${p['price']} | Colors: {', '.join(p['colors'])} | Sizes: {', '.join(p['sizes'])}"
                for p in filtered[:5]
            ]) + "\n\nWould you like to order any of these?"},
        ]
    }


def generate_dataset(total_examples=8000):
    print(f"Generating {total_examples} conversation examples...")
    print("="*70)

    scenario_distribution = {
        "simple_order":             0.25,
        "multi_item_order":         0.20,
        "search_products":          0.15,
        "order_with_size_change":   0.10,
        "order_with_color_change":  0.08,
        "track_order":              0.08,
        "order_cancellation":       0.06,
        "return_request":           0.04,
        "out_of_stock":             0.02,
        "order_history":            0.02,
    }

    scenario_counts = {s: int(total_examples * p) for s, p in scenario_distribution.items()}
    diff = total_examples - sum(scenario_counts.values())
    scenario_counts["simple_order"] += diff

    print("Scenario distribution:")
    for scenario, count in scenario_counts.items():
        print(f"  {scenario:30s}: {count:5d} ({count/total_examples*100:5.1f}%)")
    print()

    generators = {
        "simple_order":             generate_simple_order,
        "multi_item_order":         generate_multi_item_order,
        "order_with_size_change":   generate_size_change_conversation,
        "order_with_color_change":  generate_color_change_conversation,
        "order_cancellation":       generate_cancellation_conversation,
        "out_of_stock":             generate_out_of_stock_conversation,
        "order_history":            generate_order_history_conversation,
        "track_order":              generate_track_order_conversation,
        "return_request":           generate_return_request_conversation,
        "search_products":          generate_search_products_conversation,
    }

    dataset = []
    for scenario, count in scenario_counts.items():
        print(f"Generating {scenario}... ", end="", flush=True)
        for i in range(count):
            try:
                dataset.append(generators[scenario]())
                if (i + 1) % 100 == 0:
                    print(f"{i+1}...", end="", flush=True)
            except Exception as e:
                print(f"\nError in {scenario}: {e}")
        print(f" ✓ {count}")

    print(f"\n{'='*70}")
    print(f"Total conversations generated: {len(dataset)}")

    random.shuffle(dataset)
    return dataset


def save_dataset(dataset, output_path="ecommerce_function_calling_dataset.json"):
    dataset_wrapper = {
        "metadata": {
            "total_conversations": len(dataset),
            "generated_date": datetime.now().isoformat(),
            "version": "2.0",
            "domain": "e-commerce / clothing",
            "language": "English",
            "target_audience": "Ukrainian customers",
            "scenarios": list(set(conv["scenario"] for conv in dataset))
        },
        "conversations": dataset
    }
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(dataset_wrapper, f, indent=2, ensure_ascii=False)
    print(f"\nDataset saved to: {output_path}")


if __name__ == "__main__":
    print("="*70)
    print("E-COMMERCE FUNCTION CALLING DATASET GENERATOR v2.0")
    print("Domain: Clothing | Language: English")
    print("="*70)
    print()

    random.seed(None)

    dataset = generate_dataset(total_examples=12000)

    print("\nSaving dataset...")
    save_dataset(dataset, "ecommerce_function_calling_12000.json")

    print(f"\n{'='*70}")
    print("SAMPLE CONVERSATION")
    print(f"{'='*70}")

    sample = random.choice(dataset)
    print(f"\nScenario: {sample['scenario']}")
    print(f"Messages: {len(sample['messages'])}")
    print("-"*70)
    for msg in sample['messages'][:4]:
        print(f"\n[{msg['role'].upper()}]")
        if 'content' in msg and msg['content']:
            print(str(msg['content'])[:200])
        if 'tool_calls' in msg:
            for tc in msg['tool_calls']:
                print(f"→ {tc['name']}({tc['arguments']})")

    print("\nGENERATION COMPLETED SUCCESSFULLY!")

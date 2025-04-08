import redis
import json

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def add_to_cart(cart_id, item_name, quantity, price):
    """
    Додає товар до корзини в Redis
    """
    item_data = {
        'name': item_name,
        'quantity': quantity,
        'price': price
    }
    
    redis_client.hset(f"cart:{cart_id}", item_name, json.dumps(item_data))
    print(f"Додано {quantity} {item_name} до корзини {cart_id}")

if __name__ == "__main__":
    try:
        add_to_cart("user123", "apple", 3, 0.5)
        add_to_cart("user123", "banana", 2, 0.3)
        add_to_cart("user123", "orange", 4, 0.6)
        
        add_to_cart("user456", "milk", 1, 2.5)
        
    except redis.RedisError as e:
        print(f"Помилка при роботі з Redis: {e}")
import redis
import json

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def read_cart(cart_id):
    """
    Читає і виводить вміст корзини
    """
    try:
        cart_items = redis_client.hgetall(f"cart:{cart_id}")
        
        if not cart_items:
            print(f"Корзина {cart_id} порожня або не існує")
            return
            
        print(f"\nВміст корзини {cart_id}:")
        print("-" * 40)
        
        total = 0
        for item_name, item_data in cart_items.items():
            item = json.loads(item_data.decode('utf-8'))
            subtotal = item['quantity'] * item['price']
            total += subtotal
            
            print(f"Товар: {item['name']}")
            print(f"Кількість: {item['quantity']}")
            print(f"Ціна за одиницю: ${item['price']:.2f}")
            print(f"Вартість: ${subtotal:.2f}")
            print("-" * 40)
            
        print(f"Загальна сума: ${total:.2f}")
        
    except redis.RedisError as e:
        print(f"Помилка при роботі з Redis: {e}")
    except json.JSONDecodeError as e:
        print(f"Помилка при парсингу даних: {e}")

if __name__ == "__main__":
    read_cart("user123")
    read_cart("user456")
    read_cart("user789")  # неіснуюча корзина
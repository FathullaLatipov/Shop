from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

products = [
    {
        "id": 1, 
        "img": "product-1.jpg", 
        "name": "Sony camera", 
        "price": 450.00, 
        "old_price": 550.00, 
        "description": "Capture stunning photos and videos with the Sony camera. Featuring advanced technology, this camera offers superior image quality and exceptional performance in various lighting conditions. The sleek design and intuitive controls make it easy to use for both beginners and professionals. With multiple shooting modes and customizable settings, you can unleash your creativity and take your photography to the next level."
    },
    {
        "id": 2, 
        "img": "product-2.jpg", 
        "name": "Blue sweater", 
        "price": 120.00, 
        "old_price": 150.00, 
        "description": "Stay warm and stylish with this cozy blue sweater. Made from high-quality, soft fabric, this sweater provides ultimate comfort and warmth during the cold months. The elegant design and versatile color make it a perfect addition to any wardrobe, suitable for both casual outings and relaxed days at home. Pair it with your favorite jeans or trousers for a complete look."
    },
    {
        "id": 3, 
        "img": "product-3.jpg", 
        "name": "Lamp", 
        "price": 150.00, 
        "old_price": 180.00, 
        "description": "Illuminate your space with this elegant lamp, combining functionality with aesthetic appeal. The lamp features a sleek and modern design that complements any room decor. It provides adjustable lighting to suit your needs, whether you need bright light for reading or a soft glow for a cozy atmosphere. Crafted from durable materials, this lamp is built to last and enhance your living space."
    },
    {
        "id": 4, 
        "img": "product-4.jpg", 
        "name": "Sneaker", 
        "price": 375.00, 
        "old_price": 395.00, 
        "description": "Experience unmatched comfort and style with these trendy sneakers. Designed for both casual wear and athletic activities, these sneakers provide excellent support and cushioning. The breathable material ensures your feet stay cool and dry, while the durable sole offers great traction on various surfaces. Perfect for everyday use, these sneakers will quickly become your go-to footwear."
    },
    {
        "id": 5, 
        "img": "product-5.jpg", 
        "name": "Drone", 
        "price": 850.00, 
        "old_price": 950.00, 
        "description": "Explore the skies with this high-performance drone. Equipped with advanced features such as a high-definition camera and GPS navigation, this drone allows you to capture breathtaking aerial photos and videos. The user-friendly controls and stable flight capabilities make it suitable for both beginners and experienced pilots. Enjoy hours of fun and creativity with this state-of-the-art drone."
    },
    {
        "id": 6, 
        "img": "product-6.jpg", 
        "name": "Apple Watch", 
        "price": 399.00, 
        "old_price": 499.00, 
        "description": "Stay connected and track your fitness with the Apple Watch. This sleek and stylish smartwatch offers a range of features including heart rate monitoring, activity tracking, and notifications for calls and messages. With its customizable watch faces and interchangeable bands, you can personalize your Apple Watch to match your style. It's the perfect blend of technology and fashion for your wrist."
    },
    {
        "id": 7, 
        "img": "product-7.jpg", 
        "name": "Black shirt", 
        "price": 120.00, 
        "old_price": 190.00, 
        "description": "Elevate your wardrobe with this classic black shirt. Crafted from premium materials, this shirt offers a comfortable fit and a polished look. Its versatile design makes it suitable for both formal occasions and casual outings. Pair it with trousers for a professional appearance or with jeans for a more relaxed vibe. This timeless piece is a must-have for any fashion-conscious individual."
    },
    {
        "id": 8, 
        "img": "product-8.jpg", 
        "name": "Cream set", 
        "price": 430.00, 
        "old_price": 450.00, 
        "description": "Pamper yourself with this luxurious cream set. Designed to nourish and rejuvenate your skin, each product in the set is formulated with high-quality ingredients that provide deep hydration and a radiant glow. Whether you're looking to soothe dry skin or reduce signs of aging, this cream set has everything you need for a complete skincare routine. Indulge in a spa-like experience at home and enjoy healthier, more youthful-looking skin."
    },
]


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>', methods=['GET'])
def product_detail(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product is not None:
        return render_template('detail.html', product=product)
    else:
        return "Product not found", 404
    
@app.route('/policy', methods=['GET'])
def policy():
    return render_template('policy.html')

if __name__ == '__main__':
    app.run(debug=True)

import stripe

from config.settings import STRIPE_SECRET_KEY

stripe.api_key = STRIPE_SECRET_KEY


def create_stripe_product(payment):
    """
    Создает продукт в stripe.
    """
    if not (payment.course_paid or payment.lesson_paid):
        raise ValueError("Плажет должен содержать либо id курса, либо id урока")
    product = payment.course_paid if payment.course_paid else payment.lesson_paid

    try:
        stripe_product = stripe.Product.create(name=product)
    except stripe.error.StripeError as e:
        print(f"Stripe error: {e}")
        raise
    return stripe_product.get('id')


def create_stripe_price(amount, product_id):
    """
    Создает цену в stripe.
    """
    return stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        product_data={"name": product_id},
    )


def create_stripe_session(price):
    """
    Создает сессию на оплату в stripe.
    """
    session = stripe.checkout.Session.create(
        success_url="http://localhost:8000",
        line_items=[{"price": price.get('id'), "quantity": 1}],
        mode="payment",
    )
    return session.get('id'), session.get('url')

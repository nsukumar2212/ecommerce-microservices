import { Link } from 'react-router-dom'
import { useCart } from '../context/CartContext'

function Checkout() {
  const { cartItems } = useCart()

  const total = cartItems.reduce(
    (sum, item) => sum + item.price * item.quantity,
    0
  )

  if (cartItems.length === 0) {
    return (
      <main className="checkout-page">
        <h2>Checkout</h2>
        <p>Your cart is empty.</p>
      </main>
    )
  }

  return (
    <main className="checkout-page">
      <h2>Checkout</h2>

      <section className="checkout-address">
        <h3>Delivery Address</h3>

        <input
          type="text"
          placeholder="Full Name"
        />

        <input
          type="text"
          placeholder="Phone Number"
        />

        <textarea
          placeholder="Address"
        />

        <input
          type="text"
          placeholder="City"
        />

        <input
          type="text"
          placeholder="Pincode"
        />
      </section>

      <section className="checkout-summary">
        <h3>Order Summary</h3>

        {cartItems.map((item) => (
          <div
            className="checkout-item"
            key={item.id}
          >
            <p>
              {item.name} × {item.quantity}
            </p>

            <p>
              ₹{(item.price * item.quantity).toLocaleString('en-IN')}
            </p>
          </div>
        ))}

        <hr />

        <h3>
          Total: ₹{total.toLocaleString('en-IN')}
        </h3>

        <Link
  to="/payment"
  className="proceed-payment-button"
>
  Proceed to Payment
</Link>

      </section>
    </main>
  )
}

export default Checkout
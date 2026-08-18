import { Link } from 'react-router-dom'
import { useCart } from '../context/CartContext'

function Payment() {
  const { cartItems } = useCart()

  const total = cartItems.reduce(
    (sum, item) => sum + item.price * item.quantity,
    0
  )

  if (cartItems.length === 0) {
    return (
      <main className="payment-page">
        <div className="payment-card">
          <h2>No Items to Pay</h2>
          <p>Your cart is empty.</p>
        </div>
      </main>
    )
  }

  return (
    <main className="payment-page">
      <div className="payment-card">
        <h2>Payment</h2>

        <p className="payment-subtitle">
          Choose your preferred payment method
        </p>

        <div className="payment-methods">
          <label className="payment-option">
            <input
              type="radio"
              name="payment"
              value="card"
              defaultChecked
            />
            <span>💳 Credit / Debit Card</span>
          </label>

          <label className="payment-option">
            <input
              type="radio"
              name="payment"
              value="upi"
            />
            <span>📱 UPI</span>
          </label>

          <label className="payment-option">
            <input
              type="radio"
              name="payment"
              value="cod"
            />
            <span>💵 Cash on Delivery</span>
          </label>
        </div>

        <div className="payment-summary">
          <p>Items: {cartItems.length}</p>

          <h3>
            Total: ₹{total.toLocaleString('en-IN')}
          </h3>
        </div>

        <Link
  to="/order-success"
  className="pay-button"
>
  Pay ₹{total.toLocaleString('en-IN')}
</Link>
      </div>
    </main>
  )
}

export default Payment
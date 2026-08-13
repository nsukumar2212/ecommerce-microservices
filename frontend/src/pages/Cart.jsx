import { Link } from 'react-router-dom'
import { useCart } from '../context/CartContext'

function Cart() {
  const {
    cartItems,
    increaseQuantity,
    decreaseQuantity,
    removeFromCart
  } = useCart()

  const total = cartItems.reduce(
    (sum, item) => sum + item.price * item.quantity,
    0
  )

  if (cartItems.length === 0) {
    return (
      <main className="cart-page">
        <h2>Your Cart</h2>

        <div className="cart-empty">
          <h3>Your cart is empty</h3>
          <p>Add some electronics to your cart to see them here.</p>
        </div>
      </main>
    )
  }

  return (
    <main className="cart-page">
      <h2>Your Cart</h2>

      <div className="cart-items">
        {cartItems.map((item) => (
          <div className="cart-item" key={item.id}>
            <img
              src={item.image}
              alt={item.name}
              className="cart-item-image"
            />

            <div className="cart-item-info">
              <h3>{item.name}</h3>
              <p>{item.brand}</p>
              <p>₹{item.price}</p>

              <div className="quantity-controls">
                <button
                  onClick={() => decreaseQuantity(item.id)}
                >
                  -
                </button>

                <span>{item.quantity}</span>

                <button
                  onClick={() => increaseQuantity(item.id)}
                >
                  +
                </button>
              </div>

              <button
                onClick={() => removeFromCart(item.id)}
              >
                Remove
              </button>
            </div>
          </div>
        ))}
      </div>

      <div className="cart-summary">
        <h3>Order Summary</h3>

        <p>
          Total: ₹{total.toLocaleString('en-IN')}
        </p>

        <Link to="/checkout">
  Proceed to Checkout
</Link>
      </div>
    </main>
  )
}

export default Cart
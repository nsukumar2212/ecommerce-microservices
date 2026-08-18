import { Link } from 'react-router-dom'

function OrderSuccess() {
  const orderId = 'ORD' + Math.floor(100000 + Math.random() * 900000)

  return (
    <main className="order-success-page">
      <div className="order-success-card">

        <div className="success-icon">
          ✓
        </div>

        <h2>Order Placed Successfully!</h2>

        <p className="success-message">
          Thank you for your purchase. Your order has been
          placed successfully.
        </p>

        <div className="success-order-info">
          <p>
            Order ID
          </p>

          <strong>
            {orderId}
          </strong>
        </div>

        <p className="success-delivery">
          Your order will be processed and delivered soon.
        </p>

        <div className="success-actions">
          <Link
            to="/orders"
            className="view-orders-button"
          >
            View My Orders
          </Link>

          <Link
            to="/products"
            className="continue-shopping-button"
          >
            Continue Shopping
          </Link>
        </div>

      </div>
    </main>
  )
}

export default OrderSuccess
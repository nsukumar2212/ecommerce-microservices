import { Link, useParams } from 'react-router-dom'

function OrderDetails() {
  const { orderId } = useParams()

  const orders = {
    ORD1001: {
      id: 'ORD1001',
      date: '18 Aug 2026',
      status: 'Delivered',
      paymentMethod: 'Credit / Debit Card',
      address: 'Bangalore, Karnataka - 560001',
      items: [
        {
          name: 'iPhone 16',
          quantity: 1,
          price: 79999,
          image: '/images/products/iphone16.jpg'
        }
      ]
    },

    ORD1002: {
      id: 'ORD1002',
      date: '15 Aug 2026',
      status: 'Shipped',
      paymentMethod: 'UPI',
      address: 'Bangalore, Karnataka - 560002',
      items: [
        {
          name: 'MacBook Air M3',
          quantity: 1,
          price: 99999,
          image: '/images/products/macbook-air.jpg'
        }
      ]
    },

    ORD1003: {
      id: 'ORD1003',
      date: '10 Aug 2026',
      status: 'Processing',
      paymentMethod: 'Cash on Delivery',
      address: 'Bangalore, Karnataka - 560003',
      items: [
        {
          name: 'AirPods Pro 2',
          quantity: 1,
          price: 24999,
          image: '/images/products/airpods-pro2.jpg'
        },
        {
          name: 'JBL Charge 5',
          quantity: 1,
          price: 14999,
          image: '/images/products/jbl-charge5.jpg'
        }
      ]
    }
  }

  const order = orders[orderId]

  if (!order) {
    return (
      <main className="order-details-page">
        <div className="order-not-found">
          <h2>Order Not Found</h2>
          <p>We couldn't find the requested order.</p>

          <Link to="/orders">
            Back to Orders
          </Link>
        </div>
      </main>
    )
  }

  const total = order.items.reduce(
    (sum, item) => sum + item.price * item.quantity,
    0
  )

  return (
    <main className="order-details-page">
      <div className="order-details-card">

        <div className="order-details-header">
          <div>
            <h2>Order #{order.id}</h2>
            <p>Placed on {order.date}</p>
          </div>

          <span
            className={`order-status ${order.status.toLowerCase()}`}
          >
            {order.status}
          </span>
        </div>

        <section className="order-details-section">
          <h3>Ordered Products</h3>

          <div className="order-details-items">
            {order.items.map((item) => (
              <div
                className="order-details-item"
                key={item.name}
              >
                <img
                  src={item.image}
                  alt={item.name}
                />

                <div>
                  <h4>{item.name}</h4>

                  <p>
                    Quantity: {item.quantity}
                  </p>

                  <p>
                    ₹{item.price.toLocaleString('en-IN')}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </section>

        <section className="order-details-section">
          <h3>Delivery Address</h3>

          <p>{order.address}</p>
        </section>

        <section className="order-details-section">
          <h3>Payment Information</h3>

          <p>
            Payment Method: {order.paymentMethod}
          </p>
        </section>

        <div className="order-total">
          <span>Total Amount</span>

          <strong>
            ₹{total.toLocaleString('en-IN')}
          </strong>
        </div>

        <Link
          to="/orders"
          className="back-orders-button"
        >
          Back to Orders
        </Link>

      </div>
    </main>
  )
}

export default OrderDetails
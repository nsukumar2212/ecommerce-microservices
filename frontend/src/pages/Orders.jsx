import { Link } from 'react-router-dom'

function Orders() {
  const orders = [
    {
      id: 'ORD1001',
      date: '18 Aug 2026',
      status: 'Delivered',
      total: 79999,
      items: [
        {
          name: 'iPhone 16',
          quantity: 1,
          price: 79999,
          image: '/images/products/iphone16.jpg'
        }
      ]
    },
    {
      id: 'ORD1002',
      date: '15 Aug 2026',
      status: 'Shipped',
      total: 99999,
      items: [
        {
          name: 'MacBook Air M3',
          quantity: 1,
          price: 99999,
          image: '/images/products/macbook-air.jpg'
        }
      ]
    },
    {
      id: 'ORD1003',
      date: '10 Aug 2026',
      status: 'Processing',
      total: 44998,
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
  ]

  return (
    <main className="orders-page">
      <h2>My Orders</h2>

      <div className="orders-list">
        {orders.map((order) => (
          <div className="order-card" key={order.id}>

            <div className="order-header">
              <div>
                <h3>Order #{order.id}</h3>
                <p>Placed on {order.date}</p>
              </div>

              <span
                className={`order-status ${order.status.toLowerCase()}`}
              >
                {order.status}
              </span>
            </div>

            <div className="order-items">
              {order.items.map((item) => (
                <div
                  className="order-item"
                  key={item.name}
                >
                  <img
                    src={item.image}
                    alt={item.name}
                  />

                  <div>
                    <h4>{item.name}</h4>
                    <p>Quantity: {item.quantity}</p>
                    <p>
                      ₹{item.price.toLocaleString('en-IN')}
                    </p>
                  </div>
                </div>
              ))}
            </div>

            <div className="order-footer">
              <strong>
                Total: ₹{order.total.toLocaleString('en-IN')}
              </strong>

              <Link
  to={`/orders/${order.id}`}
  className="order-details-button"
>
  View Details
</Link>
            </div>

          </div>
        ))}
      </div>
    </main>
  )
}

export default Orders
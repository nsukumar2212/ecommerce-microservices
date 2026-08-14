import { Link } from 'react-router-dom'
import { useCart } from '../context/CartContext'

function Navbar() {
  const { cartItems } = useCart()

  const cartCount = cartItems.reduce(
    (total, item) => total + item.quantity,
    0
  )

  return (
    <header>
      <h1>Electronics Store</h1>

      <nav>
        <Link to="/">Home</Link>

        <Link to="/products">
          Products
        </Link>

        <Link to="/cart" className="cart-link">
  Cart ({cartCount})
</Link>

        <Link to="/login">
          Login
        </Link>
      </nav>
    </header>
  )
}

export default Navbar
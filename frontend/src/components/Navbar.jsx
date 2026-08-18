import { Link } from 'react-router-dom'
import { useCart } from '../context/CartContext'
import { useNotifications } from '../context/NotificationContext'
import { useWishlist } from '../context/WishlistContext'

function Navbar() {
  const { cartItems } = useCart()
  const { unreadCount } = useNotifications()
  const { wishlistItems } = useWishlist()

  const cartCount = cartItems.reduce(
    (total, item) => total + item.quantity,
    0
  )

  const wishlistCount = wishlistItems.length

  return (
    <header>
      <h1>Electronics Store</h1>

      <nav>
        <Link to="/">Home</Link>

        <Link to="/products">
          Products
        </Link>

        <Link to="/cart">
          Cart ({cartCount})
        </Link>

        <Link to="/notifications">
          🔔 Notifications ({unreadCount})
        </Link>

        <Link to="/wishlist">
          ❤️ Wishlist ({wishlistCount})
        </Link>

        <Link to="/profile">
          👤 Profile
        </Link>

        <Link to="/login">
          Login
        </Link>
      </nav>
    </header>
  )
}

export default Navbar
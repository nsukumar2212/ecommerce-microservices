import { Link } from 'react-router-dom'
import { useCart } from '../context/CartContext'
import { useWishlist } from '../context/WishlistContext'

function ProductCard({ product }) {
  const {
    cartItems,
    addToCart,
    increaseQuantity,
    decreaseQuantity
  } = useCart()

  const {
    addToWishlist,
    removeFromWishlist,
    isInWishlist
  } = useWishlist()

  const wishlist = isInWishlist(product.id)

  const cartItem = cartItems.find(
    (item) => item.id === product.id
  )

  function handleWishlist() {
    if (wishlist) {
      removeFromWishlist(product.id)
    } else {
      addToWishlist(product)
    }
  }

  return (
    <div className="product-card">
      <div className="product-image-container">
        <img
          src={product.image}
          alt={product.name}
          className="product-image"
        />

        <button
          className={`wishlist-button ${
            wishlist ? 'wishlist-active' : ''
          }`}
          onClick={handleWishlist}
          aria-label="Add to wishlist"
        >
          {wishlist ? '♥' : '♡'}
        </button>
      </div>

      <div className="product-info">
        <p className="product-category">
          {product.category}
        </p>

        <h3>{product.name}</h3>

        <p className="product-brand">
          {product.brand}
        </p>

        <p className="product-price">
          ₹{product.price.toLocaleString('en-IN')}
        </p>

        <div className="product-actions">
          <Link
            to={`/products/${product.id}`}
            className="details-button"
          >
            View Details
          </Link>

          {cartItem ? (
            <div className="product-quantity-controls">
              <button
                onClick={() =>
                  decreaseQuantity(product.id)
                }
              >
                −
              </button>

              <span>{cartItem.quantity}</span>

              <button
                onClick={() =>
                  increaseQuantity(product.id)
                }
              >
                +
              </button>
            </div>
          ) : (
            <button
              onClick={() => addToCart(product)}
              className="add-cart-button"
            >
              Add to Cart
            </button>
          )}
        </div>
      </div>
    </div>
  )
}

export default ProductCard
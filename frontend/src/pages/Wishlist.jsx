import { useWishlist } from '../context/WishlistContext'
import { useCart } from '../context/CartContext'
import { Link } from 'react-router-dom'

function Wishlist() {
  const {
    wishlistItems,
    removeFromWishlist
  } = useWishlist()

  const { addToCart } = useCart()

  return (
    <main className="wishlist-page">
      <h2>My Wishlist</h2>

      {wishlistItems.length === 0 ? (
        <div className="empty-wishlist">
          <h3>Your Wishlist is Empty</h3>

          <p>
            Save products you like and find them here later.
          </p>

          <Link
            to="/products"
            className="browse-products-button"
          >
            Browse Products
          </Link>
        </div>
      ) : (
        <div className="wishlist-list">
          {wishlistItems.map((product) => (
            <div
              className="wishlist-card"
              key={product.id}
            >
              <img
                src={product.image}
                alt={product.name}
                className="wishlist-image"
              />

              <div className="wishlist-info">
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

                <div className="wishlist-actions">
                  <button
                    className="wishlist-cart-button"
                    onClick={() => addToCart(product)}
                  >
                    Add to Cart
                  </button>

                  <button
                    className="wishlist-remove-button"
                    onClick={() =>
                      removeFromWishlist(product.id)
                    }
                  >
                    Remove
                  </button>

                  <Link
                    to={`/products/${product.id}`}
                    className="wishlist-details-button"
                  >
                    View Details
                  </Link>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </main>
  )
}

export default Wishlist
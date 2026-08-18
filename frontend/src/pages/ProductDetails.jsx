import { useCart } from '../context/CartContext'
import { useWishlist } from '../context/WishlistContext'
import { useParams } from 'react-router-dom'
import products from '../utils/products'

function ProductDetails() {
  const { id } = useParams()

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

  const product = products.find(
    (product) => product.id === Number(id)
  )

  if (!product) {
    return (
      <main className="product-not-found">
        <h2>Product Not Found</h2>

        <p>
          The product you're looking for doesn't exist.
        </p>
      </main>
    )
  }

  const cartItem = cartItems.find(
    (item) => item.id === product.id
  )

  const wishlist = isInWishlist(product.id)

  function handleWishlist() {
    if (wishlist) {
      removeFromWishlist(product.id)
    } else {
      addToWishlist(product)
    }
  }

  return (
    <main className="product-details">
      <div className="product-details-image">
        <img
          src={product.image}
          alt={product.name}
        />
      </div>

      <div className="product-details-info">
        <p className="product-details-category">
          {product.category}
        </p>

        <h2>{product.name}</h2>

        <p className="product-details-brand">
          Brand: {product.brand}
        </p>

        <p className="product-details-price">
          ₹{product.price.toLocaleString('en-IN')}
        </p>

        <p className="product-details-description">
          This is a high-quality {product.name}
          from {product.brand}.
        </p>

        <p className="product-details-stock">
          ✓ In Stock
        </p>

        <div className="product-details-actions">

          {cartItem ? (
            <div className="product-details-quantity-controls">
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
              className="product-details-cart-button"
              onClick={() => addToCart(product)}
            >
              Add to Cart
            </button>
          )}

          <button
            className={`product-details-wishlist-button ${
              wishlist ? 'active' : ''
            }`}
            onClick={handleWishlist}
          >
            {wishlist
              ? '♥ Remove from Wishlist'
              : '♡ Add to Wishlist'}
          </button>

        </div>
      </div>
    </main>
  )
}

export default ProductDetails
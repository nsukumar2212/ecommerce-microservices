import { Link } from 'react-router-dom'
import { useCart } from '../context/CartContext'

function ProductCard({ product }) {
  const { addToCart } = useCart()

  return (
    <div className="product-card">
      <div className="product-image-container">
        <img
          src={product.image}
          alt={product.name}
          className="product-image"
        />
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

          <button
            onClick={() => addToCart(product)}
            className="add-cart-button"
          >
            Add to Cart
          </button>
        </div>
      </div>
    </div>
  )
}

export default ProductCard
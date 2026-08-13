import { Link } from 'react-router-dom'

function ProductCard({ product }) {
  return (
    <div className="product-card">
      <img
        src={product.image}
        alt={product.name}
        className="product-image"
      />

      <h3>{product.name}</h3>

      <p>{product.brand}</p>

      <p className="product-price">
        ₹{product.price}
      </p>

      <Link to={`/products/${product.id}`}>
        View Details
      </Link>

      <button>Add to Cart</button>
    </div>
  )
}

export default ProductCard
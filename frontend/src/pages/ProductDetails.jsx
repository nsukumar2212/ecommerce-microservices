import { useCart } from '../context/CartContext'
import { useParams } from 'react-router-dom'
import products from '../utils/products'

function ProductDetails() {
  const { id } = useParams()
  const { addToCart } = useCart()

  const product = products.find(
    (product) => product.id === Number(id)
  )

  if (!product) {
    return (
      <main>
        <h2>Product Not Found</h2>
        <p>The product you're looking for doesn't exist.</p>
      </main>
    )
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
        <h2>{product.name}</h2>

        <p className="brand">
          Brand: {product.brand}
        </p>

        <p className="price">
          ₹{product.price}
        </p>

        <p>
          This is a high-quality {product.name}
          from {product.brand}.
        </p>

        <p className="stock">
          In Stock
        </p>

        <button onClick={() => addToCart(product)}>
  Add to Cart
</button>
      </div>
    </main>
  )
}

export default ProductDetails
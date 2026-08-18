import { Link } from 'react-router-dom'
import products from '../utils/products'
import ProductCard from '../components/ProductCard'

function Home() {
  const featuredProducts = products.slice(0, 4)

  const categories = [
    {
      name: 'Smartphones',
      description: 'Latest mobile phones'
    },
    {
      name: 'Laptops',
      description: 'Powerful laptops for work and gaming'
    },
    {
      name: 'Headphones',
      description: 'Wireless and wired headphones'
    },
    {
      name: 'Tablets',
      description: 'Portable devices for work and entertainment'
    }
  ]

  return (
    <main>

      {/* Hero Section */}

      <section className="hero">
        <h2>Welcome to Electronics Store</h2>

        <p>
          Discover the latest smartphones, laptops,
          headphones, tablets, and more.
        </p>

        <Link
          to="/products"
          className="shop-now-button"
        >
          Shop Now
        </Link>
      </section>

      {/* Featured Products */}

      <section className="featured-products">
        <h2>Featured Products</h2>

        <div className="product-list">
          {featuredProducts.map((product) => (
            <ProductCard
              key={product.id}
              product={product}
            />
          ))}
        </div>
      </section>

      {/* Categories */}

      <section className="categories">
        <h2>Shop by Category</h2>

        <div className="category-list">
          {categories.map((category) => (
            <Link
              key={category.name}
              to={`/products?category=${encodeURIComponent(category.name)}`}
              className="category-card"
            >
              <h3>{category.name}</h3>

              <p>{category.description}</p>
            </Link>
          ))}
        </div>
      </section>

      {/* Why Choose Us */}

      <section className="why-us">
        <h2>Why Choose Us?</h2>

        <div className="why-us-list">

          <div className="why-us-card">
            <h3>🚚 Fast Delivery</h3>
            <p>Get your products delivered quickly.</p>
          </div>

          <div className="why-us-card">
            <h3>🔒 Secure Payment</h3>
            <p>Safe and secure payment options.</p>
          </div>

          <div className="why-us-card">
            <h3>⭐ Quality Products</h3>
            <p>Shop reliable and quality electronics.</p>
          </div>

        </div>
      </section>

    </main>
  )
}

export default Home
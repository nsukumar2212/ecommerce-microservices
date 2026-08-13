function Home() {
  return (
    <main>
      <section className="hero">
        <h2>Welcome to Electronics Store</h2>
        <p>
          Discover the latest smartphones, laptops, headphones,
          and other electronics.
        </p>

        <button>Shop Now</button>
      </section>

      <section className="categories">
        <h2>Shop by Category</h2>

        <div className="category-list">
          <div className="category-card">
            <h3>Smartphones</h3>
            <p>Latest mobile phones</p>
          </div>

          <div className="category-card">
            <h3>Laptops</h3>
            <p>Powerful laptops for work and gaming</p>
          </div>

          <div className="category-card">
            <h3>Headphones</h3>
            <p>Wireless and wired headphones</p>
          </div>

          <div className="category-card">
            <h3>Accessories</h3>
            <p>Chargers, cables and more</p>
          </div>
        </div>
      </section>
    </main>
  )
}

export default Home
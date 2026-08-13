import { Link } from 'react-router-dom'

function Navbar() {
  return (
    <header>
      <h1>Electronics Store</h1>

      <nav>
        <Link to="/">Home</Link>
        <Link to="/products">Products</Link>
        <Link to="/cart">Cart</Link>
        <Link to="/login">Login</Link>
      </nav>
    </header>
  )
}

export default Navbar
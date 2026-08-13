import Checkout from './pages/Checkout'
import Cart from './pages/Cart'
import ProductDetails from './pages/ProductDetails'
import { BrowserRouter, Routes, Route } from 'react-router-dom'

import Navbar from './components/Navbar'
import Home from './pages/Home'
import Products from './pages/Products'

function App() {
  return (
    <BrowserRouter>
      <Navbar />

      <Routes>
  <Route path="/" element={<Home />} />

  <Route
    path="/products"
    element={<Products />}
  />

  <Route
    path="/products/:id"
    element={<ProductDetails />}
  />

  <Route
    path="/cart"
    element={<Cart />}
  />

  <Route
    path="/checkout"
    element={<Checkout />}
  />
</Routes>

      <footer>
        <p>© 2026 Electronics Store</p>
      </footer>
    </BrowserRouter>
  )
}

export default App
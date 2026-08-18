import OrderSuccess from './pages/OrderSuccess'
import OrderDetails from './pages/OrderDetails'
import Wishlist from './pages/Wishlist'
import Orders from './pages/Orders'
import Profile from './pages/Profile'
import Notifications from './pages/Notifications'
import Payment from './pages/Payment'
import ForgotPassword from './pages/ForgotPassword'
import Register from './pages/Register'
import Login from './pages/Login'
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
  <Route
  path="/login"
  element={<Login />}
/>
<Route
  path="/register"
  element={<Register />}
/>
<Route
  path="/forgot-password"
  element={<ForgotPassword />}
/>
<Route
  path="/payment"
  element={<Payment />}
/>
<Route
  path="/notifications"
  element={<Notifications />}
/>
<Route
  path="/profile"
  element={<Profile />}
/>
<Route
  path="/orders"
  element={<Orders />}
/>
<Route
  path="/wishlist"
  element={<Wishlist />}
/>
<Route
  path="/orders/:orderId"
  element={<OrderDetails />}
/>
<Route
  path="/order-success"
  element={<OrderSuccess />}
/>
</Routes>

      <footer>
        <p>© 2026 Electronics Store</p>
      </footer>
    </BrowserRouter>
  )
}

export default App
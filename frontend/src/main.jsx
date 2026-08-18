import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import { CartProvider } from './context/CartContext'
import { NotificationProvider } from './context/NotificationContext'
import { WishlistProvider } from './context/WishlistContext'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <CartProvider>
      <NotificationProvider>
        <WishlistProvider>
          <App />
        </WishlistProvider>
      </NotificationProvider>
    </CartProvider>
  </StrictMode>,
)
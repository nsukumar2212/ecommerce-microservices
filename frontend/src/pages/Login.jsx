import { Link } from 'react-router-dom'
import { useState } from 'react'

function Login() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')

  function handleSubmit(event) {
    event.preventDefault()

    console.log('Login submitted:', {
      email,
      password
    })
  }

  return (
    <main className="login-page">
      <div className="login-card">
        <h2>Welcome Back</h2>

        <p className="login-subtitle">
          Login to your Electronics Store account
        </p>

        <form onSubmit={handleSubmit}>
          <label>Email</label>

          <input
            type="email"
            placeholder="Enter your email"
            value={email}
            onChange={(event) => setEmail(event.target.value)}
            required
          />

          <label>Password</label>

          <input
            type="password"
            placeholder="Enter your password"
            value={password}
            onChange={(event) => setPassword(event.target.value)}
            required
          />

          <div className="forgot-password">
            <Link to="/forgot-password">
              Forgot Password?
            </Link>
          </div>

          <button type="submit">
            Login
          </button>
        </form>

        <p className="register-link">
          Don't have an account?{' '}
          <Link to="/register">
            Create Account
          </Link>
        </p>
      </div>
    </main>
  )
}

export default Login
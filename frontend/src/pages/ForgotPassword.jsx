import { Link } from 'react-router-dom'
import { useState } from 'react'

function ForgotPassword() {
  const [email, setEmail] = useState('')
  const [submitted, setSubmitted] = useState(false)

  function handleSubmit(event) {
    event.preventDefault()
    setSubmitted(true)
  }

  return (
    <main className="login-page">
      <div className="login-card">
        <h2>Forgot Password?</h2>

        <p className="login-subtitle">
          Enter your email and we'll help you reset your password.
        </p>

        {!submitted ? (
          <form onSubmit={handleSubmit}>
            <label>Email</label>

            <input
              type="email"
              placeholder="Enter your email"
              value={email}
              onChange={(event) => setEmail(event.target.value)}
              required
            />

            <button type="submit">
              Send Reset Link
            </button>
          </form>
        ) : (
          <p className="reset-message">
            If an account exists for <strong>{email}</strong>,
            password reset instructions will be sent.
          </p>
        )}

        <p className="register-link">
          <Link to="/login">
            Back to Login
          </Link>
        </p>
      </div>
    </main>
  )
}

export default ForgotPassword
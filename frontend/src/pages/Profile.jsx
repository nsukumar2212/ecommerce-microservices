import { Link } from 'react-router-dom'

function Profile() {
  return (
    <main className="profile-page">
      <div className="profile-card">

        <div className="profile-header">
          <div className="profile-avatar">
            👤
          </div>

          <div>
            <h2>My Profile</h2>
            <p>Manage your account</p>
          </div>
        </div>

        <div className="profile-details">
          <div className="profile-detail">
            <span>Name</span>
            <strong>Guest User</strong>
          </div>

          <div className="profile-detail">
            <span>Email</span>
            <strong>guest@example.com</strong>
          </div>

          <div className="profile-detail">
            <span>Phone</span>
            <strong>Not added</strong>
          </div>
        </div>

        <button className="edit-profile-button">
          Edit Profile
        </button>

        <div className="profile-options">

          <Link
            to="/orders"
            className="profile-option"
          >
            <div>
              <h3>📦 My Orders</h3>
              <p>View your previous orders</p>
            </div>

            <span>→</span>
          </Link>

          <Link
            to="/wishlist"
            className="profile-option"
          >
            <div>
              <h3>❤️ Wishlist</h3>
              <p>View your saved products</p>
            </div>

            <span>→</span>
          </Link>

          <Link
            to="/notifications"
            className="profile-option"
          >
            <div>
              <h3>🔔 Notifications</h3>
              <p>View your notifications</p>
            </div>

            <span>→</span>
          </Link>

        </div>

        <button className="logout-button">
          Logout
        </button>

      </div>
    </main>
  )
}

export default Profile
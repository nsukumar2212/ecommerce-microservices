import { useNotifications } from '../context/NotificationContext'

function Notifications() {
  const {
    notifications,
    unreadCount,
    markAsRead,
    markAllAsRead,
    removeNotification
  } = useNotifications()

  return (
    <main className="notifications-page">
      <div className="notifications-header">
        <div>
          <h2>Notifications</h2>

          <p>
            {unreadCount} unread notification
            {unreadCount !== 1 ? 's' : ''}
          </p>
        </div>

        {unreadCount > 0 && (
          <button
            className="mark-all-button"
            onClick={markAllAsRead}
          >
            Mark All as Read
          </button>
        )}
      </div>

      <div className="notifications-list">
        {notifications.length === 0 ? (
          <div className="no-notifications">
            <h3>No Notifications</h3>
            <p>You are all caught up!</p>
          </div>
        ) : (
          notifications.map((notification) => (
            <div
              key={notification.id}
              className={`notification-card ${
                notification.read ? 'read' : 'unread'
              }`}
            >
              <div className="notification-content">
                <h3>{notification.title}</h3>

                <p>{notification.message}</p>

                <span>{notification.time}</span>
              </div>

              <div className="notification-actions">
                {!notification.read && (
                  <button
                    onClick={() => markAsRead(notification.id)}
                  >
                    Mark as Read
                  </button>
                )}

                <button
                  onClick={() =>
                    removeNotification(notification.id)
                  }
                >
                  Remove
                </button>
              </div>
            </div>
          ))
        )}
      </div>
    </main>
  )
}

export default Notifications
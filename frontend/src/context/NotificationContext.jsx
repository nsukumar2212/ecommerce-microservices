import { createContext, useContext, useState } from 'react'

const NotificationContext = createContext()

const initialNotifications = [
  {
    id: 1,
    title: 'Order Confirmed',
    message: 'Your order has been confirmed successfully.',
    time: '10 minutes ago',
    read: false
  },
  {
    id: 2,
    title: 'Payment Successful',
    message: 'Your payment was completed successfully.',
    time: '30 minutes ago',
    read: false
  },
  {
    id: 3,
    title: 'New Product Available',
    message: 'Check out our latest electronics products.',
    time: '2 hours ago',
    read: true
  }
]

export function NotificationProvider({ children }) {
  const [notifications, setNotifications] = useState(
    initialNotifications
  )

  function markAsRead(id) {
    setNotifications((currentNotifications) =>
      currentNotifications.map((notification) =>
        notification.id === id
          ? { ...notification, read: true }
          : notification
      )
    )
  }

  function markAllAsRead() {
    setNotifications((currentNotifications) =>
      currentNotifications.map((notification) => ({
        ...notification,
        read: true
      }))
    )
  }

  function removeNotification(id) {
    setNotifications((currentNotifications) =>
      currentNotifications.filter(
        (notification) => notification.id !== id
      )
    )
  }

  const unreadCount = notifications.filter(
    (notification) => !notification.read
  ).length

  return (
    <NotificationContext.Provider
      value={{
        notifications,
        unreadCount,
        markAsRead,
        markAllAsRead,
        removeNotification
      }}
    >
      {children}
    </NotificationContext.Provider>
  )
}

export function useNotifications() {
  return useContext(NotificationContext)
}
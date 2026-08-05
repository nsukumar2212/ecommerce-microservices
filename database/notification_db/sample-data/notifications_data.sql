INSERT INTO notifications
(user_id, order_id, notification_type, message, notification_status)
VALUES
(1, 1, 'Email', 'Your order has been placed successfully.', 'Sent'),
(2, 2, 'SMS', 'Your payment was successful.', 'Sent'),
(1, 3, 'Push', 'Your order has been delivered.', 'Pending');
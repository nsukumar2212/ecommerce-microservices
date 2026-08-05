-- ============================================
-- NOTIFICATION SERVICE QUERIES
-- ============================================

-- 1. View all notifications
SELECT * FROM notifications;


-- 2. View all sent notifications
SELECT *
FROM notifications
WHERE notification_status = 'Sent';


-- 3. View all pending notifications
SELECT *
FROM notifications
WHERE notification_status = 'Pending';


-- 4. View all email notifications
SELECT *
FROM notifications
WHERE notification_type = 'Email';


-- 5. View notifications for a specific user
SELECT *
FROM notifications
WHERE user_id = 1;


-- 6. View notifications related to a specific order
SELECT *
FROM notifications
WHERE order_id = 1;
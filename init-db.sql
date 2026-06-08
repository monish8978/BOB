-- Initialize Database for BOB Bank Chatbot
CREATE DATABASE IF NOT EXISTS bob_db;
USE bob_db;

-- 1. Create tickets table for storing support complaints
CREATE TABLE IF NOT EXISTS tickets (
    ticket_id VARCHAR(50) PRIMARY KEY,
    user_id VARCHAR(100) NOT NULL,
    customer_name VARCHAR(150) NOT NULL,
    mobile_number VARCHAR(20) NOT NULL,
    issue_type VARCHAR(50) NOT NULL,
    category VARCHAR(50) NOT NULL,
    sub_category VARCHAR(50) NOT NULL,
    description TEXT,
    status VARCHAR(20) DEFAULT 'OPEN',
    assigned_to VARCHAR(50) DEFAULT 'Support Team',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 2. Create message_logs table for conversation audits
CREATE TABLE IF NOT EXISTS message_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(100) NOT NULL,
    sender VARCHAR(10) NOT NULL, -- 'USER' or 'BOT'
    message_text TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_user_id (user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

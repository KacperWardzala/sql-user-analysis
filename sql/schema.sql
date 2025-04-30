-- schema.sql

CREATE TABLE users (
    user_id BIGINT PRIMARY KEY,
    registration_date TEXT,
    country TEXT
);

CREATE TABLE sessions (
    session_id BIGINT PRIMARY KEY,
    user_id BIGINT,
    session_start TEXT,
    session_end TEXT,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);

CREATE TABLE purchases (
    purchase_id BIGINT PRIMARY KEY,
    user_id BIGINT,
    amount DOUBLE PRECISION,
    purchase_date TEXT,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);

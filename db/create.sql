IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'codewars_db') THEN
    CREATE DATABASE codewars_db;
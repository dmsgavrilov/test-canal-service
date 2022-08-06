import os

# Database
DATABASE_URI = os.getenv("DATABASE_URI", "postgres://postgres:123@localhost:5432")

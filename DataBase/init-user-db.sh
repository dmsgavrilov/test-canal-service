#!/bin/bash

set -e
echo "from postgres init"
echo $POSTGRES_USER
echo $DB_USER
psql -v ON_ERROR_STOP=1 --username "postgres" <<-EOSQL
    CREATE DATABASE db;
    \c db
    CREATE EXTENSION IF NOT EXISTS pgcrypto;
EOSQL

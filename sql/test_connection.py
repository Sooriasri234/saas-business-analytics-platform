from sqlalchemy import create_engine

DATABASE_URL = "postgresql://neondb_owner:npg_5heBzfL7XoPF@ep-mute-sea-aqzg9wse-pooler.c-8.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

try:
    engine = create_engine(DATABASE_URL)

    with engine.connect() as conn:
        print("Connected to Neon PostgreSQL Successfully!")

except Exception as e:
    print("Error:", e)
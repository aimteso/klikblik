from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean

metadata = MetaData()

role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("role_id", Integer, ForeignKey(role.c.id)),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)

brand = Table(
    "brand",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("created_at", TIMESTAMP, default=datetime.utcnow),
    Column("edited_at", TIMESTAMP, default=datetime.utcnow),
    Column("deleted_at", TIMESTAMP, default=datetime.utcnow),

)

category = Table(
    "category",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("created_at", TIMESTAMP, default=datetime.utcnow),
    Column("edited_at", TIMESTAMP, default=datetime.utcnow),
    Column("deleted_at", TIMESTAMP, default=datetime.utcnow),

)
scategory = Table(
    "scategory",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("created_at", TIMESTAMP, default=datetime.utcnow),
    Column("edited_at", TIMESTAMP, default=datetime.utcnow),
    Column("deleted_at", TIMESTAMP, default=datetime.utcnow),

)

item = Table(
    "item",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("bcode", String, nullable=False),
    Column("bcode1", String, nullable=True),
    Column("bcode2", String, nullable=True),
    Column("brand_id", Integer, ForeignKey(brand.c.id)),
    Column("category_id", Integer, ForeignKey(category.c.id)),
    Column("scategory_id", Integer, ForeignKey(scategory.c.id)),
    Column("created_at", TIMESTAMP, default=datetime.utcnow),
    Column("edited_at", TIMESTAMP, default=datetime.utcnow),
    Column("deleted_at", TIMESTAMP, default=datetime.utcnow),
)
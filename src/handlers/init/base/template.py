{import_base}

# async
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

# sync
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

{import_settings}

# sync
# DB_URL = "sqlite:///./sql_app.db"
# DB_URL = f"postgresql://{url_db}"
# engine = create_engine(DB_URL, connect_args={connect_args})
# SessionMaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# async def get_session():
#     async with SessionMaker() as session:
#         yield session


# async
# DB_URL = f"postgresql+asyncpg://{url_db}"
# engine = create_async_engine(DB_URL, future=True)
# AsyncSessionMaker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# async def get_async_session():
#     async with AsyncSessionMaker() as session:
#         yield session

{add_base}


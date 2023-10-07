from sqlalchemy.ext.declarative import declarative_base

# async
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

# sync
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

from src.config import settings

# sync
# DB_URL = "sqlite:///./sql_app.db"
# DB_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.HOST}:{settings.PORT}/{settings.POSTGRES_DB}"
# engine = create_engine(DB_URL, connect_args={'check_same_thread': False})
# SessionMaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# async def get_session():
#     async with SessionMaker() as session:
#         yield session


# async
# DB_URL = f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.HOST}:{settings.PORT}/{settings.POSTGRES_DB}"
# engine = create_async_engine(DB_URL, future=True)
# AsyncSessionMaker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# async def get_async_session():
#     async with AsyncSessionMaker() as session:
#         yield session

Base = declarative_base()


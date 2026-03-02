from logging.config import fileConfig
<<<<<<< HEAD
from sqlalchemy import engine_from_config, pool
from alembic import context

from db import Base, connection_url
from project.olap.models import Customer, Type, Orders, Product

config = context.config
config.set_main_option("sqlalchemy.url", connection_url)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
=======

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
from project.customer import models
from project.product import models
from project.orders import models
from db import Base
# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
>>>>>>> 2f7dfd5181a2bf7caa0f5e12869897cff7290531
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
<<<<<<< HEAD
=======
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
>>>>>>> 2f7dfd5181a2bf7caa0f5e12869897cff7290531
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
<<<<<<< HEAD
            connection=connection,
            target_metadata=target_metadata,
=======
            connection=connection, target_metadata=target_metadata
>>>>>>> 2f7dfd5181a2bf7caa0f5e12869897cff7290531
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
<<<<<<< HEAD
    run_migrations_online()
=======
    run_migrations_online()
>>>>>>> 2f7dfd5181a2bf7caa0f5e12869897cff7290531

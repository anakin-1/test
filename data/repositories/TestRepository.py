import logging

from sqlalchemy.util.compat import contextmanager

from data import models
from data.database import SessionLocal
from data.pydantics_models import ServerEntity
from data.repositories.exceptions import NotFoundError


# Context manager for the database session
@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_servers_by_flow_id(flow_id: str):
    try:
        with get_db() as db:
            servers = db.query(models.Server).filter(models.Server.used_by == flow_id).all()
            if not servers:
                print(f"No servers assigned to flow {flow_id}")
                raise Exception(f"Servers assigned to flow id not found")
            return servers
    except NotFoundError as e:
       print(f"Error in getting servers with flow id: {e}")
    except Exception as e:
       print(f"Database connection error: {e}")


def create_server(server_entity: ServerEntity):
    with get_db() as db:
        db_server = models.Server(instance_id=server_entity.instance_id,
                                  type=server_entity.type,
                                  instance_type=server_entity.instance_type,
                                  used_by=server_entity.used_by,
                                  cloudflare_no=server_entity.cloudflare_no,
                                  )
        db.add(db_server)
        db.commit()
        db.refresh(db_server)
        return db_server
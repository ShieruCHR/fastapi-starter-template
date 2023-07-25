# CRUD Operations

from sqlmodel import Session

from database import get_session


class CRUDBase:
    session: Session

    def __init__(self, session: Session):
        self.session = session

    def commit(self):
        self.session.commit()

    # Write CRUD operations here


class CRUD:
    def __init__(self):
        super(get_session)

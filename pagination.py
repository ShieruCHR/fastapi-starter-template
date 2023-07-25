from typing import TypeVar

from pydantic import conint


T = TypeVar("T")


class Pagination:
    offset: int
    limit: int

    def __init__(self, page: conint(gt=0) = 1, per: conint(gt=0) = 20):
        """
        Initializes a Pagination object.

        Parameters:
            page (int, optional): The page number to retrieve. Defaults to 1.
            per (int, optional): The number of items per page. Defaults to 20.

        Raises:
            ValueError: If `page` or `per` is less than or equal to zero.

        Example:
            pagination = Pagination(page=1, per=20)

        Example:
            @app.get("/articles")
            def get_all_articles(pagination = Annotated[Pagination, Depends(Pagination)]):
                pass
        """
        self.offset = (page - 1) * per
        self.limit = per

    def apply(self, statement: T) -> T:
        """
        Apply pagination clauses to the given statement.

        This method applies offset and limit clauses to the provided statement, which can be a SQLAlchemy
        query object or any similar construct.

        Parameters:
            statement (T): The statement to which the pagination clauses will be applied.

        Returns:
            T: The statement with the pagination clauses applied.

        Example:
            pagination = Pagination(page=1, per=20)
            statement = select(User)
            pagination_statement = pagination.apply(statement)
            return session.exec(pagination_statement)

        Example:
            pagination = Pagination(page=1, per=20)
            return session.exec(
                pagination.apply(
                    select(User)
                )
            ).all()
        """
        return statement.offset(self.offset).limit(self.limit)

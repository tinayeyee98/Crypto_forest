import aiomysql


class DatabaseManager:
    """A class to manage connections to a MySQL database."""

    def __init__(self, host="db", user="root", password="root", db="crypto_db"):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.pool = None

    async def connect(self):
        """Connect to the MySQL database."""
        self.pool = await aiomysql.create_pool(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.db,
            connect_timeout=10,
        )

    async def disconnect(self):
        """Disconnect from the MySQL database."""
        if self.pool:
            self.pool.close()
            await self.pool.wait_closed()

    async def execute_query(self, query, *args):
        """
        Execute a SQL query on the MySQL database.

        Args:
            query (str): The SQL query to execute.
            args: Optional arguments to pass to the query.

        Returns:
            list: A list of tuples representing the result of the query.
        """
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(query, args)
                return await cur.fetchall()

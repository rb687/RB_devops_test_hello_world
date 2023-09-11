from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

class db_operations:
    def __init__(self, db_conn_str=None):
        if db_conn_str:
            self.db_conn_str = db_conn_str
        self.engine = create_engine(self.db_conn_str)
        self.Session = sessionmaker(bind=self.engine)

    def test_conn(self):
        conn = self.Session()
        success = False
        try:
            res = conn.execute(text("SELECT 1;"))
            if res:
                success = True
            else:
                success = False
                raise ("Test connection Failed")
        except:
            raise
        finally:
            conn.close()

        return success

    def execute_sql(self, sql):
        conn = self.Session()
        res = None
        try:
            res = conn.execute(text(sql))
            conn.commit()
        except:
            raise
        finally:
            conn.close()

        return res


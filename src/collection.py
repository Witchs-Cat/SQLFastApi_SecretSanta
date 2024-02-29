from sqlite3 import Connection, Cursor


def toSqlTypeName(tp:type) -> str:
    if (tp is int):
        return "Integer"
    
    if (tp is str):
        return "Text"
    
    raise Exception()

def toSqlStr(value: any) -> str:
    if (type(value) is str):
        return f"'{value}'"
    
    return f"{value}"

class BaseCollection:
    modelAnnotations : dict[str, type]
    tableName : str 

    mConnection: Connection
    mCursor: Cursor

    def __init__(self, 
            db:Connection, 
            tableName:str, 
            modelAnnotations : dict[str, type]):
        
        self.modelAnnotations = modelAnnotations
        self.tableName = tableName
        self.mConnection = db
        self.mCursor = self.mConnection.cursor()
        self.create_table()

    def create_table(self) -> None:    
        query:str = ",".join([
          f"{item[0]} {toSqlTypeName(item[1])}" for item in self.modelAnnotations.items()
        ])

        self.mCursor.execute(f"CREATE TABLE IF NOT EXISTS {self.tableName} ({query});")
        self.mConnection.commit()

    def insert(self,
        values: dict[str, any]) -> None:
        print(values.values())
        self.mCursor.execute(
            f"""INSERT INTO {self.tableName} 
                ({",".join(values.keys())}) 
                VALUES ({",".join(map(toSqlStr, values.values()))}) ;""")
        
        self.mConnection.commit()
        pass

    def update(self,
        values: dict[str, str],
        where: str) -> None:
        
        query:str = ",".join( 
            [f"{key}={toSqlStr(values[key])}" 
                for key in values.keys()]
        )

        self.mCursor.execute(f"UPDATE {self.tableName} SET {query} WHERE {where};")

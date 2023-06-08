from neo4j import GraphDatabase


class Database:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def execute_query(self, query, parameters=None):
        with self.driver.session() as session:
            results = session.run(query, parameters=parameters)  # adiciona o parâmetro "parameters" aqui
            return [record for record in results]

    def drop_all(self):
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")

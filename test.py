from neo4j import GraphDatabase

class HelloWorldExample:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def print_greeting(self, message):
        with self.driver.session() as session:
            greeting = session.execute_write(self._create_and_retuen_greeting, message)
            print(greeting)

    @staticmethod
    def _create_and_retuen_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        return result.single()[0]
    
if __name__ == '__main__':
    greeter = HelloWorldExample("neo4j+s://aa38a78e.databases.neo4j.io", "neo4j", "1camhqRZcZMChJnQG6Y8x5zU1dID5yFbjjEWOXXrLkQ")
    greeter.print_greeting("hello, world")
    greeter.close()
# pip install neo4j

from dotenv import load_dotenv
import os

from langchain_community.graphs import Neo4jGraph

# Warning control
import warnings
warnings.filterwarnings("ignore")

load_dotenv('.env', override=True)
NEO4J_URI = os.getenv('NEO4J_URI')
NEO4J_USERNAME = os.getenv('NEO4J_USERNAME')
NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')
NEO4J_DATABASE = os.getenv('NEO4J_DATABASE')

kg = Neo4jGraph(
    url=NEO4J_URI, username=NEO4J_USERNAME, password=NEO4J_PASSWORD, database=NEO4J_DATABASE
)

cypher = """
  MATCH (n:Person) 
  RETURN count(n) AS numberOfPerson
  """
result = kg.query(cypher)
print(f"There are {result[0]['numberOfPerson']} nodes in this graph.")

# Delete data from the graph
# cypher = """
# MATCH (emil:Person {name:"Emil Eifrem"})-[actedIn:ACTED_IN]->(movie:Movie)
# RETURN emil.name, movie.title
# """
# kg.query(cypher)
# cypher = """
# MATCH (emil:Person {name:"Emil Eifrem"})-[actedIn:ACTED_IN]->(movie:Movie)
# DELETE actedIn
# """
# kg.query(cypher)

# Adding data to the graph
# cypher = """
# CREATE (pingan:Person {name:"陈平安"})
# CREATE (ningyao:Person {name:"宁姚"})
# RETURN pingan
# """

# kg.query(cypher)
# cypher = """
# MATCH (pingan:Person {name:"陈平安"}), (ningyao:Person {name:"宁姚"})
# MERGE (pingan)-[hasRelationship:TAOIST_COUPLE_WITH]->(ningyao)
# RETURN pingan, hasRelationship, ningyao
# """
# kg.query(cypher)

# MATCH (pingan:Person {name:"陈平安"})-[r]-(ningyao:Person {name:"宁姚"})
# SET r.name = "道侣"

# Alternatively, when writing our MATCH query, we can specify to match patterns directionlessly, by using a query such as

# MATCH (A)-[FRIEND]-(B) RETURN A, B
# which will not care about whether A is friends with B or vice versa, and allows us to choose a direction arbitrarily when we create the relationship.
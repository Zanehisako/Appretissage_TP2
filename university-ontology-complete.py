from rdflib import Graph, Namespace, RDF, RDFS, OWL, Literal, URIRef

# Initialize RDF graph
g = Graph()

# Define namespaces
EX = Namespace("http://example.org/university#")
g.bind("ex", EX)
g.bind("owl", OWL)

# Task 1: Defining Concepts and Hierarchies
# Define Person as the top-level class
g.add((EX.Person, RDF.type, OWL.Class))

# Define Student as subclass of Person
g.add((EX.Student, RDF.type, OWL.Class))
g.add((EX.Student, RDFS.subClassOf, EX.Person))

# Define Staff as subclass of Person
g.add((EX.Staff, RDF.type, OWL.Class))
g.add((EX.Staff, RDFS.subClassOf, EX.Person))

# Define Teacher as subclass of Staff
g.add((EX.Teacher, RDF.type, OWL.Class))
g.add((EX.Teacher, RDFS.subClassOf, EX.Staff))

# Define Teacher subclasses
g.add((EX.Tutor, RDF.type, OWL.Class))
g.add((EX.Tutor, RDFS.subClassOf, EX.Teacher))

g.add((EX.Supervisor, RDF.type, OWL.Class))
g.add((EX.Supervisor, RDFS.subClassOf, EX.Teacher))

# Define Module class
g.add((EX.Module, RDF.type, OWL.Class))

# Define Program hierarchy
g.add((EX.Program, RDF.type, OWL.Class))

g.add((EX.Undergraduate, RDF.type, OWL.Class))
g.add((EX.Undergraduate, RDFS.subClassOf, EX.Program))

g.add((EX.Graduate, RDF.type, OWL.Class))
g.add((EX.Graduate, RDFS.subClassOf, EX.Program))

g.add((EX.Postgraduate, RDF.type, OWL.Class))
g.add((EX.Postgraduate, RDFS.subClassOf, EX.Program))

# Define Department class
g.add((EX.Department, RDF.type, OWL.Class))

# Task 2: Creating Relationships (Roles)
# Define base teaching relationship
g.add((EX.teaches, RDF.type, OWL.ObjectProperty))
g.add((EX.teaches, RDFS.domain, EX.Teacher))
g.add((EX.teaches, RDFS.range, EX.Student))

# Define enrollment relationship
g.add((EX.enrolledIn, RDF.type, OWL.ObjectProperty))
g.add((EX.enrolledIn, RDFS.domain, EX.Student))
g.add((EX.enrolledIn, RDFS.range, EX.Program))

# Define supervision relationship
g.add((EX.supervises, RDF.type, OWL.ObjectProperty))
g.add((EX.supervises, RDFS.subPropertyOf, EX.teaches))
g.add((EX.supervises, RDFS.domain, EX.Supervisor))
g.add((EX.supervises, RDFS.range, EX.Student))

# Define tutoring relationship
g.add((EX.tutors, RDF.type, OWL.ObjectProperty))
g.add((EX.tutors, RDFS.subPropertyOf, EX.teaches))
g.add((EX.tutors, RDFS.domain, EX.Tutor))
g.add((EX.tutors, RDFS.range, EX.Student))

# Define head of department relationship
g.add((EX.headOfDepartment, RDF.type, OWL.ObjectProperty))
g.add((EX.headOfDepartment, RDFS.domain, EX.Department))
g.add((EX.headOfDepartment, RDFS.range, EX.Staff))

# Task 3: Applying Constraints
# Disjoint classes
g.add((EX.Student, OWL.disjointWith, EX.Staff))
g.add((EX.Undergraduate, OWL.disjointWith, EX.Graduate))
g.add((EX.Graduate, OWL.disjointWith, EX.Postgraduate))
g.add((EX.Undergraduate, OWL.disjointWith, EX.Postgraduate))

# Inverse properties
g.add((EX.teaches, OWL.inverseOf, EX.taughtBy))
g.add((EX.supervises, OWL.inverseOf, EX.supervisedBy))

# Cardinality constraint for headOfDepartment
head_restriction = URIRef(EX + "HeadOfDepartmentRestriction")
g.add((head_restriction, RDF.type, OWL.Restriction))
g.add((head_restriction, OWL.onProperty, EX.headOfDepartment))
g.add((head_restriction, OWL.maxCardinality, Literal(1)))
g.add((EX.Department, RDFS.subClassOf, head_restriction))

# Create some instances (including the original ones)
g.add((EX.Ahmed, RDF.type, EX.Teacher))
g.add((EX.Mohammed, RDF.type, EX.Student))
g.add((EX.Ahmed, EX.teaches, EX.Mohammed))

# Add some additional instances
g.add((EX.ComputerScience, RDF.type, EX.Department))
g.add((EX.Ahmed, EX.headOfDepartment, EX.ComputerScience))
g.add((EX.AI_Module, RDF.type, EX.Module))
g.add((EX.Ahmed, EX.teaches, EX.AI_Module))

# Print the ontology in Turtle format
print("Ontology in Turtle format:")
print(g.serialize(format="turtle"))

# Example SPARQL query to test the relationships
print("\nTeaching relationships:")
query = """
PREFIX ex: <http://example.org/university#>
SELECT ?teacher ?student
WHERE {
    ?teacher ex:teaches ?student .
    ?teacher rdf:type ex:Teacher .
    ?student rdf:type ex:Student .
}
"""
for row in g.query(query):
    print(f"{row.teacher} teaches {row.student}")

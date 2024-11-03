from rdflib import Graph, Namespace, RDF, RDFS, OWL, Literal, URIRef
# Initialize RDF graph
g = Graph()
# Define namespaces
EX = Namespace("http://example.org/university#")
g.bind("ex", EX)
g.bind("owl", OWL)
# Define the main classes
g.add((EX.Student, RDF.type, OWL.Class))
g.add((EX.Teacher, RDF.type, OWL.Class))
#Task 1
g.add((EX.Person, RDF.type, OWL.Class))

g.add((EX.Student,RDFS.subClassOf,EX.Person))

g.add((EX.Staff, RDF.type, OWL.Class))
g.add((EX.Staff,RDFS.subClassOf,EX.Person))

g.add((EX.Tutor, RDF.type, OWL.Class))
g.add((EX.Tutor,RDFS.subClassOf,EX.Teacher))

g.add((EX.Supervisor, RDF.type, OWL.Class))
g.add((EX.Supervisor,RDFS.subClassOf,EX.Teacher))

g.add((EX.Module, RDF.type, OWL.Class))

g.add((EX.Program, RDF.type, OWL.Class))

g.add((EX.Undergraduate, RDF.type, OWL.Class))
g.add((EX.Undergraduate,RDFS.subClassOf,EX.Program))

g.add((EX.Graduate, RDF.type, OWL.Class))
g.add((EX.Graduate,RDFS.subClassOf,EX.Program))

g.add((EX.Postgraduate, RDF.type, OWL.Class))
g.add((EX.Postgraduate,RDFS.subClassOf,EX.Program))


# Define properties (roles)
g.add((EX.teaches, RDF.type, OWL.ObjectProperty))
g.add((EX.teaches, RDFS.domain, EX.Teacher))
g.add((EX.teaches, RDFS.range, EX.Student))
g.add((EX.EnrolledIn, RDF.type, OWL.ObjectProperty))
g.add((EX.EnrolledIn, RDFS.domain, EX.Student))
g.add((EX.EnrolledIn, RDFS.range, EX.Teacher))
#Task2
g.add((EX.Role, RDF.type, OWL.ObjectProperty))

# Create instances (for Teacher & Student)
g.add((EX.Ahmed, RDF.type, EX.Teacher))
g.add((EX.Mohammed, RDF.type, EX.Student))
# Define relationships (Ahmed teaches Mohammed)
g.add((EX.Ahmed, EX.teaches, EX.Mohammed))
# Print the resulting triples
for subj, pred, obj in g:
   print(subj, pred, obj)

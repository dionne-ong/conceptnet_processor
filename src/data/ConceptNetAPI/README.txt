NOTE: This uses ConceptNet5 API (https://github.com/commonsense/conceptnet5/wiki/API) which means that it requires an internet connection.

Important Functions:

Name: lookup_concept
Parameters: concept (string)
Description: returns JSON of entry from conceptnet

Name: get_related_concepts
Parameters: concept (string)
Description: returns list of related concepts
Example: Dog -> Wire Haired Dachshund, Dogs, Bichon Frise, Rottie...

Name: get_similarity
Parameters: concept1 (string), concept2 (string)
Description: returns weight of the relation between concept1 and concept2 (the higher, the more similar)
Example: Sea & Ocean -> 0.841

Name: get_connection
Parameters: concept1 (string), concept2 (string)
Description: returns relations between concept1 and concept2
Example: Dog -DistinctFrom-> Cat, Dog -Antonym-> Cat, ...

Name: query
Parameters: concept, position, relation, weight (default=2.0)
Description: query concept based on a relation. position is either "node", "start", or "end" depending on what position you want the concept to be in. relation is the relation to be queried. weight is for filtering out relations which are not mentioned enough. Returns a tuple (concept1, concept2) where concept1 is the startnode and concept2 is the end node.

Example: Concept (dog); Position (end); Relation (IsA); Weight (2.0)
	can return: (wire haired dachshund, dog) ["wire haired dachshund is a dog"]
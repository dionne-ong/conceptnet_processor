from src.data.ConceptNetAPI import conceptnet

RELATION_IS_A           = "IsA"
RELATION_PART_OF        = "PartOf"
RELATION_AT_LOCATION    = "AtLocation"
RELATION_HAS_PREREQ     = "HasPrerequisite"
RELATION_CREATED_BY     = "CreatedBy"
RELATION_USED_FOR       = "UsedFor"
RELATION_CAUSES         = "Causes"
RELATION_DESIRES        = "Desires"
RELATION_CAPABLE_OF     = "CapableOf"
RELATION_HAS_PROPERTY   = "HasProperty"

def getAttribute(concept):
    choices = conceptnet.query(concept, "start", RELATION_IS_A, 1.0)

    return choices


test = conceptnet.query("pet", "start", RELATION_IS_A, 1.0)
print(test)


test = conceptnet.query("pet", "start", RELATION_PART_OF, 1.0)
print(test)


test = conceptnet.query("dog", "start", RELATION_AT_LOCATION, 1.0)
print(test)
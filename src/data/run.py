import re
from src.data.ConceptNetAPI.conceptnet import query
from src.data.filtration.concept_filtration import filter_concept
from src.data.filtration.concept_filter_config import INCLUDED_RELATIONS
from src.data.filtration.concept_filter_config import EXCLUDE_ARTICLE
from src.data.db.concepts.DBO_Concept import DBO_Concept
from src.data.db.concepts.Concept import Concept


def record_capabilities(filename):

    file = open(filename, "r")
    string = file.read()
    word_list = re.sub("[^\w]", " ",  string).split()

    for concept in word_list:
        new_concept = Concept(-1, "character", "CapableOf", concept)
        DBO_Concept.addConcept(new_concept)

def record_data(filename):

    file = open(filename, "r")
    string = file.read()
    word_list = re.sub("[^\w]", " ",  string).split()
    for word in word_list:

        if word not in EXCLUDE_ARTICLE:
            if not DBO_Concept.does_existn(word):
                for relation in INCLUDED_RELATIONS:
                    concept_array_start = query(word, "start", relation, 1.0)
                    concept_array_end   = query(word, "end", relation, 1.0)
                    concept_array = concept_array_end + concept_array_start

                    listed = filter_concept(concept_array, relation)

                    if not DBO_Concept.does_exist_relation(word, relation):
                        for concept in listed:
                            new_concept = Concept(-1, concept[0], relation, concept[1])
                            DBO_Concept.addConcept(new_concept)

            print(word, " done")
    print("STORY DONE")
    file.close()




#record_data("stories/advising a fool")
#record_data("stories/a cartload of almonds")
#record_data("stories/princess and the pea")
#record_data("stories/basic concepts")
#record_data("stories/basic verbs")
#record_capabilities("stories/basic verbs")


#record_data("stories/steadfast tin soldier")
#record_data("stories/the tinderbox")

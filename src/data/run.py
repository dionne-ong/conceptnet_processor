import re
from src.data.ConceptNetAPI.conceptnet import query
from src.data.filtration.concept_filtration import filter_concept
from src.data.filtration.concept_filter_config import INCLUDED_RELATIONS, EXCLUDE_ARTICLE
from src.data.db.concepts.DBO_Concept import DBO_Concept
from src.data.db.concepts.Concept import Concept

recorded_words = []
thresh = 2.0

def record_capabilities(filename):
    inner_count = 0

    file = open(filename, "r")
    string = file.read()
    word_list = re.sub("[^\w]", " ",  string).split()

    for concept in word_list:
        new_concept = Concept(-1, "character", "CapableOf", concept)
        DBO_Concept.addConcept(new_concept)
        inner_count += 1
    return inner_count


def record_data(filename):
    inner_count = 0
    file = open(filename, "r")
    string = file.read()
    word_list = re.sub("[^\w]", " ",  string).split()

    for word in word_list:
        if word not in recorded_words and word not in EXCLUDE_ARTICLE:
            for relation in INCLUDED_RELATIONS:
                concept_array_start = query(word, "start", relation, thresh)
                concept_array_end   = query(word, "end", relation, thresh)
                concept_array = concept_array_end + concept_array_start

                listed = concept_array
                listed = filter_concept(concept_array, relation)

                for concept in listed:
                    if not DBO_Concept.does_exist_relation(concept[0], concept[1], relation):
                        new_concept = Concept(-1, concept[0], relation, concept[1])
                        DBO_Concept.addConcept(new_concept)
                        inner_count += 1

            recorded_words.append(word)

    file.close()
    return inner_count


def record_word_data(word):
    if word not in EXCLUDE_ARTICLE:
        for relation in INCLUDED_RELATIONS:
            concept_array_start = query(word, "start", relation, thresh)
            concept_array_end = query(word, "end", relation, thresh)
            concept_array = concept_array_end + concept_array_start

            listed = filter_concept(concept_array, relation)

            for concept in listed:
                new_concept = Concept(-1, concept[0], relation, concept[1])
                DBO_Concept.addConcept(new_concept)


def restrict_data(filename):
    inner_count = 0
    file = open(filename, "r")
    string = file.read()
    word_list = re.sub("[^\w]", " ",  string).split()
    for word in word_list:
        if word not in recorded_words:
            recorded_words.append(word)

    file.close()

counted = 0

stories = []
story_count = 0

for text in stories:
    recorded_count = record_data("text_to_be_processed/"+text)
    story_count += recorded_count
    print(text + " = " + recorded_count)

counted += story_count

verbs = record_capabilities("text_to_be_processed/basic verbs")
print("VERBS: ",verbs)
counted += counted

capability = record_capabilities("text_to_be_processed/basic verb capability")
print("CAPABILITY: ",capability)
counted += counted

print("FINAL STORIES: ", story_count)
print("FINAL VERBS: ", verbs)
print("FINAL CAPABILITIES: ", capability)

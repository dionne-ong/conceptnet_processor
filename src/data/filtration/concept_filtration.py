from src.data.ConceptNetAPI import conceptnet
from src.data.filtration import concept_filter_config


def has_excluded_word(word):
    for excluded_word in concept_filter_config.EXCLUDED_WORDS:
        if excluded_word in word:
            return True
    for excluded_full in concept_filter_config.EXCLUDE_FULL:
        split_word = word.split(" ")
        for is_word in split_word:
            if is_word == excluded_full:
                return True
    return False


def is_at_excluded_location(end_word):
    for excluded_word in concept_filter_config.EXLUDED_AT_LOCATION:
        if excluded_word in end_word:
            return True
    return False


def is_capable_of_excluded_action(end_word):
    for excluded_word in concept_filter_config.EXCLUDED_CAPABLE_OF:
        if excluded_word in end_word:
            return True
    return False


def is_used_for_excluded_action(end_word):
    for excluded_word in concept_filter_config.EXCLUDED_USED_FOR:
        if excluded_word in end_word:
            return True
    return False


def filter_concept(concept_array, relation):

    to_remove = []
    for i in range(0, len(concept_array)):
        will_remove = False

        concept = concept_array[i]

        word_a = concept[0]
        word_b = concept[1]

        if( not will_remove
                and (has_excluded_word(word_a) or has_excluded_word(word_b))):
            will_remove = True

        if( not will_remove
                and relation == "AtLocation"
                and is_at_excluded_location(word_b)):
            will_remove = True

        if (not will_remove
                and relation == "CapableOf"
                and is_capable_of_excluded_action(word_b)):
            will_remove = True

        if (not will_remove
                and relation == "UsedFor"
                and is_used_for_excluded_action(word_b)):
            will_remove = True

        if will_remove:
            to_remove.append(concept)

    for removed_concept in to_remove:
        concept_array.remove(removed_concept)

    return concept_array


def filter_all_concept(word):
    final = []

    for relation in concept_filter_config.INCLUDED_RELATIONS:
        concept_array_start = conceptnet.query(word, "start", relation, 1.0)
        concept_array_end   = conceptnet.query(word, "end", relation, 1.0)
        concept_array = concept_array_end + concept_array_start

        filtered = filter_concept(concept_array, relation)

        final += filtered

    return final
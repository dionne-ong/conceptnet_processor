INCLUDED_RELATIONS = ["IsA",
                      "PartOf",
                      "AtLocation",
                      "HasPrerequisite",
                      "CreatedBy",
                      "UsedFor",
                      "Causes",
                      "Desires",
                      "CapableOf",
                      "HasProperty",
                      ]
# excluded concepts : derived from ALICE's list

#max number of words in a concept that will be accepted (if one of the concepts in a relation has more than X num of words, it will be excluded)
WORD_THRESHOLD = 3

# if concept containes <EXCLUDED_WORD> in it, it will be excluded
EXCLUDED_WORDS = [
                    "liberal",
                    "republican",
                    "democrat",
                    "communist",
                    "dictator",
                    "authoritarian",
                    "monarchy",
                    "oligarchy",
                    "homosexual",
                    "pussy",
                    "porn",
                    "sex",
                    "fellatio",
                    "cunnilingus",
                    "penis",
                    "vagina",
                    "testicle",
                    "testis",
                    "orgasm",
                    "procreate",
                    "ejaculate",
                    "ejaculation",
                    "sexual",
                    "arousal",
                    "intercourse",
                    "erection",
                    "vulva",
                    "clitoris",
                    "bestiality",
                    "xxx",
                    "xx",
                    "murder",
                    "suicide",
                    "suicidal",
                    "homicide",
                    "homicidal",
                    "poison",
                    "poisons",
                    "big cock",
                    "dick",
                    "dildo",
                    "masturbation",
                    "vibrator",
                    "whore",
                    "fuck",
                    "harass",
                    "wank off",
                    "jack off",
                    "shit",
                    "piss",
                    "voyeur",
                    "titty",
                    "cancer",
                    "swastika",
                    "erotic",
                    "stripper",
                    "flagellation",
                    "masochist",
                    "sadist",
                    "slut",
                    "disgust",
                    "slaughter",
                    "massacre",
                    "bloodshed",
                    "poop",
                    "pubic",
                    "illegal",
                    "betray",
                    "victim",
                    "methamphetamine",
                    "heroin",
                    "cocaine",
                    "prostitute",
                    "stab",
                    "alcohol",
                    "beer",
                    "vodka",
                    "naked"
                ]
    #only excludes if full word is in the concept || should probably change to regex
EXCLUDE_FULL = [
        "tit",
        "war",
        "wars",
        "rape",
        "raper",
        "rapist",
        "rapes",
        "raped",
        "tit",
        "anus",
        "anuses",

]

# exclude articles
EXCLUDE_ARTICLE = [
    "a",
    "an",
    "the"
]

#concepts with <EXCLUDED> as the end node of its AT LOCATION relation will be excluded
EXLUDED_AT_LOCATION = [
    "you",
    "person",
    "someone",
    "brothel",
    "kill",
    "killing",
    "kills",
    "killer"
]

#concepts with <EXCLUDED> as the end node of its CAPABLE OF relation will be excluded
EXCLUDED_CAPABLE_OF = [
    "torture",
    "murder",
    "steal",
    "commit crime",
    "hate",
]

#concepts with <EXCLUDED> as the end node of its USED FOR relation will be excluded

EXCLUDED_USED_FOR = [
    "kill"
]
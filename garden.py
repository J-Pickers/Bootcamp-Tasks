import spacy

nlp = spacy.load('en_core_web_sm')

# Creating list containing sentences
gardenpathSentences = ["The old man the boat.",
                       "I convinced her children are noisy."
                       "Mary gave the child a Band-Aid."
                       "That Jill is never here hurts.",
                       "The cotton clothing is made of grows in Missisippi.",
                       "The man who whistles tunes Fenders."]

# This function tokenizes the input text
def tokenize(text):
    doc = nlp(text)

    for token in doc:
        print(token.text)

# This function performs NER on the input text
def ner(text):
    doc = nlp(text)

    for ent in doc.ents:
        print(f"{ent.text:{10}} {ent.label_}")

# Calling both functions on every sentence in the list
for sentence in gardenpathSentences:
    tokenize(sentence)

for sentence in gardenpathSentences:
    ner(sentence)

# The entity GPE is defined as Countries, Cities and States.
# This makes sense as the city of Mississipi has been tagged as such.
print(spacy.explain("GPE"))

# The entity ORG is defined as Companies, Agencies Institutions etc.
# This makes sense as Fender is a manufacturer of instruments.
print(spacy.explain("ORG"))

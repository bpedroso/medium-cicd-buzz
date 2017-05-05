def generate_buzz():
  buzz_terms = sample(buzz, 2)
  phrase = ' '.join([sample(adjectives), buzz_terms[0], sample(adverbs),
    sample(verbs), buzz_terms[1]])
  return phrase.title()


import pandas as pd

endf = pd.read_csv("EN/resultsEN_bypair.tsv", sep="\t")

print(endf['construction'].unique())

constructions = ['Across object rel. clause',
                  'Across object rel. clause (no that)',
                  'Across prepositional phrase',
                  'Across subject rel. clause',
                  'In a sentenial complement',
                  'Simple',
                  'VP Coordination (long)',
                  'VP Coordination (short)',
                  'Within object rel. clause',
                  'Within object rel. clause (no that)']

constructionsNPI = ['NPI: Across object rel. clause', 'NPI: Simple']

constructionsRA = ['Reflexive Anaphora: Across a relative clause',
                  'Reflexive Anaphora: In a sentenial complement',
                  'Reflexive Anaphora: Simple']


def printer(constructions, data):
    filtered = data[
    (data["model"].str.strip() == "bert-base-cased") &
    (data["construction"].isin(constructions))
]
    print(filtered["acc"].mean())
    filtered = data[
    (data["model"].str.strip() == "bert-base-multilingual-cased") &
    (data["construction"].isin(constructions))
]
    print(filtered["acc"].mean())


print("regular")
printer(constructions, endf)
print("RA")
printer(constructionsRA, endf)
print("NPI")
printer(constructionsNPI, endf)












# "bert-base-multilingual-cased"
#'NPI: Across object rel. clause',
#                  'NPI: Simple',
# 'Reflexive Anaphora: Across a relative clause',
#                  'Reflexive Anaphora: In a sentenial complement',
#                  'Reflexive Anaphora: Simple',
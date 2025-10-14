import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Morphological complexity (CWALZ scores)
# Note that French value is a slight estimate (not explicitly stated in Bentz et al.)
c_walz = {"de": 0.397, "en": 0.329, "ru": 0.453, "he": 0.529, "fr": 0.435}

# German
dedf = pd.read_csv("de/resultsDE_bypair.tsv", sep="\t")
deAcc = dedf["acc"].mean()
#print("DE:", deAcc)

# French
frdf = pd.read_csv("FR/resultsFR_bypair.tsv", sep="\t")
frAcc = frdf["acc"].mean()
#print("FR:", frAcc)

# Hebrew
hedf = pd.read_csv("HE/resultsHE_bypair.tsv", sep="\t")
heAcc = hedf["acc"].mean()
#print("HE:", heAcc)

# Russian
rudf = pd.read_csv("RU/resultsRU_bypair.tsv", sep="\t")
ruAcc = rudf["acc"].mean()
#print("RU:", ruAcc)

# English (multilingual model)
# Only selecting constructions shared by other languages
endf = pd.read_csv("EN/resultsEN_bypair.tsv", sep="\t")

# Only selecting constructions shared by other languages
constructions = ["Across object rel. clause", "Across prepositional phrase", "Across subject rel. clause", "Simple","VP Coordination (long)", "VP coordination (short)","Within object rel. clause"]
filteredEn = endf[
    (endf["model"].str.strip() == "bert-base-multilingual-cased") &
    (endf["construction"].isin(constructions))
]
enAcc = filteredEn["acc"].mean()
#print("EN:", enAcc)

# Organize in order to create plot
langs = ["en", "de", "fr", "ru", "he"]
complexities = [c_walz[l] for l in langs]
accs = [enAcc, deAcc, frAcc, ruAcc, heAcc]

plt.figure(figsize=(8, 6))
plt.scatter(complexities, accs, color="orange", label="mBERT")

# Adding the trendline
z = np.polyfit(complexities, accs, 1) # trendline
p = np.poly1d(z) # make a function of the trendline (p(complexities gives accuracy values by language))
plt.plot(complexities, p(complexities), "--", color="orange", alpha=0.7)

# Label languages as dots in the plot
for i, lang in enumerate(langs):
    plt.text(complexities[i], accs[i] + 0.01, lang.upper(), ha="center", fontsize=10)

# Labels
plt.xlabel("Morphological Complexity (C_WALZ)")
plt.ylabel("Average Accuracy")
plt.title("mBERT Accuracy vs Morphological Complexity (C_WALZ)")

# Axis limits and ticks
plt.xticks(np.arange(0.3, 0.6, 0.05))
plt.yticks(np.arange(0.5, 1.0, 0.1))

# Legend + show plot
plt.legend(loc="upper right")
plt.grid(True)
plt.show()

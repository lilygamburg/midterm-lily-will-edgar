import pandas as pd

def txt_to_df(filepath, construction_name,language_name,curr_sentid):
    """
    Convert a txt file containing sentence pairs into a dataframe for TSV export.

    Args:
        filepath (str): Path to the  file.
        construction_name (str): Name of the construction (for the 'construction' column).
        language_name (str): language being evaluated
        curr_sentid: current sentid (so all files can be made to one)

    Returns:
        pd.DataFrame: DataFrame with columns: sentid, pairid, comparison, sentence, construction
    """
    
    # Load txt file
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = [clean_sentence(line) for line in f.readlines() if line.strip()] # take lines independently
    
    # Prepare columns
    sentid = []
    pairid = []
    comparisons = []
    sentences = []
    construction = []
    language = []
    
    sent_counter = curr_sentid # starts at where last file left off
    pair_counter = int((sent_counter-1)/2 + 1)
    
    # Loop over all pairs in the file
    for i in range(0, len(lines), 2):
        expected = lines[i] # always formatted as first sentence true
        unexpected = lines[i+1] # second sentence fall

        # Add expected sentence
        sentid.append(sent_counter)
        pairid.append(pair_counter)
        comparisons.append('expected')
        sentences.append(expected)
        construction.append(construction_name)
        language.append(language_name)
        sent_counter += 1

        # Add unexpected sentence
        sentid.append(sent_counter)
        pairid.append(pair_counter)
        comparisons.append('unexpected')
        sentences.append(unexpected)
        construction.append(construction_name)
        language.append(language_name)
        sent_counter += 1
        pair_counter += 1

    # Create DataFrame
    df = pd.DataFrame({
        'sentid': sentid,
        'pairid': pairid,
        'construction': construction,
        'language': language,
        'comparison': comparisons,
        'sentence': sentences
    })

    return [df, sent_counter]

def clean_sentence(line):
    """
    Remove the True/False label at the start of lines in txt files.
    Assumes the line starts with 'True' or 'False' followed by whitespace.
    """
    # Split on first whitespace or tab and take the rest
    parts = line.split(maxsplit=1)
    if len(parts) == 2:
        return parts[1].strip()
    else:
        return ""  # Should not be reached but if line only includes "true" or "false"

# de
deFiles = [
    ('clams/de_evalset/long_vp_coord.txt','VP Coordination (long)'),
    ('clams/de_evalset/obj_rel_across_anim.txt','Across object rel. clause'),
    ('clams/de_evalset/obj_rel_within_anim.txt','Within object rel. clause'),
    ('clams/de_evalset/prep_anim.txt','Across prepositional phrase'),
    ('clams/de_evalset/simple_agrmt.txt','Simple'),
    ('clams/de_evalset/subj_rel.txt','Across subject rel. clause'),
    ('clams/de_evalset/vp_coord.txt','VP Coordination (short)')
]

dedf = pd.DataFrame()
curr_sentID = 1  # starting sentence ID

for filename, construction in deFiles:
    [df, curr_sentID] = txt_to_df(filename, construction, 'de', curr_sentID)
    dedf = pd.concat([dedf, df], ignore_index=True)

# Export to one TSV
dedf.to_csv('min_pair_sentences/de.tsv', sep='\t', index=False)

# en

enFiles = [
    ('clams/en_evalset/long_vp_coord.txt','VP Coordination (long)'),
    ('clams/en_evalset/npi_across_anim.txt','NPI: Across object rel. clause'),
    ('clams/en_evalset/npi_across_inanim.txt','NPI: Across object rel. clause'),
    ('clams/en_evalset/obj_rel_across_anim.txt','Across object rel. clause'),
    ('clams/en_evalset/obj_rel_across_inanim.txt','Across object rel. clause'),
    ('clams/en_evalset/obj_rel_no_comp_across_anim.txt','Across object rel. clause (no that)'),
    ('clams/en_evalset/obj_rel_no_comp_across_inanim.txt','Across object rel. clause (no that)'),
    ('clams/en_evalset/obj_rel_no_comp_within_anim.txt','Within object rel. clause (no that)'),
    ('clams/en_evalset/obj_rel_no_comp_within_inanim.txt','Within object rel. clause (no that)'),
    ('clams/en_evalset/obj_rel_within_anim.txt','Within object rel. clause'),
    ('clams/en_evalset/obj_rel_within_inanim.txt','Within object rel. clause'),
    ('clams/en_evalset/prep_anim.txt','Across prepositional phrase'),
    ('clams/en_evalset/prep_inanim.txt','Across prepositional phrase'),
    ('clams/en_evalset/reflexive_sent_comp.txt','Reflexive Anaphora: In a sentenial complement'),
    ('clams/en_evalset/reflexives_across.txt','Reflexive Anaphora: Across a relative clause'),
    ('clams/en_evalset/sent_comp.txt','In a sentenial complement'),
    ('clams/en_evalset/simple_agrmt.txt','Simple'),
    ('clams/en_evalset/simple_npi_anim.txt','NPI: Simple'),
    ('clams/en_evalset/simple_npi_inanim.txt','NPI: Simple'),
    ('clams/en_evalset/simple_reflexives.txt','Reflexive Anaphora: Simple'),
    ('clams/en_evalset/subj_rel.txt','Across subject rel. clause'),
    ('clams/en_evalset/vp_coord.txt','VP Coordination (short)')
]

endf = pd.DataFrame()
curr_sentID = 1  # starting sentence ID

for filename, construction in enFiles:
    [df, curr_sentID] = txt_to_df(filename, construction, 'en', curr_sentID)
    endf = pd.concat([endf, df], ignore_index=True)

# Export to one TSV
endf.to_csv('min_pair_sentences/en.tsv', sep='\t', index=False)

frFiles = [
    ('clams/fr_evalset/long_vp_coord.txt','VP Coordination (long)'),
    ('clams/fr_evalset/obj_rel_across_anim.txt','Across object rel. clause'),
    ('clams/fr_evalset/obj_rel_within_anim.txt','Within object rel. clause'),
    ('clams/fr_evalset/prep_anim.txt','Across prepositional phrase'),
    ('clams/fr_evalset/simple_agrmt.txt','Simple'),
    ('clams/fr_evalset/subj_rel.txt','Across subject rel. clause'),
    ('clams/fr_evalset/vp_coord.txt','VP coordination (short)')
]

frdf = pd.DataFrame()
curr_sentID = 1  # starting sentence ID

for filename, construction in frFiles:
    [df, curr_sentID] = txt_to_df(filename, construction, 'fr', curr_sentID)
    frdf = pd.concat([frdf, df], ignore_index=True)

# Export to one TSV
frdf.to_csv('min_pair_sentences/fr.tsv', sep='\t', index=False)

#he
heFiles = [
    ('clams/he_evalset/long_vp_coord.txt','VP Coordination (long)'),
    ('clams/he_evalset/obj_rel_across_anim.txt','Across object rel. clause'),
    ('clams/he_evalset/obj_rel_within_anim.txt','Within object rel. clause'),
    ('clams/he_evalset/prep_anim.txt','Across prepositional phrase'),
    ('clams/he_evalset/simple_agrmt.txt','Simple'),
    ('clams/he_evalset/subj_rel.txt','Across subject rel. clause'),
    ('clams/he_evalset/vp_coord.txt','VP coordination (short)')
]

hedf = pd.DataFrame()
curr_sentID = 1  # starting sentence ID

for filename, construction in heFiles:
    [df, curr_sentID] = txt_to_df(filename, construction, 'he', curr_sentID)
    hedf = pd.concat([hedf, df], ignore_index=True)

# Export to one TSV
hedf.to_csv('min_pair_sentences/he.tsv', sep='\t', index=False)

#ru
ruFiles = [
    ('clams/ru_evalset/long_vp_coord.txt','VP Coordination (long)'),
    ('clams/ru_evalset/obj_rel_across_anim.txt','Across object rel. clause'),
    ('clams/ru_evalset/obj_rel_within_anim.txt','Within object rel. clause'),
    ('clams/ru_evalset/prep_anim.txt','Across prepositional phrase'),
    ('clams/ru_evalset/simple_agrmt.txt','Simple'),
    ('clams/ru_evalset/subj_rel.txt','Across subject rel. clause'),
    ('clams/ru_evalset/vp_coord.txt','VP coordination (short)')
]

rudf = pd.DataFrame()
curr_sentID = 1  # starting sentence ID

for filename, construction in ruFiles:
    [df, curr_sentID] = txt_to_df(filename, construction, 'ru', curr_sentID)
    rudf = pd.concat([rudf, df], ignore_index=True)

# Export to one TSV
rudf.to_csv('min_pair_sentences/ru.tsv', sep='\t', index=False)

"""
this script is used to add traits into one single file
"""

age_trait = ['stroke', 'alzheimers', 'parkinson', 't_2_diabetes', 'metabolic_syndrome', 'obesity', 'cardiovascular_disease', 'hypertension', 'age_related_macular_degeneration']
cancer = ['prostate', 'colorectal', 'ovarian', 'pancreatic', 'breast']
single_list = age_trait + cancer
# print(single_list)


out_single_file = open('age_trait_and_cancer.tsv', 'w')
out_age_trait = open('age_trait.tsv', 'w')
out_cancer = open('cancer.tsv', 'w')
for trait in age_trait:
    with open(trait + '.entries.tsv', 'r') as f:
        for line in f:
            out_single_file.write(line)
            out_age_trait.write(line)
for trait in cancer:
    with open(trait + '.entries.tsv', 'r') as f:
        for line in f:
            out_single_file.write(line)
            out_cancer.write(line)
out_single_file.close()
out_age_trait.close()
out_cancer.close()
print('job done!')
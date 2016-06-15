"""
add trait associated gene from each trait list. Then add info to each gene
example usage: python3 get_trait_asso_gene_and_add_info.py stoke.entries.tsv stoke.genes.info.tsv
"""

# from add_mafkb_gwas_mapping_to_1kflank_mapping import build_ensg_other_info_dict


def build_ensg_other_info_dict():
    d = {}
    with open('asso_efo_count_each_gene_add_gwas_mapping_mafkb_gene_length.tsv', 'r') as f:
        next(f)
        for line in f:
            ensg = line.strip().split('\t', 1)[0]
            other_info = line.strip().split('\t', 1)[1]
            d[ensg] = other_info
    return d


def convert_nonetype_to_none_str(sth_could_be_nonetype):
    if not sth_could_be_nonetype:
        sth_could_be_nonetype = ''
        print(1)
    else:
        pass
    return sth_could_be_nonetype


def write_file(trait_list, dic):
    for trait in trait_list:
        l = []
        outfile = open(trait + '.genes.tsv', 'w')
        with open(trait + '.entries.tsv', 'r') as f:
            for line in f:
                # print(len(line.strip().split('\t')))
                if len(line.strip().split('\t')) > 36:
                    # print(line)
                    ensg = line.strip().split('\t')[36]
                    # print(ensg)
                    if ',' in ensg:
                        for i in ensg.split(','):
                            l.append(i)

                    else:
                        l.append(ensg)
                    # print(l)
                    # print(len(l))
                    # ensg = convert_nonetype_to_none_str(ensg)
                    # if not ensg:
                    #     l.append(ensg)
                    #     print(l)
        l = list(set(l))
        # print(l)
        for gene in l:
            other_info = dic.get(gene)
            # if not other_info:
            outfile.write(gene + '\t' + other_info + '\n')
        outfile.close()


def write_file_for_combined_trait(combined_trait_file_name, outfile_name, dic):
    l = []
    outfile = open(outfile_name, 'w')
    with open(combined_trait_file_name, 'r') as f:
        for line in f:
            # print(len(line.strip().split('\t')))
            if len(line.strip().split('\t')) > 36:
                # print(line)
                ensg = line.strip().split('\t')[36]
                # print(ensg)
                if ',' in ensg:
                    for i in ensg.split(','):
                        l.append(i)

                else:
                    l.append(ensg)
                # print(l)
                # print(len(l))
                # ensg = convert_nonetype_to_none_str(ensg)
                # if not ensg:
                #     l.append(ensg)
                #     print(l)
    l = list(set(l))
    # print(l)
    for gene in l:
        other_info = dic.get(gene)
        # if not other_info:
        outfile.write(gene + '\t' + other_info + '\n')
    outfile.close()


dictionary = build_ensg_other_info_dict()
age_trait = ['stroke', 'alzheimers', 'parkinson', 't_2_diabetes', 'metabolic_syndrome', 'obesity', 'cardiovascular_disease', 'hypertension', 'age_related_macular_degeneration']
cancer = ['prostate', 'colorectal', 'ovarian', 'pancreatic', 'breast']
write_file(age_trait, dictionary)
write_file(cancer, dictionary)

write_file_for_combined_trait('age_trait.tsv', 'age_trait_genes.tsv', dictionary)
write_file_for_combined_trait('age_trait_and_cancer.tsv', 'age_trait_and_cancer_genes.tsv', dictionary)
write_file_for_combined_trait('cancer.tsv', 'cancer_genes.tsv', dictionary)
print('job done!')


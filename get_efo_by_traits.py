"""
1. create a list of EFOs for traits interested
2. check if EFOs of an association file is in the list
3. if 2 is true, extract that entry(into a separate file) and rs ids(put into a list)
4. use rs ids, get gene it mapped to
    a. build a dictionary from combined single mapping file
    b.
5. add a column of mapped genes to each entry
6.
"""


# age related disease EFO list
stroke = ['http://www.ebi.ac.uk/efo/EFO_0000712']
alzheimers = ['http://www.ebi.ac.uk/efo/EFO_0000249']
parkinson = ['http://www.ebi.ac.uk/efo/EFO_0002508']
t_2_diabetes = ['http://www.ebi.ac.uk/efo/EFO_0001360']
metabolic_syndrome = ['http://www.ebi.ac.uk/efo/EFO_0000195']
obesity = ['http://www.ebi.ac.uk/efo/EFO_0001073', 'http://www.ebi.ac.uk/efo/EFO_0001074']
cardiovascular_disease = ['http://www.ebi.ac.uk/efo/EFO_0000319']
hypertension = ['http://www.ebi.ac.uk/efo/EFO_0000537']
age_related_macular_degeneration = ['http://www.ebi.ac.uk/efo/EFO_0001365']
# cancers
prostate = ['http://www.ebi.ac.uk/efo/EFO_0001663', 'http://www.ebi.ac.uk/efo/EFO_0000673', 'http://www.ebi.ac.uk/efo/EFO_1000498', 'http://www.ebi.ac.uk/efo/EFO_1000065', 'http://www.ebi.ac.uk/efo/EFO_0002621', 'http://www.ebi.ac.uk/efo/EFO_1000499']
colorectal = ['http://www.ebi.ac.uk/efo/EFO_0005842', 'http://www.ebi.ac.uk/efo/EFO_0005406', 'http://www.ebi.ac.uk/efo/EFO_0004142', 'http://www.ebi.ac.uk/efo/EFO_1000193', 'http://www.ebi.ac.uk/efo/EFO_0000365', 'http://www.ebi.ac.uk/efo/EFO_1000196', 'http://www.ebi.ac.uk/efo/EFO_1000198', 'http://www.ebi.ac.uk/efo/EFO_1000190', 'http://www.ebi.ac.uk/efo/EFO_1000192', 'http://www.ebi.ac.uk/efo/EFO_1000195', 'http://www.ebi.ac.uk/efo/EFO_1000197', 'http://www.ebi.ac.uk/efo/EFO_1000657', 'http://www.ebi.ac.uk/efo/EFO_0004288', 'http://www.ebi.ac.uk/efo/EFO_0005631', 'http://www.ebi.ac.uk/efo/EFO_1000504', 'http://www.ebi.ac.uk/efo/EFO_1000506', 'http://www.ebi.ac.uk/efo/EFO_1000503', 'http://www.ebi.ac.uk/efo/EFO_1000505']
ovarian = ['http://www.ebi.ac.uk/efo/EFO_0001075', 'http://www.ebi.ac.uk/efo/EFO_1000422', 'http://www.ebi.ac.uk/efo/EFO_1000414', 'http://www.ebi.ac.uk/efo/EFO_1000412', 'http://www.ebi.ac.uk/efo/EFO_0006460', 'http://www.ebi.ac.uk/efo/EFO_0003893', 'http://www.ebi.ac.uk/efo/EFO_0006718', 'http://www.ebi.ac.uk/efo/EFO_1000420', 'http://www.ebi.ac.uk/efo/EFO_1000413', 'http://www.ebi.ac.uk/efo/EFO_0006463', 'http://www.ebi.ac.uk/efo/EFO_1000113', 'http://www.ebi.ac.uk/efo/EFO_1000428', 'http://www.ebi.ac.uk/efo/EFO_1000437', 'http://www.ebi.ac.uk/efo/EFO_1000431', 'http://www.ebi.ac.uk/efo/EFO_1000605', 'http://www.ebi.ac.uk/efo/EFO_1000415', 'http://www.ebi.ac.uk/efo/EFO_1000115', 'http://www.ebi.ac.uk/efo/EFO_1000434', 'http://www.ebi.ac.uk/efo/EFO_1000135', 'http://www.ebi.ac.uk/efo/EFO_0006462', 'http://www.ebi.ac.uk/efo/EFO_1000424', 'http://www.ebi.ac.uk/efo/EFO_1000423', 'http://www.ebi.ac.uk/efo/EFO_1000425', 'http://www.ebi.ac.uk/efo/EFO_1000357', 'http://www.ebi.ac.uk/efo/EFO_1000137', 'http://www.ebi.ac.uk/efo/EFO_1000416', 'http://www.ebi.ac.uk/efo/EFO_1000116', 'http://www.ebi.ac.uk/efo/EFO_1000435', 'http://www.ebi.ac.uk/efo/EFO_1000043', 'http://www.ebi.ac.uk/efo/EFO_1000426', 'http://www.ebi.ac.uk/efo/EFO_0006461', 'http://www.ebi.ac.uk/efo/EFO_1000112', 'http://www.ebi.ac.uk/efo/EFO_1000427', 'http://www.ebi.ac.uk/efo/EFO_1000139', 'http://www.ebi.ac.uk/efo/EFO_1000432', 'http://www.ebi.ac.uk/efo/EFO_0002507', 'http://www.ebi.ac.uk/efo/EFO_1000419', 'http://www.ebi.ac.uk/efo/EFO_1000138', 'http://www.ebi.ac.uk/efo/EFO_1000433', 'http://www.ebi.ac.uk/efo/EFO_0002917', 'http://www.ebi.ac.uk/efo/EFO_1000421', 'http://www.ebi.ac.uk/efo/EFO_1000042', 'http://www.ebi.ac.uk/efo/EFO_1000358', 'http://www.ebi.ac.uk/efo/EFO_1000136', 'http://www.ebi.ac.uk/efo/EFO_1000114', 'http://www.ebi.ac.uk/efo/EFO_1000429', 'http://www.ebi.ac.uk/efo/EFO_1000140', 'http://www.ebi.ac.uk/efo/EFO_1000117', 'http://www.ebi.ac.uk/efo/EFO_1000430', 'http://www.ebi.ac.uk/efo/EFO_0002511', 'http://www.ebi.ac.uk/efo/EFO_0002510']
pancreatic = ['http://www.ebi.ac.uk/efo/EFO_0002618', 'http://www.ebi.ac.uk/efo/EFO_0003860', 'http://www.ebi.ac.uk/efo/EFO_1000441', 'http://www.ebi.ac.uk/efo/EFO_1000440', 'http://www.ebi.ac.uk/efo/EFO_1000044', 'http://www.ebi.ac.uk/efo/EFO_1000445', 'http://www.ebi.ac.uk/efo/EFO_0006471', 'http://www.ebi.ac.uk/efo/EFO_0007416', 'http://www.ebi.ac.uk/efo/EFO_1000443', 'http://www.ebi.ac.uk/efo/EFO_1000606', 'http://www.ebi.ac.uk/efo/EFO_0002517', 'http://www.ebi.ac.uk/efo/EFO_1000359', 'http://www.ebi.ac.uk/efo/EFO_0006732', 'http://www.ebi.ac.uk/efo/EFO_1000133', 'http://www.ebi.ac.uk/efo/EFO_1000045', 'http://www.ebi.ac.uk/efo/EFO_1000439', 'http://www.ebi.ac.uk/efo/EFO_1000444', 'http://www.ebi.ac.uk/efo/EFO_1000442', 'http://www.ebi.ac.uk/efo/EFO_1000398', 'http://www.ebi.ac.uk/efo/EFO_1000607']
breast = ['http://www.ebi.ac.uk/efo/EFO_0000305', 'http://www.ebi.ac.uk/efo/EFO_1000650', 'http://www.ebi.ac.uk/efo/EFO_0006861', 'http://www.ebi.ac.uk/efo/EFO_0005537', 'http://www.ebi.ac.uk/efo/EFO_1000649', 'http://www.ebi.ac.uk/efo/EFO_0000304', 'http://www.ebi.ac.uk/efo/EFO_1000402', 'http://www.ebi.ac.uk/efo/EFO_1000306', 'http://www.ebi.ac.uk/efo/EFO_1000040', 'http://www.ebi.ac.uk/efo/EFO_0000306', 'http://www.ebi.ac.uk/efo/EFO_1000307', 'http://www.ebi.ac.uk/efo/EFO_1000294', 'http://www.ebi.ac.uk/efo/EFO_1000071', 'http://www.ebi.ac.uk/efo/EFO_0000580', 'http://www.ebi.ac.uk/efo/EFO_1000053', 'http://www.ebi.ac.uk/efo/EFO_1000019', 'http://www.ebi.ac.uk/efo/EFO_1000047', 'http://www.ebi.ac.uk/efo/EFO_1000326', 'http://www.ebi.ac.uk/efo/EFO_1000984', 'http://www.ebi.ac.uk/efo/EFO_0006318', 'http://www.ebi.ac.uk/efo/EFO_1000382', 'http://www.ebi.ac.uk/efo/EFO_1000146', 'http://www.ebi.ac.uk/efo/EFO_1000144', 'http://www.ebi.ac.uk/efo/EFO_0000432', 'http://www.ebi.ac.uk/efo/EFO_0000281']


def get_efo_list(line_from_gwas_asso_file):
    with open('no_efo_mapping_entries.tsv', 'a') as f:
        try:
            efo_list = line_from_gwas_asso_file.strip().split('\t')[35].split(',')
            return efo_list
        except IndexError:
            # print(line_from_gwas_asso_file)
            f.write(line_from_gwas_asso_file)


def classify_to_each_file(line_from_gwas_asso_file, trait_name_list):
    trait_list = [stroke, alzheimers, parkinson, t_2_diabetes, metabolic_syndrome, obesity, cardiovascular_disease, hypertension, age_related_macular_degeneration, prostate, colorectal, ovarian, pancreatic, breast]
    names = trait_name_list
    for i in trait_list:
        # print(names[trait_list.index(i)])
        trait_name = (names[trait_list.index(i)])   # together with the names list, just for generate a proper file name
        with open(trait_name + '.entries.tsv', 'a') as f:
            efo_list = get_efo_list(line_from_gwas_asso_file)
            try:
                for j in efo_list:
                    if j in i:
                        f.write(line_from_gwas_asso_file)
                    else:
                        pass
            except TypeError:
                with open('no_efo_mapping_entries.tsv', 'a') as f:
                    print(line_from_gwas_asso_file.strip())
                    f.write(line_from_gwas_asso_file)
    return


def check_if_duplicated_lines_exits(trait_name_list):
    """
    this function is used to check if duplicated lines exits
    :param trait_name_list:
    :return:
    """
    for trait_name in trait_name_list:
        print(trait_name)
        with open(trait_name + '.entries.tsv', 'r') as f:
            seen = set()
            for line in f:
                if line in seen:
                    # print(line)
                    return False
                else:
                    seen.add(line)


trait_name_list = ['stroke', 'alzheimers', 'parkinson', 't_2_diabetes', 'metabolic_syndrome', 'obesity', 'cardiovascular_disease', 'hypertension', 'age_related_macular_degeneration', 'prostate', 'colorectal', 'ovarian', 'pancreatic', 'breast']
with open('gwas_asso_file_1kb_flank_my_mapping.tsv', 'r') as f:
    next(f)
    for line in f:
        classify_to_each_file(line, trait_name_list)
    print('job done!')
assert check_if_duplicated_lines_exits(trait_name_list)
print('no duplicated lines found in all trait files!')


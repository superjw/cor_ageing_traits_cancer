"""
this script is used to add default GWAS-Catalog mapping info and MAF/kb and other info into 1kb flank mapping file ---
`asso_efo_count_each_gene.tsv`
"""


def build_ensg_other_info_dict():
    d = {}
    with open('../correlation_analysis_traits_af_pi/no_m_traits_af_single_file_glength.tsv', 'r') as f:
        next(f)
        for line in f:
            ensg = line.strip().split('\t', 1)[0]
            other_info = line.strip().split('\t', 1)[1]
            d[ensg] = other_info
    return d


ensg_other_info_dict = build_ensg_other_info_dict()
outfile = open('asso_efo_count_each_gene_add_gwas_mapping_mafkb_gene_length.tsv', 'w')
outfile.write('ENSG\tasso_count\tefo_count/mapped_traits\teas\tamr\tafr\teur\tsas\tAF\tgene_name\tno_of_m_traits\tgene_length\n')
with open('asso_efo_count_each_gene.tsv', 'r') as f:
    header = next(f)
    for line in f:
        ensg = line.strip().split('\t', 1)[0]
        new_line = line.strip() + '\t' + ensg_other_info_dict.get(ensg)
        outfile.write(new_line + '\n')
print('job done!')

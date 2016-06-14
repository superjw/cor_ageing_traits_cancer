"""
script for adding my own mapping to GWAS-Catalog SNPs
I use GRCh37 gene positions and 1kb flank both side
"""


def build_rs_gene_mapping_dict():
    d_id = {}
    d_name = {}
    with open('../maf_per_kb_analysis/single_mapping_file.tsv', 'r') as f:
        for line in f:
            line = line.strip().split('\t')
            try:
                d_id[line[2]] = line[8]
                d_name[line[2]] = line[9]
            except IndexError:
                pass
    print('dict-build done!')
    return d_id, d_name


def convert_nonetype_to_none_str(sth_could_be_nonetype):
    """
    used to deal with the issues when trying add NoneType to strings. potential error see below
    Error: TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
    :param sth_could_be_nonetype:
    :return:
    """
    if not sth_could_be_nonetype:
        sth_could_be_nonetype = ''
        print(1)
    else:
        pass
    return sth_could_be_nonetype


def get_gid_gname_from_dict(rs_id_list, id_dict, name_dict):
    gid = ''
    gname = ''
    for i in rs_id_list:
        id_in_line = id_dict.get(i.replace(' ', ''))
        gname_in_line = name_dict.get(i.replace(' ', ''))
        gid += convert_nonetype_to_none_str(id_in_line) + ','
        gname += convert_nonetype_to_none_str(gname_in_line) + ','
    return gid.strip(','), gname.strip(',')


gene_id_dict, gene_name_dict = build_rs_gene_mapping_dict()
outfile = open('gwas_asso_file_1kb_flank_my_mapping.tsv', 'w')
with open('./03/gwas_catalog_associations_ontology-annotated.tsv', 'r') as f:
    header = next(f)
    outfile.write(header + '\t1kb_mapped_gene_id\t1kb_mapped_gene_name\n')
    for line in f:
        rs = line.strip().split('\t')[21].split(',')
        if rs:
            gene_id_string, gene_name_sting = get_gid_gname_from_dict(rs, gene_id_dict, gene_name_dict)
            outfile.write(line + '\t' + gene_id_string + '\t' + gene_name_sting + '\n')
outfile.close()
print('job done!')
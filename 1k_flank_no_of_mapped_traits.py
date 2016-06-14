"""
this script is used for count no_of_mapped_traits of each gene based on mapping with 1kb flank
"""


def get_set_of_ensg(association_file_with_mapping_obj):
    l = []
    # expr = r''
    next(association_file_with_mapping_obj)
    for line in association_file_with_mapping_obj:
        ensg = line.strip().split('\t')[36].replace(' ', '')
        if not ensg:
            if ',' in ensg:
                ensg = ensg.split(',')
                for i in ensg:
                    l.append(i)
            else:
                l.append(ensg)
        print('gene list set built!')
    return list(set(l))


def get_number_of_asso_and_efo(ensembl_gene_id, asso_file_obj):
    no_of_association = 0
    efo_list = []
    next(asso_file_obj)
    for line in asso_file_obj:
        if ensembl_gene_id in line.strip().split('\t')[36].replace(' ', ''):
            efo_link = line.strip().split('\t')[35].replace(' ', '')
            if ',' in efo_link:
                for efo in efo_link:
                    if efo not in efo_list:
                        efo_list.append(efo)
                    else:
                        pass
            else:
                if efo not in efo_list:
                    efo_list.append(efo)
                else:
                    pass
            no_of_association += 1
        else:
            print(line)
            pass
    return str(no_of_association), str(len(efo_list))


outfile = open('asso_efo_count_each_gene.tsv', 'w')
outfile.write('ENSG\tasso_count\tefo_count/mapped_traits\n')
with open('gwas_asso_file_1kb_flank_my_mapping.tsv', 'r') as f:
    ensg_ids = get_set_of_ensg(f)
    for ensg in ensg_ids:
        asso_count, efo_count = get_number_of_asso_and_efo(ensg, f)
        outfile.write(ensg + '\t' + asso_count + '\t' + efo_count + '\n')
        # print(ensg + '\t' + asso_count + '\t' + efo_count)
outfile.close()
print('job done!')

"""
this script is used for count no_of_mapped_traits of each gene based on mapping with 1kb flank
"""


def get_set_of_ensg(association_file_with_mapping_obj):
    l = []
    next(association_file_with_mapping_obj)
    for line in association_file_with_mapping_obj:
        # print(line)
        try:
            ensg = line.strip().split('\t')[36].replace(' ', '')
            if ',' in ensg:
                ensg = ensg.split(',')
                for i in ensg:
                    l.append(i)
            else:
                l.append(ensg)
            # print(ensg)
            # print('===========')
        except IndexError:
            pass
    print('gene list set built!')
    # print(list(set(l)))
    return list(set(l))


def get_number_of_asso_and_efo(ensembl_gene_id):
    inf = open('gwas_asso_file_1kb_flank_my_mapping.tsv', 'r')
    no_of_association = 0
    efo_list = []
    next(inf)
    for line in inf:
        print(line.strip())
        # if ensembl_gene_id in line.strip().split('\t')[36].replace(' ', ''):
        print(ensembl_gene_id)
        if ensembl_gene_id in line:
            efo_link = line.strip().split('\t')[35].replace(' ', '')
            if ',' in efo_link:
                for efo in efo_link:
                    if efo not in efo_list:
                        efo_list.append(efo)
                    else:
                        pass
            else:
                if efo_link not in efo_list:
                    efo_list.append(efo_link)
                else:
                    pass
            no_of_association += 1
            print(no_of_association)
        else:
            # print(line)
            pass
    inf.close()
    return str(no_of_association), str(len(efo_list))


outfile = open('asso_efo_count_each_gene.tsv', 'w')
outfile.write('ENSG\tasso_count\tefo_count/mapped_traits\n')
infile = open('gwas_asso_file_1kb_flank_my_mapping.tsv', 'r')
ensg_ids = get_set_of_ensg(infile)
# print(ensg_ids)
for ensg in ensg_ids:
    # print(ensg)
    asso_count, efo_count = get_number_of_asso_and_efo(ensg)
    outfile.write(ensg + '\t' + asso_count + '\t' + efo_count + '\n')
    # print(ensg + '\t' + asso_count + '\t' + efo_count)
outfile.close()
infile.close()
print('job done!')

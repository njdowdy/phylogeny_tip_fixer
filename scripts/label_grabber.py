def grab_labels(file_with_bad_tips, output_file):
    import re
    import csv

    # each label must be between " ' " to be captured
    # convert to NEXUS format with figtree and/or manually add them to each
    tree = open(file_with_bad_tips, 'r')
    tree_content = tree.read()

    m = re.findall("(\')(.*?)(\')", tree_content)

    # extract tip labels
    n = []
    for match in m:
        n.append(match[1])

    # extract each piece of info from each label
    o = []
    for match in n:
        o.append(re.findall("([A-Z]\w+)", match))

    # separate label info
    sequence_id = ['sequence_id']
    genbank_accession_id = ['genbank_accession_id']
    ahe_id = ['ahe_id']
    specimen_id = ['specimen_id']
    genus = ['genus']
    species = ['species']
    subspecies = ['subspecies']
    locality = ['locality']
    catalognum = ['catalognum']
    institution_storing = ['institution_storing']
    gene_name = ['gene_name']
    original_tip_label = ['original_tip_label']
    count = 0
    for label in o:
        original_tip_label.append(n[count])
        count = count + 1
        if "seq1" not in label[0]:  # indicative of BOLD data
            sequence_id.append(label[0].replace("_", "-"))
            gene_name.append(label[2])
            if len(label) < 4:
                genbank_accession_id.append('NA')
            else:
                genbank_accession_id.append(label[3])
            ahe_id.append('NA')
            specimen_id.append('CROSSREF')
            genus.append(label[1].split('_')[0])
            species.append(label[1].split('_')[1])
            locality.append("CROSSREF")
            catalognum.append("CROSSREF")
            institution_storing.append("CROSSREF")
            if len(label[1].split('_')) > 2:
                subspecies.append(label[1].split('_')[2])
            else:
                subspecies.append(label[1].split('_')[1])
        else:
            new_lab = label[0].split('_Lepidoptera_Erebidae_')
            id_labs = new_lab[0].split('_')
            sequence_id.append(id_labs[0])
            gene_name.append('COI-MITOBIM')
            genbank_accession_id.append('NA')
            catalognum.append("NA")
            institution_storing.append("Milwaukee Public Museum")
            if len(id_labs) == 1:
                ahe_id.append('NA')
                specimen_id.append('NA')
            elif len(id_labs) == 2:
                if "AHE" in id_labs[1]:
                    ahe_id.append(id_labs[1])
                    specimen_id.append('NA')
                else:
                    ahe_id.append('NA')
                    specimen_id.append(id_labs[1])
            else:
                if "AHE" in id_labs[1]:
                    ahe_id.append(id_labs[1])
                    specimen_id.append(id_labs[2])
                else:
                    ahe_id.append(id_labs[2])
                    specimen_id.append(id_labs[1])
            name_labs = new_lab[1].split('_')[0:-1]
            genus.append(name_labs[0])
            species.append(name_labs[1])
            if len(name_labs) > 4:
                subspecies.append(name_labs[2])
                locality.append(name_labs[3])
            else:
                subspecies.append(name_labs[1])
                locality.append(name_labs[2])

    data = zip(original_tip_label, catalognum, sequence_id, gene_name, genbank_accession_id, ahe_id,
               specimen_id, genus, species, subspecies, locality, institution_storing)

    # write sample data
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        [writer.writerow(r) for r in data]

    return()

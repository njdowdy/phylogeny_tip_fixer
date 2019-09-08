def grab_labels(specimen_data, input_data, output_file):

    import pandas as pd

    # grab locality, institution_storing, catalognum
    specdata = pd.read_csv(specimen_data, sep='\t')
    data = pd.read_csv(input_data, sep=',')

    df = specdata.loc[specdata['processid'].isin(data.loc[data['locality'] == "CROSSREF"].sequence_id.tolist())]

    data.loc[data['locality'] == "CROSSREF", 'locality'] = df.province.tolist()
    data.loc[data['institution_storing'] == "CROSSREF", 'institution_storing'] = df.institution_storing.tolist()
    data.loc[data['catalognum'] == "CROSSREF", 'catalognum'] = df.catalognum.tolist()
    data.loc[data['specimen_id'] == "CROSSREF", 'specimen_id'] = df.sampleid.tolist()

    data.to_csv(output_file, sep=',')

    return()

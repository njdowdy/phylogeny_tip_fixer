def label_rebuilder(file_to_fix, input_data, output_file):
    import pandas as pd
    import numpy as np

    phylip = open(file_to_fix, 'r')
    phylip_content = phylip.read()

    data = pd.read_csv(input_data, sep=',')
    data = data.replace(np.nan, '', regex=True)
    og_tips = data.original_tip_label.to_list()
    data['subspecies2'] = " " + data['subspecies']
    data.loc[data['subspecies2'] == " " + data['species'], 'subspecies2'] = ""
    data['new_tips'] = data['genus'] + ' ' + data['species'] + data['subspecies2'] + " (" + data['index'].astype(
        'str') + ":" + data['ahe_label'] + " " + data['state'] + ")"
    new_tips = data.new_tips.to_list()

    dictionary = dict(zip(og_tips, new_tips))
    for old, new in dictionary.items():
        phylip_content = phylip_content.replace(old, new)

    file1 = open(output_file, "x")

    file1.write(phylip_content)
    file1.close()

    return ()

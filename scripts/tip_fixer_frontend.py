from scripts import label_grabber as lb
from scripts import data_associator as da
from scripts import tip_rebuilder as tr

# grab tip labels and store info in csv
badtips = 'input/RAxML_bipartitions.result.tre.nexus.txt' # should be a .txt file
output = 'output/COI_data.csv' # should be a .csv file
lb.grab_labels(badtips, output)

# associate tip labels with other BOLD data
specimen_data = 'input/Hypoprepia_All_SpecimenData.txt' # should be a .txt file
input_data = output
output_file = output.replace('data','data_edited')
da.grab_labels(specimen_data, input_data, output_file)

# manually fix any missing data if possible and add a "state" and "ahe_label" column

# rebuild tip labels
file_to_fix = 'input/Hypoprepia_COI_AHE_DATA.phy.txt' # should be a .txt file
input_data = 'output/COI_data_edited_state_added.csv' # should be a .csv file
output_file = file_to_fix.replace('input', 'output').replace('.txt','').replace('.','_tipLabsFixed.')
tr.label_rebuilder(file_to_fix, input_data, output_file)

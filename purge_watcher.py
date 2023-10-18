import re
import pandas as pd

def purge_watcher(path_purge_file, path_out_file):
  """ Returns a pandas dataframe of files up for deletion each month on Digital Alliance or SciNet
  Keyword Args:
  * path_purge_file (str): Path to the input file, including file title, ex. dir/subdir/myOldSciNetFiles.txt
  * path_out_file (str): Path to the output destination, including file title, ex. dir/subdir/upForDeletion.csv

  Returns:
  * G_count (list of int): A list indicating the number of atoms with i edges in G, where i is the index of G_count
  """
  
  if not type(path_purge_file) is str or not type(path_out_file) is str:
    raise TypeError("Only string paths are allowed")
  text_file = open(path_purge_file, "r")
  filename = text_file.readlines()
  filetype = []
  filepath = []

  # Regex commands to clean up data (Stackexchange used to find correct syntax)
  # These terms must be adjusted to fit your directory structure, these ones are set up for Niagara
  regex = '.*?/gpfs/.*/(.*)'
  regex2 = '(\..*)'
  regex3 = '.*?(/gpfs/.*)'

  # Use regex to get the file names, type/extension, and path in directory
  for i, l in enumerate(filename):
    filepath.append(re.findall(regex3, l)[0])
    filename[i] = re.findall(regex, l)[0]
    filetype.append(re.findall(regex2, filename[i])[0])
  text_file.close()

  # Ensure extraction did not pull inconsistent number of names, types, or paths
  if any(len(x) != len(filename) for x in [filename, filetype, filepath]):
    raise ValueError("Number of files, filetypes, or filepaths found do not match each other")

  print("Purge list processed, detected {} files".format(len(filepath)))

  # Format dict for pandas use
  data = {
    "filename": filename,
    "filetype": filetype,
    "filepath": filepath
  }

  #load data into a DataFrame object:
  out_data = pd.DataFrame(data)
  print("Dataframe has shape", out_data.shape)
  out_data.sort_values(by=["filetype", "filename"], inplace = True, ignore_index = True)
  print(out_data.head(5))
  out_data.to_csv(path_out_file)

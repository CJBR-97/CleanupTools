# CleanupTools
Code for organizing, reading, and removing files in a user-friendly way.

The purge_watcher.py and purge_watcher_bash.py python files were constructed for the list of files produced by SciNet on their Niagara supercomputer during monthly purges. The first version was developed for use in a Python environment such as Colab, and the "bash" version is for use in the terminal. The bash version comes with -h help functionality, and was originally developed from a bash shell script (.sh).

## Documentation

### purge_watcher_bash.py 
An arbitrary use case is shown below, for a file containing 10 items to be purged.  First load an environment with the required Python packages (pandas, etc).
<br>

```
source home/yourdir/ENV/bin/activate  
(ENV) python purge_watcher_bash.py --path_purge_file="filename.txt" --path_out_file="outfile.csv"
```

Which produces output as follows.

```
Received arguments as input path ['filename.txt'] and output path ['outfile.csv']
Note: regex commands here are for Niagara specifically, other file separators and printout formats may require adjustments. User-tunability of these is pending
Beginning function purge_watcher...
Purge list processed, detected 10 files
Dataframe has shape (10, 3)
                          filename filetype filepath
0  file_to_be_purged_0.csv     .csv  /path_0...
1  file_to_be_purged_1.csv     .csv  /path_1...
2  file_to_be_purged_2.csv     .csv  /path_2...
3  file_to_be_purged_3.csv     .csv  /path_3...
4  file_to_be_purged_4.csv     .csv  /path_4...
...Completed function purge_watcher
```

import glob
import pandas as pd
import os.path

# interesting_files = glob.glob("*.csv")
# header_saved = False
# with open('output.csv','wb') as fout:
#     for filename in interesting_files:
#         with open(filename) as fin:
#             header = next(fin)
#             if not header_saved:
#                 fout.write(header)
#                 header_saved = True
#             for line in fin:
#                 fout.write(line)

path ='t_annual' # use your path
fname = 't_annual.csv'

allFiles = glob.glob(path + "/*.csv")
print len(allFiles)
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_, index_col=None, header=0)
    list_.append(df)
frame = pd.concat(list_)
frame = frame.set_index('fid')
print frame

# try:
#     os.remove(fname)
# except OSError:
#     pass
# frame.to_csv(fname)
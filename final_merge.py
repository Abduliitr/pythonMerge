import pandas as pd
import xlrd
import os
from pandas import ExcelWriter
from pandas import ExcelFile

def getFilePath(req_name, main_dir):

    # print("req_name is " + req_name)
    # print("main_dir is " + main_dir)

    dirName = '/home/cadbury/Desktop/download_and_extract_files/Output/' + main_dir

    for (dirpath, dirnames, filenames) in os.walk(dirName):
        if(req_name in dirnames):
            for(dirpath, dirnames, filenames) in os.walk(dirpath+'/'+req_name):
                # print(filenames)
                if('domains' in filenames):
                    # print("Domains found in \"" + req_name + "\" Directory in \""+ main_dir +"! at path: ")
                    # print(dirpath+"/domains----------------------------")
                    return (dirpath+"/domains") 
    
def merge_code(path1, path2, path3, output_name):
    
    if(os.path.isfile(path1)):
        f1 = open(path1)
        string1=f1.read()
        f1.close()
    else:
        string1=''
    if(os.path.isfile(path2)):
        f2 = open(path2)
        string2=f2.read()
        f2.close()
    else:
        string2=''
    if(os.path.isfile(path3)):
        f3 = open(path3)
        string3=f3.read()
        f3.close()
    else:
        string3=''
    
    string4=string1.splitlines()
    string5=string2.splitlines()
    string6=string3.splitlines()

    set1 = set(string4)
    set2 = set(string5)
    set3 = set(string6)

    set_after_merge = set1.union(set2)
    final_set=set3.union(set_after_merge)

    print("Merging files...")

    set1.clear()
    set2.clear()
    set3.clear()
    s = '\n '
    result_path = 'Results/'+output_name
    print("Saving... file to "+result_path)
    with open(result_path, 'a+') as f:
        f.write(s.join(final_set))

    


def main():

    dirName = '/home/cadbury/Desktop/download_and_extract_files/Output'
    
    df = pd.read_excel('Master-CF-Categories.xlsx', 'Sheet1')
    # Column headings: Index(['Master Name', 'ShallaList', 'Capitole', 'MESD List'], dtype='object')

    for i in df.index:
       
        output_name = ''
        extracted1_name = ''
        extracted2_name = ''
        extracted3_name = ''

        if(not(pd.isnull(df['Master Name'][i]))):
            output_name = df['Master Name'][i]
        if(not(pd.isnull(df['ShallaList'][i]))):
            extracted1_name = (df['ShallaList'][i])
        if(not(pd.isnull(df['Capitole'][i]))):
            extracted2_name = (df['Capitole'][i])
        if(not(pd.isnull(df['MESD List'][i]))):
            extracted3_name = (df['MESD List'][i])

        # print(output_name)

        # print(extracted1_name)
        if(extracted1_name != ''):
            path1 = getFilePath(extracted1_name, 'extracted1')
        else: 
            path1 = 'invalid_path1'
        # print(path1)

        # print(extracted2_name)
        if(extracted2_name!=''):
            path2 = getFilePath(extracted2_name, 'extracted2')
        else:
            path2='invalid_path2' 
        # print(path2)

        # print(extracted3_name)
        if(extracted3_name!=''):
            path3 = getFilePath(extracted3_name, 'extracted3')
        else:
            path3 = 'invalid_path3' 
        # print(path3)

        merge_code(path1, path2, path3, output_name)
        print("Saved file extracted1:" + extracted1_name +", extracted2:"+ extracted2_name+", extracted3:" +extracted3_name + " to Results/"+output_name)
        print('---------------------------------------------------------------')

    print("**************Successfully Completed Saving "+ str(len(df.index))+" files to Results folder! ****************************")


if __name__ == '__main__':
    main()

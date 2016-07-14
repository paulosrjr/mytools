import argparse
import os
#import sys
import binascii

parser = argparse.ArgumentParser()
parser.add_argument('--folder', default="./", required=True, help="Folder is necessary")
parser.add_argument('--pattern', default="./pattern.pat", help="Default file is the pattern.pat in local dir")
parser.add_argument('--replace', default="./replace.rep", help="Default file is the replace.rep in local dir")

args = parser.parse_args()

#print("~ Folder: {}".format(args.folder))
#print("~ Pattern: {}".format(args.pattern))
#print("~ Replace: {}".format(args.replace))

root_dir = format(args.folder)
pattern_to_replace = format(args.pattern)
replacement_in_file = format(args.replace)

if root_dir:
  for root, directories, filenames in os.walk(root_dir):
     for filename in filenames:
        #print os.path.join(root, filename)
        file_to_change = os.path.join(root, filename)
        #with open("pattern.txt") as file_with_pattern:
        with open(pattern_to_replace) as file_with_pattern:
           str_file_with_pattern = file_with_pattern.read()
        bin_file_with_pattern = bin(int(binascii.hexlify(str_file_with_pattern), 16)).replace("b", "")
        #with open("replace.txt") as file_with_replacement:
        with open(replacement_in_file) as file_with_replacement:
           str_file_with_replacement = file_with_replacement.read()
        bin_file_with_replacement = bin(int(binascii.hexlify(str_file_with_replacement), 16)).replace("b", "")
        #with open("texto.txt") as file_to_read:
        with open(file_to_change) as file_to_read:
           str_file_to_read = file_to_read.read()
        bin_file_to_read = bin(int(binascii.hexlify(str_file_to_read), 16)).replace("b", "")
        bin_final_replacement = bin_file_to_read.replace(bin_file_with_replacement, bin_file_with_pattern)

        int_final_replacement = int(bin_final_replacement, 2)


        str_final_replacement = binascii.unhexlify('%x' % int_final_replacement)
        final_file = open(file_to_change, "w")
        final_file.write(str_final_replacement)
        final_file.close()
        print(file_to_change)
else:
    print ("Root directory error")
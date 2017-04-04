import sys
import hashlib


if len(sys.argv) != 2:
    print 'usage: email_hash.py [email_filename]'
    sys.exit()

#get the name of the input file which contains the email addresses
input_filename = sys.argv[1]

#output file for hashed emails
output_filename = input_filename + '_hashed_ouput.txt'

#open file to read eMail addresses
input_file = open(input_filename, "r")

#open the output file to write hashed email addresses to
output_file = open(output_filename, "w")

for email_address in input_file:
    #strip any blanks or carriage returns from the email address, and set to lower case
    #hash the email address using SHA256.  
    hash_object = hashlib.sha256( email_address.strip().lower() )

    #write the hashed email address to the output file and a carraige return
    output_file.write(hash_object.hexdigest() + '\n')
                         
#close the files    
input_file.close()
output_file.close()

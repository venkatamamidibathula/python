import os,csv

#Open the CSV File first with defined encoding
new_file=open('example.csv',encoding='utf-8')
#Read the new file.
csv_read_file=csv.reader(new_file)

#Create a list
new_list=list(csv_read_file)
# Print the list
print(new_list)

# Print the email address of first 10 people
email_index=new_list[0].index('email')
# for i in new_list[1:15]:
#     print(i)

# Print the list of emails

new_email_list=[]
for i  in new_list[1:15]:
    new_email_list.append(i[email_index])
print(new_email_list)


#Write to a new file
file_to_write=open('tosavefile','w',newline='')
csv_writer=csv.writer(file_to_write,delimiter='')
csv_writer.writerows([1,2,3],[23,34,56])
file_to_write.close()

#Append to existing files
newline_to_write=open('tosavefile','a',newline='')
csv_writer=csv.writer(newline_to_write,delimiter='')
csv_writer.writerows([1,2,3],[23,34,56])
newline_to_write.close()
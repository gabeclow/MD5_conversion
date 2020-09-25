
open('match_file', 'w').close()  # overwrite
# emailandSha = open('result_list', 'r')
#
# for index, line in enumerate(emailandSha):
#     sha_only = open('ShaOnly', 'r')
#     for sha_line in sha_only:
#         if line.__contains__(sha_line):
#             print("true:" + sha_line)
#             doc = open('match_file', "a")
#             doc.write(line)
#             doc.write("\n")
#             doc.close()

sha = open('ShaOnly', 'r')
for sha_line in sha:
    both = open('result_list', 'r')
    flag = 0
    for line in both:
        if line.__contains__(sha_line):
            doc = open('match_file', "a")
            just_email = line.split(',')[0]
            doc.write(just_email)
            doc.write("\n")
            print(just_email)
            doc.close()
            flag = 1
        if line.__contains__("EndFile") and flag == 0:
            doc = open('match_file', "a")
            doc.write("N/A")
            doc.write("\n")
            doc.close()
            flag = 0

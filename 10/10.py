white_list = []
searches = []
for i in range(int(input())):
    white_list.append(input())
for i in range(int(input())):
    searches.append(input())
for search in searches:
    if search in white_list:
        print(search)

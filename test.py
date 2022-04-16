s1 = "ab"
s2 = "eidbaooo"

s2_list = []

for i in range(len(s2)-len(s1)+1):
    s2_list.append(s2[i:i+len(s1)])
print(s2_list)

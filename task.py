#name = ['Nike','Adidas','Puma','New Balance','python']
# for i in name:
#     print(i)

# for i in range(len(name)):
#     print(name[i])
# for i in range(len(name)):
#     for j in range(i+1):
#         print(name[i])

# d = {'Alex': 25, 'Petr': 54}
# print(d)
# print(len(d))
# d['Kate']=65
#print(d)
#print(d['Alex'])
#print(d['Petr'])
#d[25]=54
#print(d)

#for key, value in d.items():
#    print(key)
#    print(value)

# for key, value in d.items():
#     print("ключ:" + str(key) + ",значение:" + str(value))

# a = ["first", 1,2,3, "second",10,20, "third", 15,56,70, "fourth", -50]
# my_dict = {}
# current_str = None
#
# for e in a:
#     if(type(e) == str):
#         my_dict[e] = []
#         current_str = e
#     else:
#         my_dict(current_str).append(e)
# print(my_dict)

# my_text = 'привет как дела что делаешь как тебя зовут сколько тебе лет Мое чудесное утро все отлично'
# # my_dict = {}
# for word in my_text.split():
#     if word in my_dict:
#         my_dict[word] = my_dict[word]+1
#     else:
#         my_dict[word] = 1
# print(my_dict)

# for word in my_text.split():
#     my_dict[word] = my_dict.get(word,0)+1
# print(my_dict)


# def create_2d_arr(m,n):
#        arr3 = []
#
#        for i in range(m):
#                internal_arr = []
#                for j in range(n):
#                        internal_arr.append(0)
#        arr3.append(internal_arr)
#        return arr3
#
# arr_5_10 = create_2d_arr(5,10)
# print_matrix(arr_5_10)
#
# '''
# 4 5 6
# 3 2 1
# 0 7 8
#
# 7 8 9
# 6 5 4
# 3 2 1
#
# 34 5 6 6
# 545 65 4 4
# 67 4 4 3
#
# 56 4 5 4
# 56 4 3 8
# 9 0 7 5
#
# '''
# def swap(arr,i,j):
#         temp = arr[i]
#         arr[i] = arr[j]
#         arr[j] = temp
# def mirror_2d_arr(arr_2d):
#         for arr in arr_2d:
#                 for i in range(len(arr)//2):
#                         swap(arr, i, len(arr) - 1 - i)
# print_matrix(arr2)

# a = [2,6,7,9,43]
# c = [num * 2 for num in a]
# print(c)
#
# range3 = [num * 3 for num in range(1,6)]
# print(range3)
# range_element = []
# for num in range(1,6):
#         range_element.append(num*3)
# print(range_element)

#a = [1,3 ,5,9,87,55]
#a_filtered = []
#for num in a:
#        if num <10:
#                a_filtered.append(num)
#print(a_filtered)

# a_filtered = [num for num in a if < 10]
# print(a_filtered)
#a_filtered_squared = [num ** 2 for num in a if < 10]
#print(a_filtered_squared)

#word = ['hello', 'good morning', 'hi', 'baby', 'kind']
#words_filtered = [word + "." for word in word if len(word)>6]
#print(words_filtered)

# a = [20,16,12,8,4]
# a_filterd = [num*2 for num in range(10,1,-1) if num %2==0]
# print(a_filterd)

# a = set
# print(a)
# a = set(['hi',34,54,'umka'])
# print(a)
# b = {'hello', 'uno', 877, 654}
# print(b)

#a = {'a','7','8','96'}
#for el in a:
#        print(el)

# my_list = [1,3,1,1,'hello','hello']
# my_set = set()
# for el in my_list:
#         my_set.add(my_list)
# print(my_set)

# a = {'hello','hey',29,87,56}
# print(8 in a)
# print('hey' not in a)
# print(9 not in a)
# print(87 not in a)
# print('hg' not in a)

# my_list = [1,5,3,5]
# my_set = {1,5,3,5}
# print(my_list[2])
# print(my_set[1])

my_list = [3,4,4,6,5,4,3,3,56]
#my_set = set(my_list)
#total = 0
#for el in my_set:
#        total+=1

#print(total)


# sum = ([8,5,35,53,654])
# print(sum)

# sum = ({443,555,4563,435,3225,42})
# print(sum)

# print(sum(set(my_list)))
print({4,4,355,35}[35,4])
def my_function(input_dict,input_list):
        if len(input_list) > len(input_dict):
                return False
        for list_el in input_list:
                if list_el not in input_dict:
                        return True
        return True
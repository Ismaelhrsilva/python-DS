ft_list = ["Hello"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here
ft_list.append("World!")
ft_tuple = ft_tuple[:1] + ("Brazil!",)
ft_set.add("São Paulo!")
ft_set.remove("tutu!")
ft_dict['Hello'] = "42SP!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

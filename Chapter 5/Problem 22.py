#Exercise 22

inp = input("enter a string here: ")[1:-1]  #the input will be as "{string}", so i will take just the "string" without the {} by take all of the string without the frist and the last element

def permutations(inp):
  final_result = "{" # the return variable of the function, I will add every possible permutation to it, and put at the first of it {
  ress = [i for i in inp] #creating list for every character of the input string

  for i in range(3): # 3 Because there are 3 characters

    ress[1], ress[2] = ress[2], ress[1] # ABC >> ACB || CAB >> CBA || BCA >> BAC # By shifting the second and the third element together
    final_result += "".join(ress) + ", " # join and cocatenate the list with the string

    ress[0], ress[1] = ress[1], ress[0] # ACB >> CAB || CBA >> BCA || BAC >> ABC # By shifting the first two elements together
    final_result += "".join(ress) + ", "

  final_result = final_result[:-2] # except last 2 value which are (", ") so we ignore them 
  return final_result + "}" # putting "}" at the end to represent it as a set

print(permutations(inp))
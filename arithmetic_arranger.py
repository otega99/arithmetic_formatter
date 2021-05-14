def arithmetic_arranger(problems,display_results=False):
  arranged_problems=""
  if len(problems) > 5:
    arranged_problems= 'Error: Too many problems.'
  else:
    str1,str2,str3,str4="","","",""   
    for problem in problems:
      if '+' in problem or '-' in problem:
        num1,sign,num2=problem.split(' ')
        try:
          int(num1)
          int(num2)
        except:
          arranged_problems='Error: Numbers must only contain digits.'
          break
        if int(num1)>9999 or int(num2)>9999:
          arranged_problems='Error: Numbers cannot be more than four digits.'
          break
        else:
          dashes=len(str(max([int(num1),int(num2)])))+2
          solution=''
          if sign=='+':
            solution=str(int(num1)+int(num2))
          else:
            solution=str(int(num1)-int(num2))
          arranged_problems='y'      
          str1+="{}    ".format(" "*(dashes-len(num1))+num1)
          str2+="{}    ".format(sign+" "*(dashes-(len(num2)+1))+num2)
          str3+="{}    ".format("-"*dashes)
          str4+="{}    ".format(" "*(dashes-len(solution))+solution)
          arranged_problems=str1.rstrip()+"\n"+str2.rstrip()+"\n"+str3.rstrip()
      else:
        arranged_problems="Error: Operator must be '+' or '-'."
        break
    if display_results==True:
      arranged_problems+="\n"+str4.rstrip()
  return arranged_problems
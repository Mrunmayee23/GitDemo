import re
def arithmetic_arranger(problems, solve=True):
  if len(problems) > 5:
    return "Error: Too many problems."
  first = ""
  second = ""
  lines = ""
  sumx = ""
  string = ""
  for problem in problems:
    if re.search("[^\s0-9.+-]", problem):
      if re.search("[/]",problem) or re.search("[*]", problem):
        return "Error: Numbers must only contain digits."
      return "Error: Operator must be '+' or '-'."
    firstNum = problem.split(" ")[0]
    operator = problem.split(" ")[1]
    secondNum = problem.split(" ")[2]
    if len(firstNum) > 4 or len(secondNum) > 4:
      return "Error: Numbers cannot be more than four digits."
    sum = " "
    if operator == "+":
      sum = str(int(firstNum) + int(secondNum))
    elif operator == "-":
      sum = str(int(top) - int(bottom))

    length = max(len(firstNum), len(secondNum)) + 2
    top = firstNum.rjust(length)
    bottom = operator + secondNum.rjust(length - 1)
    line = ""
    res = str(sum).rjust(length)
    for s in range(length):
      line += "-"

    if problem != problems[-1]:
      first += top + '  ';
      second += bottom + '  ';
      lines += line + '  '
      sumx += sum + '  ';

    else:
      first += top;
      second += bottom;
      lines += line;
      sumx += sum;

    if solve:
      string = first + '\n' + second + '\n' + lines + '\n' + sumx
    else:
      string = first + '\n' + second + '\n' + lines
    return string
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
from pip._vendor.distlib.compat import raw_input
cond = True
def my_function():
   print("You will be asked the  number ofb feet for purchase and the type of lr (common or select)")
def final_compute(board, total, lumber):
   f= 0.00
   if (int(lumber) == 1):
       total = int(board) * 2
   else:
       total = int(board) * 1
   if (int(total) <= 10000):
       f = int(total)
   if (int(total) > 10000 and int(total) < 50000):
       f = int(total) - (int(total) * 10 / 100)
   if (int(total) > 50000):
       f = int(total) - (int(total) * 20 / 100)
   print(int(f))
def my_compute(b, l):
       if (int(l) == 2):
           total = int(b) * 1
       else:
           total = int(b) * 2
       final_compute(b, total, l)
while cond:
   my_function()
   b = raw_input('Enter number ofb feet:')
   l = raw_input('Enter a 1 for select lr or a 2 for common lr')
   my_compute(b, l)
   cond = raw_input(' Continue (y/n)?:')
   if (cond == 'n'):
       cond = False
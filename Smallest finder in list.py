
a=[23,45,12,78,34,5,67] 
def  smallest(a):
          small=a[0]
          for i in a:
              if i <small:
                  small=i
          return small
 
print(smallest(a))

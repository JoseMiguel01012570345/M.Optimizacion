from numpy.random import rand
from numpy import asarray, double
from sympy import N
from sympy import symbols, diff,cos, exp
import os
import time

#-------------------------------DESCENSON MAXIMO DEL GRADIENTE-----------------------------------------

# Nota: Para la revision del algoritmo, descomente

#-------------------------------------------------------------------------------
#-------------------------------PROBLEM 162-----------------------------------------

# def derivate(f,X0,Y0):
   
#    x, y = symbols('x y')

#    df_dx = diff(f, x)
#    df_dy = diff(f, y)

#    Df_dx= df_dx.subs({x: X0, y: Y0})
#    Df_dy= df_dy.subs({x: X0, y: Y0})
   
#    return (Df_dx,Df_dy)

# def gradient_descent(f,X0,Y0,epsilon,step):
   
#     gradient=derivate(f,X0,Y0)
#     gradientX=gradient[0]
#     gradientY=gradient[1]

#     iterations=0
#     n=0
#     next=(X0**6 + Y0**4-17)**2 + (2*X0+Y0-4)**2

#     while abs(next-n) >epsilon : # modify the function
       
#       os.system('cls' if os.name == 'nt' else 'clear')

#       if gradientX>0: # if gradient is positive, step back for minimum
#          X0=X0-step
#       else:
#          X0=X0+step # if gradient is negative, keep going for minimum

#       if gradientY>0: # if gradient is positive, step back for minimum
#          Y0=Y0-step
#       else:
#          Y0=Y0+step # if gradient is negative, keep going for minimum
      
#       gradient=derivate(f,X0,Y0) 
#       gradientX=gradient[0]
#       gradientY=gradient[1]
      
#       iterations+=1      
#       print("iteration: ",iterations)
#       n=next
#       next=(X0**6 + Y0**4-17)**2 + (2*X0+Y0-4)**2

#     return (X0,Y0)

# # introduce iterval for X
# print("iterval for X")
# print("minimum for X: ")
# minX=double(input())
# print("maximum for X: ")
# maxX=double(input())

# # introduce iterval for Y
# print("iterval for Y")
# print("minimum for Y: ")
# minY=double(input())
# print("maximum for Y: ")
# maxY=double(input())


# boundsX = asarray([[minX, maxX]])
# boundsY = asarray([[minY, maxY]])


# X0=(boundsX[:, 1] - boundsX[:, 0])[0] /2
# Y0=(boundsY[:, 1] - boundsY[:, 0])[0]/4

# epsilon=0.0001
# step=0.00001

# x,y=symbols('x y')
# f=(x**6 + y**4-17)**2 + (2*x+y-4)**2

# resoult=gradient_descent(f,X0,Y0,epsilon=epsilon,step=step)

# print("resoult: ",resoult)
#-------------------------------------------------------------------------------
#-------------------------------PROBLEM 171-----------------------------------------

# def derivate(f,X0,Y0):
   
#    x, y = symbols('x y')

#    df_dx = diff(f, x)
#    df_dy = diff(f, y)

#    Df_dx= df_dx.subs({x: X0, y: Y0})
#    Df_dy= df_dy.subs({x: X0, y: Y0})
   
#    return (Df_dx,Df_dy)

# def gradient_descent(f,X0,Y0,epsilon,step,b,m):
   
#    gradient=derivate(f,X0,Y0)
#    gradientX=gradient[0]
#    gradientY=gradient[1]

#    iterations=0
#    print(e**((-((X0)**2*m +(Y0)**2*m)/(b**(2*m))) - 2*e**(X0**2+Y0**2)) * (cos(X0)**2) * (cos(Y0)**2))

#    n=10
#    next=e**((-((X0)**2*m +(Y0)**2*m)/(b**(2*m))) - 2*e**(X0**2+Y0**2)) * (cos(X0)**2) * (cos(Y0)**2)

#    tempo=time.time()

#    clean=0
#    while next-n>epsilon : # modify the function
       
#       if clean ==10:
#          os.system('cls' if os.name == 'nt' else 'clear')
#          clean=0      

#       if gradientX>0: # if gradient is positive, step back for minimum
         
#          if X0-step <20 and X0-step > -20 :
#             X0=X0-step
#       else:
#          if X0-step <20 and X0-step > -20 :
#             X0=X0+step # if gradient is negative, keep going for minimum

#       if gradientY>0: # if gradient is positive, step back for minimum
#          if Y0-step <20 and Y0-step > -20 :
#             Y0=Y0-step
#       else:
#          if Y0-step <20 and Y0-step > -20 :
#             Y0=Y0+step # if gradient is negative, keep going for minimum
      
#       gradient=derivate(f,X0,Y0) 
#       gradientX=gradient[0]
#       gradientY=gradient[1]
      
#       n=next
#       next=e**((-((X0)**2*m +(Y0)**2*m)/(b**(2*m))) - 2*e**(X0**2+Y0**2)) * (cos(X0)**2) * (cos(Y0)**2)

#       iterations+=1      

#       if time.time() - tempo >=1:
        
#          print('f(x,y)= ',e**((-((X0)**2*m +(Y0)**2*m)/(b**(2*m))) - 2*e**(X0**2+Y0**2)) * (cos(X0)**2) * (cos(Y0)**2))
#          print("best resoult: ",(X0,Y0))
#          print("iteration: ",iterations)
         
#          clean+=1
#          tempo=time.time()

#    return (X0,Y0)


# boundsX = asarray([[-20, 20]])
# boundsY = asarray([[-20, 20]])


# X0=(boundsX[:, 1] - boundsX[:, 0])[0] /20
# Y0=(boundsY[:, 1] - boundsY[:, 0])[0]/4


# data_collected=False
# while not data_collected:
#    try:
#       print("intoduce m")
#       m=double(input())

#       data_collected=True

#    except:
#       print("most introduce a number")

# data_collected1=False
# while not data_collected1:
#    try:
#       print("intoduce beta")
#       b=double(input())

#       data_collected1=True

#    except:
#       print("most introduce a number")

# data_collected2=False
# while not data_collected2:
#    try:
      
#       print("intoduce epsilon")
#       epsilon=double(input())
      
#       data_collected=True

#    except:
#       print("most introduce a number")


# step=0.001

# x,y=symbols('x y')
# e=exp(1)

# f=e**((-(x+y)/(b**(2*m))) - 2*e**(x**2+y**2)) * (cos(x)**2) * (cos(y)**2) 

# resoult=gradient_descent(f,X0,Y0,epsilon=epsilon,step=step, b=b,m=m)

# os.system('cls' if os.name == 'nt' else 'clear')
# print('resoult: ', resoult)
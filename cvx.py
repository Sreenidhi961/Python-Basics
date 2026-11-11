from cvxopt import matrix,solvers
A=matrix([[-1.0,-1.0,1.0],[-1.0,0.0,0.0]])
print(A)
b=matrix([-1.0,-1.0,1.0])
print(b)
c=matrix([1.0,1.0])
print(c)
sol=solvers.lp(c,A,b)
print(sol['x'])

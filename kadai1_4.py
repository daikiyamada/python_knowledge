from vpython import *
r = vector(1,0,0)
v = vector(0,1,0.1)
m=1
q=-1
B=vector(0,0,1)
def alpha(v):
    return (q/m)*cross(v,B)

Tmax = 2*pi*20
h = 0.01
T = arange(0,Tmax,h)
S1 = canvas(width=800,height = 800,background=color.white,foreground=color.black)
S1.up = vector(0,0,1)
S1.forward = vector(-1,-1,-1)
M = arrow(pos=vector(0,0,0),axis=B,length=mag(B),color=color.cyan)
Ball = sphere(pos=r,radius=0.1,color=color.blue,make_trail=True)
Velocity = arrow(pos=r,axis=v,length=0.1,color=color.yellow)
Arrow = arrow(pos=r,axis=alpha(v),length=0.1,color=color.red)
for t in T:
    rate(100)
    r_m = r+v*h/2.0
    v_m = v+alpha(v)*(h/2.0)
    r = r+v_m*h
    v = v+alpha(v_m)*h
    Ball.pos = r
    Velocity.pos = r
    Velocity.axis = v
    Velocity.length = mag(v)*0.3
    Arrow.pos = r
    Arrow.axis = alpha(v)
    Arrow.length = mag(alpha(r))*0.3

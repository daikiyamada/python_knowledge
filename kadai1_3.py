from vpython import *

def alpha(r):
    a = (k/m)*r.z
    return vector(0,0,-a)

S1 = canvas(width=400,height = 300,background=color.white,foreground=color.black)
S1.up = vector(0,0,1)
S1.forward = vector(-1,0,0)
S1.range = 1.5
r = vector(0,0,1)
v = vector(0,0,0)
k = 1.0
m = 1.0
Tmax = 2*pi*20
h = 0.01
T = arange(0,Tmax,h)

Ball = sphere(canvas=S1,pos=r,radius=0.1,color=color.blue,make_trail=False)

H = helix(pos=vector(0,0,0),axis = r,length=mag(r),radius = 0.1,coils=10,thickness = 0.01)
G1 = graph(width=400,height = 300,title='<b>harmonic oscillation</b>',xtitle='<i>t</i>',ytitle='<i>r.z</i>')
G2 = graph(width=400,height=300,title='<b>total energy</b>',xtitle = '<i>t</i>',ytitle='<i>E</i>')
f1 = gcurve(graph=G1,color=color.cyan)
f2 = gcurve(graph=G2,color = color.red)
for t in T:
    rate(50)
    r_m = r+v*h/2.0
    v_m = v+alpha(r)*(h/2.0)
    r = r+v_m*h
    v = v+alpha(r_m)*h
    Ball.pos = r
    H.axis = r
    H.length = mag(r)
    f1.plot(pos=(t,r.z))
    E = 0.5*m*mag2(v)+0.5*k*r.z**2
    f2.plot(pos=(t,E))

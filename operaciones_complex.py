import math

def suma_complex(x,y):
    z=[x[i]+y[i] for i in range(len(x))]
    
    return z

def mult_complex(x,y):
    z=[x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]]
    
    return z

def resta_complex(x,y):
    z= [x[i]-y[i]for i in range(len(x))]
    print(z)

    return z
def conjugado_complex(x):
    z=[x[0],-x[1]]
    print(z)
    return z
def division_complex(x,y):
    conjugado_y=conjugado_complex(y)
    numerador=mult_complex(x, conjugado_y)
    denominador=mult_complex(y, conjugado_y) 
    z=[numerador[0]/denominador[0],numerador[1]/denominador[0]]
    print(z)
    return z

def modulo_complex(x):
    z=(x[0]**2+x[1]**2)**0.5
   
    return z
def cartesiano_polar(x):
    modulo=modulo_complex(x)
    fase_rad=math.atan2(x[1], x[0])
    
    
    z=[modulo,fase_rad]
    
    return z
    
def polar_cartesiano(x):
    fase_rad=x[1]
    a=x[0]*math.cos(fase_rad)
    b=x[0]*math.sin(fase_rad)
    z=[a,b]
    
    return z
def fase_complex_polar(x):
    fase=x[1]
    
    return fase
def fase_complex_cartesiano(x):
    fase_rad=math.atan2(x[1], x[0])
    fase_grados=math.degrees(fase_rad)
    
    return fase_grados, fase_rad


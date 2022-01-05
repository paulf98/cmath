import numpy as np 
import matplotlib.pyplot as plt 
 
angle = np.linspace( 0 , 2 * np.pi , 200 ) 
 
x = np.cos( angle ) 
y = np.sin( angle ) 
 
figure, axes = plt.subplots( 1 ) 
 
axes.plot( x, y ) 
axes.set_aspect( 1 ) 

plt.arrow(1.0, 0.0, 0.0, 1.0, color="g", head_width=0.05)
plt.arrow(0.0, 1.0, -1.0, 0.0, color="g", head_width=0.05)
plt.arrow(-1.0, 0.0, 0.0, -1.0, color="g", head_width=0.05)
plt.arrow(0.0, -1.0, 1.0, 0.0, color="g", head_width=0.05)

arrowxy = 0.5*np.sqrt(2.0)
plt.arrow(arrowxy, arrowxy,-arrowxy, arrowxy,color="g",head_width=0.05)

plt.title( 'Parametric Equation Circle' ) 
plt.show() 
import gmsh
import sys
import math

gmsh.initialize()
gmsh.model.add('Torus')
gmsh.merge('C:/Tor.stl')

angle=40
Patch = False
Boundary = True
curveangle = 180
gmsh.model.mesh.classifySurfaces(angle*math.pi/180., Patch, Boundary, curveangle*math.pi/180.)
gmsh.model.mesh.createGeometry()

s = gmsh.model.getEntities(2)
l = gmsh.model.geo.addSurfaceLoop([s[i][1] for i in range(len(s))])
gmsh.model.geo.addVolume([l])
gmsh.model.geo.synchronize()

gmsh.model.mesh.generate(3)
gmsh.write('Tor.msh')

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()
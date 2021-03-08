import gmsh
import math
import sys

gmsh.initialize()

gmsh.model.add('cat')

gmsh.merge('C:/sitting_cat/sitting_cat.stl')

gmsh.model.mesh.createTopology()

angle = 40
forceParametrizablePatches = False
includeBoundary = True
curveAngle = 20

gmsh.model.mesh.classifySurfaces(angle * math.pi/180., includeBoundary, forceParametrizablePatches, curveAngle * math.pi/180.)
gmsh.model.mesh.createGeometry()
gmsh.model.geo.synchronize()

s = gmsh.model.getEntities(2)
l = gmsh.model.geo.addSurfaceLoop([s[i][1] for i in range(len(s))])
v = gmsh.model.geo.addVolume([l])

m = gmsh.model.addPhysicalGroup(2, [s])
gmsh.model.mesh.setSize(gmsh.model.getEntities(0), 0.001)

gmsh.model.mesh.createGeometry()
gmsh.model.geo.synchronize()

gmsh.model.mesh.generate(3)
gmsh.write('cat.msh')

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()
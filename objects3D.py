import random
from math import sqrt

class Cube3D:
	def __init__(self,size,pos):

		size = size/2

		self.verts = [	(-size+pos[0],-size+pos[1],-size+pos[2]),
						(size+pos[0],-size+pos[1],-size+pos[2]),
						(size+pos[0],size+pos[1],-size+pos[2]),
						(-size+pos[0],size+pos[1],-size+pos[2]),
						(-size+pos[0],-size+pos[1],size+pos[2]),
						(size+pos[0],-size+pos[1],size+pos[2]),
						(size+pos[0],size+pos[1],size+pos[2]),
						(-size+pos[0],size+pos[1],size+pos[2])]	

		self.edges = [	(0,1),(0,3),(0,4),(1,2),(1,5),(2,3),
						(2,6),(3,7),(4,5),(4,7),(5,6),(6,7)]

		self.faces = [	(0,1,2,3),(4,5,6,7),(0,1,5,4),
						(2,3,7,6),(0,3,7,4),(1,2,6,5)]

		self.colors = []

		for i in range(6):
			self.colors += [(	random.randrange(255),
								random.randrange(255),
								random.randrange(255))]

		self.face_centers = []

		for face in self.faces:
			center = [0,0,0]
			for i in face:
				center[0] += self.verts[i][0]
				center[1] += self.verts[i][1]
				center[2] += self.verts[i][2]
			for j in range(3):
				center[j] /= len(face)
			self.face_centers += [center]


		self.all = [self.verts,self.edges,self.faces,self.colors,self.face_centers]

class Rect3D:
	def __init__(self,pos,l,h,w):

		x,y,z = pos[0],pos[1],pos[2]

		self.verts = [	(-l+x,-h+y,-w+z),
						( l+x,-h+y,-w+z),
						( l+x, h+y,-w+z),
						(-l+x, h+y,-w+z),
						(-l+x,-h+y, w+z),
						( l+x,-h+y, w+z),
						( l+x, h+y, w+z),
						(-l+x, h+y, w+z)]

		self.edges = [	(0,1),(0,3),(0,4),(1,2),(1,5),(2,3),
					(2,6),(3,7),(4,5),(4,7),(5,6),(6,7)]

		self.faces = [	(0,1,2,3),(4,5,6,7),(0,1,5,4),
						(2,3,7,6),(0,3,7,4),(1,2,6,5)]

		self.colors = []

		for i in range(6):
			self.colors += [(	random.randrange(255),
								random.randrange(255),
								random.randrange(255))]

		self.face_centers = []

		for face in self.faces:
			center = [0,0,0]
			for i in face:
				center[0] += self.verts[i][0]
				center[1] += self.verts[i][1]
				center[2] += self.verts[i][2]
			for j in range(3):
				center[j] /= len(face)
			self.face_centers += [center]

		self.all = [self.verts,self.edges,self.faces,self.colors,self.face_centers]

class Rock3D:
	def __init__(self,pos):

		x,y,z = pos[0],pos[1],pos[2]

		self.verts = [	(x+0.75,	y,		z+0.5),
						(x+0.4,		y,		z+0.9),
						(x-0.5,		y,		z+0.75),
						(x-0.8,		y,		z-0.75),
						(x+0.5,		y,		z-0.8),
						(x+0.5,		y-0.5,	z+0.5),
						(x-0.1,		y-0.5,	z+0.4),
						(x-0.4,		y-0.5,	z),
						(x,			y-0.5,	z-0.2),
						(x+0.25,	y-0.5,	z+0.1)]	

		self.edges = [	(0,1),(0,4),(0,5),(1,2),(1,5),(1,6),(2,3),(2,6),(2,7),
						(3,4),(3,7),(3,8),(4,5),(4,8),(5,6),(5,8),(6,7),(7,8)]

		self.faces = [	(0,1,5),(1,5,6),(1,2,6),(2,6,7),(2,3,7),(3,7,8),
						(3,4,8),(4,8,5),(4,0,5),(5,6,7),(7,8,5),(1,4,0),
						(1,2,3),(1,3,4)]

		self.colors = []

		col = (100,100,100)

		for i in range(len(self.faces)):
			self.colors += [col]
			col = (col[0]+10,col[0]+10,col[0]+10)

		self.colors[-3] = self.colors[-1]
		self.colors[-2] = self.colors[-1]

		self.face_centers = []

		for face in self.faces:
			center = [0,0,0]
			for i in face:
				center[0] += self.verts[i][0]
				center[1] += self.verts[i][1]
				center[2] += self.verts[i][2]
			for j in range(3):
				center[j] /= len(face)
			self.face_centers += [center]

		self.all = [self.verts,self.edges,self.faces,self.colors,self.face_centers]

class Hex3D:
	def __init__(self,pos):

		x,y,z = pos[0],pos[1],pos[2]

		self.verts = [	(x+0.5,y,z+((0.5/3)*sqrt(3))),
						(x,y,z+((1/3)*sqrt(3))),
						(x-0.5,y,z+((0.5/3)*sqrt(3))),
						(x-0.5,y,z-((0.5/3)*sqrt(3))),
						(x,y,z-((1/3)*sqrt(3))),
						(x+0.5,y,z-((0.5/3)*sqrt(3))),
						(x,y,z)]

		self.edges = [	(0,1),(0,5),(0,6),(1,2),(1,6),(2,3),(2,6),
						(3,4),(3,6),(4,5),(4,6),(5,6)]

		self.faces = [	(0,1,6),(1,2,6),(2,3,6),(3,4,6),(4,5,6),(0,5,6)]

		self.colors = [(100,100,100)]*6

		self.face_centers = []

		for face in self.faces:
			center = [0,0,0]
			for i in face:
				center[0] += self.verts[i][0]
				center[1] += self.verts[i][1]
				center[2] += self.verts[i][2]
			for j in range(3):
				center[j] /= len(face)
			self.face_centers += [center]

		self.all = [self.verts,self.edges,self.faces,self.colors,self.face_centers]

class Groundtile3D:
	def __init__(self,pos):

		x,y,z = pos[0],pos[1],pos[2]

		self.verts = [	(x+1,y,z+1),(x+1,y,z-1),
						(x-1,y,z+1),(x-1,y,z-1)]

		self.edges = [(0,1),(0,2),(0,3),(1,3),(2,3)]

		self.faces = [(0,1,2),(1,2,3)]

		self.colors = [(100,100,100)]*2

		self.face_centers = []

		for face in self.faces:
			center = [0,0,0]
			for i in face:
				center[0] += self.verts[i][0]
				center[1] += self.verts[i][1]
				center[2] += self.verts[i][2]
			for j in range(3):
				center[j] /= len(face)
			self.face_centers += [center]

		self.all = [self.verts,self.edges,self.faces,self.colors,self.face_centers]

def tile(size,pos):
	x,y,z = pos
	tilelist = []
	for i in range(size):
		for j in range(size):
			tilelist += [Groundtile3D((x+2*i,y,z+2*j)).all]
	return tilelist


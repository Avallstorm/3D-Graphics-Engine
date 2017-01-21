import pygame, sys, math
from objects3D import Cube3D, Rect3D, Rock3D, Groundtile3D, tile

#===============================================================================
#Helper functions

def rotate2d(pos,rad):
	""" Rotates the coordinates of pos by rad radiants around point pos

	Args:
		pos (:obj:`tuple` of :obj:`float` len = 2): position in the plane pos

		rad (:obj: 'float'): radiants of rotation

	Returns: float, float

	"""
	x, y = pos;
	s, c = math.sin(rad),math.cos(rad)
	return x*c-y*s, y*c+x*s

def drawobjects(objs):
	""" Draws given mesh objects onto the screen, taking into account their
		position in 3D space as well as their priority

	Args:
		objs (:obj:`list` of :obj:`list` of Any): Lists containing the
			information about various mesh objects.

		REQUIRMENT:
			lists within objs must come from the .all method of a 3D object
			class withine the module Objects3D.py

	Side effects: Draws mesh objects onto the pygame screen

	Notes: One of the main functions of the program

	Returns: float, float
	"""

	face_list = []
	face_color = []

	# depth ordering of faces
	depth = []

	for obj in objs:

		# All verticies in current object
		vert_list = []
		screen_coords = []
		center_screen_coords = []

		for x,y,z in obj[0]:
			# Modifying the coordinates of the object relative to the camera
			x -= cam.pos[0]
			y -= cam.pos[1]
			z -= cam.pos[2]

			x,z = rotate2d((x,z),cam.rot[1])
			y,z = rotate2d((y,z),cam.rot[0])
			vert_list += [(x,y,z)]

			altz = z

			if altz < 0:
				altz = 1

			# Generating object depth
			f = 400/altz
			x,y = x*f,y*f
			screen_coords += [(cx + int(x), cy + int(y))]

		# addind point to centroid of each object face.
		for x,y,z in obj[4]:
			# Modifying the coordinates of the object relative to the camera
			x -= cam.pos[0]
			y -= cam.pos[1]
			z -= cam.pos[2]

			x,z = rotate2d((x,z),cam.rot[1])
			y,z = rotate2d((y,z),cam.rot[0])

			if z == 0:
				z = 0.01

			# Adding object depth
			f = 400/z
			x,y = x*f,y*f
			center_screen_coords += [(cx + int(x), cy + int(y), z)]

		for f in range(len(obj[2])):
			face = obj[2][f]
			a,b,c = center_screen_coords[f]

			on_screen = False
			#Checking if an object should be on screen based on it's verticies 
			#	and central points
			for i in face:
				x,y = screen_coords[i]
				infront = vert_list[i][2] > 0 
				vertonscr = x>0 and x<width and y>0 and y<height
				centonscr = a>0 and a<width and b>0 and b<height
				centinfront = c > 0
				if (infront and vertonscr) or (centonscr and centinfront):
					on_screen=True
					break

			if on_screen:

				coords = [screen_coords[i] for i in face]
				face_list += [coords]
				face_color += [obj[3][f]]

				#Simple (yet not entirly correct) face sorting algorithm
				depth += [sum(sum(vert_list[j][i] for j in face)**2 for i in range(3))]


		order = sorted(range(len(face_list)),\
			key = lambda i:depth[i], reverse = True)

		for i in order:
			# Draw faces onto screen in order
			pygame.draw.polygon(screen,face_color[i],face_list[i])

#===============================================================================
#Camera Class

class Cam:
	"""Camera dictating where objects will be drawn based on position and
			angle.


	__init__

	Initializes a camera instance

		Args:
			pos   (:obj:`tuple` of :obj:`float` len = 3): position of the camera
				in 3D space
			rot   (:obj:`tuple` of :obj:`float` len = 2): rotational position 
				of camera in 3D space

		Returns: (:obj: Camera)

	"""
	def __init__(self,pos=(0,0,0),rot=(0,0)):
		self.pos = list(pos)
		self.rot = list(rot)

	def events(self,event):
		""" uses mouse movement events to rotate the camera

		Side effect: Mutates self

		Returns: None

		"""
		if event.type == pygame.MOUSEMOTION:
			x,y = event.rel
			x/=400
			y/=400
			self.rot[0] += y
			self.rot[1] += x

	def update(self,dt,key):
		""" Updates location of camera based on key input

		Side effect: Mutates self

		Returns: None

		"""
		s = dt * 10

		if key[pygame.K_q]: self.pos[1] -= s
		if key[pygame.K_e] and self.pos[1] < -0.7: self.pos[1] += s

		x,y = s*math.sin(self.rot[1]),s*math.cos(self.rot[1])

		if key[pygame.K_w]:
			self.pos[2] += y
			self.pos[0] += x
		if key[pygame.K_s]:
			self.pos[2] -= y
			self.pos[0] -= x
		if key[pygame.K_a]:
			self.pos[0] -= y
			self.pos[2] += x
		if key[pygame.K_d]:
			self.pos[0] += y
			self.pos[2] -= x

#===============================================================================
#Data

meshes = []

#Data for multiple cubes simulation
if "cubes" in sys.argv:
	n = int(sys.argv[-1])
	for i in range(n):
		for j in range(n):
			meshes += [Cube3D(1,(i,0,j)).all]

#Data for rock simulation
elif "rocks" in sys.argv:
	rock1 = Rock3D((1,0,1)).all
	rock2 = Rock3D((3,0,-1)).all
	meshes += [rock1, rock2]


#===============================================================================
def main():
	# Pulling global variables
	global cam, cx, cy, width, height, screen

	# Checking if there is no valid arguments
	if len(meshes) == 0:
		print("No arguments recongnized")
		pygame.quit()
		sys.exit()

	# Setup for pygame screen
	pygame.init()
	width,height = 800,800
	cx,cy = width//2,height//2
	screen = pygame.display.set_mode((width,height))
	clock = pygame.time.Clock()
	cam = Cam((0,-1,-5))

	# Setup for pygame inputs
	pygame.event.get()
	pygame.mouse.get_rel()
	pygame.mouse.set_visible(0)
	pygame.event.set_grab(1)

	while True:
		dt = clock.tick()/1000

		#pygame event loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
			cam.events(event)

		#Drawing background onto the screen
		screen.fill((135, 206, 235))
		angle = cam.rot[0]
		while(angle > 2*math.pi):
			angle -= 2*math.pi
		horizon = (400 - (1600/math.pi)*angle - cam.pos[1]*10)
		pygame.draw.rect(screen, (0,123,12) , [0, horizon, 800, 800])

		#Drawing all objects
		drawobjects(meshes)

		pygame.display.flip()

		#key retrival for camera
		key = pygame.key.get_pressed()
		cam.update(dt,key)

		if key[pygame.K_ESCAPE]:
			pygame.quit()
			sys.exit()

if __name__ == '__main__':
	main()
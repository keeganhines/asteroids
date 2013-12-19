# Sean Attacks || asteroids video game || K. Hines 07.23.13 || Thanks to A. Barkley for photoshop skills
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0.5
started = False

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.png")


# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50,lifespan=50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([50, 50], [100, 100], 50)
#asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")
#asteroid_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/19824959/sean1.png")
asteroid_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/19824959/sean1c.png")

######### make a bunch of image objects
sean1_info=ImageInfo([50, 50], [100, 100], 50)
sean1_image=simplegui.load_image("https://dl.dropboxusercontent.com/u/19824959/sean1c.png")

sean2_info=ImageInfo([50,50],[100,100],50)
sean2_image=simplegui.load_image("https://dl.dropboxusercontent.com/u/19824959/sean2e.png")

sean3_info=ImageInfo([58,75],[116,150],80)
sean3_image=simplegui.load_image("https://dl.dropboxusercontent.com/u/19824959/possum01.png")

sean4_info=ImageInfo([68,70],[136,140],100)
sean4_image=simplegui.load_image("https://dl.dropboxusercontent.com/u/19824959/possum02.png")

sean5_info=ImageInfo([44,63],[88,125],60)
sean5_image=simplegui.load_image("https://dl.dropboxusercontent.com/u/19824959/possum03.png")

sean6_info=ImageInfo([36,50],[72,100],50)
sean6_image=simplegui.load_image("https://dl.dropboxusercontent.com/u/19824959/possum04.png")

sean7_info=ImageInfo([65,54],[130,108],60)
sean7_image=simplegui.load_image("https://dl.dropboxusercontent.com/u/19824959/possum05.png")

sean8_info=ImageInfo([56,70],[112,140],64)
sean8_image=simplegui.load_image("https://dl.dropboxusercontent.com/u/19824959/possum06.png")

sean9_info=ImageInfo([56,72],[112,145],65)
sean9_image=simplegui.load_image("https://dl.dropboxusercontent.com/u/19824959/possum07.png")

sean10_info=ImageInfo([58,65],[115,129],60)
sean10_image=simplegui.load_image("https://dl.dropboxusercontent.com/u/19824959/possum08.png")

sean11_info=ImageInfo([63.5,62.5],[127,125],65)
sean11_image=simplegui.load_image("https://dl.dropboxusercontent.com/u/19824959/possum09.png")

sean12_info=ImageInfo([75,56.5],[150,113],60)
sean12_image=simplegui.load_image("https://dl.dropboxusercontent.com/u/19824959/possum10.png")

sean13_info=ImageInfo([75,60.5],[150,121],60)
sean13_image=simplegui.load_image("https://dl.dropboxusercontent.com/u/19824959/possum11.png")

sean14_info=ImageInfo([51.5,70],[103,140],55)
sean14_image=simplegui.load_image("https://dl.dropboxusercontent.com/u/19824959/possum12.png")

sean15_info=ImageInfo([57.5,72.5],[115,145],60)
sean15_image=simplegui.load_image("https://dl.dropboxusercontent.com/u/19824959/possum13.png")

sean16_info=ImageInfo([58.5,72.5],[117,145],60)
sean16_image=simplegui.load_image("https://dl.dropboxusercontent.com/u/19824959/possum14.png")

sean17_info=ImageInfo([41,75],[82,150],55)
sean17_image=simplegui.load_image("https://dl.dropboxusercontent.com/u/19824959/possum15.png")

sean18_info=ImageInfo([49,70],[98,140],60)
sean18_image=simplegui.load_image("https://dl.dropboxusercontent.com/u/19824959/possum16.png")

sean19_info=ImageInfo([51.5,70],[103,140],60)
sean19_image=simplegui.load_image("https://dl.dropboxusercontent.com/u/19824959/possum17.png")

sean20_info=ImageInfo([47.5,62.5],[95,125],55)
sean20_image=simplegui.load_image("https://dl.dropboxusercontent.com/u/19824959/possum18.png")

sean21_info=ImageInfo([53,70],[106,140],60)
sean21_image=simplegui.load_image("https://dl.dropboxusercontent.com/u/19824959/possum19.png")

sean22_info=ImageInfo([57,75],[114,150],60)
sean22_image=simplegui.load_image("https://dl.dropboxusercontent.com/u/19824959/possum20.png")

sean23_info=ImageInfo([75,70],[150,140],70)
sean23_image=simplegui.load_image("https://dl.dropboxusercontent.com/u/19824959/possum21.png")


# make list of image objects
image_info_list=[sean1_info,sean2_info,sean3_info,sean4_info,sean5_info,sean6_info,sean7_info,sean8_info,sean9_info,sean10_info,sean11_info,sean12_info,sean13_info,sean14_info,sean15_info,sean16_info,sean17_info,sean18_info,sean19_info,sean20_info,sean21_info,sean22_info,sean23_info]
image_list=[sean1_image,sean2_image,sean3_image,sean4_image,sean5_image,sean6_image,sean7_image,sean8_image,sean9_image,sean10_image,sean11_image,sean12_image,sean13_image,sean14_image,sean15_image,sean16_image,sean17_image,sean18_image,sean19_image,sean20_image,sean21_image,sean22_image,sean23_image]


# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets 
# .ogg versions of sounds are also available, just replace .mp3 by .ogg
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions 
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


# Ship class
class Ship:

    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def get_position(self):
        return self.pos
    def get_radius(self):
        return self.radius
    
    def draw(self,canvas):
        if self.thrust:
            canvas.draw_image(self.image, [self.image_center[0] + self.image_size[0], self.image_center[1]] , self.image_size,
                              self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size,
                              self.pos, self.image_size, self.angle)
        # canvas.draw_circle(self.pos, self.radius, 1, "White", "White")

    def update(self):
        # update angle
        self.angle += self.angle_vel
        
        # update position
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT

        # update velocity
        k=.2
        forward=[math.cos(self.angle),math.sin(self.angle)]
        if self.thrust:
            self.vel[0]+=k*forward[0]
            self.vel[1]+=k*forward[1]
            
         #friction
        c=.0075
        self.vel[0]*=(1-c)
        self.vel[1]*=(1-c)
        
        

    def set_thrust(self, on):
        self.thrust = on
        if on:
            ship_thrust_sound.rewind()
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.pause()
       
    def increment_angle_vel(self):
        self.angle_vel += .1
        
    def decrement_angle_vel(self):
        self.angle_vel -= .1
        
    def shoot(self):
        global missile_group
        forward = angle_to_vector(self.angle)
        missile_pos = [self.pos[0] + self.radius * forward[0], self.pos[1] + self.radius * forward[1]]
        missile_vel = [self.vel[0] + 6 * forward[0], self.vel[1] + 6 * forward[1]]
        a_missile = Sprite(missile_pos, missile_vel, self.angle, 0, missile_image, missile_info, missile_sound)
        missile_group.add(a_missile)
    
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def get_position(self):
        return self.pos
    def get_radius(self):
        return self.radius
    
    def draw(self, canvas):
        if self.animated:
            
            canvas.draw_image(self.image, [(self.image_center[0]*self.age + self.image_size[0]/2),self.image_center[1]], self.image_size,
                          self.pos, self.image_size, self.angle)
        else:    
            canvas.draw_image(self.image, self.image_center, self.image_size,
                          self.pos, self.image_size, self.angle)

    def update(self):
        # update angle
        self.angle += self.angle_vel
        
        # update position
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
    
        #update age
        self.age+=1
        
        if self.age < self.lifespan:
            return False
        else:
            return True
        
    def collide(self,other_object):   
        if dist(self.get_position(),other_object.get_position()) < (self.get_radius()+other_object.get_radius()):
            return True
        else:
            return False
# key handlers to control ship   
def keydown(key):
    if key == simplegui.KEY_MAP['left']:
        my_ship.decrement_angle_vel()
    elif key == simplegui.KEY_MAP['right']:
        my_ship.increment_angle_vel()
    elif key == simplegui.KEY_MAP['up']:
        my_ship.set_thrust(True)
    elif key == simplegui.KEY_MAP['space']:
        my_ship.shoot()
        
def keyup(key):
    if key == simplegui.KEY_MAP['left']:
        my_ship.increment_angle_vel()
    elif key == simplegui.KEY_MAP['right']:
        my_ship.decrement_angle_vel()
    elif key == simplegui.KEY_MAP['up']:
        my_ship.set_thrust(False)
        
# mouseclick handlers that reset UI and conditions whether splash image is drawn
def click(pos):
    global started
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True

def draw(canvas):
    global time, started , lives, score, rock_group
    
    if lives<=0:
        started=False
        lives=3
        score=0
        soundtrack.rewind()
        soundtrack.play()
        for rock in rock_group:
            rock_group.remove(rock)
        
    
    # animiate background
    time += 1
    center = debris_info.get_center()
    size = debris_info.get_size()
    wtime = (time / 8) % center[0]
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, [center[0] - wtime, center[1]], [size[0] - 2 * wtime, size[1]], 
                                [WIDTH / 2 + 1.25 * wtime, HEIGHT / 2], [WIDTH - 2.5 * wtime, HEIGHT])
    canvas.draw_image(debris_image, [size[0] - wtime, center[1]], [2 * wtime, size[1]], 
                                [1.25 * wtime, HEIGHT / 2], [2.5 * wtime, HEIGHT])

    # draw UI
    canvas.draw_text("Lives", [50, 50], 22, "White")
    canvas.draw_text("Score", [680, 50], 22, "White")
    canvas.draw_text(str(lives), [50, 80], 22, "White")
    canvas.draw_text(str(score), [680, 80], 22, "White")

    #check if ship hit any rocks
    if group_collide(rock_group,my_ship)>0:
        lives -=1
        #print group_collide(rock_group,my_ship)
        
    #check for missile-rock collision
    if group_group_collide(missile_group,rock_group)>0:
        score+=1
    
    # draw ship and sprites
    my_ship.draw(canvas)

  
    
    # update ship and sprites
    my_ship.update()
   
    process_sprite_group(rock_group,canvas)    
    process_sprite_group(missile_group,canvas)
    process_sprite_group(explosion_group,canvas)
    

# timer handler that spawns a rock    
def process_sprite_group(someset,somecanvas):
    for item in someset:
        if not item.update():
            item.update()
            item.draw(somecanvas)
        else:
            someset.discard(item)

        
def group_collide(somegroup,other_object):
    global lives, explosion_group
    group_copy=somegroup
    hit =0
    for item in group_copy:
       
        if item.collide(other_object):
            somegroup.discard(item)
            hit=1
            an_explosion=Sprite(item.get_position(),[0,0],0,0,explosion_image,explosion_info,explosion_sound)
            explosion_group.add(an_explosion)
    return hit
    
def group_group_collide(groupA,groupB):
    hits=0
    groupAcopy=groupA
    for item in groupAcopy:
        hits+=group_collide(groupB,item)
    return hits
        
        
    
def rock_spawner():
    global rock_group
    
    
    if len(rock_group)<8:
        rock_pos = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]
        rock_vel = [random.random() * .6 - .3, random.random() * .6 - .3]
        rock_avel = random.random() * .02 - .01
        #so need to pick asteroid_image and asteroid_info randomly from a list of Image_info objects
        i=random.randrange(0,len(image_list))
        a_rock = Sprite(rock_pos, rock_vel, 0, rock_avel, image_list[i], image_info_list[i])
        
        if dist(a_rock.get_position(),my_ship.get_position())>200:
            rock_group.add(a_rock)
# initialize stuff
frame = simplegui.create_frame("SEAN ATTACKS", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
rock_group=set([])
missile_group=set([])
explosion_group=set([])
# register handlers
frame.set_keyup_handler(keyup)
frame.set_keydown_handler(keydown)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

timer = simplegui.create_timer(500.0, rock_spawner)

# get things rolling
timer.start()
frame.start()

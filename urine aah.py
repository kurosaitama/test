#warning: my name is kuro,  i do horrible stuff and don't you dare sell my thing for 1000$ and get rich off me, i'll take care of your stupid buisness as a letter for some random guru

from ursina import *
from ursina import Default, camera
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders.unlit_shader import unlit_shader



game = Ursina()

window.fps_counter.enabled = True
window.cog_button.enaled = False
window.entity_counter.enabled = False
window.collider_counter.enabled = True

current_texture = 'grass'
current_color = color.green


def change_block():
    global current_block
    destroy(current_block)
    current_block = Entity(parent=camera.ui,
                           model= 'quad',
                           texture=current_texture,
                           color=current_color,
                           scale=0.1,
                           position=(0, -0.35,0))
def update():
    global current_texture
    global current_color
    global current_block
    if held_keys['escape']:
        application.quit()
    if held_keys['2']:
        current_texture = 'brick'
        current_color = color.red
        change_block()
    if held_keys['1']:
        current_texture = 'grass'
        current_color = color.green
        change_block()


        if player.y < -2:
            player.position = (0, 2, 0) #trk lul
        
    

#FirstEntity= Model="cube", position=(1, 2, 3),
                      #texture= "grass",
                        #color=color.green, scale=(20, 0, 20) ,collider= 'box')

#def input(key):
    #if key == "right mouse down" and block.hovered:
        #block = Button(model="cube", position= (x, 0, z),
                       #texture="grass",
                       #color= color.green,
                       #scale=1
                        #, collider="box",
                        #parent=scene
                        #,highlight_color = color.light_gray)




class Block(Button):
    def __init__(self, texture='grass', this_color = color.green, position=(0,0,0), breakable = True):
        super().__init__(parent=scene,
                         position=position,
                                   texture=texture,
                                   highlight_color = color.light_gray,
                                   collider= "box",
                                   color = this_color,
                                   model='cube')
        self.breakable = breakable

    def input(self, key):
            if key == 'left mouse down' and self.hovered and self.breakable:
                destroy(self)
            if key == 'right mouse down' and self.hovered:
                new_block =  Block(current_texture, this_color = current_color, position=self.position+mouse.normal)

        
for x in range(20):
    for z in range(20):
        for y in range(5):
            if y == 1:
             block = Block('grass',color.green, position=(x,-y,z))
            elif y == 2:
                block = Block('grass',color.brown, position=(x,-y,z))
            elif y== 3:
                block = Block('grass',color.light_gray, position=(x,-y,z))
            elif y== 4:
                block = Block('grass',color.black, position=(x,-y,z), breakable= False)






Sky()

border = Entity(parent=camera.ui, model='quad', color= color.gray, scale=0.11, position=(0,-0.35,1))
current_block = Entity(parent=camera.ui, model='quad',texture=current_texture, color= current_color, scale=0.1, position=(0,-0.35,0))
#EditorCamera()
player = FirstPersonController(position= (0, 2, 0)) #if you want freecam remove the # in editorcamera, also you cant use with each other


game.run ()
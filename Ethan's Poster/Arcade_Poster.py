import arcade


WIDTH = 640
HEIGHT = 480


RECT_WIDTH = 225
RECT_HEIGHT = 900


center_x = 130      # Initial x position
center_y = 75       # Initial y position
delta_x = 3       # change in x
#delta_y = 1      # change in y

def on_update(delta_time):
    global center_x, center_y
    global delta_x#, #delta_y

    center_x += delta_x
    center_y# += #delta_y

    # Figure out if we hit the edge and need to reverse.
    if center_x < RECT_WIDTH // 2 or center_x > WIDTH - RECT_WIDTH // 2:
        delta_x *= -1

    #if center_y < RECT_HEIGHT // 2 or center_y > HEIGHT - RECT_HEIGHT // 2:
        #delta_y *= -1

def on_draw():
    arcade.start_render()
    #x (Left and right. More = right less = left)
    #y (Up and down. More = up and less = down)
    #z (Width)

    arcade.draw_rectangle_filled(center_x, center_y, RECT_WIDTH, RECT_HEIGHT, arcade.color.BLACK)
    arcade.draw_text("Cyberbullying Is Bad", 175, 405, arcade.color.WHITE, 24)
    arcade.draw_text("Cyberbullying almost", 40, 45, arcade.color.WHITE, 30)
    arcade.draw_text("guarantees depression ", 40, 20, arcade.color.WHITE, 30)
    arcade.draw_text("Both the victim and the bully", 200, 200, arcade.color.WHITE, 30)
    arcade.draw_text("are negatively affected", 200, 175, arcade.color.WHITE, 30)
    arcade.draw_text("There are no benefits", 30, 300, arcade.color.WHITE, 30)
    texture = arcade.load_texture("images/126-1266990_black-and-white-stock-cellphone-clipart-coloring-page.png")
    scale = .1
    arcade.draw_texture_rectangle(540, 120, scale * texture.width,
                                  scale * texture.height, texture, 0)
    texture = arcade.load_texture("images/phomne.png")
    scale = .1
    arcade.draw_texture_rectangle(540, 300, scale * texture.width,
                                  scale * texture.height, texture, 0)
    texture = arcade.load_texture("images/phone.png")
    scale = .1
    arcade.draw_texture_rectangle(125, 200, scale * texture.width,
                                  scale * texture.height, texture, 0)
    texture = arcade.load_texture("images/tilted.png")
    scale = .3
    arcade.draw_texture_rectangle(115, 400, scale * texture.width,
                                  scale * texture.height, texture, 0)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "Anti-cyberbully Poster")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/60)

    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()

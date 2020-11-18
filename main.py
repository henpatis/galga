def on_a_pressed():
    global dart
    dart = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . 4 4 . . . . . . . . . . 
                    . 4 4 4 4 4 . . . . . . . . . . 
                    4 4 4 4 4 4 2 2 2 2 2 2 2 2 2 2 
                    4 4 4 4 4 4 2 2 2 2 2 2 2 2 2 2 
                    . 4 4 4 4 4 . . . . . . . . . . 
                    . 4 4 4 4 4 . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        mySprite,
        200,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy()
    sprite.destroy(effects.fire, 100)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    mySprite.destroy()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

mySprite2: Sprite = None
dart: Sprite = None
mySprite: Sprite = None
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . 8 8 . . . . . . . . 
            . . 8 2 . . 8 8 . . . . . . . . 
            . . 1 1 1 . 8 8 . . 9 9 9 9 9 . 
            . . 2 2 2 2 8 8 . 9 9 9 9 9 9 9 
            . . f 8 6 6 6 6 6 6 9 9 9 9 9 9 
            . . . . . . 2 2 . . . . . . . . 
            . . . . . . 2 2 . . . . . . . . 
            . . . . . . 2 2 . . . . . . . . 
            . . . . . . 2 2 . . . . . . . . 
            . . . . . . 2 2 . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
mySprite.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
info.set_life(3)
controller.move_sprite(mySprite, 200, 200)

def on_update_interval():
    global mySprite2
    mySprite2 = sprites.create(img("""
            . . . . . . . . 2 . . . . . . . 
                    . . . . . . . 2 4 . . . . . . . 
                    . . . . . . . 4 2 . . . . . . . 
                    . . . . . . . 2 4 . . . . . . . 
                    . . . . . . . 4 2 9 9 9 9 9 9 . 
                    . . . . 2 2 2 2 4 9 9 9 9 9 9 . 
                    . . . . . . 2 2 2 2 9 9 9 9 9 . 
                    . . . . . . . . 2 4 . . . . . . 
                    . . . . . . . . 4 2 . . . . . . 
                    . . . . . . . . 2 4 . . . . . . 
                    . . . . . . . . 4 2 . . . . . . 
                    . . . . . . . . 2 . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    mySprite2.set_velocity(-100, 0)
    mySprite2.set_position(180, randint(0, 120))
game.on_update_interval(500, on_update_interval)

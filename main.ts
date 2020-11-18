controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    dart = sprites.createProjectileFromSprite(img`
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
        `, mySprite, 200, 0)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.destroy()
    sprite.destroy(effects.fire, 100)
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    mySprite.destroy()
    info.changeLifeBy(-1)
})
let mySprite2: Sprite = null
let dart: Sprite = null
let mySprite: Sprite = null
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
mySprite.setFlag(SpriteFlag.StayInScreen, true)
info.setLife(3)
controller.moveSprite(mySprite, 200, 200)
game.onUpdateInterval(500, function () {
    mySprite2 = sprites.create(img`
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
        `, SpriteKind.Enemy)
    mySprite2.setVelocity(-100, 0)
    mySprite2.setPosition(180, randint(0, 120))
})

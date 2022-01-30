extends KinematicBody2D

var max_speed: int = 70
var max_steering: float = 2.5
var velocity: Vector2
var avoid_force: int = 1000

onready var raycasts = $raycasts


func _physics_process(delta):
	var steering: Vector2 = Vector2.ZERO
	steering += seek_steering()
	steering += avoid_obstacles_steering()
	steering = steering.clamped(max_steering)
	velocity += steering 
	velocity = velocity.clamped(max_speed)
	velocity = move_and_slide(velocity)

func seek_steering() -> Vector2:
	var desired_velocity: Vector2 = (get_global_mouse_position() - position).normalized() * max_speed
	return desired_velocity

func avoid_obstacles_steering() -> Vector2:
	raycasts.rotation = velocity.angle()
	for raycast in raycasts.get_children():
		raycast.cast_to.x = velocity.length()
		if raycast.is_colliding():
			var obstacle:PhysicsBody2D = raycast.get_collider()
			return(position + velocity - obstacle.position).normalized()*avoid_force
	return Vector2.ZERO

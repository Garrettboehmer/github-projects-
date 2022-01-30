extends KinematicBody2D

onready var path = []
onready var threshold = 15
onready var direction = Vector2.ZERO
onready var speed = 100
onready var velocity = Vector2.ZERO
signal just_spawned

#func _ready():
#	emit_signal('just_spawned',self)
func _process(delta):
	if path.size()<=0:
		emit_signal('just_spawned',self)
	elif path.size()>0:
		move_to_target()
	
func move_to_target():
	if global_position.distance_to(path[0]) < threshold:
		path.remove(0)
	else:
		direction = global_position.direction_to(path[0])
		velocity = direction * speed
		velocity = move_and_slide(velocity)

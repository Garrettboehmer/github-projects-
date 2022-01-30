extends KinematicBody2D

onready var speed = 25
signal wander
onready var path = []
onready var threshold = 15
onready var velocity = Vector2.ZERO
onready var stats = $stats
onready var label = $Label
onready var good_guys = []
onready var found_good_guy = null
onready var state = WANDER
onready var where_warrior_was_sent_by_world = null
onready var area_2 = $senses
onready var cool_down = $cool_down
onready var seek = Vector2.ZERO


enum {
	WANDER,
	ATTACK
}

func _physics_process(delta):
	label.text = str(stats.health)
	if stats.health <=0:
		queue_free()
	match state:
			WANDER:
				speed = 50
				wander()
			ATTACK:
				move_to_enemy()
				attack()
#	elif path.size()<=0:
#		emit_signal("wander", self)

func move_to_enemy():
	if is_instance_valid(found_good_guy):
		seek = global_position.direction_to(found_good_guy.global_position)
		velocity = seek * speed
		velocity = move_and_slide(velocity)

func wander():
	if path.size()<=0:
		emit_signal("wander", self)
	var distance = path[-1].distance_to(global_position)
	move_to_target()
	if distance <= 50:
		emit_signal("wander", self)

var max_speed: int = 15
var max_steering: float = 5
var avoid_force: int = 1000

func move_to_target():
	var steering = Vector2.ZERO
	if path.size()>0:
		if global_position.distance_to(path[0]) < threshold:
			path.remove(0)
		else:
			steering += seek_steering()
			#steering += avoid_obstacles_steering()
			steering = steering.clamped(max_steering)
			velocity += steering
			velocity = velocity.clamped(max_speed)
			velocity = move_and_slide(velocity)
onready var direction
func seek_steering() -> Vector2:
	var desired_velocity: Vector2 = (path[0] - global_position).normalized() * max_speed
	return desired_velocity

func _on_senses_body_entered(_body):
	#good_guys = area_2.get_overlapping_bodies()
	good_guys.append(_body)
	found_good_guy = _body
	if good_guys.size() >= 0:
		state = ATTACK

func _on_senses_body_exited(body):
	var index = good_guys.find(body)
	if index != -1:
		good_guys.remove(index)
	if good_guys.size()<=0:
		state = WANDER

func attack():
	if is_instance_valid(found_good_guy):
		var distance = found_good_guy.global_position.distance_to(global_position)
		if distance <= 10 and cool_down.is_stopped():
			found_good_guy.stats.health -= stats.damage
			cool_down.start()
		if found_good_guy.stats.health <= 0:
			var index = good_guys.find(found_good_guy)
			if index != -1:
				good_guys.remove(index)

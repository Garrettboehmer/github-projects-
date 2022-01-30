extends KinematicBody2D

onready var world = get_tree().get_root().get_node('world')
onready var threshold = 15
onready var path = []
onready var direction = Vector2.ZERO
onready var velocity = Vector2.ZERO
onready var speed = 100
onready var state = MOVE
onready var where_warrior_was_sent_by_world = world.quest_giver_area
onready var label = $Label
onready var enemy_spotted = []
onready var attack_area  = $attack_area
onready var seek = Vector2.ZERO
onready var stats = $stats
signal what_is_this
signal wander
signal get_new_path
signal loot
signal where_is_this_tile
onready var found_bad_guy
onready var cool_down  =$cooldown_timer
onready var where_to_avoid
#onready var has_quest = false

func _ready():
	emit_signal('get_new_path', self, QUEST_GIVER)
	percentage_health = (float(stats.health)/stats.max_health)*100
	
onready var percentage_health = null
func _process(delta):
	percentage_health = (float(stats.health)/stats.max_health)*100
	#label.text = str(percentage_health,' ', state)

enum {QUEST_AREA,
	QUEST_GIVER,
	HEALING_POOL,
	}

onready var im_there = false
enum {
	MOVE,
	WANDER,
	ATTACK,
	RUN_AWAY,
	HEALING,
	MAINTENANCE,
}
func _on_senses_area_entered(area):
	if area == world.quest_giver_area:
		emit_signal('get_new_path', self, QUEST_AREA)

func _on_Timer_timeout():
	if world.quest_group_recs.has(where_warrior_was_sent_by_world):
		if percentage_health > 50 and enemy_spotted.size()<=0:
			state=WANDER
		elif percentage_health > 50 and enemy_spotted.size()>0:
			state=ATTACK
		elif percentage_health <=50 and where_warrior_was_sent_by_world != world.healing_spot_area:
			state = RUN_AWAY
	elif !world.quest_group_recs.has(where_warrior_was_sent_by_world):
		if percentage_health <= 50:
			state = MOVE
		elif percentage_health>=100 and where_warrior_was_sent_by_world != world.quest_giver_area:
			emit_signal('get_new_path', self, QUEST_GIVER)
	if where_warrior_was_sent_by_world == world.healing_spot_area:
		print('HEALING_POOL')
		emit_signal('get_new_path', self, HEALING_POOL)
	elif where_warrior_was_sent_by_world in world.quest_group_recs:
		emit_signal('get_new_path', self, QUEST_AREA)
		print('QUEST_AREA')
	elif where_warrior_was_sent_by_world == world.quest_giver_area:
		emit_signal('get_new_path', self, QUEST_GIVER)
		print('QUEST_GIVER')

func _physics_process(delta):
	label.text = str(stats.health, ' ', state)
	if stats.health <= 0:
		queue_free()
	match state:
		MOVE:
			speed = 100
			move_to_target()
		WANDER:
			speed = 100
			wander()
		ATTACK:
			if enemy_spotted.size()>0:
				found_bad_guy = enemy_spotted[0]
				move_to_enemy()
				attack()
		RUN_AWAY:
			emit_signal('get_new_path', self, HEALING_POOL)

func wander():
	if path.size()>0:
		var distance = path[-1].distance_to(global_position)
		move_to_target()
		if distance <= 100:
			emit_signal("wander", self)

func move_to_enemy():
	if is_instance_valid(found_bad_guy):
		seek = global_position.direction_to(found_bad_guy.global_position)
		velocity = seek * speed
		velocity = move_and_slide(velocity)

func attack():
	if is_instance_valid(found_bad_guy):
		var distance = found_bad_guy.global_position.distance_to(global_position)
		if distance <= 10 and cool_down.is_stopped():
			found_bad_guy.stats.health -= stats.damage
			cool_down.start()
			if found_bad_guy.stats.health <= 0:
				emit_signal('loot', self)
				stats.kill_count += 1
				var index = enemy_spotted.find(found_bad_guy)
				if index != -1:
					enemy_spotted.remove(index)

var max_speed: int = 70
var max_steering: float = 5
var avoid_force: int = 1000

func move_to_target():
	var steering = Vector2.ZERO
	if path.size()>0:
		if global_position.distance_to(path[0]) < threshold:
			path.remove(0)
		else:
			steering += seek_steering()
			steering += avoid_obstacles_steering()
			steering = steering.clamped(max_steering)
			velocity += steering
			velocity = velocity.clamped(max_speed)
			velocity = move_and_slide(velocity)

func _on_attack_area_body_entered(_body):
	enemy_spotted.append(_body)

onready var raycasts = $raycasts
func seek_steering() -> Vector2:
	var desired_velocity: Vector2 = (path[0] - global_position).normalized() * max_speed
	return desired_velocity

func avoid_obstacles_steering() -> Vector2:
	raycasts.rotation = velocity.angle()
	for raycast in raycasts.get_children():
		raycast.cast_to.x = velocity.length()
		if raycast.is_colliding():
			var obstacle = raycast.get_collider()
			where_to_avoid = obstacle.global_position
			if obstacle.name == 'dirt cliff':
				var where_they_hit = raycast.get_collision_point()
				emit_signal('where_is_this_tile', where_they_hit, self)
				#print(where_to_avoid)
			return(global_position + velocity - where_to_avoid).normalized()*avoid_force
	return Vector2.ZERO

func _on_attack_area_body_exited(body):
	if is_instance_valid(body):
		if enemy_spotted.size()>0:
			var index = enemy_spotted.find(body)
			if index != -1:
				enemy_spotted.remove(index)





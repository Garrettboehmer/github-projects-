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
onready var found_bad_guy
onready var cool_down  =$cooldown_timer
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

func _physics_process(delta):
	label.text = str(stats.health, ' ', state)
	if stats.health <= 0:
		queue_free()
	if path.size() > 0:
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
	var distance = path[-1].distance_to(global_position)
	move_to_target()
	if distance <= 50:
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

func move_to_target():
	if global_position.distance_to(path[0]) < threshold:
		path.remove(0)
	else:
		direction = global_position.direction_to(path[0])
		velocity = direction * speed
		velocity = move_and_slide(velocity)

func _on_attack_area_body_entered(_body):
	enemy_spotted.append(_body)

func _on_attack_area_body_exited(body):
	if is_instance_valid(body):
		if enemy_spotted.size()>0:
			var index = enemy_spotted.find(body)
			if index != -1:
				enemy_spotted.remove(index)




extends Node
export var max_health = 1
onready var health = max_health
export var damage = 5
onready var kill_count = 0
var level = 1
onready var level_up_condition  = kill_count + (level*5)
onready var cool_down = get_parent().get_node("cooldown_timer")

func _process(delta):
	#get_parent().label.text = str(get_parent().percentage_health, ' ', level, '\n', ' damage ', damage, ' ', 'max_health ', max_health )
	if kill_count >= level_up_condition:
		level += 1
		kill_count = 0
		damage += 2
		max_health += 10
		cool_down.set_wait_time(2.0-(.03*level))


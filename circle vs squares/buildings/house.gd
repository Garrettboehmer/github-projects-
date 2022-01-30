extends StaticBody2D

onready var Villiger = preload("res://heroes/Villiger.tscn")
onready var HOW_MANY_VILLIGERS = 2
onready var villigers = []
onready var spawner = $villiger_spawner
func _ready():
	pass

func _on_Timer_timeout():
	if villigers.size()<HOW_MANY_VILLIGERS:
		var new_villiger = Villiger.instance()
		add_child(new_villiger)
		new_villiger.global_position = spawner.global_position
		villigers.append(new_villiger)
		new_villiger.connect('just_spawned',get_parent(),'villiger_spawned')

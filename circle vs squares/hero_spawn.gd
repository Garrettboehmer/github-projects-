extends ReferenceRect

onready var good_guys = []
const HOW_MANY_HEROES = 1
var Warrior = preload("res://heroes/warrior2.tscn")
onready var label = $Label
onready var count = 0

func _process(delta):
	if good_guys.size() < HOW_MANY_HEROES:
		var new_warrior = Warrior.instance()
		new_warrior.connect('wander',get_parent(),'wander')
		new_warrior.connect('get_new_path',get_parent(),'sending_new_path')
		new_warrior.connect('where_is_this_tile',get_parent().get_node("dirt cliff"), 'sending_position')
		add_child(new_warrior)
		new_warrior.global_position = rect_position
		good_guys.append(new_warrior)

func _on_Timer_timeout():
	for hero in good_guys:
		if !is_instance_valid(hero):
			count += 1
			var index = good_guys.find(hero)
			good_guys.remove(index)
			label.text = str('how many heroes died ', count)

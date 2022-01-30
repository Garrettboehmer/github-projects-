extends ReferenceRect


const HOW_MANY_ENEMIES = 0
onready var area = $quest_area_3a
onready var enemy_group = []
var Enemy = preload("res://enemies/Enemy.tscn")
onready var label = $Label
onready var count = 0

func _on_Timer_timeout():
	for enemys in enemy_group:
			if !is_instance_valid(enemys):
				count += 1
				var index = enemy_group.find(enemys)
				enemy_group.remove(index)
				label.text = str('how many died in 1 = ', count)
	while enemy_group.size()<HOW_MANY_ENEMIES:
		var new_enemy = Enemy.instance()
		add_child(new_enemy)
		new_enemy.global_position = rect_position + Vector2(randf() * rect_size.x, randf()* rect_size.y)
		enemy_group.append(new_enemy)
		new_enemy.connect('wander',get_parent(),'wander')
		new_enemy.where_warrior_was_sent_by_world = area

extends ReferenceRect


onready var healing_party = []
onready var healing_time = $Timer


func _on_healing_area_body_entered(body):
	print('hit')
	healing_party.append(body)

func _on_healing_area_body_exited(body):
	var index = healing_party.find(body)
	healing_party.remove(index)


func _on_Timer_timeout():
	for heroes in healing_party:
		if heroes.percentage_health < 100:
			heroes.stats.health += 10

extends StaticBody2D

onready var is_placed = false
onready var something_in_way_of_placing = []
onready var mesh = $MeshInstance2D
export (Color,RGBA) var red
export (Color,RGBA) var yellow
var current_color = yellow
#onready var House = preload("res://buildings/house.tscn")
onready var can_be_placed = true
func _process(delta):
	if Input.is_action_just_pressed("ui_select") and can_be_placed:
		queue_free()
	if something_in_way_of_placing.size()>1:
		current_color = red
		can_be_placed = false
	else:
		current_color = yellow
		can_be_placed = true
	mesh.material.set_shader_param('current_color', current_color)


func _on_Area2D_body_entered(body):
	if is_placed==false:
		something_in_way_of_placing.append(body)


func _on_Area2D_body_exited(body):
	if is_placed==false:
		var index = something_in_way_of_placing.find(body)
		something_in_way_of_placing.remove(index)


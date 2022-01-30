extends Node2D

var Warrior = preload("res://heroes/warrior2.tscn")
var Enemy = preload("res://enemies/Enemy.tscn")
var House_pic = preload("res://buildings/house_pic.tscn")
onready var House = preload("res://buildings/house.tscn")
onready var quest_area_1 = $quest_area_1
onready var quest_1a  = $quest_area_1/quest_area_1a
onready var quest_area_2 = $quest_area_2
onready var quest_2a = $quest_area_2/quest_area_2a
onready var quest_area_3 = $quest_area_3
onready var quest_3a = $quest_area_3/quest_area_3a
onready var quest_area_4 = $quest_area_4
onready var quest_4a = $quest_area_4/quest_area_4a
onready var quest_area_5 = $quest_area_5
onready var quest_5a = $quest_area_5/quest_area_5a
onready var nav = $Navigation2D
onready var quest_giver = $quest_giver
onready var quest_giver_area = $quest_giver/quest_area
onready var quest_group_areas = []
onready var quest_group_recs = []
onready var quest_spot = null

onready var good_guys = []

onready var quest_rect_obj = []

onready var label = $Label

onready var healing_spot = $healing_spot
onready var healing_spot_area = $healing_spot/healing_area
onready var new_house_pic = null
onready var house_button1 = $Control/house_building_button
func wander(hero):
	var index = quest_group_recs.find(hero.where_warrior_was_sent_by_world)
	var where_am_i = quest_rect_obj[index]
	var max_x_wander = where_am_i.rect_position.x
	var max_y_wander = where_am_i.rect_position.y
	var random = RandomNumberGenerator.new()
	random.randomize()
	var ran_x = random.randi_range(max_x_wander,max_x_wander+where_am_i.rect_size.x)
	var ran_y = random.randi_range(max_y_wander,max_y_wander+where_am_i.rect_size.y)
	var wander_point = Vector2(ran_x,ran_y)
	hero.path = nav.get_simple_path(hero.global_position, wander_point)

enum {
	MOVE,
	WANDER,
	ATTACK,
	RUN_AWAY,
	HEALING,
	MAINTENANCE
}
func _process(delta):
	house_button1.text = str('House')
	var mouse_position = get_viewport().get_mouse_position()
	#label.text = str(Engine.get_frames_per_second())
	
	if is_instance_valid(new_house_pic):
		if new_house_pic != null:
			new_house_pic.global_position = mouse_position
		if Input.is_action_just_pressed("ui_select") and new_house_pic.can_be_placed:
			var new_house = House.instance()
			add_child(new_house)
			new_house.global_position = new_house_pic.global_position

func _ready():
	OS.set_current_screen(0)
	quest_group_recs = [quest_5a,
						quest_2a,
						quest_3a,
						quest_1a,
						quest_4a]

	quest_rect_obj = [quest_area_5,
					quest_area_2,
					quest_area_3,
					quest_area_1,
					quest_area_4]

enum {QUEST_AREA,
	QUEST_GIVER,
	HEALING_POOL,
	}

func send_on_a_quest(warrior):
	var ran
	if warrior.stats.level >=1 and warrior.stats.level <=5:
		ran = 0
	elif warrior.stats.level >=6 and warrior.stats.level <=10:
		ran = 1
	elif warrior.stats.level >=11 and warrior.stats.level <=15:
		ran = 2
	elif warrior.stats.level >=16 and warrior.stats.level <=20:
		ran = 3
	elif warrior.stats.level >=21:
		ran = 4
	warrior.direction = nav.get_simple_path(warrior.global_position, quest_group_recs[ran].global_position)
	warrior.where_warrior_was_sent_by_world = quest_group_recs[ran]
func send_back_to_quest_giver(warrior):
	warrior.path = nav.get_simple_path(warrior.global_position, quest_giver.global_position)
	warrior.where_warrior_was_sent_by_world = quest_giver_area
func send_for_healing(warrior):
	warrior.path = nav.get_simple_path(warrior.global_position, healing_spot_area.global_position) 
	warrior.where_warrior_was_sent_by_world = healing_spot_area

func sending_new_path(warrior, where_to_go):
	match where_to_go:
		QUEST_AREA:
			send_on_a_quest(warrior)
		QUEST_GIVER:
			send_back_to_quest_giver(warrior)
		HEALING_POOL:
			send_for_healing(warrior)
onready var gathering_square = $gathering_square
func villiger_spawned(villiger):
	villiger.path = nav.get_simple_path(villiger.global_position, gathering_square.rect_position, false)

func _on_house_building_button_pressed():
	new_house_pic = House_pic.instance()
	add_child(new_house_pic)
	



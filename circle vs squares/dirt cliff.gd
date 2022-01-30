extends TileMap



func sending_position(where_they_hit, warrior):
	var mouse_pos = where_they_hit
	var tile_pos = map_to_world(world_to_map(mouse_pos))
	warrior.where_to_avoid = tile_pos

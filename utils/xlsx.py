def sheet_writer(game_sheet, games_list) -> int:
    game_sheet[f"A1"] = "Appid"
    game_sheet[f"B1"] = "Game Name"
    game_sheet[f"C1"] = "Protected Achievements Count"
    game_sheet[f"D1"] = "Total Achievements Count"
    game_sheet[f"E1"] = "All Protected Achievements"

    write_counter = 1
    for game in games_list:
        write_counter += 1
        game_sheet[f"A{write_counter}"] = game.appid
        game_sheet[f"B{write_counter}"] = game.name
        game_sheet[f"C{write_counter}"] = game.protected_count
        game_sheet[f"D{write_counter}"] = game.achievement_count
        game_sheet[f"E{write_counter}"] = ";".join([key for key, ach in game.achievements.items() if ach.protected])

    return write_counter

import easygui

favourite_places = ["Italy", "France", "England"]

easygui.msgbox(f"The place I would most like to visit is "
               f"{favourite_places[0]}", title="Location One")
easygui.msgbox(f"My second choice would be {favourite_places[1]}",
               title="Location Two")
easygui.msgbox(f"My third choice for places to visit is {favourite_places[2]}",
               title="Location Three")

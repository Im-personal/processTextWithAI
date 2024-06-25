from fixthelink import *

#That's an example!
set_api_key("API-KEY")
init("testlink")
res = add_tags_to_text("Давным давно существовали только два типа пользователей: telegram.ogr и facebook.com. Но однажды между ними случилась война: после долгих сражений появиляся некий @mrdog который написал на почту email@myown.test и сделал все и справился со всем. Крутой был тип! Гордимся им.")
print(res)
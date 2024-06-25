from fixthelink import *

set_api_key("[your key]")
init("testlink")
res = add_tags_to_text("Давным давно существовали только два типа пользователей: telegram.ogr и facebook.com. Но однажды между ними случилась война: после долгих сражений появиляся некий @mrdog который написал на почту email@myown.test и сделал все и справился со всем. Крутой был тип! Гордимся им.")
print(res)
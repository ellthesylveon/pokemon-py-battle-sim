from typing import TypeAlias

Pokemon: TypeAlias = dict[str, str | int | list[str | int | float] | dict[str, bool]]
Move: TypeAlias = dict[str, str | int | dict[str, bool] | None]